=========
Changelog
=========

9.0.0 (2025-04-15)
------------------

* Drop Python 3.8, Support Python 3.12 (`#743 <https://github.com/elastic/eland/pull/743>`_)
* Support Pandas 2 (`#742 <https://github.com/elastic/eland/pull/742>`_)
* Upgrade transformers to 4.47 (`#752 <https://github.com/elastic/eland/pull/752>`_)
* Remove ML model export as sklearn Pipeline (`#744 <https://github.com/elastic/eland/pull/744>`_)
* Allow scikit-learn 1.5 (`#729 <https://github.com/elastic/eland/pull/729>`_)
* Migrate docs from AsciiDoc to Markdown (`#762 <https://github.com/elastic/eland/pull/762>`_)

8.17.0 (2025-01-07)
-------------------

* Support sparse embedding models such as SPLADE-v3-DistilBERT (`#740 <https://github.com/elastic/eland/pull/740>`_)

8.16.0 (2024-11-13)
-------------------

* Add deprecation warning for ESGradientBoostingModel subclasses (`#738 <https://github.com/elastic/eland/pull/738>`_)

8.15.4 (2024-10-17)
-------------------

* Revert "Allow reading Elasticsearch certs in Wolfi image" (`#734 <https://github.com/elastic/eland/pull/734>`_)

8.15.3 (2024-10-09)
-------------------

* Added support for DeBERTa-V2 tokenizer (`#717 <https://github.com/elastic/eland/pull/717>`_)
* Fixed ``--ca-cert`` with a shared Elasticsearch Docker volume (`#732 <https://github.com/elastic/eland/pull/732>`_)

8.15.2 (2024-10-02)
-------------------

* Fixed Docker image build (`#728 <https://github.com/elastic/eland/pull/728>`_)

8.15.1 (2024-10-01)
-------------------

* Upgraded PyTorch to version 2.3.1, which is compatible with Elasticsearch 8.15.2 or above (`#718 <https://github.com/elastic/eland/pull/718>`_)
* Migrated to distroless Wolfi base Docker image (`#720 <https://github.com/elastic/eland/pull/720>`_)


8.15.0 (2024-08-12)
-------------------

* Added a default truncation of ``second`` for text similarity (`#713 <https://github.com/elastic/eland/pull/713>`_)
* Added note about using text_similarity for rerank in the CLI (`#716 <https://github.com/elastic/eland/pull/716>`_)
* Added support for lists in result hits (`#707 <https://github.com/elastic/eland/pull/707>`_)
* Removed input fields from exported LTR models (`#708 <https://github.com/elastic/eland/pull/708>`_)

8.14.0 (2024-06-10)
-------------------

Added
^^^^^

* Added Elasticsearch Serverless support in DataFrames (`#690`_, contributed by `@AshokChoudhary11`_) and eland_import_hub_model (`#698`_)

Fixed
^^^^^

* Fixed Python 3.8 support (`#695`_, contributed by `@bartbroere`_)
* Fixed non _source fields missing from the results hits (`#693`_, contributed by `@bartbroere`_)

.. _@AshokChoudhary11: https://github.com/AshokChoudhary11
.. _#690: https://github.com/elastic/eland/pull/690
.. _#693: https://github.com/elastic/eland/pull/693
.. _#695: https://github.com/elastic/eland/pull/695
.. _#698: https://github.com/elastic/eland/pull/698

8.13.1 (2024-05-03)
-------------------

Added
^^^^^

* Added support for HTTP proxies in eland_import_hub_model (`#688`_)

.. _#688: https://github.com/elastic/eland/pull/688

8.13.0 (2024-03-27)
-------------------

Added
^^^^^

* Added support for Python 3.11 (`#681`_) 
* Added ``eland.DataFrame.to_json`` function (`#661`_, contributed by `@bartbroere`_)
* Added override option to specify the model's max input size (`#674`_)

Changed
^^^^^^^

* Upgraded torch to 2.1.2 (`#671`_)
* Mirrored pandas' ``lineterminator`` instead of ``line_terminator`` in ``to_csv`` (`#595`_, contributed by `@bartbroere`_)

.. _#595: https://github.com/elastic/eland/pull/595
.. _#661: https://github.com/elastic/eland/pull/661
.. _#671: https://github.com/elastic/eland/pull/671
.. _#674: https://github.com/elastic/eland/pull/674
.. _#681: https://github.com/elastic/eland/pull/681


8.12.1 (2024-01-30)
-------------------

Fixed
^^^^^

* Fix missing value support for XGBRanker (`#654`_)

.. _#654: https://github.com/elastic/eland/pull/654


8.12.0 (2024-01-18)
-------------------

Added
^^^^^

* Supported XGBRanker model (`#649`_)
* Accepted LTR (Learning to rank) model config when importing model (`#645`_, `#651`_)
* Added LTR feature logger (`#648`_)
* Added ``prefix_string`` config option to the import model hub script (`#642`_)
* Made online retail analysis notebook runnable in Colab (`#641`_)
* Added new movie dataset to the tests (`#646`_)


.. _#641: https://github.com/elastic/eland/pull/641
.. _#642: https://github.com/elastic/eland/pull/642
.. _#645: https://github.com/elastic/eland/pull/645
.. _#646: https://github.com/elastic/eland/pull/646
.. _#648: https://github.com/elastic/eland/pull/648
.. _#649: https://github.com/elastic/eland/pull/649
.. _#651: https://github.com/elastic/eland/pull/651

8.11.1 (2023-11-22)
-------------------
Added
^^^^^

* Make demo notebook runnable in Colab (`#630`_)

Changed
^^^^^^^

* Bump Shap version to 0.43 (`#636`_)

Fixed
^^^^^

* Fix failed import of Sentence Transformer RoBERTa models  (`#637`_)


.. _#630: https://github.com/elastic/eland/pull/630
.. _#636: https://github.com/elastic/eland/pull/636
.. _#637: https://github.com/elastic/eland/pull/637

8.11.0 (2023-11-08)
-------------------

Added
^^^^^

* Support E5 small multilingual model (`#625`_)

Changed
^^^^^^^

* Stream writes in ``ed.DataFrame.to_csv()`` (`#579`_)
* Improve memory estimation for NLP models (`#568`_)

Fixed
^^^^^

* Fixed deprecations in preparation of Pandas 2.0 support (`#602`_, `#603`_, contributed by `@bartbroere`_)


.. _#568: https://github.com/elastic/eland/pull/568
.. _#579: https://github.com/elastic/eland/pull/579
.. _#602: https://github.com/elastic/eland/pull/602
.. _#603: https://github.com/elastic/eland/pull/603
.. _#625: https://github.com/elastic/eland/pull/625

8.10.1 (2023-10-11)
-------------------

Fixed
^^^^^

* Fixed direct usage of TransformerModel (`#619`_)

.. _#619: https://github.com/elastic/eland/pull/619

8.10.0 (2023-10-09)
-------------------

Added
^^^^^

* Published pre-built Docker images to docker.elastic.co/eland/eland (`#613`_)
* Allowed importing private HuggingFace models (`#608`_)
* Added Apple Silicon (arm64) support to Docker image (`#615`_)
* Allowed importing some DPR models like ance-dpr-context-multi (`#573`_)
* Allowed using the Pandas API without monitoring/main permissions (`#581`_)

Changed
^^^^^^^

* Updated Docker image to Debian 12 Bookworm (`#613`_)
* Reduced Docker image size by not installing unused PyTorch GPU support on amd64 (`#615`_)
* Reduced model chunk size to 1MB (`#605`_)

Fixed
^^^^^

* Fixed deprecations in preparation of Pandas 2.0 support (`#593`_, `#596`_, contributed by `@bartbroere`_)

.. _@bartbroere: https://github.com/bartbroere
.. _#613: https://github.com/elastic/eland/pull/613
.. _#608: https://github.com/elastic/eland/pull/608
.. _#615: https://github.com/elastic/eland/pull/615
.. _#573: https://github.com/elastic/eland/pull/573
.. _#581: https://github.com/elastic/eland/pull/581
.. _#605: https://github.com/elastic/eland/pull/605
.. _#593: https://github.com/elastic/eland/pull/593
.. _#596: https://github.com/elastic/eland/pull/596

8.9.0 (2023-08-24)
------------------

Added
^^^^^

* Simplify embedding model support and loading (`#569`_)
* Make eland_import_hub_model easier to find on Windows (`#559`_)
* Update trained model inference endpoint (`#556`_)
* Add BertJapaneseTokenizer support with bert_ja tokenization configuration (`#534`_)
* Add ability to upload xlm-roberta tokenized models (`#518`_)
* Tolerate different model output formats when measuring embedding size (`#535`_)
* Generate valid NLP model id from file path (`#541`_)
* Upgrade torch to 1.13.1 and check the cluster version before uploading a NLP model (`#522`_)
* Set embedding_size config parameter for Text Embedding models (`#532`_)
* Add support for the pass_through task (`#526`_)

Fixed
^^^^^

* Fixed black to comply with the code style (`#557`_)
* Fixed No module named 'torch' (`#553`_)
* Fix autosummary directive by removing hack autosummaries (`#548`_)
* Prevent TypeError with None check (`#525`_)

.. _#518: https://github.com/elastic/eland/pull/518
.. _#522: https://github.com/elastic/eland/pull/522
.. _#525: https://github.com/elastic/eland/pull/525
.. _#526: https://github.com/elastic/eland/pull/526
.. _#532: https://github.com/elastic/eland/pull/532
.. _#534: https://github.com/elastic/eland/pull/534
.. _#535: https://github.com/elastic/eland/pull/535
.. _#541: https://github.com/elastic/eland/pull/541
.. _#548: https://github.com/elastic/eland/pull/548
.. _#553: https://github.com/elastic/eland/pull/553
.. _#556: https://github.com/elastic/eland/pull/556
.. _#557: https://github.com/elastic/eland/pull/557
.. _#559: https://github.com/elastic/eland/pull/559
.. _#569: https://github.com/elastic/eland/pull/569


8.7.0 (2023-03-30)
------------------

Added
^^^^^

* Added a new NLP model task type "text_similarity" (`#486`_)
* Added a new NLP model task type "text_expansion" (`#520`_)
* Added support for exporting an Elastic ML model as a scikit-learn pipeline via ``MLModel.export_model()`` (`#509`_)

Fixed
^^^^^

* Fixed an issue that occurred when LightGBM was installed but libomp wasn't installed on the system. (`#499`_)

.. _#486: https://github.com/elastic/eland/pull/486
.. _#499: https://github.com/elastic/eland/pull/499
.. _#509: https://github.com/elastic/eland/pull/509
.. _#520: https://github.com/elastic/eland/pull/520


8.3.0 (2022-07-11)
------------------

Added
^^^^^

* Added a new NLP model task type "auto" which infers the task type based on model configuration and architecture  (`#475`_)

Changed
^^^^^^^

* Changed required version of 'torch' package to `>=1.11.0,<1.12` to match required PyTorch version for Elasticsearch 8.3 (was `>=1.9.0,<2`) (`#479`_)
* Changed the default value of the `--task-type` parameter for the `eland_import_hub_model` CLI to be "auto" (`#475`_)

Fixed
^^^^^

* Fixed decision tree classifier serialization to account for probabilities (`#465`_)
* Fixed PyTorch model quantization (`#472`_)

.. _#465: https://github.com/elastic/eland/pull/465
.. _#472: https://github.com/elastic/eland/pull/472
.. _#475: https://github.com/elastic/eland/pull/475
.. _#479: https://github.com/elastic/eland/pull/479


8.2.0 (2022-05-09)
------------------

Added
^^^^^

* Added support for passing Cloud ID via ``--cloud-id`` to ``eland_import_hub_model`` CLI tool (`#462`_)
* Added support for authenticating via ``--es-username``, ``--es-password``, and ``--es-api-key`` to the ``eland_import_hub_model`` CLI tool (`#461`_)
* Added support for XGBoost 1.6 (`#458`_)
* Added support for ``question_answering`` NLP tasks (`#457`_)

.. _#457: https://github.com/elastic/eland/pull/457
.. _#458: https://github.com/elastic/eland/pull/458
.. _#461: https://github.com/elastic/eland/pull/461
.. _#462: https://github.com/elastic/eland/pull/462


8.1.0 (2022-03-31)
------------------

Added
^^^^^

* Added support for ``eland.Series.unique()`` (`#448`_, contributed by `@V1NAY8`_)
* Added ``--ca-certs`` and ``--insecure`` options to ``eland_import_hub_model`` for configuring TLS (`#441`_)

.. _#448: https://github.com/elastic/eland/pull/448
.. _#441: https://github.com/elastic/eland/pull/441


8.0.0 (2022-02-10)
------------------

Added
^^^^^

* Added support for Natural Language Processing (NLP) models using PyTorch (`#394`_)
* Added new extra ``eland[pytorch]`` for installing all dependencies needed for PyTorch (`#394`_)
* Added a CLI script ``eland_import_hub_model`` for uploading HuggingFace models to Elasticsearch (`#403`_)
* Added support for v8.0 of the Python Elasticsearch client (`#415`_)
* Added a warning if Eland detects it's communicating with an incompatible Elasticsearch version (`#419`_)
* Added support for ``number_samples`` to LightGBM and Scikit-Learn models (`#397`_, contributed by `@V1NAY8`_)
* Added ability to use datetime types for filtering dataframes (`284`_, contributed by `@Fju`_)
* Added pandas ``datetime64`` type to use the Elasticsearch ``date`` type (`#425`_, contributed by `@Ashton-Sidhu`_)
* Added ``es_verify_mapping_compatibility`` parameter to disable schema enforcement with ``pandas_to_eland`` (`#423`_, contributed by `@Ashton-Sidhu`_)

Changed
^^^^^^^

* Changed ``to_pandas()`` to only use Point-in-Time and ``search_after`` instead of using Scroll APIs
  for pagination.

.. _@Fju: https://github.com/Fju
.. _@Ashton-Sidhu: https://github.com/Ashton-Sidhu
.. _#419: https://github.com/elastic/eland/pull/419
.. _#415: https://github.com/elastic/eland/pull/415
.. _#397: https://github.com/elastic/eland/pull/397
.. _#394: https://github.com/elastic/eland/pull/394
.. _#403: https://github.com/elastic/eland/pull/403
.. _#284: https://github.com/elastic/eland/pull/284
.. _#424: https://github.com/elastic/eland/pull/425
.. _#423: https://github.com/elastic/eland/pull/423


7.14.1b1 (2021-08-30)
---------------------

Added
^^^^^

* Added support for ``DataFrame.iterrows()`` and ``DataFrame.itertuples()`` (`#380`_, contributed by `@kxbin`_)

Performance
^^^^^^^^^^^

* Simplified result collectors to increase performance transforming Elasticsearch results to pandas (`#378`_, contributed by `@V1NAY8`_)
* Changed search pagination function to yield batches of hits (`#379`_)

.. _@kxbin: https://github.com/kxbin
.. _#378: https://github.com/elastic/eland/pull/378
.. _#379: https://github.com/elastic/eland/pull/379
.. _#380: https://github.com/elastic/eland/pull/380


7.14.0b1 (2021-08-09)
---------------------

Added
^^^^^

* Added support for Pandas 1.3.x (`#362`_, contributed by `@V1NAY8`_)
* Added support for LightGBM 3.x (`#362`_, contributed by `@V1NAY8`_)
* Added ``DataFrame.idxmax()`` and ``DataFrame.idxmin()`` methods (`#353`_, contributed by `@V1NAY8`_)
* Added type hints to ``eland.ndframe`` and ``eland.operations`` (`#366`_, contributed by `@V1NAY8`_)

Removed
^^^^^^^

* Removed support for Pandas <1.2 (`#364`_)
* Removed support for Python 3.6 to match Pandas (`#364`_)

Changed
^^^^^^^

* Changed paginated search function to use `Point-in-Time`_ and `Search After`_ features
  instead of Scroll when connected to Elasticsearch 7.12+ (`#370`_ and `#376`_, contributed by `@V1NAY8`_)
* Optimized the ``FieldMappings.aggregate_field_name()`` method (`#373`_, contributed by `@V1NAY8`_)

 .. _Point-in-Time: https://www.elastic.co/guide/en/elasticsearch/reference/current/point-in-time-api.html
 .. _Search After: https://www.elastic.co/guide/en/elasticsearch/reference/7.14/paginate-search-results.html#search-after
 .. _#353: https://github.com/elastic/eland/pull/353 
 .. _#362: https://github.com/elastic/eland/pull/362
 .. _#364: https://github.com/elastic/eland/pull/364
 .. _#366: https://github.com/elastic/eland/pull/366
 .. _#370: https://github.com/elastic/eland/pull/370
 .. _#373: https://github.com/elastic/eland/pull/373
 .. _#376: https://github.com/elastic/eland/pull/376


7.13.0b1 (2021-06-22)
---------------------

Added
^^^^^

* Added ``DataFrame.quantile()``, ``Series.quantile()``, and
  ``DataFrameGroupBy.quantile()`` aggregations (`#318`_ and `#356`_, contributed by `@V1NAY8`_)

Changed
^^^^^^^

* Changed the error raised when ``es_index_pattern`` doesn't point to any indices
  to be more user-friendly (`#346`_)

Fixed
^^^^^

* Fixed a warning about conflicting field types when wildcards are used
  in ``es_index_pattern`` (`#346`_)

* Fixed sorting when using ``DataFrame.groupby()`` with ``dropna``
  (`#322`_, contributed by `@V1NAY8`_)

* Fixed deprecated usage ``numpy.int`` in favor of ``numpy.int_`` (`#354`_, contributed by `@V1NAY8`_)

 .. _#318: https://github.com/elastic/eland/pull/318
 .. _#322: https://github.com/elastic/eland/pull/322
 .. _#346: https://github.com/elastic/eland/pull/346
 .. _#354: https://github.com/elastic/eland/pull/354
 .. _#356: https://github.com/elastic/eland/pull/356


7.10.1b1 (2021-01-12)
---------------------

Added
^^^^^

* Added support for Pandas 1.2.0 (`#336`_)

* Added ``DataFrame.mode()`` and ``Series.mode()`` aggregation (`#323`_, contributed by `@V1NAY8`_)

* Added support for ``pd.set_option("display.max_rows", None)``
  (`#308`_, contributed by `@V1NAY8`_)

* Added Elasticsearch storage usage to ``df.info()`` (`#321`_, contributed by `@V1NAY8`_)

Removed
^^^^^^^

* Removed deprecated aliases ``read_es``, ``read_csv``, ``DataFrame.info_es``,
  and ``MLModel(overwrite=True)`` (`#331`_, contributed by `@V1NAY8`_)

 .. _#336: https://github.com/elastic/eland/pull/336
 .. _#331: https://github.com/elastic/eland/pull/331
 .. _#323: https://github.com/elastic/eland/pull/323
 .. _#321: https://github.com/elastic/eland/pull/321
 .. _#308: https://github.com/elastic/eland/pull/308


7.10.0b1 (2020-10-29)
---------------------

Added
^^^^^

* Added ``DataFrame.groupby()`` method with all aggregations
  (`#278`_, `#291`_, `#292`_, `#300`_ contributed by `@V1NAY8`_)

* Added ``es_match()`` method to ``DataFrame`` and ``Series`` for
  filtering rows with full-text search (`#301`_)

* Added support for type hints of the ``elasticsearch-py`` package (`#295`_)

* Added support for passing dictionaries to ``es_type_overrides`` parameter
  in the ``pandas_to_eland()`` function to directly control the field mapping
  generated in Elasticsearch (`#310`_)

* Added ``es_dtypes`` property to ``DataFrame`` and ``Series`` (`#285`_) 

Changed
^^^^^^^

* Changed ``pandas_to_eland()`` to use the ``parallel_bulk()``
  helper instead of single-threaded ``bulk()`` helper to improve
  performance (`#279`_, contributed by `@V1NAY8`_)

* Changed the ``es_type_overrides`` parameter in ``pandas_to_eland()``
  to raise ``ValueError`` if an unknown column is given (`#302`_)

* Changed ``DataFrame.filter()`` to preserve the order of items
  (`#283`_, contributed by `@V1NAY8`_)

* Changed when setting ``es_type_overrides={"column": "text"}`` in
  ``pandas_to_eland()`` will automatically add the ``column.keyword``
  sub-field so that aggregations are available for the field as well (`#310`_)

Fixed
^^^^^

* Fixed ``Series.__repr__`` when the series is empty (`#306`_)

 .. _#278: https://github.com/elastic/eland/pull/278
 .. _#279: https://github.com/elastic/eland/pull/279
 .. _#283: https://github.com/elastic/eland/pull/283
 .. _#285: https://github.com/elastic/eland/pull/285
 .. _#291: https://github.com/elastic/eland/pull/291
 .. _#292: https://github.com/elastic/eland/pull/292
 .. _#295: https://github.com/elastic/eland/pull/295
 .. _#300: https://github.com/elastic/eland/pull/300
 .. _#301: https://github.com/elastic/eland/pull/301
 .. _#302: https://github.com/elastic/eland/pull/302
 .. _#306: https://github.com/elastic/eland/pull/306
 .. _#310: https://github.com/elastic/eland/pull/310


7.9.1a1 (2020-09-29)
--------------------

Added
^^^^^

* Added the ``predict()`` method and ``model_type``,
  ``feature_names``, and ``results_field`` properties
  to ``MLModel``  (`#266`_)


Deprecated
^^^^^^^^^^

* Deprecated ``ImportedMLModel`` in favor of
  ``MLModel.import_model(...)`` (`#266`_)


Changed
^^^^^^^

* Changed DataFrame aggregations to use ``numeric_only=None``
  instead of ``numeric_only=True`` by default. This is the same
  behavior as Pandas (`#270`_, contributed by `@V1NAY8`_)

Fixed
^^^^^

* Fixed ``DataFrame.agg()`` when given a string instead of a list of
  aggregations will now properly return a ``Series`` instead of
  a ``DataFrame`` (`#263`_, contributed by `@V1NAY8`_)


 .. _#263: https://github.com/elastic/eland/pull/263
 .. _#266: https://github.com/elastic/eland/pull/266
 .. _#270: https://github.com/elastic/eland/pull/270


7.9.0a1 (2020-08-18)
--------------------

Added
^^^^^

* Added support for Pandas v1.1 (`#253`_)
* Added support for LightGBM ``LGBMRegressor`` and ``LGBMClassifier`` to ``ImportedMLModel`` (`#247`_, `#252`_)
* Added support for ``multi:softmax`` and ``multi:softprob`` XGBoost operators to ``ImportedMLModel`` (`#246`_)
* Added column names to ``DataFrame.__dir__()`` for better auto-completion support (`#223`_, contributed by `@leonardbinet`_)
* Added support for ``es_if_exists='append'`` to ``pandas_to_eland()`` (`#217`_)
* Added support for aggregating datetimes with ``nunique`` and ``mean`` (`#253`_)
* Added ``es_compress_model_definition`` parameter to ``ImportedMLModel`` constructor (`#220`_)
* Added ``.size`` and ``.ndim`` properties to ``DataFrame`` and ``Series`` (`#231`_ and `#233`_)
* Added ``.dtype`` property to ``Series`` (`#258`_)
* Added support for using ``pandas.Series`` with ``Series.isin()`` (`#231`_)
* Added type hints to many APIs in ``DataFrame`` and ``Series`` (`#231`_)

Deprecated
^^^^^^^^^^

* Deprecated  the ``overwrite`` parameter in favor of ``es_if_exists`` in ``ImportedMLModel`` constructor (`#249`_, contributed by `@V1NAY8`_)

Changed
^^^^^^^

* Changed aggregations for datetimes to be higher precision when available (`#253`_)

Fixed
^^^^^

* Fixed ``ImportedMLModel.predict()`` to fail when ``errors`` are present in the ``ingest.simulate`` response (`#220`_)
* Fixed ``Series.median()`` aggregation to return a scalar instead of ``pandas.Series`` (`#253`_)
* Fixed ``Series.describe()`` to return a ``pandas.Series`` instead of ``pandas.DataFrame`` (`#258`_)
* Fixed ``DataFrame.mean()`` and ``Series.mean()`` dtype (`#258`_)
* Fixed ``DataFrame.agg()`` aggregations when using ``extended_stats`` Elasticsearch aggregation (`#253`_)

 .. _@leonardbinet: https://github.com/leonardbinet
 .. _@V1NAY8: https://github.com/V1NAY8
 .. _#217: https://github.com/elastic/eland/pull/217
 .. _#220: https://github.com/elastic/eland/pull/220
 .. _#223: https://github.com/elastic/eland/pull/223
 .. _#231: https://github.com/elastic/eland/pull/231
 .. _#233: https://github.com/elastic/eland/pull/233
 .. _#246: https://github.com/elastic/eland/pull/246
 .. _#247: https://github.com/elastic/eland/pull/247
 .. _#249: https://github.com/elastic/eland/pull/249
 .. _#252: https://github.com/elastic/eland/pull/252
 .. _#253: https://github.com/elastic/eland/pull/253
 .. _#258: https://github.com/elastic/eland/pull/258


7.7.0a1 (2020-05-20)
--------------------

Added
^^^^^

* Added the package to Conda Forge, install via
  ``conda install -c conda-forge eland`` (`#209`_)
* Added ``DataFrame.sample()`` and ``Series.sample()`` for querying
  a random sample of data from the index (`#196`_, contributed by `@mesejo`_)
* Added ``Series.isna()`` and ``Series.notna()`` for filtering out
  missing, ``NaN`` or null values from a column (`#210`_, contributed by `@mesejo`_)
* Added ``DataFrame.filter()`` and ``Series.filter()`` for reducing an axis
  using a sequence of items or a pattern (`#212`_)
* Added ``DataFrame.to_pandas()`` and ``Series.to_pandas()`` for converting
  an Eland dataframe or series into a Pandas dataframe or series inline (`#208`_)
* Added support for XGBoost v1.0.0 (`#200`_)

Deprecated
^^^^^^^^^^

* Deprecated ``info_es()`` in favor of ``es_info()`` (`#208`_)
* Deprecated ``eland.read_csv()`` in favor of ``eland.csv_to_eland()`` (`#208`_)
* Deprecated ``eland.read_es()`` in favor of ``eland.DataFrame()`` (`#208`_)

Changed
^^^^^^^

* Changed ``var`` and ``std`` aggregations to use sample instead of
  population in line with Pandas (`#185`_)
* Changed painless scripts to use ``source`` rather than ``inline`` to improve
  script caching performance (`#191`_, contributed by `@mesejo`_)
* Changed minimum ``elasticsearch`` Python library version to v7.7.0 (`#207`_)
* Changed name of ``Index.field_name`` to ``Index.es_field_name`` (`#208`_)

Fixed
^^^^^

* Fixed ``DeprecationWarning`` raised from ``pandas.Series`` when an
  an empty series was created without specifying ``dtype`` (`#188`_, contributed by `@mesejo`_)
* Fixed a bug when filtering columns on complex combinations of and and or (`#204`_)
* Fixed an issue where ``DataFrame.shape`` would return a larger value than
  in the index if a sized operation like ``.head(X)`` was applied to the data
  frame (`#205`_, contributed by `@mesejo`_)
* Fixed issue where both ``scikit-learn`` and ``xgboost`` libraries were
  required to use ``eland.ml.ImportedMLModel``, now only one library is
  required to use this feature (`#206`_)

 .. _#200: https://github.com/elastic/eland/pull/200
 .. _#201: https://github.com/elastic/eland/pull/201
 .. _#204: https://github.com/elastic/eland/pull/204
 .. _#205: https://github.com/elastic/eland/pull/205
 .. _#206: https://github.com/elastic/eland/pull/206
 .. _#207: https://github.com/elastic/eland/pull/207
 .. _#191: https://github.com/elastic/eland/pull/191
 .. _#210: https://github.com/elastic/eland/pull/210
 .. _#185: https://github.com/elastic/eland/pull/185
 .. _#188: https://github.com/elastic/eland/pull/188
 .. _#196: https://github.com/elastic/eland/pull/196
 .. _#208: https://github.com/elastic/eland/pull/208
 .. _#209: https://github.com/elastic/eland/pull/209
 .. _#212: https://github.com/elastic/eland/pull/212

7.6.0a5 (2020-04-14)
--------------------

Added
^^^^^

* Added support for Pandas v1.0.0 (`#141`_, contributed by `@mesejo`_)
* Added ``use_pandas_index_for_es_ids`` parameter to ``pandas_to_eland()`` (`#154`_)
* Added ``es_type_overrides`` parameter to ``pandas_to_eland()`` (`#181`_)
* Added ``NDFrame.var()``, ``.std()`` and ``.median()`` aggregations (`#175`_, `#176`_, contributed by `@mesejo`_)
* Added ``DataFrame.es_query()`` to allow modifying ES queries directly (`#156`_)
* Added ``eland.__version__`` (`#153`_, contributed by `@mesejo`_)

Removed
^^^^^^^

* Removed support for Python 3.5 (`#150`_)
* Removed ``eland.Client()`` interface, use
  ``elasticsearch.Elasticsearch()`` client instead (`#166`_)
* Removed all private objects from top-level ``eland`` namespace (`#170`_)
* Removed ``geo_points`` from ``pandas_to_eland()`` in favor of ``es_type_overrides`` (`#181`_)

Changed
^^^^^^^

* Changed ML model serialization to be slightly smaller (`#159`_)
* Changed minimum ``elasticsearch`` Python library version to v7.6.0 (`#181`_)

Fixed
^^^^^

* Fixed ``inference_config`` being required on ML models for ES >=7.8 (`#174`_)
* Fixed unpacking for ``DataFrame.aggregate("median")`` (`#161`_)

 .. _@mesejo: https://github.com/mesejo
 .. _#141: https://github.com/elastic/eland/pull/141
 .. _#150: https://github.com/elastic/eland/pull/150
 .. _#153: https://github.com/elastic/eland/pull/153
 .. _#154: https://github.com/elastic/eland/pull/154
 .. _#156: https://github.com/elastic/eland/pull/156
 .. _#159: https://github.com/elastic/eland/pull/159
 .. _#161: https://github.com/elastic/eland/pull/161
 .. _#166: https://github.com/elastic/eland/pull/166
 .. _#170: https://github.com/elastic/eland/pull/170
 .. _#174: https://github.com/elastic/eland/pull/174
 .. _#175: https://github.com/elastic/eland/pull/175
 .. _#176: https://github.com/elastic/eland/pull/176
 .. _#181: https://github.com/elastic/eland/pull/181

7.6.0a4 (2020-03-23)
--------------------

Changed
^^^^^^^

* Changed requirement for ``xgboost`` from ``>=0.90`` to ``==0.90``

Fixed
^^^^^

* Fixed issue in ``DataFrame.info()`` when called on an empty frame (`#135`_)
* Fixed issues where many ``_source`` fields would generate
  a ``too_long_frame`` error (`#135`_, `#137`_)

 .. _#135: https://github.com/elastic/eland/pull/135
 .. _#137: https://github.com/elastic/eland/pull/137
