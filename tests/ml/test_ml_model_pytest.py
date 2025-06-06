#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from typing import Tuple

import numpy as np
import pytest

from eland.ml import MLModel
from eland.ml.ltr import FeatureLogger, LTRModelConfig, QueryFeatureExtractor
from eland.ml.transformers import get_model_transformer
from tests import (
    ES_IS_SERVERLESS,
    ES_TEST_CLIENT,
    ES_VERSION,
    NATIONAL_PARKS_INDEX_NAME,
)

try:
    from sklearn import datasets
    from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
    from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

try:
    from xgboost import XGBClassifier, XGBRanker, XGBRegressor

    HAS_XGBOOST = True
except ImportError:
    HAS_XGBOOST = False

try:
    from lightgbm import LGBMClassifier, LGBMRegressor

    HAS_LIGHTGBM = True
except ImportError:
    HAS_LIGHTGBM = False


requires_sklearn = pytest.mark.skipif(
    not HAS_SKLEARN, reason="This test requires 'scikit-learn' package to run"
)
requires_xgboost = pytest.mark.skipif(
    not HAS_XGBOOST, reason="This test requires 'xgboost' package to run"
)
requires_no_ml_extras = pytest.mark.skipif(
    HAS_SKLEARN or HAS_XGBOOST,
    reason="This test requires 'scikit-learn' and 'xgboost' to not be installed",
)

requires_lightgbm = pytest.mark.skipif(
    not HAS_LIGHTGBM, reason="This test requires 'lightgbm' package to run."
)


def requires_elasticsearch_version(minimum_version: Tuple[int, int, int]):
    return pytest.mark.skipif(
        ES_VERSION < minimum_version,
        reason=f"This test requires Elasticsearch version {'.'.join(str(v) for v in minimum_version)} or later.",
    )


def skip_if_multiclass_classifition():
    if ES_VERSION < (7, 7):
        raise pytest.skip(
            "Skipped because multiclass classification "
            "isn't supported on Elasticsearch 7.6"
        )


def random_rows(data, size):
    return data[np.random.randint(data.shape[0], size=size), :]


def check_prediction_equality(es_model: MLModel, py_model, test_data):
    # Get some test results
    test_results = py_model.predict(np.asarray(test_data))
    es_results = es_model.predict(test_data)
    np.testing.assert_almost_equal(test_results, es_results, decimal=2)


def randomize_model_id(prefix, suffix_size=10):
    import random
    import string

    return f"{prefix}-{''.join(random.choices(string.ascii_lowercase, k=suffix_size))}"


class TestMLModel:
    @requires_no_ml_extras
    def test_import_ml_model_when_dependencies_are_not_available(self):
        from eland.ml import MLModel  # noqa: F401

    @requires_sklearn
    def test_unpack_and_raise_errors_in_ingest_simulate(self, mocker):
        # Train model
        training_data = datasets.make_classification(n_features=5)
        classifier = DecisionTreeClassifier()
        classifier.fit(training_data[0], training_data[1])

        # Serialise the models to Elasticsearch
        feature_names = ["f0", "f1", "f2", "f3", "f4"]
        model_id = "test_decision_tree_classifier"
        test_data = [[0.1, 0.2, 0.3, -0.5, 1.0], [1.6, 2.1, -10, 50, -1.0]]

        es_model = MLModel.import_model(
            ES_TEST_CLIENT,
            model_id,
            classifier,
            feature_names,
            es_if_exists="replace",
            es_compress_model_definition=True,
        )

        # Mock the ingest.simulate API to return an error within {'docs': [...]}
        mock = mocker.patch.object(ES_TEST_CLIENT.ingest, "simulate")
        mock.return_value = {
            "docs": [
                {
                    "error": {
                        "type": "x_content_parse_exception",
                        "reason": "[1:1052] [inference_model_definition] failed to parse field [trained_model]",
                    }
                }
            ]
        }

        with pytest.raises(RuntimeError) as err:
            es_model.predict(test_data)

        assert repr(err.value) == (
            'RuntimeError("Failed to run prediction for model ID '
            "'test_decision_tree_classifier'\", {'type': 'x_content_parse_exception', "
            "'reason': '[1:1052] [inference_model_definition] failed to parse "
            "field [trained_model]'})"
        )

    @requires_sklearn
    @pytest.mark.parametrize("compress_model_definition", [True, False])
    @pytest.mark.parametrize("multi_class", [True, False])
    def test_decision_tree_classifier(self, compress_model_definition, multi_class):
        # Train model
        training_data = (
            datasets.make_classification(
                n_features=7,
                n_classes=3,
                n_clusters_per_class=2,
                n_informative=6,
                n_redundant=1,
            )
            if multi_class
            else datasets.make_classification(n_features=7)
        )
        classifier = DecisionTreeClassifier()
        classifier.fit(training_data[0], training_data[1])

        # Serialise the models to Elasticsearch
        feature_names = ["f0", "f1", "f2", "f3", "f4", "f5", "f6"]
        model_id = "test_decision_tree_classifier"

        es_model = MLModel.import_model(
            ES_TEST_CLIENT,
            model_id,
            classifier,
            feature_names,
            es_if_exists="replace",
            es_compress_model_definition=compress_model_definition,
        )

        # Get some test results
        check_prediction_equality(
            es_model, classifier, random_rows(training_data[0], 20)
        )

        # Clean up
        es_model.delete_model()

    @requires_sklearn
    @pytest.mark.parametrize("compress_model_definition", [True, False])
    def test_decision_tree_regressor(self, compress_model_definition):
        # Train model
        training_data = datasets.make_regression(n_features=5)
        regressor = DecisionTreeRegressor()
        regressor.fit(training_data[0], training_data[1])

        # Serialise the models to Elasticsearch
        feature_names = ["f0", "f1", "f2", "f3", "f4"]
        model_id = "test_decision_tree_regressor"

        es_model = MLModel.import_model(
            ES_TEST_CLIENT,
            model_id,
            regressor,
            feature_names,
            es_if_exists="replace",
            es_compress_model_definition=compress_model_definition,
        )
        # Get some test results
        check_prediction_equality(
            es_model, regressor, random_rows(training_data[0], 20)
        )

        # Clean up
        es_model.delete_model()

    def _normalize_ltr_score_from_XGBRanker(self, ranker, ltr_model_config, scores):
        """Normalize the scores of an XGBRanker model as ES implementation of LTR would do.

        Parameters
        ----------
        ranker : XGBRanker
            The XGBRanker model to retrieve the minimum score from.

        ltr_model_config : LTRModelConfig
            LTR model config.

        Returns
        -------
        scores : List[float]
            Normalized scores for the model.
        """

        if (ES_VERSION[0] == 8 and ES_VERSION >= (8, 19)) or (
            ES_VERSION >= (9, 1) or ES_IS_SERVERLESS
        ):
            # In 8.19 and 9.1, the scores are normalized if there are negative scores
            min_model_score, _ = (
                get_model_transformer(
                    ranker, feature_names=ltr_model_config.feature_names
                )
                .transform()
                .bounds()
            )
            if min_model_score < 0:
                scores = [score - min_model_score for score in scores]

        return scores

    @requires_elasticsearch_version((8, 12))
    @requires_xgboost
    @pytest.mark.parametrize("compress_model_definition", [True, False])
    @pytest.mark.parametrize(
        "objective",
        ["rank:ndcg", "rank:map", "rank:pairwise"],
    )
    def test_learning_to_rank(self, objective, compress_model_definition):
        X, y = datasets.make_classification(
            n_features=3, n_informative=2, n_redundant=1
        )
        rng = np.random.default_rng()
        qid = rng.integers(0, 3, size=X.shape[0])

        # Sort the inputs based on query index
        sorted_idx = np.argsort(qid)
        X = X[sorted_idx, :]
        y = y[sorted_idx]
        qid = qid[sorted_idx]

        ranker = XGBRanker(objective=objective)
        ranker.fit(X, y, qid=qid)

        # Serialise the models to Elasticsearch
        model_id = randomize_model_id("test_learning_to_rank")
        ltr_model_config = LTRModelConfig(
            feature_extractors=[
                QueryFeatureExtractor(
                    feature_name="title_bm25",
                    query={"match": {"title": "{{query_string}}"}},
                ),
                QueryFeatureExtractor(
                    feature_name="description_bm25",
                    query={"match": {"description_bm25": "{{query_string}}"}},
                ),
                QueryFeatureExtractor(
                    feature_name="visitors",
                    query={
                        "script_score": {
                            "query": {"exists": {"field": "visitors"}},
                            "script": {"source": 'return doc["visitors"].value;'},
                        }
                    },
                ),
            ]
        )

        es_model = MLModel.import_ltr_model(
            ES_TEST_CLIENT,
            model_id,
            ranker,
            ltr_model_config,
            es_compress_model_definition=compress_model_definition,
        )

        # Verify the saved inference config contains the passed LTR config
        response = ES_TEST_CLIENT.ml.get_trained_models(model_id=model_id)
        assert response.meta.status == 200
        assert response.body["count"] == 1

        saved_trained_model_config = response.body["trained_model_configs"][0]

        assert "input" in saved_trained_model_config
        assert "field_names" in saved_trained_model_config["input"]

        if not ES_IS_SERVERLESS and ES_VERSION < (8, 15):
            assert len(saved_trained_model_config["input"]["field_names"]) == 3
        else:
            assert not len(saved_trained_model_config["input"]["field_names"])

        saved_inference_config = saved_trained_model_config["inference_config"]

        assert "learning_to_rank" in saved_inference_config
        assert "feature_extractors" in saved_inference_config["learning_to_rank"]
        saved_feature_extractors = saved_inference_config["learning_to_rank"][
            "feature_extractors"
        ]

        assert all(
            feature_extractor.to_dict() in saved_feature_extractors
            for feature_extractor in ltr_model_config.feature_extractors
        )

        # Execute search with rescoring
        search_result = ES_TEST_CLIENT.search(
            index=NATIONAL_PARKS_INDEX_NAME,
            query={"terms": {"_id": ["park_yosemite", "park_everglades"]}},
            rescore={
                "learning_to_rank": {
                    "model_id": model_id,
                    "params": {"query_string": "yosemite"},
                },
                "window_size": 2,
            },
        )

        # Assert that rescored search result match predition.
        doc_scores = [hit["_score"] for hit in search_result["hits"]["hits"]]

        feature_logger = FeatureLogger(
            ES_TEST_CLIENT, NATIONAL_PARKS_INDEX_NAME, ltr_model_config
        )
        expected_scores = sorted(
            [
                ranker.predict(np.asarray([doc_features]))[0]
                for _, doc_features in feature_logger.extract_features(
                    {"query_string": "yosemite"}, ["park_yosemite", "park_everglades"]
                ).items()
            ],
            reverse=True,
        )

        expected_scores = self._normalize_ltr_score_from_XGBRanker(
            ranker, ltr_model_config, expected_scores
        )

        np.testing.assert_almost_equal(expected_scores, doc_scores, decimal=2)

        # Verify prediction is not supported for LTR
        try:
            es_model.predict([0])
        except NotImplementedError:
            pass

        # Clean up
        ES_TEST_CLIENT.cluster.health(
            index=".ml-*", wait_for_active_shards="all"
        )  # Added to prevent flakiness in the test
        es_model.delete_model()

    @requires_sklearn
    @pytest.mark.parametrize("compress_model_definition", [True, False])
    def test_random_forest_classifier(self, compress_model_definition):
        # Train model
        training_data = datasets.make_classification(n_features=5)
        classifier = RandomForestClassifier()
        classifier.fit(training_data[0], training_data[1])

        # Serialise the models to Elasticsearch
        feature_names = ["f0", "f1", "f2", "f3", "f4"]
        model_id = "test_random_forest_classifier"

        es_model = MLModel.import_model(
            ES_TEST_CLIENT,
            model_id,
            classifier,
            feature_names,
            es_if_exists="replace",
            es_compress_model_definition=compress_model_definition,
        )
        # Get some test results
        check_prediction_equality(
            es_model, classifier, random_rows(training_data[0], 20)
        )

        # Clean up

        es_model.delete_model()

    @requires_sklearn
    @pytest.mark.parametrize("compress_model_definition", [True, False])
    def test_random_forest_regressor(self, compress_model_definition):
        # Train model
        training_data = datasets.make_regression(n_features=5)
        regressor = RandomForestRegressor()
        regressor.fit(training_data[0], training_data[1])

        # Serialise the models to Elasticsearch
        feature_names = ["f0", "f1", "f2", "f3", "f4"]
        model_id = "test_random_forest_regressor"

        es_model = MLModel.import_model(
            ES_TEST_CLIENT,
            model_id,
            regressor,
            feature_names,
            es_if_exists="replace",
            es_compress_model_definition=compress_model_definition,
        )
        # Get some test results
        check_prediction_equality(
            es_model, regressor, random_rows(training_data[0], 20)
        )

        match = f"Trained machine learning model {model_id} already exists"
        with pytest.raises(ValueError, match=match):
            MLModel.import_model(
                ES_TEST_CLIENT,
                model_id,
                regressor,
                feature_names,
                es_if_exists="fail",
                es_compress_model_definition=compress_model_definition,
            )

        # Clean up
        es_model.delete_model()

    @requires_xgboost
    @pytest.mark.parametrize("compress_model_definition", [True, False])
    @pytest.mark.parametrize("multi_class", [True, False])
    def test_xgb_classifier(self, compress_model_definition, multi_class):
        # test both multiple and binary classification
        if multi_class:
            skip_if_multiclass_classifition()
            training_data = datasets.make_classification(
                n_features=5, n_classes=3, n_informative=3
            )
            classifier = XGBClassifier(
                booster="gbtree", objective="multi:softmax", use_label_encoder=False
            )
        else:
            training_data = datasets.make_classification(n_features=5)
            classifier = XGBClassifier(booster="gbtree", use_label_encoder=False)

        # Train model
        classifier.fit(training_data[0], training_data[1])

        # Serialise the models to Elasticsearch
        feature_names = ["f0", "f1", "f2", "f3", "f4"]
        model_id = "test_xgb_classifier"

        es_model = MLModel.import_model(
            ES_TEST_CLIENT,
            model_id,
            classifier,
            feature_names,
            es_if_exists="replace",
            es_compress_model_definition=compress_model_definition,
        )
        # Get some test results
        check_prediction_equality(
            es_model, classifier, random_rows(training_data[0], 20)
        )

        # Clean up
        es_model.delete_model()

    @requires_xgboost
    @pytest.mark.parametrize(
        "objective", ["multi:softmax", "multi:softprob", "binary:logistic"]
    )
    @pytest.mark.parametrize("booster", ["gbtree", "dart"])
    def test_xgb_classifier_objectives_and_booster(self, objective, booster):
        # test both multiple and binary classification
        if objective.startswith("multi"):
            skip_if_multiclass_classifition()
            training_data = datasets.make_classification(
                n_features=5, n_classes=3, n_informative=3
            )
            classifier = XGBClassifier(
                booster=booster, objective=objective, use_label_encoder=False
            )
        else:
            training_data = datasets.make_classification(n_features=5)
            classifier = XGBClassifier(
                booster=booster, objective=objective, use_label_encoder=False
            )

        # Train model
        classifier.fit(training_data[0], training_data[1])

        # Serialise the models to Elasticsearch
        feature_names = ["feature0", "feature1", "feature2", "feature3", "feature4"]
        model_id = "test_xgb_classifier"

        es_model = MLModel.import_model(
            ES_TEST_CLIENT, model_id, classifier, feature_names, es_if_exists="replace"
        )
        # Get some test results
        check_prediction_equality(
            es_model, classifier, random_rows(training_data[0], 20)
        )

        # Clean up
        es_model.delete_model()

    @requires_xgboost
    @pytest.mark.parametrize("compress_model_definition", [True, False])
    @pytest.mark.parametrize(
        "objective",
        ["rank:ndcg", "rank:map", "rank:pairwise"],
    )
    def test_xgb_ranker(self, compress_model_definition, objective):
        X, y = datasets.make_classification(n_features=5)
        rng = np.random.default_rng()
        qid = rng.integers(0, 3, size=X.shape[0])

        # Sort the inputs based on query index
        sorted_idx = np.argsort(qid)
        X = X[sorted_idx, :]
        y = y[sorted_idx]
        qid = qid[sorted_idx]

        ranker = XGBRanker(objective=objective)
        ranker.fit(X, y, qid=qid)

        # Serialise the models to Elasticsearch
        feature_names = ["f0", "f1", "f2", "f3", "f4"]
        model_id = "test_xgb_ranker"

        es_model = MLModel.import_model(
            ES_TEST_CLIENT,
            model_id,
            ranker,
            feature_names,
            es_if_exists="replace",
            es_compress_model_definition=compress_model_definition,
        )

        # Get some test results
        check_prediction_equality(es_model, ranker, random_rows(X, 20))

        # Clean up
        es_model.delete_model()

    @requires_xgboost
    @pytest.mark.parametrize("compress_model_definition", [True, False])
    @pytest.mark.parametrize(
        "objective",
        [
            "reg:squarederror",
            "reg:squaredlogerror",
            "reg:linear",
            "reg:logistic",
            "reg:pseudohubererror",
        ],
    )
    @pytest.mark.parametrize("booster", ["gbtree", "dart"])
    def test_xgb_regressor(self, compress_model_definition, objective, booster):
        # Train model
        training_data = datasets.make_regression(n_features=5)
        regressor = XGBRegressor(objective=objective, booster=booster)
        regressor.fit(
            training_data[0],
            np.exp(training_data[1] - np.max(training_data[1]))
            / sum(np.exp(training_data[1])),
        )

        # Serialise the models to Elasticsearch
        feature_names = ["f0", "f1", "f2", "f3", "f4"]
        model_id = "test_xgb_regressor"

        es_model = MLModel.import_model(
            ES_TEST_CLIENT,
            model_id,
            regressor,
            feature_names,
            es_if_exists="replace",
            es_compress_model_definition=compress_model_definition,
        )
        # Get some test results
        check_prediction_equality(
            es_model, regressor, random_rows(training_data[0], 20)
        )

        # Clean up
        es_model.delete_model()

    @requires_xgboost
    def test_predict_single_feature_vector(self):
        # Train model
        training_data = datasets.make_regression(n_features=1)
        regressor = XGBRegressor()
        regressor.fit(training_data[0], training_data[1])

        # Get some test results
        test_data = [[0.1]]
        test_results = regressor.predict(np.asarray(test_data))

        # Serialise the models to Elasticsearch
        feature_names = ["f0"]
        model_id = "test_xgb_regressor"

        es_model = MLModel.import_model(
            ES_TEST_CLIENT, model_id, regressor, feature_names, es_if_exists="replace"
        )

        # Single feature
        es_results = es_model.predict(test_data[0])

        np.testing.assert_almost_equal(test_results, es_results, decimal=2)

        # Clean up
        es_model.delete_model()

    @requires_lightgbm
    @pytest.mark.parametrize("compress_model_definition", [True, False])
    @pytest.mark.parametrize(
        "objective",
        ["regression", "regression_l1", "huber", "fair", "quantile", "mape"],
    )
    @pytest.mark.parametrize("booster", ["gbdt", "rf", "dart", "goss"])
    def test_lgbm_regressor(self, compress_model_definition, objective, booster):
        # Train model
        training_data = datasets.make_regression(n_features=5)
        if booster == "rf":
            regressor = LGBMRegressor(
                boosting_type=booster,
                objective=objective,
                bagging_fraction=0.5,
                bagging_freq=3,
            )
        else:
            regressor = LGBMRegressor(boosting_type=booster, objective=objective)
        regressor.fit(training_data[0], training_data[1])

        # Serialise the models to Elasticsearch
        feature_names = ["Column_0", "Column_1", "Column_2", "Column_3", "Column_4"]
        model_id = "test_lgbm_regressor"

        es_model = MLModel.import_model(
            ES_TEST_CLIENT,
            model_id,
            regressor,
            feature_names,
            es_if_exists="replace",
            es_compress_model_definition=compress_model_definition,
        )
        # Get some test results
        check_prediction_equality(
            es_model, regressor, random_rows(training_data[0], 20)
        )

        # Clean up
        es_model.delete_model()

    @requires_lightgbm
    @pytest.mark.parametrize("compress_model_definition", [True, False])
    @pytest.mark.parametrize("objective", ["binary", "multiclass", "multiclassova"])
    @pytest.mark.parametrize("booster", ["gbdt", "dart", "goss"])
    def test_lgbm_classifier_objectives_and_booster(
        self, compress_model_definition, objective, booster
    ):
        # test both multiple and binary classification
        if objective.startswith("multi"):
            skip_if_multiclass_classifition()
            training_data = datasets.make_classification(
                n_features=5, n_classes=3, n_informative=3
            )
            classifier = LGBMClassifier(boosting_type=booster, objective=objective)
        else:
            training_data = datasets.make_classification(n_features=5)
            classifier = LGBMClassifier(boosting_type=booster, objective=objective)

        # Train model
        classifier.fit(training_data[0], training_data[1])

        # Serialise the models to Elasticsearch
        feature_names = ["Column_0", "Column_1", "Column_2", "Column_3", "Column_4"]
        model_id = "test_lgbm_classifier"

        es_model = MLModel.import_model(
            ES_TEST_CLIENT,
            model_id,
            classifier,
            feature_names,
            es_if_exists="replace",
            es_compress_model_definition=compress_model_definition,
        )

        check_prediction_equality(
            es_model, classifier, random_rows(training_data[0], 20)
        )

        # Clean up
        es_model.delete_model()
