# AttendanceSystemIDSC

**Full f4 Folder Upload â€” Attendance System Project**

---

## Project Structure

+-- .gitignore
+-- attendance.db
+-- QR_Attendance.iss
+-- README.md
+-- uploadF4FullBranch.ps1
+-- attendance_app/
|   +-- app.py
|   +-- attendance.db
|   +-- AttendanceLauncher.spec
|   +-- AttendanceLauncher_v1.0.spec
|   +-- awww.py
|   +-- build.bat
|   +-- credentials.txt
|   +-- fix.py
|   +-- launcher.py
|   +-- requirements.txt
|   +-- server.log
|   +-- utils.py
|   +-- __pycache__/
|   |   +-- utils.cpython-311.pyc
|   +-- assets/
|   |   +-- logo.ico
|   +-- build/
|   |   +-- AttendanceLauncher/
|   |   |   +-- Analysis-00.toc
|   |   |   +-- AttendanceLauncher.pkg
|   |   |   +-- base_library.zip
|   |   |   +-- EXE-00.toc
|   |   |   +-- PKG-00.toc
|   |   |   +-- PYZ-00.pyz
|   |   |   +-- PYZ-00.toc
|   |   |   +-- warn-AttendanceLauncher.txt
|   |   |   +-- xref-AttendanceLauncher.html
|   |   |   +-- localpycs/
|   |   |   |   +-- pyimod01_archive.pyc
|   |   |   |   +-- pyimod02_importers.pyc
|   |   |   |   +-- pyimod03_ctypes.pyc
|   |   |   |   +-- pyimod04_pywin32.pyc
|   |   |   |   +-- struct.pyc
|   +-- dist/
|   |   +-- AttendanceLauncher.exe
|   +-- output/
|   +-- static/
|   |   +-- logo.ico
|   |   +-- logo.png
|   +-- templates/
|   |   +-- admin_dashboard.html
|   |   +-- admin_login.html
|   |   +-- change_credentials.html
|   |   +-- index.html
|   |   +-- register.html
|   |   +-- thankyou.html
|   |   +-- static/
|   +-- venv/
|   |   +-- pyvenv.cfg
|   |   +-- Include/
|   |   +-- Lib/
|   |   |   +-- site-packages/
|   |   |   |   +-- distutils-precedence.pth
|   |   |   |   +-- pefile.py
|   |   |   |   +-- peutils.py
|   |   |   |   +-- six.py
|   |   |   |   +-- __pycache__/
|   |   |   |   |   +-- pefile.cpython-311.pyc
|   |   |   |   |   +-- peutils.cpython-311.pyc
|   |   |   |   |   +-- six.cpython-311.pyc
|   |   |   |   +-- _distutils_hack/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- override.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- override.cpython-311.pyc
|   |   |   |   +-- _pyinstaller_hooks_contrib/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- compat.py
|   |   |   |   |   +-- rthooks.dat
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- __init__.cpython-39.pyc
|   |   |   |   |   |   +-- compat.cpython-311.pyc
|   |   |   |   |   +-- pre_find_module_path/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- pre_safe_import_module/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- hook-tensorflow.py
|   |   |   |   |   |   +-- hook-win32com.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-tensorflow.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-win32com.cpython-311.pyc
|   |   |   |   |   +-- rthooks/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- pyi_rth_cryptography_openssl.py
|   |   |   |   |   |   +-- pyi_rth_enchant.py
|   |   |   |   |   |   +-- pyi_rth_ffpyplayer.py
|   |   |   |   |   |   +-- pyi_rth_findlibs.py
|   |   |   |   |   |   +-- pyi_rth_nltk.py
|   |   |   |   |   |   +-- pyi_rth_osgeo.py
|   |   |   |   |   |   +-- pyi_rth_pygraphviz.py
|   |   |   |   |   |   +-- pyi_rth_pyproj.py
|   |   |   |   |   |   +-- pyi_rth_pyqtgraph_multiprocess.py
|   |   |   |   |   |   +-- pyi_rth_pythoncom.py
|   |   |   |   |   |   +-- pyi_rth_pywintypes.py
|   |   |   |   |   |   +-- pyi_rth_tensorflow.py
|   |   |   |   |   |   +-- pyi_rth_traitlets.py
|   |   |   |   |   |   +-- pyi_rth_usb.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_cryptography_openssl.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_enchant.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_ffpyplayer.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_findlibs.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_nltk.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_osgeo.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_pygraphviz.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_pyproj.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_pyqtgraph_multiprocess.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_pythoncom.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_pywintypes.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_tensorflow.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_traitlets.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyi_rth_usb.cpython-311.pyc
|   |   |   |   |   +-- stdhooks/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- hook-_mssql.py
|   |   |   |   |   |   +-- hook-_mysql.py
|   |   |   |   |   |   +-- hook-accessible_output2.py
|   |   |   |   |   |   +-- hook-adbutils.py
|   |   |   |   |   |   +-- hook-adios.py
|   |   |   |   |   |   +-- hook-afmformats.py
|   |   |   |   |   |   +-- hook-aliyunsdkcore.py
|   |   |   |   |   |   +-- hook-altair.py
|   |   |   |   |   |   +-- hook-amazonproduct.py
|   |   |   |   |   |   +-- hook-anyio.py
|   |   |   |   |   |   +-- hook-apkutils.py
|   |   |   |   |   |   +-- hook-appdirs.py
|   |   |   |   |   |   +-- hook-appy.pod.py
|   |   |   |   |   |   +-- hook-apscheduler.py
|   |   |   |   |   |   +-- hook-argon2.py
|   |   |   |   |   |   +-- hook-astor.py
|   |   |   |   |   |   +-- hook-astroid.py
|   |   |   |   |   |   +-- hook-astropy.py
|   |   |   |   |   |   +-- hook-astropy_iers_data.py
|   |   |   |   |   |   +-- hook-av.py
|   |   |   |   |   |   +-- hook-avro.py
|   |   |   |   |   |   +-- hook-azurerm.py
|   |   |   |   |   |   +-- hook-backports.py
|   |   |   |   |   |   +-- hook-backports.zoneinfo.py
|   |   |   |   |   |   +-- hook-bacon.py
|   |   |   |   |   |   +-- hook-bcrypt.py
|   |   |   |   |   |   +-- hook-bitsandbytes.py
|   |   |   |   |   |   +-- hook-black.py
|   |   |   |   |   |   +-- hook-bleak.py
|   |   |   |   |   |   +-- hook-blib2to3.py
|   |   |   |   |   |   +-- hook-blspy.py
|   |   |   |   |   |   +-- hook-bokeh.py
|   |   |   |   |   |   +-- hook-boto.py
|   |   |   |   |   |   +-- hook-boto3.py
|   |   |   |   |   |   +-- hook-botocore.py
|   |   |   |   |   |   +-- hook-branca.py
|   |   |   |   |   |   +-- hook-BTrees.py
|   |   |   |   |   |   +-- hook-cairocffi.py
|   |   |   |   |   |   +-- hook-cairosvg.py
|   |   |   |   |   |   +-- hook-capstone.py
|   |   |   |   |   |   +-- hook-cassandra.py
|   |   |   |   |   |   +-- hook-celpy.py
|   |   |   |   |   |   +-- hook-certifi.py
|   |   |   |   |   |   +-- hook-cf_units.py
|   |   |   |   |   |   +-- hook-cftime.py
|   |   |   |   |   |   +-- hook-charset_normalizer.py
|   |   |   |   |   |   +-- hook-cloudpickle.py
|   |   |   |   |   |   +-- hook-cloudscraper.py
|   |   |   |   |   |   +-- hook-clr.py
|   |   |   |   |   |   +-- hook-clr_loader.py
|   |   |   |   |   |   +-- hook-cmocean.py
|   |   |   |   |   |   +-- hook-compliance_checker.py
|   |   |   |   |   |   +-- hook-comtypes.client.py
|   |   |   |   |   |   +-- hook-countrycode.py
|   |   |   |   |   |   +-- hook-countryinfo.py
|   |   |   |   |   |   +-- hook-Crypto.py
|   |   |   |   |   |   +-- hook-Cryptodome.py
|   |   |   |   |   |   +-- hook-cryptography.py
|   |   |   |   |   |   +-- hook-CTkMessagebox.py
|   |   |   |   |   |   +-- hook-cumm.py
|   |   |   |   |   |   +-- hook-customtkinter.py
|   |   |   |   |   |   +-- hook-cv2.py
|   |   |   |   |   |   +-- hook-cx_Oracle.py
|   |   |   |   |   |   +-- hook-cytoolz.itertoolz.py
|   |   |   |   |   |   +-- hook-dash.py
|   |   |   |   |   |   +-- hook-dash_bootstrap_components.py
|   |   |   |   |   |   +-- hook-dash_core_components.py
|   |   |   |   |   |   +-- hook-dash_html_components.py
|   |   |   |   |   |   +-- hook-dash_renderer.py
|   |   |   |   |   |   +-- hook-dash_table.py
|   |   |   |   |   |   +-- hook-dash_uploader.py
|   |   |   |   |   |   +-- hook-dask.py
|   |   |   |   |   |   +-- hook-datasets.py
|   |   |   |   |   |   +-- hook-dateparser.py
|   |   |   |   |   |   +-- hook-dateparser.utils.strptime.py
|   |   |   |   |   |   +-- hook-dateutil.py
|   |   |   |   |   |   +-- hook-dbus_fast.py
|   |   |   |   |   |   +-- hook-dclab.py
|   |   |   |   |   |   +-- hook-detectron2.py
|   |   |   |   |   |   +-- hook-discid.py
|   |   |   |   |   |   +-- hook-distorm3.py
|   |   |   |   |   |   +-- hook-distributed.py
|   |   |   |   |   |   +-- hook-dns.rdata.py
|   |   |   |   |   |   +-- hook-docutils.py
|   |   |   |   |   |   +-- hook-docx.py
|   |   |   |   |   |   +-- hook-docx2pdf.py
|   |   |   |   |   |   +-- hook-duckdb.py
|   |   |   |   |   |   +-- hook-dynaconf.py
|   |   |   |   |   |   +-- hook-easyocr.py
|   |   |   |   |   |   +-- hook-eccodeslib.py
|   |   |   |   |   |   +-- hook-eckitlib.py
|   |   |   |   |   |   +-- hook-eel.py
|   |   |   |   |   |   +-- hook-emoji.py
|   |   |   |   |   |   +-- hook-enchant.py
|   |   |   |   |   |   +-- hook-eng_to_ipa.py
|   |   |   |   |   |   +-- hook-ens.py
|   |   |   |   |   |   +-- hook-enzyme.parsers.ebml.core.py
|   |   |   |   |   |   +-- hook-eth_abi.py
|   |   |   |   |   |   +-- hook-eth_account.py
|   |   |   |   |   |   +-- hook-eth_hash.py
|   |   |   |   |   |   +-- hook-eth_keyfile.py
|   |   |   |   |   |   +-- hook-eth_keys.py
|   |   |   |   |   |   +-- hook-eth_rlp.py
|   |   |   |   |   |   +-- hook-eth_typing.py
|   |   |   |   |   |   +-- hook-eth_utils.network.py
|   |   |   |   |   |   +-- hook-eth_utils.py
|   |   |   |   |   |   +-- hook-exchangelib.py
|   |   |   |   |   |   +-- hook-fabric.py
|   |   |   |   |   |   +-- hook-fairscale.py
|   |   |   |   |   |   +-- hook-faker.py
|   |   |   |   |   |   +-- hook-falcon.py
|   |   |   |   |   |   +-- hook-fastai.py
|   |   |   |   |   |   +-- hook-fastparquet.py
|   |   |   |   |   |   +-- hook-fckitlib.py
|   |   |   |   |   |   +-- hook-ffpyplayer.py
|   |   |   |   |   |   +-- hook-fiona.py
|   |   |   |   |   |   +-- hook-flask_compress.py
|   |   |   |   |   |   +-- hook-flask_restx.py
|   |   |   |   |   |   +-- hook-flex.py
|   |   |   |   |   |   +-- hook-flirpy.py
|   |   |   |   |   |   +-- hook-fmpy.py
|   |   |   |   |   |   +-- hook-folium.py
|   |   |   |   |   |   +-- hook-freetype.py
|   |   |   |   |   |   +-- hook-frictionless.py
|   |   |   |   |   |   +-- hook-fsspec.py
|   |   |   |   |   |   +-- hook-fvcore.nn.py
|   |   |   |   |   |   +-- hook-gadfly.py
|   |   |   |   |   |   +-- hook-gbulb.py
|   |   |   |   |   |   +-- hook-gcloud.py
|   |   |   |   |   |   +-- hook-geopandas.py
|   |   |   |   |   |   +-- hook-gitlab.py
|   |   |   |   |   |   +-- hook-globus_sdk.py
|   |   |   |   |   |   +-- hook-gmplot.py
|   |   |   |   |   |   +-- hook-gmsh.py
|   |   |   |   |   |   +-- hook-gooey.py
|   |   |   |   |   |   +-- hook-google.api_core.py
|   |   |   |   |   |   +-- hook-google.cloud.bigquery.py
|   |   |   |   |   |   +-- hook-google.cloud.core.py
|   |   |   |   |   |   +-- hook-google.cloud.kms_v1.py
|   |   |   |   |   |   +-- hook-google.cloud.pubsub_v1.py
|   |   |   |   |   |   +-- hook-google.cloud.speech.py
|   |   |   |   |   |   +-- hook-google.cloud.storage.py
|   |   |   |   |   |   +-- hook-google.cloud.translate.py
|   |   |   |   |   |   +-- hook-googleapiclient.model.py
|   |   |   |   |   |   +-- hook-grapheme.py
|   |   |   |   |   |   +-- hook-graphql_query.py
|   |   |   |   |   |   +-- hook-great_expectations.py
|   |   |   |   |   |   +-- hook-gribapi.py
|   |   |   |   |   |   +-- hook-grpc.py
|   |   |   |   |   |   +-- hook-gst._gst.py
|   |   |   |   |   |   +-- hook-gtk.py
|   |   |   |   |   |   +-- hook-h3.py
|   |   |   |   |   |   +-- hook-h5py.py
|   |   |   |   |   |   +-- hook-hdf5plugin.py
|   |   |   |   |   |   +-- hook-hexbytes.py
|   |   |   |   |   |   +-- hook-HtmlTestRunner.py
|   |   |   |   |   |   +-- hook-httplib2.py
|   |   |   |   |   |   +-- hook-humanize.py
|   |   |   |   |   |   +-- hook-hydra.py
|   |   |   |   |   |   +-- hook-ijson.py
|   |   |   |   |   |   +-- hook-imageio.py
|   |   |   |   |   |   +-- hook-imageio_ffmpeg.py
|   |   |   |   |   |   +-- hook-iminuit.py
|   |   |   |   |   |   +-- hook-intake.py
|   |   |   |   |   |   +-- hook-IPython.py
|   |   |   |   |   |   +-- hook-iso639.py
|   |   |   |   |   |   +-- hook-itk.py
|   |   |   |   |   |   +-- hook-jaraco.text.py
|   |   |   |   |   |   +-- hook-jedi.py
|   |   |   |   |   |   +-- hook-jieba.py
|   |   |   |   |   |   +-- hook-jinja2.py
|   |   |   |   |   |   +-- hook-jinxed.py
|   |   |   |   |   |   +-- hook-jira.py
|   |   |   |   |   |   +-- hook-jsonpath_rw_ext.py
|   |   |   |   |   |   +-- hook-jsonrpcserver.py
|   |   |   |   |   |   +-- hook-jsonschema.py
|   |   |   |   |   |   +-- hook-jsonschema_specifications.py
|   |   |   |   |   |   +-- hook-jupyterlab.py
|   |   |   |   |   |   +-- hook-kaleido.py
|   |   |   |   |   |   +-- hook-khmernltk.py
|   |   |   |   |   |   +-- hook-kinterbasdb.py
|   |   |   |   |   |   +-- hook-langchain.py
|   |   |   |   |   |   +-- hook-langchain_classic.py
|   |   |   |   |   |   +-- hook-langcodes.py
|   |   |   |   |   |   +-- hook-langdetect.py
|   |   |   |   |   |   +-- hook-laonlp.py
|   |   |   |   |   |   +-- hook-lark.py
|   |   |   |   |   |   +-- hook-ldfparser.py
|   |   |   |   |   |   +-- hook-lensfunpy.py
|   |   |   |   |   |   +-- hook-libaudioverse.py
|   |   |   |   |   |   +-- hook-librosa.py
|   |   |   |   |   |   +-- hook-lightgbm.py
|   |   |   |   |   |   +-- hook-lightning.py
|   |   |   |   |   |   +-- hook-limits.py
|   |   |   |   |   |   +-- hook-linear_operator.py
|   |   |   |   |   |   +-- hook-lingua.py
|   |   |   |   |   |   +-- hook-litestar.py
|   |   |   |   |   |   +-- hook-llvmlite.py
|   |   |   |   |   |   +-- hook-logilab.py
|   |   |   |   |   |   +-- hook-lxml.etree.py
|   |   |   |   |   |   +-- hook-lxml.isoschematron.py
|   |   |   |   |   |   +-- hook-lxml.objectify.py
|   |   |   |   |   |   +-- hook-lxml.py
|   |   |   |   |   |   +-- hook-lz4.py
|   |   |   |   |   |   +-- hook-magic.py
|   |   |   |   |   |   +-- hook-mako.codegen.py
|   |   |   |   |   |   +-- hook-mariadb.py
|   |   |   |   |   |   +-- hook-markdown.py
|   |   |   |   |   |   +-- hook-mecab.py
|   |   |   |   |   |   +-- hook-metpy.py
|   |   |   |   |   |   +-- hook-migrate.py
|   |   |   |   |   |   +-- hook-mimesis.py
|   |   |   |   |   |   +-- hook-minecraft_launcher_lib.py
|   |   |   |   |   |   +-- hook-mistune.py
|   |   |   |   |   |   +-- hook-mnemonic.py
|   |   |   |   |   |   +-- hook-monai.py
|   |   |   |   |   |   +-- hook-moviepy.audio.fx.all.py
|   |   |   |   |   |   +-- hook-moviepy.video.fx.all.py
|   |   |   |   |   |   +-- hook-mpl_toolkits.basemap.py
|   |   |   |   |   |   +-- hook-msoffcrypto.py
|   |   |   |   |   |   +-- hook-nacl.py
|   |   |   |   |   |   +-- hook-names.py
|   |   |   |   |   |   +-- hook-nanite.py
|   |   |   |   |   |   +-- hook-narwhals.py
|   |   |   |   |   |   +-- hook-nbconvert.py
|   |   |   |   |   |   +-- hook-nbdime.py
|   |   |   |   |   |   +-- hook-nbformat.py
|   |   |   |   |   |   +-- hook-nbt.py
|   |   |   |   |   |   +-- hook-ncclient.py
|   |   |   |   |   |   +-- hook-netCDF4.py
|   |   |   |   |   |   +-- hook-nicegui.py
|   |   |   |   |   |   +-- hook-niquests.py
|   |   |   |   |   |   +-- hook-nltk.py
|   |   |   |   |   |   +-- hook-nnpy.py
|   |   |   |   |   |   +-- hook-notebook.py
|   |   |   |   |   |   +-- hook-numba.py
|   |   |   |   |   |   +-- hook-numbers_parser.py
|   |   |   |   |   |   +-- hook-numcodecs.py
|   |   |   |   |   |   +-- hook-nvidia.cublas.py
|   |   |   |   |   |   +-- hook-nvidia.cuda_cupti.py
|   |   |   |   |   |   +-- hook-nvidia.cuda_nvcc.py
|   |   |   |   |   |   +-- hook-nvidia.cuda_nvrtc.py
|   |   |   |   |   |   +-- hook-nvidia.cuda_runtime.py
|   |   |   |   |   |   +-- hook-nvidia.cudnn.py
|   |   |   |   |   |   +-- hook-nvidia.cufft.py
|   |   |   |   |   |   +-- hook-nvidia.curand.py
|   |   |   |   |   |   +-- hook-nvidia.cusolver.py
|   |   |   |   |   |   +-- hook-nvidia.cusparse.py
|   |   |   |   |   |   +-- hook-nvidia.nccl.py
|   |   |   |   |   |   +-- hook-nvidia.nvjitlink.py
|   |   |   |   |   |   +-- hook-nvidia.nvtx.py
|   |   |   |   |   |   +-- hook-office365.py
|   |   |   |   |   |   +-- hook-onnxruntime.py
|   |   |   |   |   |   +-- hook-opencc.py
|   |   |   |   |   |   +-- hook-OpenGL.py
|   |   |   |   |   |   +-- hook-OpenGL_accelerate.py
|   |   |   |   |   |   +-- hook-openpyxl.py
|   |   |   |   |   |   +-- hook-opentelemetry.py
|   |   |   |   |   |   +-- hook-orjson.py
|   |   |   |   |   |   +-- hook-osgeo.py
|   |   |   |   |   |   +-- hook-pandas_flavor.py
|   |   |   |   |   |   +-- hook-panel.py
|   |   |   |   |   |   +-- hook-parsedatetime.py
|   |   |   |   |   |   +-- hook-parso.py
|   |   |   |   |   |   +-- hook-passlib.py
|   |   |   |   |   |   +-- hook-paste.exceptions.reporter.py
|   |   |   |   |   |   +-- hook-patoolib.py
|   |   |   |   |   |   +-- hook-patsy.py
|   |   |   |   |   |   +-- hook-pdfminer.py
|   |   |   |   |   |   +-- hook-pendulum.py
|   |   |   |   |   |   +-- hook-phonenumbers.py
|   |   |   |   |   |   +-- hook-pingouin.py
|   |   |   |   |   |   +-- hook-pint.py
|   |   |   |   |   |   +-- hook-pinyin.py
|   |   |   |   |   |   +-- hook-platformdirs.py
|   |   |   |   |   |   +-- hook-plotly.py
|   |   |   |   |   |   +-- hook-pointcept.py
|   |   |   |   |   |   +-- hook-pptx.py
|   |   |   |   |   |   +-- hook-prettytable.py
|   |   |   |   |   |   +-- hook-psutil.py
|   |   |   |   |   |   +-- hook-psychopy.py
|   |   |   |   |   |   +-- hook-psycopg_binary.py
|   |   |   |   |   |   +-- hook-psycopg2.py
|   |   |   |   |   |   +-- hook-publicsuffix2.py
|   |   |   |   |   |   +-- hook-pubsub.core.py
|   |   |   |   |   |   +-- hook-puremagic.py
|   |   |   |   |   |   +-- hook-py.py
|   |   |   |   |   |   +-- hook-pyarrow.py
|   |   |   |   |   |   +-- hook-pycountry.py
|   |   |   |   |   |   +-- hook-pycparser.py
|   |   |   |   |   |   +-- hook-pycrfsuite.py
|   |   |   |   |   |   +-- hook-pydantic.py
|   |   |   |   |   |   +-- hook-pydicom.py
|   |   |   |   |   |   +-- hook-pydivert.py
|   |   |   |   |   |   +-- hook-pyecharts.py
|   |   |   |   |   |   +-- hook-pyexcel.py
|   |   |   |   |   |   +-- hook-pyexcel_io.py
|   |   |   |   |   |   +-- hook-pyexcel_ods.py
|   |   |   |   |   |   +-- hook-pyexcel_ods3.py
|   |   |   |   |   |   +-- hook-pyexcel_odsr.py
|   |   |   |   |   |   +-- hook-pyexcel_xls.py
|   |   |   |   |   |   +-- hook-pyexcel_xlsx.py
|   |   |   |   |   |   +-- hook-pyexcel_xlsxw.py
|   |   |   |   |   |   +-- hook-pyexcelerate.Writer.py
|   |   |   |   |   |   +-- hook-pyexcel-io.py
|   |   |   |   |   |   +-- hook-pyexcel-ods.py
|   |   |   |   |   |   +-- hook-pyexcel-ods3.py
|   |   |   |   |   |   +-- hook-pyexcel-odsr.py
|   |   |   |   |   |   +-- hook-pyexcel-xls.py
|   |   |   |   |   |   +-- hook-pyexcel-xlsx.py
|   |   |   |   |   |   +-- hook-pyexcel-xlsxw.py
|   |   |   |   |   |   +-- hook-pygraphviz.py
|   |   |   |   |   |   +-- hook-pygwalker.py
|   |   |   |   |   |   +-- hook-pylibmagic.py
|   |   |   |   |   |   +-- hook-pylint.py
|   |   |   |   |   |   +-- hook-pylsl.py
|   |   |   |   |   |   +-- hook-pymediainfo.py
|   |   |   |   |   |   +-- hook-pymorphy3.py
|   |   |   |   |   |   +-- hook-pymssql.py
|   |   |   |   |   |   +-- hook-pynng.py
|   |   |   |   |   |   +-- hook-pynput.py
|   |   |   |   |   |   +-- hook-pyodbc.py
|   |   |   |   |   |   +-- hook-pyopencl.py
|   |   |   |   |   |   +-- hook-pypdfium2.py
|   |   |   |   |   |   +-- hook-pypdfium2_raw.py
|   |   |   |   |   |   +-- hook-pypemicro.py
|   |   |   |   |   |   +-- hook-pyphen.py
|   |   |   |   |   |   +-- hook-pyppeteer.py
|   |   |   |   |   |   +-- hook-pyproj.py
|   |   |   |   |   |   +-- hook-pypsexec.py
|   |   |   |   |   |   +-- hook-pypylon.py
|   |   |   |   |   |   +-- hook-pyqtgraph.py
|   |   |   |   |   |   +-- hook-pyshark.py
|   |   |   |   |   |   +-- hook-pysnmp.py
|   |   |   |   |   |   +-- hook-pystray.py
|   |   |   |   |   |   +-- hook-PyTaskbar.py
|   |   |   |   |   |   +-- hook-pytest.py
|   |   |   |   |   |   +-- hook-pythainlp.py
|   |   |   |   |   |   +-- hook-pythoncom.py
|   |   |   |   |   |   +-- hook-pyttsx.py
|   |   |   |   |   |   +-- hook-pyttsx3.py
|   |   |   |   |   |   +-- hook-pyviz_comms.py
|   |   |   |   |   |   +-- hook-pyvjoy.py
|   |   |   |   |   |   +-- hook-pywintypes.py
|   |   |   |   |   |   +-- hook-pywt.py
|   |   |   |   |   |   +-- hook-qtmodern.py
|   |   |   |   |   |   +-- hook-radicale.py
|   |   |   |   |   |   +-- hook-raven.py
|   |   |   |   |   |   +-- hook-rawpy.py
|   |   |   |   |   |   +-- hook-rdflib.py
|   |   |   |   |   |   +-- hook-redmine.py
|   |   |   |   |   |   +-- hook-regex.py
|   |   |   |   |   |   +-- hook-reportlab.lib.utils.py
|   |   |   |   |   |   +-- hook-reportlab.pdfbase._fontdata.py
|   |   |   |   |   |   +-- hook-resampy.py
|   |   |   |   |   |   +-- hook-rlp.py
|   |   |   |   |   |   +-- hook-rpy2.py
|   |   |   |   |   |   +-- hook-rtree.py
|   |   |   |   |   |   +-- hook-ruamel.yaml.py
|   |   |   |   |   |   +-- hook-rubicon.py
|   |   |   |   |   |   +-- hook-sacremoses.py
|   |   |   |   |   |   +-- hook-sam2.py
|   |   |   |   |   |   +-- hook-saml2.py
|   |   |   |   |   |   +-- hook-schwifty.py
|   |   |   |   |   |   +-- hook-seedir.py
|   |   |   |   |   |   +-- hook-selectolax.py
|   |   |   |   |   |   +-- hook-selenium.py
|   |   |   |   |   |   +-- hook-sentry_sdk.py
|   |   |   |   |   |   +-- hook-setuptools_scm.py
|   |   |   |   |   |   +-- hook-shapely.py
|   |   |   |   |   |   +-- hook-shotgun_api3.py
|   |   |   |   |   |   +-- hook-simplemma.py
|   |   |   |   |   |   +-- hook-skimage.color.py
|   |   |   |   |   |   +-- hook-skimage.data.py
|   |   |   |   |   |   +-- hook-skimage.draw.py
|   |   |   |   |   |   +-- hook-skimage.exposure.py
|   |   |   |   |   |   +-- hook-skimage.feature.py
|   |   |   |   |   |   +-- hook-skimage.filters.py
|   |   |   |   |   |   +-- hook-skimage.future.py
|   |   |   |   |   |   +-- hook-skimage.graph.py
|   |   |   |   |   |   +-- hook-skimage.io.py
|   |   |   |   |   |   +-- hook-skimage.measure.py
|   |   |   |   |   |   +-- hook-skimage.metrics.py
|   |   |   |   |   |   +-- hook-skimage.morphology.py
|   |   |   |   |   |   +-- hook-skimage.py
|   |   |   |   |   |   +-- hook-skimage.registration.py
|   |   |   |   |   |   +-- hook-skimage.restoration.py
|   |   |   |   |   |   +-- hook-skimage.transform.py
|   |   |   |   |   |   +-- hook-sklearn.cluster.py
|   |   |   |   |   |   +-- hook-sklearn.externals.array_api_compat.cupy.py
|   |   |   |   |   |   +-- hook-sklearn.externals.array_api_compat.dask.array.py
|   |   |   |   |   |   +-- hook-sklearn.externals.array_api_compat.numpy.py
|   |   |   |   |   |   +-- hook-sklearn.externals.array_api_compat.torch.py
|   |   |   |   |   |   +-- hook-sklearn.linear_model.py
|   |   |   |   |   |   +-- hook-sklearn.metrics.cluster.py
|   |   |   |   |   |   +-- hook-sklearn.metrics.pairwise.py
|   |   |   |   |   |   +-- hook-sklearn.metrics.py
|   |   |   |   |   |   +-- hook-sklearn.neighbors.py
|   |   |   |   |   |   +-- hook-sklearn.py
|   |   |   |   |   |   +-- hook-sklearn.tree.py
|   |   |   |   |   |   +-- hook-sklearn.utils.py
|   |   |   |   |   |   +-- hook-skyfield.py
|   |   |   |   |   |   +-- hook-slixmpp.py
|   |   |   |   |   |   +-- hook-sound_lib.py
|   |   |   |   |   |   +-- hook-sounddevice.py
|   |   |   |   |   |   +-- hook-soundfile.py
|   |   |   |   |   |   +-- hook-spacy.py
|   |   |   |   |   |   +-- hook-speech_recognition.py
|   |   |   |   |   |   +-- hook-spiceypy.py
|   |   |   |   |   |   +-- hook-spnego.py
|   |   |   |   |   |   +-- hook-srsly.msgpack._packer.py
|   |   |   |   |   |   +-- hook-sspilib.raw.py
|   |   |   |   |   |   +-- hook-statsmodels.tsa.statespace.py
|   |   |   |   |   |   +-- hook-stdnum.py
|   |   |   |   |   |   +-- hook-storm.database.py
|   |   |   |   |   |   +-- hook-sudachipy.py
|   |   |   |   |   |   +-- hook-sunpy.py
|   |   |   |   |   |   +-- hook-sv_ttk.py
|   |   |   |   |   |   +-- hook-swagger_spec_validator.py
|   |   |   |   |   |   +-- hook-tableauhyperapi.py
|   |   |   |   |   |   +-- hook-tables.py
|   |   |   |   |   |   +-- hook-tcod.py
|   |   |   |   |   |   +-- hook-tensorflow.py
|   |   |   |   |   |   +-- hook-text_unidecode.py
|   |   |   |   |   |   +-- hook-textdistance.py
|   |   |   |   |   |   +-- hook-thinc.backends.numpy_ops.py
|   |   |   |   |   |   +-- hook-thinc.py
|   |   |   |   |   |   +-- hook-timezonefinder.py
|   |   |   |   |   |   +-- hook-timm.py
|   |   |   |   |   |   +-- hook-tinycss2.py
|   |   |   |   |   |   +-- hook-tkinterdnd2.py
|   |   |   |   |   |   +-- hook-tkinterweb.py
|   |   |   |   |   |   +-- hook-tkinterweb_tkhtml.py
|   |   |   |   |   |   +-- hook-toga.py
|   |   |   |   |   |   +-- hook-toga_cocoa.py
|   |   |   |   |   |   +-- hook-toga_gtk.py
|   |   |   |   |   |   +-- hook-toga_winforms.py
|   |   |   |   |   |   +-- hook-torch.py
|   |   |   |   |   |   +-- hook-torchao.py
|   |   |   |   |   |   +-- hook-torchaudio.py
|   |   |   |   |   |   +-- hook-torchtext.py
|   |   |   |   |   |   +-- hook-torchvision.io.image.py
|   |   |   |   |   |   +-- hook-torchvision.py
|   |   |   |   |   |   +-- hook-trame.py
|   |   |   |   |   |   +-- hook-trame_client.py
|   |   |   |   |   |   +-- hook-trame_code.py
|   |   |   |   |   |   +-- hook-trame_components.py
|   |   |   |   |   |   +-- hook-trame_datagrid.py
|   |   |   |   |   |   +-- hook-trame_deckgl.py
|   |   |   |   |   |   +-- hook-trame_formkit.py
|   |   |   |   |   |   +-- hook-trame_grid.py
|   |   |   |   |   |   +-- hook-trame_iframe.py
|   |   |   |   |   |   +-- hook-trame_keycloak.py
|   |   |   |   |   |   +-- hook-trame_leaflet.py
|   |   |   |   |   |   +-- hook-trame_markdown.py
|   |   |   |   |   |   +-- hook-trame_matplotlib.py
|   |   |   |   |   |   +-- hook-trame_mesh_streamer.py
|   |   |   |   |   |   +-- hook-trame_plotly.py
|   |   |   |   |   |   +-- hook-trame_pvui.py
|   |   |   |   |   |   +-- hook-trame_quasar.py
|   |   |   |   |   |   +-- hook-trame_rca.py
|   |   |   |   |   |   +-- hook-trame_router.py
|   |   |   |   |   |   +-- hook-trame_simput.py
|   |   |   |   |   |   +-- hook-trame_tauri.py
|   |   |   |   |   |   +-- hook-trame_tweakpane.py
|   |   |   |   |   |   +-- hook-trame_vega.py
|   |   |   |   |   |   +-- hook-trame_vtk.py
|   |   |   |   |   |   +-- hook-trame_vtk3d.py
|   |   |   |   |   |   +-- hook-trame_vtklocal.py
|   |   |   |   |   |   +-- hook-trame_vuetify.py
|   |   |   |   |   |   +-- hook-trame_xterm.py
|   |   |   |   |   |   +-- hook-transformers.py
|   |   |   |   |   |   +-- hook-travertino.py
|   |   |   |   |   |   +-- hook-trimesh.py
|   |   |   |   |   |   +-- hook-triton.py
|   |   |   |   |   |   +-- hook-ttkthemes.py
|   |   |   |   |   |   +-- hook-ttkwidgets.py
|   |   |   |   |   |   +-- hook-tzdata.py
|   |   |   |   |   |   +-- hook-tzwhere.py
|   |   |   |   |   |   +-- hook-u1db.py
|   |   |   |   |   |   +-- hook-ultralytics.py
|   |   |   |   |   |   +-- hook-umap.py
|   |   |   |   |   |   +-- hook-unidecode.py
|   |   |   |   |   |   +-- hook-uniseg.py
|   |   |   |   |   |   +-- hook-urllib3.py
|   |   |   |   |   |   +-- hook-urllib3_future.py
|   |   |   |   |   |   +-- hook-usb.py
|   |   |   |   |   |   +-- hook-uuid6.py
|   |   |   |   |   |   +-- hook-uvicorn.py
|   |   |   |   |   |   +-- hook-uvloop.py
|   |   |   |   |   |   +-- hook-vaderSentiment.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkAcceleratorsVTKmCore.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkAcceleratorsVTKmDataModel.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkAcceleratorsVTKmFilters.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkChartsCore.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonColor.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonComputationalGeometry.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonDataModel.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonExecutionModel.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonMath.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonMisc.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonPython.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonSystem.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonTransforms.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkDomainsChemistry.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkDomainsChemistryOpenGL2.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersAMR.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersCellGrid.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersCore.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersExtraction.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersFlowPaths.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersGeneral.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersGeneric.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersGeometry.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersGeometryPreview.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersHybrid.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersHyperTree.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersImaging.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersModeling.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersParallel.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersParallelDIY2.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersParallelImaging.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersParallelStatistics.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersPoints.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersProgrammable.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersPython.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersReduction.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersSelection.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersSMP.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersSources.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersStatistics.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersTemporal.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersTensor.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersTexture.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersTopology.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersVerdict.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkGeovisCore.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingColor.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingCore.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingFourier.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingGeneral.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingHybrid.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingMath.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingMorphological.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingOpenGL2.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingSources.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingStatistics.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingStencil.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkInfovisCore.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkInfovisLayout.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkInteractionImage.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkInteractionStyle.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkInteractionWidgets.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOAMR.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOAsynchronous.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOAvmesh.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOCellGrid.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOCesium3DTiles.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOCGNSReader.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOChemistry.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOCityGML.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOCONVERGECFD.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOCore.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOEngys.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOEnSight.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOERF.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOExodus.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOExport.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOExportGL2PS.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOExportPDF.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOFDS.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOFLUENTCFF.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOGeoJSON.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOGeometry.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOH5part.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOH5Rage.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOHDF.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOImage.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOImport.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOInfovis.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOIOSS.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOLANLX3D.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOLegacy.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOLSDyna.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOMINC.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOMotionFX.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOMovie.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIONetCDF.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOOggTheora.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOOMF.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOParallel.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOParallelExodus.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOParallelLSDyna.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOParallelXML.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOPIO.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOPLY.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOSegY.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOSQL.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOTecplotTable.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOTRUCHAS.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOVeraOut.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOVideo.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOVPIC.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOXdmf2.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOXML.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkIOXMLParser.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkParallelCore.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkPythonContext2D.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingAnnotation.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingCellGrid.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingContext2D.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingContextOpenGL2.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingCore.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingExternal.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingFreeType.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingGL2PSOpenGL2.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingGridAxes.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingHyperTreeGrid.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingImage.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingLabel.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingLICOpenGL2.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingLOD.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingMatplotlib.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingOpenGL2.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingParallel.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingSceneGraph.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingUI.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingVolume.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingVolumeAMR.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingVolumeOpenGL2.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingVR.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingVRModels.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingVtkJS.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkSerializationManager.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkTestingRendering.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkTestingSerialization.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkViewsContext2D.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkViewsCore.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkViewsInfovis.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkWebCore.py
|   |   |   |   |   |   +-- hook-vtkmodules.vtkWebGLExporter.py
|   |   |   |   |   |   +-- hook-vtkpython.py
|   |   |   |   |   |   +-- hook-wavefile.py
|   |   |   |   |   |   +-- hook-weasyprint.py
|   |   |   |   |   |   +-- hook-web3.py
|   |   |   |   |   |   +-- hook-webassets.py
|   |   |   |   |   |   +-- hook-webrtcvad.py
|   |   |   |   |   |   +-- hook-websockets.py
|   |   |   |   |   |   +-- hook-webview.py
|   |   |   |   |   |   +-- hook-win32com.py
|   |   |   |   |   |   +-- hook-wordcloud.py
|   |   |   |   |   |   +-- hook-workflow.py
|   |   |   |   |   |   +-- hook-wx.lib.activex.py
|   |   |   |   |   |   +-- hook-wx.lib.pubsub.py
|   |   |   |   |   |   +-- hook-wx.xrc.py
|   |   |   |   |   |   +-- hook-xarray.py
|   |   |   |   |   |   +-- hook-Xlib.py
|   |   |   |   |   |   +-- hook-xml.dom.html.HTMLDocument.py
|   |   |   |   |   |   +-- hook-xml.sax.saxexts.py
|   |   |   |   |   |   +-- hook-xmldiff.py
|   |   |   |   |   |   +-- hook-xmlschema.py
|   |   |   |   |   |   +-- hook-xsge_gui.py
|   |   |   |   |   |   +-- hook-xyzservices.py
|   |   |   |   |   |   +-- hook-yapf_third_party.py
|   |   |   |   |   |   +-- hook-z3c.rml.py
|   |   |   |   |   |   +-- hook-zarr.py
|   |   |   |   |   |   +-- hook-zeep.py
|   |   |   |   |   |   +-- hook-zmq.py
|   |   |   |   |   |   +-- hook-zoneinfo.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-_mssql.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-_mysql.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-accessible_output2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-adbutils.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-adios.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-afmformats.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-aliyunsdkcore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-altair.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-amazonproduct.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-anyio.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-apkutils.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-appdirs.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-appy.pod.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-apscheduler.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-argon2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-astor.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-astroid.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-astropy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-astropy_iers_data.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-av.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-avro.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-azurerm.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-backports.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-backports.zoneinfo.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-bacon.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-bcrypt.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-bitsandbytes.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-black.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-bleak.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-blib2to3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-blspy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-bokeh.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-boto.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-boto3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-botocore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-branca.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-BTrees.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cairocffi.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cairosvg.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-capstone.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cassandra.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-celpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-certifi.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cf_units.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cftime.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-charset_normalizer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cloudpickle.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cloudscraper.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-clr.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-clr_loader.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cmocean.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-compliance_checker.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-comtypes.client.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-countrycode.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-countryinfo.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-Crypto.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-Cryptodome.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cryptography.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-CTkMessagebox.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cumm.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-customtkinter.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cv2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cx_Oracle.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-cytoolz.itertoolz.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dash.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dash_bootstrap_components.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dash_core_components.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dash_html_components.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dash_renderer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dash_table.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dash_uploader.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dask.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-datasets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dateparser.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dateparser.utils.strptime.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dateutil.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dbus_fast.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dclab.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-detectron2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-discid.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-distorm3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-distributed.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dns.rdata.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-docutils.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-docx.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-docx2pdf.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-duckdb.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-dynaconf.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-easyocr.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eccodeslib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eckitlib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-emoji.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-enchant.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eng_to_ipa.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-ens.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-enzyme.parsers.ebml.core.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eth_abi.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eth_account.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eth_hash.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eth_keyfile.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eth_keys.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eth_rlp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eth_typing.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eth_utils.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-eth_utils.network.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-exchangelib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-fabric.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-fairscale.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-faker.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-falcon.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-fastai.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-fastparquet.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-fckitlib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-ffpyplayer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-fiona.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-flask_compress.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-flask_restx.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-flex.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-flirpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-fmpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-folium.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-freetype.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-frictionless.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-fsspec.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-fvcore.nn.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gadfly.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gbulb.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gcloud.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-geopandas.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gitlab.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-globus_sdk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gmplot.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gmsh.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gooey.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-google.api_core.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-google.cloud.bigquery.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-google.cloud.core.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-google.cloud.kms_v1.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-google.cloud.pubsub_v1.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-google.cloud.speech.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-google.cloud.storage.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-google.cloud.translate.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-googleapiclient.model.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-grapheme.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-graphql_query.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-great_expectations.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gribapi.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-grpc.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gst._gst.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gtk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-h3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-h5py.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-hdf5plugin.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-hexbytes.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-HtmlTestRunner.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-httplib2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-humanize.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-hydra.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-ijson.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-imageio.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-imageio_ffmpeg.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-iminuit.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-intake.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-IPython.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-iso639.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-itk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-jaraco.text.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-jedi.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-jieba.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-jinja2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-jinxed.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-jira.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-jsonpath_rw_ext.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-jsonrpcserver.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-jsonschema.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-jsonschema_specifications.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-jupyterlab.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-kaleido.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-khmernltk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-kinterbasdb.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-langchain.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-langchain_classic.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-langcodes.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-langdetect.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-laonlp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-lark.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-ldfparser.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-lensfunpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-libaudioverse.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-librosa.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-lightgbm.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-lightning.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-limits.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-linear_operator.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-lingua.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-litestar.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-llvmlite.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-logilab.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-lxml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-lxml.etree.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-lxml.isoschematron.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-lxml.objectify.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-lz4.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-magic.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-mako.codegen.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-mariadb.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-markdown.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-mecab.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-metpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-migrate.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-mimesis.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-minecraft_launcher_lib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-mistune.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-mnemonic.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-monai.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-moviepy.audio.fx.all.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-moviepy.video.fx.all.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-mpl_toolkits.basemap.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-msoffcrypto.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nacl.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-names.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nanite.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-narwhals.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nbconvert.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nbdime.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nbformat.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nbt.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-ncclient.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-netCDF4.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nicegui.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-niquests.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nltk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nnpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-notebook.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-numba.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-numbers_parser.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-numcodecs.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.cublas.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.cuda_cupti.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.cuda_nvcc.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.cuda_nvrtc.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.cuda_runtime.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.cudnn.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.cufft.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.curand.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.cusolver.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.cusparse.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.nccl.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.nvjitlink.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-nvidia.nvtx.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-office365.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-onnxruntime.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-opencc.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-OpenGL.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-OpenGL_accelerate.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-openpyxl.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-opentelemetry.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-orjson.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-osgeo.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pandas_flavor.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-panel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-parsedatetime.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-parso.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-passlib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-paste.exceptions.reporter.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-patoolib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-patsy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pdfminer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pendulum.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-phonenumbers.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pingouin.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pint.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pinyin.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-platformdirs.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-plotly.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pointcept.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pptx.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-prettytable.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-psutil.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-psychopy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-psycopg_binary.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-psycopg2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-publicsuffix2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pubsub.core.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-puremagic.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-py.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyarrow.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pycountry.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pycparser.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pycrfsuite.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pydantic.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pydicom.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pydivert.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyecharts.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel_io.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel_ods.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel_ods3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel_odsr.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel_xls.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel_xlsx.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel_xlsxw.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcelerate.Writer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel-io.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel-ods.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel-ods3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel-odsr.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel-xls.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel-xlsx.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyexcel-xlsxw.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pygraphviz.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pygwalker.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pylibmagic.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pylint.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pylsl.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pymediainfo.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pymorphy3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pymssql.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pynng.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pynput.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyodbc.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyopencl.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pypdfium2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pypdfium2_raw.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pypemicro.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyphen.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyppeteer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyproj.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pypsexec.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pypylon.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyqtgraph.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyshark.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pysnmp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pystray.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyTaskbar.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pytest.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pythainlp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pythoncom.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyttsx.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyttsx3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyviz_comms.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pyvjoy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pywintypes.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pywt.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-qtmodern.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-radicale.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-raven.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-rawpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-rdflib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-redmine.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-regex.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-reportlab.lib.utils.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-reportlab.pdfbase._fontdata.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-resampy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-rlp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-rpy2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-rtree.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-ruamel.yaml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-rubicon.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sacremoses.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sam2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-saml2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-schwifty.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-seedir.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-selectolax.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-selenium.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sentry_sdk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-setuptools_scm.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-shapely.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-shotgun_api3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-simplemma.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.color.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.data.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.draw.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.exposure.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.feature.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.filters.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.future.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.graph.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.io.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.measure.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.metrics.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.morphology.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.registration.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.restoration.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skimage.transform.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.cluster.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.externals.array_api_compat.cupy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.externals.array_api_compat.dask.array.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.externals.array_api_compat.numpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.externals.array_api_compat.torch.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.linear_model.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.metrics.cluster.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.metrics.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.metrics.pairwise.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.neighbors.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.tree.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sklearn.utils.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-skyfield.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-slixmpp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sound_lib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sounddevice.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-soundfile.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-spacy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-speech_recognition.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-spiceypy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-spnego.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-srsly.msgpack._packer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sspilib.raw.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-statsmodels.tsa.statespace.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-stdnum.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-storm.database.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sudachipy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sunpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sv_ttk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-swagger_spec_validator.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-tableauhyperapi.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-tables.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-tcod.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-tensorflow.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-text_unidecode.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-textdistance.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-thinc.backends.numpy_ops.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-thinc.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-timezonefinder.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-timm.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-tinycss2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-tkinterdnd2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-tkinterweb.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-tkinterweb_tkhtml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-toga.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-toga_cocoa.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-toga_gtk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-toga_winforms.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-torch.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-torchao.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-torchaudio.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-torchtext.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-torchvision.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-torchvision.io.image.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_client.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_code.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_components.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_datagrid.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_deckgl.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_formkit.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_grid.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_iframe.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_keycloak.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_leaflet.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_markdown.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_matplotlib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_mesh_streamer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_plotly.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_pvui.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_quasar.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_rca.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_router.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_simput.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_tauri.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_tweakpane.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_vega.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_vtk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_vtk3d.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_vtklocal.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_vuetify.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trame_xterm.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-transformers.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-travertino.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-trimesh.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-triton.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-ttkthemes.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-ttkwidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-tzdata.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-tzwhere.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-u1db.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-ultralytics.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-umap.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-unidecode.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-uniseg.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-urllib3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-urllib3_future.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-usb.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-uuid6.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-uvicorn.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-uvloop.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vaderSentiment.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkAcceleratorsVTKmCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkAcceleratorsVTKmDataModel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkAcceleratorsVTKmFilters.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkChartsCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonColor.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonComputationalGeometry.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonDataModel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonExecutionModel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonMath.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonMisc.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonPython.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonSystem.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkCommonTransforms.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkDomainsChemistry.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkDomainsChemistryOpenGL2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersAMR.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersCellGrid.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersExtraction.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersFlowPaths.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersGeneral.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersGeneric.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersGeometry.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersGeometryPreview.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersHybrid.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersHyperTree.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersImaging.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersModeling.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersParallel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersParallelDIY2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersParallelImaging.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersParallelStatistics.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersPoints.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersProgrammable.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersPython.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersReduction.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersSelection.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersSMP.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersSources.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersStatistics.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersTemporal.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersTensor.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersTexture.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersTopology.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkFiltersVerdict.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkGeovisCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingColor.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingFourier.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingGeneral.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingHybrid.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingMath.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingMorphological.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingOpenGL2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingSources.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingStatistics.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkImagingStencil.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkInfovisCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkInfovisLayout.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkInteractionImage.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkInteractionStyle.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkInteractionWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOAMR.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOAsynchronous.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOAvmesh.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOCellGrid.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOCesium3DTiles.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOCGNSReader.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOChemistry.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOCityGML.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOCONVERGECFD.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOEngys.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOEnSight.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOERF.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOExodus.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOExport.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOExportGL2PS.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOExportPDF.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOFDS.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOFLUENTCFF.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOGeoJSON.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOGeometry.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOH5part.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOH5Rage.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOHDF.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOImage.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOImport.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOInfovis.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOIOSS.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOLANLX3D.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOLegacy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOLSDyna.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOMINC.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOMotionFX.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOMovie.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIONetCDF.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOOggTheora.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOOMF.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOParallel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOParallelExodus.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOParallelLSDyna.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOParallelXML.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOPIO.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOPLY.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOSegY.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOSQL.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOTecplotTable.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOTRUCHAS.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOVeraOut.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOVideo.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOVPIC.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOXdmf2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOXML.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkIOXMLParser.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkParallelCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkPythonContext2D.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingAnnotation.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingCellGrid.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingContext2D.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingContextOpenGL2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingExternal.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingFreeType.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingGL2PSOpenGL2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingGridAxes.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingHyperTreeGrid.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingImage.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingLabel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingLICOpenGL2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingLOD.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingMatplotlib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingOpenGL2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingParallel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingSceneGraph.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingUI.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingVolume.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingVolumeAMR.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingVolumeOpenGL2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingVR.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingVRModels.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkRenderingVtkJS.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkSerializationManager.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkTestingRendering.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkTestingSerialization.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkViewsContext2D.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkViewsCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkViewsInfovis.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkWebCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkmodules.vtkWebGLExporter.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-vtkpython.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-wavefile.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-weasyprint.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-web3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-webassets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-webrtcvad.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-websockets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-webview.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-win32com.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-wordcloud.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-workflow.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-wx.lib.activex.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-wx.lib.pubsub.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-wx.xrc.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-xarray.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-Xlib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-xml.dom.html.HTMLDocument.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-xml.sax.saxexts.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-xmldiff.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-xmlschema.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-xsge_gui.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-xyzservices.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-yapf_third_party.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-z3c.rml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-zarr.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-zeep.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-zmq.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-zoneinfo.cpython-311.pyc
|   |   |   |   |   +-- utils/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- nvidia_cuda.py
|   |   |   |   |   |   +-- vtkmodules.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- nvidia_cuda.cpython-311.pyc
|   |   |   |   |   |   |   +-- vtkmodules.cpython-311.pyc
|   |   |   |   +-- altgraph/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- Dot.py
|   |   |   |   |   +-- Graph.py
|   |   |   |   |   +-- GraphAlgo.py
|   |   |   |   |   +-- GraphStat.py
|   |   |   |   |   +-- GraphUtil.py
|   |   |   |   |   +-- ObjectGraph.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Dot.cpython-311.pyc
|   |   |   |   |   |   +-- Graph.cpython-311.pyc
|   |   |   |   |   |   +-- GraphAlgo.cpython-311.pyc
|   |   |   |   |   |   +-- GraphStat.cpython-311.pyc
|   |   |   |   |   |   +-- GraphUtil.cpython-311.pyc
|   |   |   |   |   |   +-- ObjectGraph.cpython-311.pyc
|   |   |   |   +-- altgraph-0.17.5.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- zip-safe
|   |   |   |   +-- blinker/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _utilities.py
|   |   |   |   |   +-- base.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _utilities.cpython-311.pyc
|   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   +-- blinker-1.9.0.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- certifi/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- __main__.py
|   |   |   |   |   +-- cacert.pem
|   |   |   |   |   +-- core.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   +-- core.cpython-311.pyc
|   |   |   |   +-- certifi-2025.11.12.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE
|   |   |   |   +-- charset_normalizer/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- __main__.py
|   |   |   |   |   +-- api.py
|   |   |   |   |   +-- cd.py
|   |   |   |   |   +-- constant.py
|   |   |   |   |   +-- legacy.py
|   |   |   |   |   +-- md.cp311-win_amd64.pyd
|   |   |   |   |   +-- md.py
|   |   |   |   |   +-- md__mypyc.cp311-win_amd64.pyd
|   |   |   |   |   +-- models.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- utils.py
|   |   |   |   |   +-- version.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   +-- cd.cpython-311.pyc
|   |   |   |   |   |   +-- constant.cpython-311.pyc
|   |   |   |   |   |   +-- legacy.cpython-311.pyc
|   |   |   |   |   |   +-- md.cpython-311.pyc
|   |   |   |   |   |   +-- models.cpython-311.pyc
|   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   +-- version.cpython-311.pyc
|   |   |   |   |   +-- cli/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __main__.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   +-- charset_normalizer-3.4.4.dist-info/
|   |   |   |   |   +-- entry_points.txt
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE
|   |   |   |   +-- click/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _compat.py
|   |   |   |   |   +-- _termui_impl.py
|   |   |   |   |   +-- _textwrap.py
|   |   |   |   |   +-- _utils.py
|   |   |   |   |   +-- _winconsole.py
|   |   |   |   |   +-- core.py
|   |   |   |   |   +-- decorators.py
|   |   |   |   |   +-- exceptions.py
|   |   |   |   |   +-- formatting.py
|   |   |   |   |   +-- globals.py
|   |   |   |   |   +-- parser.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- shell_completion.py
|   |   |   |   |   +-- termui.py
|   |   |   |   |   +-- testing.py
|   |   |   |   |   +-- types.py
|   |   |   |   |   +-- utils.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _compat.cpython-311.pyc
|   |   |   |   |   |   +-- _termui_impl.cpython-311.pyc
|   |   |   |   |   |   +-- _textwrap.cpython-311.pyc
|   |   |   |   |   |   +-- _utils.cpython-311.pyc
|   |   |   |   |   |   +-- _winconsole.cpython-311.pyc
|   |   |   |   |   |   +-- core.cpython-311.pyc
|   |   |   |   |   |   +-- decorators.cpython-311.pyc
|   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   +-- formatting.cpython-311.pyc
|   |   |   |   |   |   +-- globals.cpython-311.pyc
|   |   |   |   |   |   +-- parser.cpython-311.pyc
|   |   |   |   |   |   +-- shell_completion.cpython-311.pyc
|   |   |   |   |   |   +-- termui.cpython-311.pyc
|   |   |   |   |   |   +-- testing.cpython-311.pyc
|   |   |   |   |   |   +-- types.cpython-311.pyc
|   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   +-- click-8.3.1.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   +-- colorama/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- ansi.py
|   |   |   |   |   +-- ansitowin32.py
|   |   |   |   |   +-- initialise.py
|   |   |   |   |   +-- win32.py
|   |   |   |   |   +-- winterm.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- ansi.cpython-311.pyc
|   |   |   |   |   |   +-- ansitowin32.cpython-311.pyc
|   |   |   |   |   |   +-- initialise.cpython-311.pyc
|   |   |   |   |   |   +-- win32.cpython-311.pyc
|   |   |   |   |   |   +-- winterm.cpython-311.pyc
|   |   |   |   |   +-- tests/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- ansi_test.py
|   |   |   |   |   |   +-- ansitowin32_test.py
|   |   |   |   |   |   +-- initialise_test.py
|   |   |   |   |   |   +-- isatty_test.py
|   |   |   |   |   |   +-- utils.py
|   |   |   |   |   |   +-- winterm_test.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- ansi_test.cpython-311.pyc
|   |   |   |   |   |   |   +-- ansitowin32_test.cpython-311.pyc
|   |   |   |   |   |   |   +-- initialise_test.cpython-311.pyc
|   |   |   |   |   |   |   +-- isatty_test.cpython-311.pyc
|   |   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   |   +-- winterm_test.cpython-311.pyc
|   |   |   |   +-- colorama-0.4.6.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   +-- dateutil/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _common.py
|   |   |   |   |   +-- _version.py
|   |   |   |   |   +-- easter.py
|   |   |   |   |   +-- relativedelta.py
|   |   |   |   |   +-- rrule.py
|   |   |   |   |   +-- tzwin.py
|   |   |   |   |   +-- utils.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _common.cpython-311.pyc
|   |   |   |   |   |   +-- _version.cpython-311.pyc
|   |   |   |   |   |   +-- easter.cpython-311.pyc
|   |   |   |   |   |   +-- relativedelta.cpython-311.pyc
|   |   |   |   |   |   +-- rrule.cpython-311.pyc
|   |   |   |   |   |   +-- tzwin.cpython-311.pyc
|   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   +-- parser/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _parser.py
|   |   |   |   |   |   +-- isoparser.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _parser.cpython-311.pyc
|   |   |   |   |   |   |   +-- isoparser.cpython-311.pyc
|   |   |   |   |   +-- tz/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _common.py
|   |   |   |   |   |   +-- _factories.py
|   |   |   |   |   |   +-- tz.py
|   |   |   |   |   |   +-- win.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _common.cpython-311.pyc
|   |   |   |   |   |   |   +-- _factories.cpython-311.pyc
|   |   |   |   |   |   |   +-- tz.cpython-311.pyc
|   |   |   |   |   |   |   +-- win.cpython-311.pyc
|   |   |   |   |   +-- zoneinfo/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- dateutil-zoneinfo.tar.gz
|   |   |   |   |   |   +-- rebuild.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- rebuild.cpython-311.pyc
|   |   |   |   +-- et_xmlfile/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- incremental_tree.py
|   |   |   |   |   +-- xmlfile.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- incremental_tree.cpython-311.pyc
|   |   |   |   |   |   +-- xmlfile.cpython-311.pyc
|   |   |   |   +-- et_xmlfile-2.0.0.dist-info/
|   |   |   |   |   +-- AUTHORS.txt
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENCE.python
|   |   |   |   |   +-- LICENCE.rst
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- flask/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- __main__.py
|   |   |   |   |   +-- app.py
|   |   |   |   |   +-- blueprints.py
|   |   |   |   |   +-- cli.py
|   |   |   |   |   +-- config.py
|   |   |   |   |   +-- ctx.py
|   |   |   |   |   +-- debughelpers.py
|   |   |   |   |   +-- globals.py
|   |   |   |   |   +-- helpers.py
|   |   |   |   |   +-- logging.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- sessions.py
|   |   |   |   |   +-- signals.py
|   |   |   |   |   +-- templating.py
|   |   |   |   |   +-- testing.py
|   |   |   |   |   +-- typing.py
|   |   |   |   |   +-- views.py
|   |   |   |   |   +-- wrappers.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   +-- app.cpython-311.pyc
|   |   |   |   |   |   +-- blueprints.cpython-311.pyc
|   |   |   |   |   |   +-- cli.cpython-311.pyc
|   |   |   |   |   |   +-- config.cpython-311.pyc
|   |   |   |   |   |   +-- ctx.cpython-311.pyc
|   |   |   |   |   |   +-- debughelpers.cpython-311.pyc
|   |   |   |   |   |   +-- globals.cpython-311.pyc
|   |   |   |   |   |   +-- helpers.cpython-311.pyc
|   |   |   |   |   |   +-- logging.cpython-311.pyc
|   |   |   |   |   |   +-- sessions.cpython-311.pyc
|   |   |   |   |   |   +-- signals.cpython-311.pyc
|   |   |   |   |   |   +-- templating.cpython-311.pyc
|   |   |   |   |   |   +-- testing.cpython-311.pyc
|   |   |   |   |   |   +-- typing.cpython-311.pyc
|   |   |   |   |   |   +-- views.cpython-311.pyc
|   |   |   |   |   |   +-- wrappers.cpython-311.pyc
|   |   |   |   |   +-- json/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- provider.py
|   |   |   |   |   |   +-- tag.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- provider.cpython-311.pyc
|   |   |   |   |   |   |   +-- tag.cpython-311.pyc
|   |   |   |   |   +-- sansio/
|   |   |   |   |   |   +-- app.py
|   |   |   |   |   |   +-- blueprints.py
|   |   |   |   |   |   +-- README.md
|   |   |   |   |   |   +-- scaffold.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- app.cpython-311.pyc
|   |   |   |   |   |   |   +-- blueprints.cpython-311.pyc
|   |   |   |   |   |   |   +-- scaffold.cpython-311.pyc
|   |   |   |   +-- flask-3.1.2.dist-info/
|   |   |   |   |   +-- entry_points.txt
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- REQUESTED
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   +-- idna/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- codec.py
|   |   |   |   |   +-- compat.py
|   |   |   |   |   +-- core.py
|   |   |   |   |   +-- idnadata.py
|   |   |   |   |   +-- intranges.py
|   |   |   |   |   +-- package_data.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- uts46data.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- codec.cpython-311.pyc
|   |   |   |   |   |   +-- compat.cpython-311.pyc
|   |   |   |   |   |   +-- core.cpython-311.pyc
|   |   |   |   |   |   +-- idnadata.cpython-311.pyc
|   |   |   |   |   |   +-- intranges.cpython-311.pyc
|   |   |   |   |   |   +-- package_data.cpython-311.pyc
|   |   |   |   |   |   +-- uts46data.cpython-311.pyc
|   |   |   |   +-- idna-3.11.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE.md
|   |   |   |   +-- itsdangerous/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _json.py
|   |   |   |   |   +-- encoding.py
|   |   |   |   |   +-- exc.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- serializer.py
|   |   |   |   |   +-- signer.py
|   |   |   |   |   +-- timed.py
|   |   |   |   |   +-- url_safe.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _json.cpython-311.pyc
|   |   |   |   |   |   +-- encoding.cpython-311.pyc
|   |   |   |   |   |   +-- exc.cpython-311.pyc
|   |   |   |   |   |   +-- serializer.cpython-311.pyc
|   |   |   |   |   |   +-- signer.cpython-311.pyc
|   |   |   |   |   |   +-- timed.cpython-311.pyc
|   |   |   |   |   |   +-- url_safe.cpython-311.pyc
|   |   |   |   +-- itsdangerous-2.2.0.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- jinja2/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _identifier.py
|   |   |   |   |   +-- async_utils.py
|   |   |   |   |   +-- bccache.py
|   |   |   |   |   +-- compiler.py
|   |   |   |   |   +-- constants.py
|   |   |   |   |   +-- debug.py
|   |   |   |   |   +-- defaults.py
|   |   |   |   |   +-- environment.py
|   |   |   |   |   +-- exceptions.py
|   |   |   |   |   +-- ext.py
|   |   |   |   |   +-- filters.py
|   |   |   |   |   +-- idtracking.py
|   |   |   |   |   +-- lexer.py
|   |   |   |   |   +-- loaders.py
|   |   |   |   |   +-- meta.py
|   |   |   |   |   +-- nativetypes.py
|   |   |   |   |   +-- nodes.py
|   |   |   |   |   +-- optimizer.py
|   |   |   |   |   +-- parser.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- runtime.py
|   |   |   |   |   +-- sandbox.py
|   |   |   |   |   +-- tests.py
|   |   |   |   |   +-- utils.py
|   |   |   |   |   +-- visitor.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _identifier.cpython-311.pyc
|   |   |   |   |   |   +-- async_utils.cpython-311.pyc
|   |   |   |   |   |   +-- bccache.cpython-311.pyc
|   |   |   |   |   |   +-- compiler.cpython-311.pyc
|   |   |   |   |   |   +-- constants.cpython-311.pyc
|   |   |   |   |   |   +-- debug.cpython-311.pyc
|   |   |   |   |   |   +-- defaults.cpython-311.pyc
|   |   |   |   |   |   +-- environment.cpython-311.pyc
|   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   +-- ext.cpython-311.pyc
|   |   |   |   |   |   +-- filters.cpython-311.pyc
|   |   |   |   |   |   +-- idtracking.cpython-311.pyc
|   |   |   |   |   |   +-- lexer.cpython-311.pyc
|   |   |   |   |   |   +-- loaders.cpython-311.pyc
|   |   |   |   |   |   +-- meta.cpython-311.pyc
|   |   |   |   |   |   +-- nativetypes.cpython-311.pyc
|   |   |   |   |   |   +-- nodes.cpython-311.pyc
|   |   |   |   |   |   +-- optimizer.cpython-311.pyc
|   |   |   |   |   |   +-- parser.cpython-311.pyc
|   |   |   |   |   |   +-- runtime.cpython-311.pyc
|   |   |   |   |   |   +-- sandbox.cpython-311.pyc
|   |   |   |   |   |   +-- tests.cpython-311.pyc
|   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   +-- visitor.cpython-311.pyc
|   |   |   |   +-- jinja2-3.1.6.dist-info/
|   |   |   |   |   +-- entry_points.txt
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   +-- markupsafe/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _native.py
|   |   |   |   |   +-- _speedups.c
|   |   |   |   |   +-- _speedups.cp311-win_amd64.pyd
|   |   |   |   |   +-- _speedups.pyi
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _native.cpython-311.pyc
|   |   |   |   +-- markupsafe-3.0.3.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   +-- numpy/
|   |   |   |   |   +-- __config__.py
|   |   |   |   |   +-- __config__.pyi
|   |   |   |   |   +-- __init__.cython-30.pxd
|   |   |   |   |   +-- __init__.pxd
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   +-- _array_api_info.py
|   |   |   |   |   +-- _array_api_info.pyi
|   |   |   |   |   +-- _configtool.py
|   |   |   |   |   +-- _configtool.pyi
|   |   |   |   |   +-- _distributor_init.py
|   |   |   |   |   +-- _distributor_init.pyi
|   |   |   |   |   +-- _expired_attrs_2_0.py
|   |   |   |   |   +-- _expired_attrs_2_0.pyi
|   |   |   |   |   +-- _globals.py
|   |   |   |   |   +-- _globals.pyi
|   |   |   |   |   +-- _pytesttester.py
|   |   |   |   |   +-- _pytesttester.pyi
|   |   |   |   |   +-- conftest.py
|   |   |   |   |   +-- dtypes.py
|   |   |   |   |   +-- dtypes.pyi
|   |   |   |   |   +-- exceptions.py
|   |   |   |   |   +-- exceptions.pyi
|   |   |   |   |   +-- matlib.py
|   |   |   |   |   +-- matlib.pyi
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- version.py
|   |   |   |   |   +-- version.pyi
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __config__.cpython-311.pyc
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _array_api_info.cpython-311.pyc
|   |   |   |   |   |   +-- _configtool.cpython-311.pyc
|   |   |   |   |   |   +-- _distributor_init.cpython-311.pyc
|   |   |   |   |   |   +-- _expired_attrs_2_0.cpython-311.pyc
|   |   |   |   |   |   +-- _globals.cpython-311.pyc
|   |   |   |   |   |   +-- _pytesttester.cpython-311.pyc
|   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   +-- dtypes.cpython-311.pyc
|   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   +-- matlib.cpython-311.pyc
|   |   |   |   |   |   +-- version.cpython-311.pyc
|   |   |   |   |   +-- _core/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- _add_newdocs.py
|   |   |   |   |   |   +-- _add_newdocs.pyi
|   |   |   |   |   |   +-- _add_newdocs_scalars.py
|   |   |   |   |   |   +-- _add_newdocs_scalars.pyi
|   |   |   |   |   |   +-- _asarray.py
|   |   |   |   |   |   +-- _asarray.pyi
|   |   |   |   |   |   +-- _dtype.py
|   |   |   |   |   |   +-- _dtype.pyi
|   |   |   |   |   |   +-- _dtype_ctypes.py
|   |   |   |   |   |   +-- _dtype_ctypes.pyi
|   |   |   |   |   |   +-- _exceptions.py
|   |   |   |   |   |   +-- _exceptions.pyi
|   |   |   |   |   |   +-- _internal.py
|   |   |   |   |   |   +-- _internal.pyi
|   |   |   |   |   |   +-- _machar.py
|   |   |   |   |   |   +-- _machar.pyi
|   |   |   |   |   |   +-- _methods.py
|   |   |   |   |   |   +-- _methods.pyi
|   |   |   |   |   |   +-- _multiarray_tests.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _multiarray_tests.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _multiarray_umath.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _multiarray_umath.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _operand_flag_tests.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _operand_flag_tests.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _rational_tests.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _rational_tests.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _simd.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _simd.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _simd.pyi
|   |   |   |   |   |   +-- _string_helpers.py
|   |   |   |   |   |   +-- _string_helpers.pyi
|   |   |   |   |   |   +-- _struct_ufunc_tests.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _struct_ufunc_tests.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _type_aliases.py
|   |   |   |   |   |   +-- _type_aliases.pyi
|   |   |   |   |   |   +-- _ufunc_config.py
|   |   |   |   |   |   +-- _ufunc_config.pyi
|   |   |   |   |   |   +-- _umath_tests.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _umath_tests.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- arrayprint.py
|   |   |   |   |   |   +-- arrayprint.pyi
|   |   |   |   |   |   +-- cversions.py
|   |   |   |   |   |   +-- defchararray.py
|   |   |   |   |   |   +-- defchararray.pyi
|   |   |   |   |   |   +-- einsumfunc.py
|   |   |   |   |   |   +-- einsumfunc.pyi
|   |   |   |   |   |   +-- fromnumeric.py
|   |   |   |   |   |   +-- fromnumeric.pyi
|   |   |   |   |   |   +-- function_base.py
|   |   |   |   |   |   +-- function_base.pyi
|   |   |   |   |   |   +-- getlimits.py
|   |   |   |   |   |   +-- getlimits.pyi
|   |   |   |   |   |   +-- memmap.py
|   |   |   |   |   |   +-- memmap.pyi
|   |   |   |   |   |   +-- multiarray.py
|   |   |   |   |   |   +-- multiarray.pyi
|   |   |   |   |   |   +-- numeric.py
|   |   |   |   |   |   +-- numeric.pyi
|   |   |   |   |   |   +-- numerictypes.py
|   |   |   |   |   |   +-- numerictypes.pyi
|   |   |   |   |   |   +-- overrides.py
|   |   |   |   |   |   +-- overrides.pyi
|   |   |   |   |   |   +-- printoptions.py
|   |   |   |   |   |   +-- printoptions.pyi
|   |   |   |   |   |   +-- records.py
|   |   |   |   |   |   +-- records.pyi
|   |   |   |   |   |   +-- shape_base.py
|   |   |   |   |   |   +-- shape_base.pyi
|   |   |   |   |   |   +-- strings.py
|   |   |   |   |   |   +-- strings.pyi
|   |   |   |   |   |   +-- umath.py
|   |   |   |   |   |   +-- umath.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _add_newdocs.cpython-311.pyc
|   |   |   |   |   |   |   +-- _add_newdocs_scalars.cpython-311.pyc
|   |   |   |   |   |   |   +-- _asarray.cpython-311.pyc
|   |   |   |   |   |   |   +-- _dtype.cpython-311.pyc
|   |   |   |   |   |   |   +-- _dtype_ctypes.cpython-311.pyc
|   |   |   |   |   |   |   +-- _exceptions.cpython-311.pyc
|   |   |   |   |   |   |   +-- _internal.cpython-311.pyc
|   |   |   |   |   |   |   +-- _machar.cpython-311.pyc
|   |   |   |   |   |   |   +-- _methods.cpython-311.pyc
|   |   |   |   |   |   |   +-- _string_helpers.cpython-311.pyc
|   |   |   |   |   |   |   +-- _type_aliases.cpython-311.pyc
|   |   |   |   |   |   |   +-- _ufunc_config.cpython-311.pyc
|   |   |   |   |   |   |   +-- arrayprint.cpython-311.pyc
|   |   |   |   |   |   |   +-- cversions.cpython-311.pyc
|   |   |   |   |   |   |   +-- defchararray.cpython-311.pyc
|   |   |   |   |   |   |   +-- einsumfunc.cpython-311.pyc
|   |   |   |   |   |   |   +-- fromnumeric.cpython-311.pyc
|   |   |   |   |   |   |   +-- function_base.cpython-311.pyc
|   |   |   |   |   |   |   +-- getlimits.cpython-311.pyc
|   |   |   |   |   |   |   +-- memmap.cpython-311.pyc
|   |   |   |   |   |   |   +-- multiarray.cpython-311.pyc
|   |   |   |   |   |   |   +-- numeric.cpython-311.pyc
|   |   |   |   |   |   |   +-- numerictypes.cpython-311.pyc
|   |   |   |   |   |   |   +-- overrides.cpython-311.pyc
|   |   |   |   |   |   |   +-- printoptions.cpython-311.pyc
|   |   |   |   |   |   |   +-- records.cpython-311.pyc
|   |   |   |   |   |   |   +-- shape_base.cpython-311.pyc
|   |   |   |   |   |   |   +-- strings.cpython-311.pyc
|   |   |   |   |   |   |   +-- umath.cpython-311.pyc
|   |   |   |   |   |   +-- include/
|   |   |   |   |   |   |   +-- numpy/
|   |   |   |   |   |   |   |   +-- __multiarray_api.c
|   |   |   |   |   |   |   |   +-- __multiarray_api.h
|   |   |   |   |   |   |   |   +-- __ufunc_api.c
|   |   |   |   |   |   |   |   +-- __ufunc_api.h
|   |   |   |   |   |   |   |   +-- _neighborhood_iterator_imp.h
|   |   |   |   |   |   |   |   +-- _numpyconfig.h
|   |   |   |   |   |   |   |   +-- _public_dtype_api_table.h
|   |   |   |   |   |   |   |   +-- arrayobject.h
|   |   |   |   |   |   |   |   +-- arrayscalars.h
|   |   |   |   |   |   |   |   +-- dtype_api.h
|   |   |   |   |   |   |   |   +-- halffloat.h
|   |   |   |   |   |   |   |   +-- ndarrayobject.h
|   |   |   |   |   |   |   |   +-- ndarraytypes.h
|   |   |   |   |   |   |   |   +-- npy_2_compat.h
|   |   |   |   |   |   |   |   +-- npy_2_complexcompat.h
|   |   |   |   |   |   |   |   +-- npy_3kcompat.h
|   |   |   |   |   |   |   |   +-- npy_common.h
|   |   |   |   |   |   |   |   +-- npy_cpu.h
|   |   |   |   |   |   |   |   +-- npy_endian.h
|   |   |   |   |   |   |   |   +-- npy_math.h
|   |   |   |   |   |   |   |   +-- npy_no_deprecated_api.h
|   |   |   |   |   |   |   |   +-- npy_os.h
|   |   |   |   |   |   |   |   +-- numpyconfig.h
|   |   |   |   |   |   |   |   +-- ufuncobject.h
|   |   |   |   |   |   |   |   +-- utils.h
|   |   |   |   |   |   |   |   +-- random/
|   |   |   |   |   |   |   |   |   +-- bitgen.h
|   |   |   |   |   |   |   |   |   +-- distributions.h
|   |   |   |   |   |   |   |   |   +-- libdivide.h
|   |   |   |   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   |   +-- lib/
|   |   |   |   |   |   |   +-- npymath.lib
|   |   |   |   |   |   |   +-- npy-pkg-config/
|   |   |   |   |   |   |   |   +-- mlib.ini
|   |   |   |   |   |   |   |   +-- npymath.ini
|   |   |   |   |   |   |   +-- pkgconfig/
|   |   |   |   |   |   |   |   +-- numpy.pc
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- _locales.py
|   |   |   |   |   |   |   +-- _natype.py
|   |   |   |   |   |   |   +-- test__exceptions.py
|   |   |   |   |   |   |   +-- test_abc.py
|   |   |   |   |   |   |   +-- test_api.py
|   |   |   |   |   |   |   +-- test_argparse.py
|   |   |   |   |   |   |   +-- test_array_api_info.py
|   |   |   |   |   |   |   +-- test_array_coercion.py
|   |   |   |   |   |   |   +-- test_array_interface.py
|   |   |   |   |   |   |   +-- test_arraymethod.py
|   |   |   |   |   |   |   +-- test_arrayobject.py
|   |   |   |   |   |   |   +-- test_arrayprint.py
|   |   |   |   |   |   |   +-- test_casting_floatingpoint_errors.py
|   |   |   |   |   |   |   +-- test_casting_unittests.py
|   |   |   |   |   |   |   +-- test_conversion_utils.py
|   |   |   |   |   |   |   +-- test_cpu_dispatcher.py
|   |   |   |   |   |   |   +-- test_cpu_features.py
|   |   |   |   |   |   |   +-- test_custom_dtypes.py
|   |   |   |   |   |   |   +-- test_cython.py
|   |   |   |   |   |   |   +-- test_datetime.py
|   |   |   |   |   |   |   +-- test_defchararray.py
|   |   |   |   |   |   |   +-- test_deprecations.py
|   |   |   |   |   |   |   +-- test_dlpack.py
|   |   |   |   |   |   |   +-- test_dtype.py
|   |   |   |   |   |   |   +-- test_einsum.py
|   |   |   |   |   |   |   +-- test_errstate.py
|   |   |   |   |   |   |   +-- test_extint128.py
|   |   |   |   |   |   |   +-- test_function_base.py
|   |   |   |   |   |   |   +-- test_getlimits.py
|   |   |   |   |   |   |   +-- test_half.py
|   |   |   |   |   |   |   +-- test_hashtable.py
|   |   |   |   |   |   |   +-- test_indexerrors.py
|   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   +-- test_item_selection.py
|   |   |   |   |   |   |   +-- test_limited_api.py
|   |   |   |   |   |   |   +-- test_longdouble.py
|   |   |   |   |   |   |   +-- test_machar.py
|   |   |   |   |   |   |   +-- test_mem_overlap.py
|   |   |   |   |   |   |   +-- test_mem_policy.py
|   |   |   |   |   |   |   +-- test_memmap.py
|   |   |   |   |   |   |   +-- test_multiarray.py
|   |   |   |   |   |   |   +-- test_multithreading.py
|   |   |   |   |   |   |   +-- test_nditer.py
|   |   |   |   |   |   |   +-- test_nep50_promotions.py
|   |   |   |   |   |   |   +-- test_numeric.py
|   |   |   |   |   |   |   +-- test_numerictypes.py
|   |   |   |   |   |   |   +-- test_overrides.py
|   |   |   |   |   |   |   +-- test_print.py
|   |   |   |   |   |   |   +-- test_protocols.py
|   |   |   |   |   |   |   +-- test_records.py
|   |   |   |   |   |   |   +-- test_regression.py
|   |   |   |   |   |   |   +-- test_scalar_ctors.py
|   |   |   |   |   |   |   +-- test_scalar_methods.py
|   |   |   |   |   |   |   +-- test_scalarbuffer.py
|   |   |   |   |   |   |   +-- test_scalarinherit.py
|   |   |   |   |   |   |   +-- test_scalarmath.py
|   |   |   |   |   |   |   +-- test_scalarprint.py
|   |   |   |   |   |   |   +-- test_shape_base.py
|   |   |   |   |   |   |   +-- test_simd.py
|   |   |   |   |   |   |   +-- test_simd_module.py
|   |   |   |   |   |   |   +-- test_stringdtype.py
|   |   |   |   |   |   |   +-- test_strings.py
|   |   |   |   |   |   |   +-- test_ufunc.py
|   |   |   |   |   |   |   +-- test_umath.py
|   |   |   |   |   |   |   +-- test_umath_accuracy.py
|   |   |   |   |   |   |   +-- test_umath_complex.py
|   |   |   |   |   |   |   +-- test_unicode.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- _locales.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _natype.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test__exceptions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_abc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_argparse.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_array_api_info.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_array_coercion.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_array_interface.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_arraymethod.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_arrayobject.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_arrayprint.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_casting_floatingpoint_errors.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_casting_unittests.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_conversion_utils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_cpu_dispatcher.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_cpu_features.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_custom_dtypes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_cython.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_datetime.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_defchararray.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_deprecations.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_dlpack.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_dtype.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_einsum.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_errstate.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_extint128.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_function_base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_getlimits.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_half.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_hashtable.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_indexerrors.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_item_selection.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_limited_api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_longdouble.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_machar.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_mem_overlap.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_mem_policy.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_memmap.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_multiarray.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_multithreading.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_nditer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_nep50_promotions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_numeric.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_numerictypes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_overrides.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_print.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_protocols.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_records.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_regression.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_scalar_ctors.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_scalar_methods.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_scalarbuffer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_scalarinherit.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_scalarmath.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_scalarprint.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_shape_base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_simd.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_simd_module.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_stringdtype.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_strings.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_ufunc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_umath.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_umath_accuracy.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_umath_complex.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_unicode.cpython-311.pyc
|   |   |   |   |   |   |   +-- data/
|   |   |   |   |   |   |   |   +-- astype_copy.pkl
|   |   |   |   |   |   |   |   +-- generate_umath_validation_data.cpp
|   |   |   |   |   |   |   |   +-- recarray_from_file.fits
|   |   |   |   |   |   |   |   +-- umath-validation-set-arccos.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-arccosh.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-arcsin.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-arcsinh.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-arctan.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-arctanh.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-cbrt.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-cos.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-cosh.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-exp.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-exp2.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-expm1.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-log.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-log10.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-log1p.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-log2.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-README.txt
|   |   |   |   |   |   |   |   +-- umath-validation-set-sin.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-sinh.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-tan.csv
|   |   |   |   |   |   |   |   +-- umath-validation-set-tanh.csv
|   |   |   |   |   |   |   +-- examples/
|   |   |   |   |   |   |   |   +-- cython/
|   |   |   |   |   |   |   |   |   +-- checks.pyx
|   |   |   |   |   |   |   |   |   +-- meson.build
|   |   |   |   |   |   |   |   |   +-- setup.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- setup.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- limited_api/
|   |   |   |   |   |   |   |   |   +-- limited_api_latest.c
|   |   |   |   |   |   |   |   |   +-- limited_api1.c
|   |   |   |   |   |   |   |   |   +-- limited_api2.pyx
|   |   |   |   |   |   |   |   |   +-- meson.build
|   |   |   |   |   |   |   |   |   +-- setup.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- setup.cpython-311.pyc
|   |   |   |   |   +-- _pyinstaller/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- hook-numpy.py
|   |   |   |   |   |   +-- hook-numpy.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-numpy.cpython-311.pyc
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- pyinstaller-smoke.py
|   |   |   |   |   |   |   +-- test_pyinstaller.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyinstaller-smoke.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_pyinstaller.cpython-311.pyc
|   |   |   |   |   +-- _typing/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _add_docstring.py
|   |   |   |   |   |   +-- _array_like.py
|   |   |   |   |   |   +-- _char_codes.py
|   |   |   |   |   |   +-- _dtype_like.py
|   |   |   |   |   |   +-- _extended_precision.py
|   |   |   |   |   |   +-- _nbit.py
|   |   |   |   |   |   +-- _nbit_base.py
|   |   |   |   |   |   +-- _nbit_base.pyi
|   |   |   |   |   |   +-- _nested_sequence.py
|   |   |   |   |   |   +-- _scalars.py
|   |   |   |   |   |   +-- _shape.py
|   |   |   |   |   |   +-- _ufunc.py
|   |   |   |   |   |   +-- _ufunc.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _add_docstring.cpython-311.pyc
|   |   |   |   |   |   |   +-- _array_like.cpython-311.pyc
|   |   |   |   |   |   |   +-- _char_codes.cpython-311.pyc
|   |   |   |   |   |   |   +-- _dtype_like.cpython-311.pyc
|   |   |   |   |   |   |   +-- _extended_precision.cpython-311.pyc
|   |   |   |   |   |   |   +-- _nbit.cpython-311.pyc
|   |   |   |   |   |   |   +-- _nbit_base.cpython-311.pyc
|   |   |   |   |   |   |   +-- _nested_sequence.cpython-311.pyc
|   |   |   |   |   |   |   +-- _scalars.cpython-311.pyc
|   |   |   |   |   |   |   +-- _shape.cpython-311.pyc
|   |   |   |   |   |   |   +-- _ufunc.cpython-311.pyc
|   |   |   |   |   +-- _utils/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- _convertions.py
|   |   |   |   |   |   +-- _convertions.pyi
|   |   |   |   |   |   +-- _inspect.py
|   |   |   |   |   |   +-- _inspect.pyi
|   |   |   |   |   |   +-- _pep440.py
|   |   |   |   |   |   +-- _pep440.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _convertions.cpython-311.pyc
|   |   |   |   |   |   |   +-- _inspect.cpython-311.pyc
|   |   |   |   |   |   |   +-- _pep440.cpython-311.pyc
|   |   |   |   |   +-- char/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- core/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- _dtype.py
|   |   |   |   |   |   +-- _dtype.pyi
|   |   |   |   |   |   +-- _dtype_ctypes.py
|   |   |   |   |   |   +-- _dtype_ctypes.pyi
|   |   |   |   |   |   +-- _internal.py
|   |   |   |   |   |   +-- _multiarray_umath.py
|   |   |   |   |   |   +-- _utils.py
|   |   |   |   |   |   +-- arrayprint.py
|   |   |   |   |   |   +-- defchararray.py
|   |   |   |   |   |   +-- einsumfunc.py
|   |   |   |   |   |   +-- fromnumeric.py
|   |   |   |   |   |   +-- function_base.py
|   |   |   |   |   |   +-- getlimits.py
|   |   |   |   |   |   +-- multiarray.py
|   |   |   |   |   |   +-- numeric.py
|   |   |   |   |   |   +-- numerictypes.py
|   |   |   |   |   |   +-- overrides.py
|   |   |   |   |   |   +-- overrides.pyi
|   |   |   |   |   |   +-- records.py
|   |   |   |   |   |   +-- shape_base.py
|   |   |   |   |   |   +-- umath.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _dtype.cpython-311.pyc
|   |   |   |   |   |   |   +-- _dtype_ctypes.cpython-311.pyc
|   |   |   |   |   |   |   +-- _internal.cpython-311.pyc
|   |   |   |   |   |   |   +-- _multiarray_umath.cpython-311.pyc
|   |   |   |   |   |   |   +-- _utils.cpython-311.pyc
|   |   |   |   |   |   |   +-- arrayprint.cpython-311.pyc
|   |   |   |   |   |   |   +-- defchararray.cpython-311.pyc
|   |   |   |   |   |   |   +-- einsumfunc.cpython-311.pyc
|   |   |   |   |   |   |   +-- fromnumeric.cpython-311.pyc
|   |   |   |   |   |   |   +-- function_base.cpython-311.pyc
|   |   |   |   |   |   |   +-- getlimits.cpython-311.pyc
|   |   |   |   |   |   |   +-- multiarray.cpython-311.pyc
|   |   |   |   |   |   |   +-- numeric.cpython-311.pyc
|   |   |   |   |   |   |   +-- numerictypes.cpython-311.pyc
|   |   |   |   |   |   |   +-- overrides.cpython-311.pyc
|   |   |   |   |   |   |   +-- records.cpython-311.pyc
|   |   |   |   |   |   |   +-- shape_base.cpython-311.pyc
|   |   |   |   |   |   |   +-- umath.cpython-311.pyc
|   |   |   |   |   +-- ctypeslib/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- _ctypeslib.py
|   |   |   |   |   |   +-- _ctypeslib.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _ctypeslib.cpython-311.pyc
|   |   |   |   |   +-- distutils/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- _shell_utils.py
|   |   |   |   |   |   +-- armccompiler.py
|   |   |   |   |   |   +-- ccompiler.py
|   |   |   |   |   |   +-- ccompiler_opt.py
|   |   |   |   |   |   +-- conv_template.py
|   |   |   |   |   |   +-- core.py
|   |   |   |   |   |   +-- cpuinfo.py
|   |   |   |   |   |   +-- exec_command.py
|   |   |   |   |   |   +-- extension.py
|   |   |   |   |   |   +-- from_template.py
|   |   |   |   |   |   +-- fujitsuccompiler.py
|   |   |   |   |   |   +-- intelccompiler.py
|   |   |   |   |   |   +-- lib2def.py
|   |   |   |   |   |   +-- line_endings.py
|   |   |   |   |   |   +-- log.py
|   |   |   |   |   |   +-- mingw32ccompiler.py
|   |   |   |   |   |   +-- misc_util.py
|   |   |   |   |   |   +-- msvc9compiler.py
|   |   |   |   |   |   +-- msvccompiler.py
|   |   |   |   |   |   +-- npy_pkg_config.py
|   |   |   |   |   |   +-- numpy_distribution.py
|   |   |   |   |   |   +-- pathccompiler.py
|   |   |   |   |   |   +-- system_info.py
|   |   |   |   |   |   +-- unixccompiler.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _shell_utils.cpython-311.pyc
|   |   |   |   |   |   |   +-- armccompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- ccompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- ccompiler_opt.cpython-311.pyc
|   |   |   |   |   |   |   +-- conv_template.cpython-311.pyc
|   |   |   |   |   |   |   +-- core.cpython-311.pyc
|   |   |   |   |   |   |   +-- cpuinfo.cpython-311.pyc
|   |   |   |   |   |   |   +-- exec_command.cpython-311.pyc
|   |   |   |   |   |   |   +-- extension.cpython-311.pyc
|   |   |   |   |   |   |   +-- from_template.cpython-311.pyc
|   |   |   |   |   |   |   +-- fujitsuccompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- intelccompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- lib2def.cpython-311.pyc
|   |   |   |   |   |   |   +-- line_endings.cpython-311.pyc
|   |   |   |   |   |   |   +-- log.cpython-311.pyc
|   |   |   |   |   |   |   +-- mingw32ccompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- misc_util.cpython-311.pyc
|   |   |   |   |   |   |   +-- msvc9compiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- msvccompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- npy_pkg_config.cpython-311.pyc
|   |   |   |   |   |   |   +-- numpy_distribution.cpython-311.pyc
|   |   |   |   |   |   |   +-- pathccompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- system_info.cpython-311.pyc
|   |   |   |   |   |   |   +-- unixccompiler.cpython-311.pyc
|   |   |   |   |   |   +-- checks/
|   |   |   |   |   |   |   +-- cpu_asimd.c
|   |   |   |   |   |   |   +-- cpu_asimddp.c
|   |   |   |   |   |   |   +-- cpu_asimdfhm.c
|   |   |   |   |   |   |   +-- cpu_asimdhp.c
|   |   |   |   |   |   |   +-- cpu_avx.c
|   |   |   |   |   |   |   +-- cpu_avx2.c
|   |   |   |   |   |   |   +-- cpu_avx512_clx.c
|   |   |   |   |   |   |   +-- cpu_avx512_cnl.c
|   |   |   |   |   |   |   +-- cpu_avx512_icl.c
|   |   |   |   |   |   |   +-- cpu_avx512_knl.c
|   |   |   |   |   |   |   +-- cpu_avx512_knm.c
|   |   |   |   |   |   |   +-- cpu_avx512_skx.c
|   |   |   |   |   |   |   +-- cpu_avx512_spr.c
|   |   |   |   |   |   |   +-- cpu_avx512cd.c
|   |   |   |   |   |   |   +-- cpu_avx512f.c
|   |   |   |   |   |   |   +-- cpu_f16c.c
|   |   |   |   |   |   |   +-- cpu_fma3.c
|   |   |   |   |   |   |   +-- cpu_fma4.c
|   |   |   |   |   |   |   +-- cpu_lsx.c
|   |   |   |   |   |   |   +-- cpu_neon.c
|   |   |   |   |   |   |   +-- cpu_neon_fp16.c
|   |   |   |   |   |   |   +-- cpu_neon_vfpv4.c
|   |   |   |   |   |   |   +-- cpu_popcnt.c
|   |   |   |   |   |   |   +-- cpu_rvv.c
|   |   |   |   |   |   |   +-- cpu_sse.c
|   |   |   |   |   |   |   +-- cpu_sse2.c
|   |   |   |   |   |   |   +-- cpu_sse3.c
|   |   |   |   |   |   |   +-- cpu_sse41.c
|   |   |   |   |   |   |   +-- cpu_sse42.c
|   |   |   |   |   |   |   +-- cpu_ssse3.c
|   |   |   |   |   |   |   +-- cpu_sve.c
|   |   |   |   |   |   |   +-- cpu_vsx.c
|   |   |   |   |   |   |   +-- cpu_vsx2.c
|   |   |   |   |   |   |   +-- cpu_vsx3.c
|   |   |   |   |   |   |   +-- cpu_vsx4.c
|   |   |   |   |   |   |   +-- cpu_vx.c
|   |   |   |   |   |   |   +-- cpu_vxe.c
|   |   |   |   |   |   |   +-- cpu_vxe2.c
|   |   |   |   |   |   |   +-- cpu_xop.c
|   |   |   |   |   |   |   +-- extra_avx512bw_mask.c
|   |   |   |   |   |   |   +-- extra_avx512dq_mask.c
|   |   |   |   |   |   |   +-- extra_avx512f_reduce.c
|   |   |   |   |   |   |   +-- extra_vsx_asm.c
|   |   |   |   |   |   |   +-- extra_vsx3_half_double.c
|   |   |   |   |   |   |   +-- extra_vsx4_mma.c
|   |   |   |   |   |   |   +-- test_flags.c
|   |   |   |   |   |   +-- command/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- autodist.py
|   |   |   |   |   |   |   +-- bdist_rpm.py
|   |   |   |   |   |   |   +-- build.py
|   |   |   |   |   |   |   +-- build_clib.py
|   |   |   |   |   |   |   +-- build_ext.py
|   |   |   |   |   |   |   +-- build_py.py
|   |   |   |   |   |   |   +-- build_scripts.py
|   |   |   |   |   |   |   +-- build_src.py
|   |   |   |   |   |   |   +-- config.py
|   |   |   |   |   |   |   +-- config_compiler.py
|   |   |   |   |   |   |   +-- develop.py
|   |   |   |   |   |   |   +-- egg_info.py
|   |   |   |   |   |   |   +-- install.py
|   |   |   |   |   |   |   +-- install_clib.py
|   |   |   |   |   |   |   +-- install_data.py
|   |   |   |   |   |   |   +-- install_headers.py
|   |   |   |   |   |   |   +-- sdist.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- autodist.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- bdist_rpm.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- build.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- build_clib.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- build_ext.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- build_py.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- build_scripts.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- build_src.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- config.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- config_compiler.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- develop.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- egg_info.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- install.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- install_clib.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- install_data.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- install_headers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- sdist.cpython-311.pyc
|   |   |   |   |   |   +-- fcompiler/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- absoft.py
|   |   |   |   |   |   |   +-- arm.py
|   |   |   |   |   |   |   +-- compaq.py
|   |   |   |   |   |   |   +-- environment.py
|   |   |   |   |   |   |   +-- fujitsu.py
|   |   |   |   |   |   |   +-- g95.py
|   |   |   |   |   |   |   +-- gnu.py
|   |   |   |   |   |   |   +-- hpux.py
|   |   |   |   |   |   |   +-- ibm.py
|   |   |   |   |   |   |   +-- intel.py
|   |   |   |   |   |   |   +-- lahey.py
|   |   |   |   |   |   |   +-- mips.py
|   |   |   |   |   |   |   +-- nag.py
|   |   |   |   |   |   |   +-- none.py
|   |   |   |   |   |   |   +-- nv.py
|   |   |   |   |   |   |   +-- pathf95.py
|   |   |   |   |   |   |   +-- pg.py
|   |   |   |   |   |   |   +-- sun.py
|   |   |   |   |   |   |   +-- vast.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- absoft.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- arm.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- compaq.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- environment.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- fujitsu.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- g95.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- gnu.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hpux.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- ibm.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- intel.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- lahey.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- mips.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- nag.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- none.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- nv.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pathf95.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pg.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- sun.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- vast.cpython-311.pyc
|   |   |   |   |   |   +-- mingw/
|   |   |   |   |   |   |   +-- gfortran_vs2003_hack.c
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_build_ext.py
|   |   |   |   |   |   |   +-- test_ccompiler_opt.py
|   |   |   |   |   |   |   +-- test_ccompiler_opt_conf.py
|   |   |   |   |   |   |   +-- test_exec_command.py
|   |   |   |   |   |   |   +-- test_fcompiler.py
|   |   |   |   |   |   |   +-- test_fcompiler_gnu.py
|   |   |   |   |   |   |   +-- test_fcompiler_intel.py
|   |   |   |   |   |   |   +-- test_fcompiler_nagfor.py
|   |   |   |   |   |   |   +-- test_from_template.py
|   |   |   |   |   |   |   +-- test_log.py
|   |   |   |   |   |   |   +-- test_mingw32ccompiler.py
|   |   |   |   |   |   |   +-- test_misc_util.py
|   |   |   |   |   |   |   +-- test_npy_pkg_config.py
|   |   |   |   |   |   |   +-- test_shell_utils.py
|   |   |   |   |   |   |   +-- test_system_info.py
|   |   |   |   |   |   |   +-- utilities.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_build_ext.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_ccompiler_opt.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_ccompiler_opt_conf.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_exec_command.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_fcompiler.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_fcompiler_gnu.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_fcompiler_intel.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_fcompiler_nagfor.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_from_template.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_log.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_mingw32ccompiler.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_misc_util.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_npy_pkg_config.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_shell_utils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_system_info.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- utilities.cpython-311.pyc
|   |   |   |   |   +-- doc/
|   |   |   |   |   |   +-- ufuncs.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- ufuncs.cpython-311.pyc
|   |   |   |   |   +-- f2py/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- __main__.py
|   |   |   |   |   |   +-- __version__.py
|   |   |   |   |   |   +-- __version__.pyi
|   |   |   |   |   |   +-- _isocbind.py
|   |   |   |   |   |   +-- _isocbind.pyi
|   |   |   |   |   |   +-- _src_pyf.py
|   |   |   |   |   |   +-- _src_pyf.pyi
|   |   |   |   |   |   +-- auxfuncs.py
|   |   |   |   |   |   +-- auxfuncs.pyi
|   |   |   |   |   |   +-- capi_maps.py
|   |   |   |   |   |   +-- capi_maps.pyi
|   |   |   |   |   |   +-- cb_rules.py
|   |   |   |   |   |   +-- cb_rules.pyi
|   |   |   |   |   |   +-- cfuncs.py
|   |   |   |   |   |   +-- cfuncs.pyi
|   |   |   |   |   |   +-- common_rules.py
|   |   |   |   |   |   +-- common_rules.pyi
|   |   |   |   |   |   +-- crackfortran.py
|   |   |   |   |   |   +-- crackfortran.pyi
|   |   |   |   |   |   +-- diagnose.py
|   |   |   |   |   |   +-- diagnose.pyi
|   |   |   |   |   |   +-- f2py2e.py
|   |   |   |   |   |   +-- f2py2e.pyi
|   |   |   |   |   |   +-- f90mod_rules.py
|   |   |   |   |   |   +-- f90mod_rules.pyi
|   |   |   |   |   |   +-- func2subr.py
|   |   |   |   |   |   +-- func2subr.pyi
|   |   |   |   |   |   +-- rules.py
|   |   |   |   |   |   +-- rules.pyi
|   |   |   |   |   |   +-- setup.cfg
|   |   |   |   |   |   +-- symbolic.py
|   |   |   |   |   |   +-- symbolic.pyi
|   |   |   |   |   |   +-- use_rules.py
|   |   |   |   |   |   +-- use_rules.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   |   +-- __version__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _isocbind.cpython-311.pyc
|   |   |   |   |   |   |   +-- _src_pyf.cpython-311.pyc
|   |   |   |   |   |   |   +-- auxfuncs.cpython-311.pyc
|   |   |   |   |   |   |   +-- capi_maps.cpython-311.pyc
|   |   |   |   |   |   |   +-- cb_rules.cpython-311.pyc
|   |   |   |   |   |   |   +-- cfuncs.cpython-311.pyc
|   |   |   |   |   |   |   +-- common_rules.cpython-311.pyc
|   |   |   |   |   |   |   +-- crackfortran.cpython-311.pyc
|   |   |   |   |   |   |   +-- diagnose.cpython-311.pyc
|   |   |   |   |   |   |   +-- f2py2e.cpython-311.pyc
|   |   |   |   |   |   |   +-- f90mod_rules.cpython-311.pyc
|   |   |   |   |   |   |   +-- func2subr.cpython-311.pyc
|   |   |   |   |   |   |   +-- rules.cpython-311.pyc
|   |   |   |   |   |   |   +-- symbolic.cpython-311.pyc
|   |   |   |   |   |   |   +-- use_rules.cpython-311.pyc
|   |   |   |   |   |   +-- _backends/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   |   +-- _backend.py
|   |   |   |   |   |   |   +-- _backend.pyi
|   |   |   |   |   |   |   +-- _distutils.py
|   |   |   |   |   |   |   +-- _distutils.pyi
|   |   |   |   |   |   |   +-- _meson.py
|   |   |   |   |   |   |   +-- _meson.pyi
|   |   |   |   |   |   |   +-- meson.build.template
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _backend.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _distutils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _meson.cpython-311.pyc
|   |   |   |   |   |   +-- src/
|   |   |   |   |   |   |   +-- fortranobject.c
|   |   |   |   |   |   |   +-- fortranobject.h
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_abstract_interface.py
|   |   |   |   |   |   |   +-- test_array_from_pyobj.py
|   |   |   |   |   |   |   +-- test_assumed_shape.py
|   |   |   |   |   |   |   +-- test_block_docstring.py
|   |   |   |   |   |   |   +-- test_callback.py
|   |   |   |   |   |   |   +-- test_character.py
|   |   |   |   |   |   |   +-- test_common.py
|   |   |   |   |   |   |   +-- test_crackfortran.py
|   |   |   |   |   |   |   +-- test_data.py
|   |   |   |   |   |   |   +-- test_docs.py
|   |   |   |   |   |   |   +-- test_f2cmap.py
|   |   |   |   |   |   |   +-- test_f2py2e.py
|   |   |   |   |   |   |   +-- test_isoc.py
|   |   |   |   |   |   |   +-- test_kind.py
|   |   |   |   |   |   |   +-- test_mixed.py
|   |   |   |   |   |   |   +-- test_modules.py
|   |   |   |   |   |   |   +-- test_parameter.py
|   |   |   |   |   |   |   +-- test_pyf_src.py
|   |   |   |   |   |   |   +-- test_quoted_character.py
|   |   |   |   |   |   |   +-- test_regression.py
|   |   |   |   |   |   |   +-- test_return_character.py
|   |   |   |   |   |   |   +-- test_return_complex.py
|   |   |   |   |   |   |   +-- test_return_integer.py
|   |   |   |   |   |   |   +-- test_return_logical.py
|   |   |   |   |   |   |   +-- test_return_real.py
|   |   |   |   |   |   |   +-- test_routines.py
|   |   |   |   |   |   |   +-- test_semicolon_split.py
|   |   |   |   |   |   |   +-- test_size.py
|   |   |   |   |   |   |   +-- test_string.py
|   |   |   |   |   |   |   +-- test_symbolic.py
|   |   |   |   |   |   |   +-- test_value_attrspec.py
|   |   |   |   |   |   |   +-- util.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_abstract_interface.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_array_from_pyobj.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_assumed_shape.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_block_docstring.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_callback.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_character.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_crackfortran.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_data.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_docs.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_f2cmap.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_f2py2e.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_isoc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_kind.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_mixed.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_modules.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_parameter.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_pyf_src.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_quoted_character.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_regression.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_return_character.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_return_complex.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_return_integer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_return_logical.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_return_real.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_routines.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_semicolon_split.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_size.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_string.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_symbolic.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_value_attrspec.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- util.cpython-311.pyc
|   |   |   |   |   |   |   +-- src/
|   |   |   |   |   |   |   |   +-- abstract_interface/
|   |   |   |   |   |   |   |   |   +-- foo.f90
|   |   |   |   |   |   |   |   |   +-- gh18403_mod.f90
|   |   |   |   |   |   |   |   +-- array_from_pyobj/
|   |   |   |   |   |   |   |   |   +-- wrapmodule.c
|   |   |   |   |   |   |   |   +-- assumed_shape/
|   |   |   |   |   |   |   |   |   +-- .f2py_f2cmap
|   |   |   |   |   |   |   |   |   +-- foo_free.f90
|   |   |   |   |   |   |   |   |   +-- foo_mod.f90
|   |   |   |   |   |   |   |   |   +-- foo_use.f90
|   |   |   |   |   |   |   |   |   +-- precision.f90
|   |   |   |   |   |   |   |   +-- block_docstring/
|   |   |   |   |   |   |   |   |   +-- foo.f
|   |   |   |   |   |   |   |   +-- callback/
|   |   |   |   |   |   |   |   |   +-- foo.f
|   |   |   |   |   |   |   |   |   +-- gh17797.f90
|   |   |   |   |   |   |   |   |   +-- gh18335.f90
|   |   |   |   |   |   |   |   |   +-- gh25211.f
|   |   |   |   |   |   |   |   |   +-- gh25211.pyf
|   |   |   |   |   |   |   |   |   +-- gh26681.f90
|   |   |   |   |   |   |   |   +-- cli/
|   |   |   |   |   |   |   |   |   +-- gh_22819.pyf
|   |   |   |   |   |   |   |   |   +-- hi77.f
|   |   |   |   |   |   |   |   |   +-- hiworld.f90
|   |   |   |   |   |   |   |   +-- common/
|   |   |   |   |   |   |   |   |   +-- block.f
|   |   |   |   |   |   |   |   |   +-- gh19161.f90
|   |   |   |   |   |   |   |   +-- crackfortran/
|   |   |   |   |   |   |   |   |   +-- accesstype.f90
|   |   |   |   |   |   |   |   |   +-- common_with_division.f
|   |   |   |   |   |   |   |   |   +-- data_common.f
|   |   |   |   |   |   |   |   |   +-- data_multiplier.f
|   |   |   |   |   |   |   |   |   +-- data_stmts.f90
|   |   |   |   |   |   |   |   |   +-- data_with_comments.f
|   |   |   |   |   |   |   |   |   +-- foo_deps.f90
|   |   |   |   |   |   |   |   |   +-- gh15035.f
|   |   |   |   |   |   |   |   |   +-- gh17859.f
|   |   |   |   |   |   |   |   |   +-- gh22648.pyf
|   |   |   |   |   |   |   |   |   +-- gh23533.f
|   |   |   |   |   |   |   |   |   +-- gh23598.f90
|   |   |   |   |   |   |   |   |   +-- gh23598Warn.f90
|   |   |   |   |   |   |   |   |   +-- gh23879.f90
|   |   |   |   |   |   |   |   |   +-- gh27697.f90
|   |   |   |   |   |   |   |   |   +-- gh2848.f90
|   |   |   |   |   |   |   |   |   +-- operators.f90
|   |   |   |   |   |   |   |   |   +-- privatemod.f90
|   |   |   |   |   |   |   |   |   +-- publicmod.f90
|   |   |   |   |   |   |   |   |   +-- pubprivmod.f90
|   |   |   |   |   |   |   |   |   +-- unicode_comment.f90
|   |   |   |   |   |   |   |   +-- f2cmap/
|   |   |   |   |   |   |   |   |   +-- .f2py_f2cmap
|   |   |   |   |   |   |   |   |   +-- isoFortranEnvMap.f90
|   |   |   |   |   |   |   |   +-- isocintrin/
|   |   |   |   |   |   |   |   |   +-- isoCtests.f90
|   |   |   |   |   |   |   |   +-- kind/
|   |   |   |   |   |   |   |   |   +-- foo.f90
|   |   |   |   |   |   |   |   +-- mixed/
|   |   |   |   |   |   |   |   |   +-- foo.f
|   |   |   |   |   |   |   |   |   +-- foo_fixed.f90
|   |   |   |   |   |   |   |   |   +-- foo_free.f90
|   |   |   |   |   |   |   |   +-- modules/
|   |   |   |   |   |   |   |   |   +-- module_data_docstring.f90
|   |   |   |   |   |   |   |   |   +-- use_modules.f90
|   |   |   |   |   |   |   |   |   +-- gh25337/
|   |   |   |   |   |   |   |   |   |   +-- data.f90
|   |   |   |   |   |   |   |   |   |   +-- use_data.f90
|   |   |   |   |   |   |   |   |   +-- gh26920/
|   |   |   |   |   |   |   |   |   |   +-- two_mods_with_no_public_entities.f90
|   |   |   |   |   |   |   |   |   |   +-- two_mods_with_one_public_routine.f90
|   |   |   |   |   |   |   |   +-- negative_bounds/
|   |   |   |   |   |   |   |   |   +-- issue_20853.f90
|   |   |   |   |   |   |   |   +-- parameter/
|   |   |   |   |   |   |   |   |   +-- constant_array.f90
|   |   |   |   |   |   |   |   |   +-- constant_both.f90
|   |   |   |   |   |   |   |   |   +-- constant_compound.f90
|   |   |   |   |   |   |   |   |   +-- constant_integer.f90
|   |   |   |   |   |   |   |   |   +-- constant_non_compound.f90
|   |   |   |   |   |   |   |   |   +-- constant_real.f90
|   |   |   |   |   |   |   |   +-- quoted_character/
|   |   |   |   |   |   |   |   |   +-- foo.f
|   |   |   |   |   |   |   |   +-- regression/
|   |   |   |   |   |   |   |   |   +-- AB.inc
|   |   |   |   |   |   |   |   |   +-- assignOnlyModule.f90
|   |   |   |   |   |   |   |   |   +-- datonly.f90
|   |   |   |   |   |   |   |   |   +-- f77comments.f
|   |   |   |   |   |   |   |   |   +-- f77fixedform.f95
|   |   |   |   |   |   |   |   |   +-- f90continuation.f90
|   |   |   |   |   |   |   |   |   +-- incfile.f90
|   |   |   |   |   |   |   |   |   +-- inout.f90
|   |   |   |   |   |   |   |   |   +-- lower_f2py_fortran.f90
|   |   |   |   |   |   |   |   |   +-- mod_derived_types.f90
|   |   |   |   |   |   |   |   +-- return_character/
|   |   |   |   |   |   |   |   |   +-- foo77.f
|   |   |   |   |   |   |   |   |   +-- foo90.f90
|   |   |   |   |   |   |   |   +-- return_complex/
|   |   |   |   |   |   |   |   |   +-- foo77.f
|   |   |   |   |   |   |   |   |   +-- foo90.f90
|   |   |   |   |   |   |   |   +-- return_integer/
|   |   |   |   |   |   |   |   |   +-- foo77.f
|   |   |   |   |   |   |   |   |   +-- foo90.f90
|   |   |   |   |   |   |   |   +-- return_logical/
|   |   |   |   |   |   |   |   |   +-- foo77.f
|   |   |   |   |   |   |   |   |   +-- foo90.f90
|   |   |   |   |   |   |   |   +-- return_real/
|   |   |   |   |   |   |   |   |   +-- foo77.f
|   |   |   |   |   |   |   |   |   +-- foo90.f90
|   |   |   |   |   |   |   |   +-- routines/
|   |   |   |   |   |   |   |   |   +-- funcfortranname.f
|   |   |   |   |   |   |   |   |   +-- funcfortranname.pyf
|   |   |   |   |   |   |   |   |   +-- subrout.f
|   |   |   |   |   |   |   |   |   +-- subrout.pyf
|   |   |   |   |   |   |   |   +-- size/
|   |   |   |   |   |   |   |   |   +-- foo.f90
|   |   |   |   |   |   |   |   +-- string/
|   |   |   |   |   |   |   |   |   +-- char.f90
|   |   |   |   |   |   |   |   |   +-- fixed_string.f90
|   |   |   |   |   |   |   |   |   +-- gh24008.f
|   |   |   |   |   |   |   |   |   +-- gh24662.f90
|   |   |   |   |   |   |   |   |   +-- gh25286.f90
|   |   |   |   |   |   |   |   |   +-- gh25286.pyf
|   |   |   |   |   |   |   |   |   +-- gh25286_bc.pyf
|   |   |   |   |   |   |   |   |   +-- scalar_string.f90
|   |   |   |   |   |   |   |   |   +-- string.f
|   |   |   |   |   |   |   |   +-- value_attrspec/
|   |   |   |   |   |   |   |   |   +-- gh21665.f90
|   |   |   |   |   +-- fft/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- _helper.py
|   |   |   |   |   |   +-- _helper.pyi
|   |   |   |   |   |   +-- _pocketfft.py
|   |   |   |   |   |   +-- _pocketfft.pyi
|   |   |   |   |   |   +-- _pocketfft_umath.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _pocketfft_umath.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- helper.py
|   |   |   |   |   |   +-- helper.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _helper.cpython-311.pyc
|   |   |   |   |   |   |   +-- _pocketfft.cpython-311.pyc
|   |   |   |   |   |   |   +-- helper.cpython-311.pyc
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_helper.py
|   |   |   |   |   |   |   +-- test_pocketfft.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_helper.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_pocketfft.cpython-311.pyc
|   |   |   |   |   +-- lib/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- _array_utils_impl.py
|   |   |   |   |   |   +-- _array_utils_impl.pyi
|   |   |   |   |   |   +-- _arraypad_impl.py
|   |   |   |   |   |   +-- _arraypad_impl.pyi
|   |   |   |   |   |   +-- _arraysetops_impl.py
|   |   |   |   |   |   +-- _arraysetops_impl.pyi
|   |   |   |   |   |   +-- _arrayterator_impl.py
|   |   |   |   |   |   +-- _arrayterator_impl.pyi
|   |   |   |   |   |   +-- _datasource.py
|   |   |   |   |   |   +-- _datasource.pyi
|   |   |   |   |   |   +-- _format_impl.py
|   |   |   |   |   |   +-- _format_impl.pyi
|   |   |   |   |   |   +-- _function_base_impl.py
|   |   |   |   |   |   +-- _function_base_impl.pyi
|   |   |   |   |   |   +-- _histograms_impl.py
|   |   |   |   |   |   +-- _histograms_impl.pyi
|   |   |   |   |   |   +-- _index_tricks_impl.py
|   |   |   |   |   |   +-- _index_tricks_impl.pyi
|   |   |   |   |   |   +-- _iotools.py
|   |   |   |   |   |   +-- _iotools.pyi
|   |   |   |   |   |   +-- _nanfunctions_impl.py
|   |   |   |   |   |   +-- _nanfunctions_impl.pyi
|   |   |   |   |   |   +-- _npyio_impl.py
|   |   |   |   |   |   +-- _npyio_impl.pyi
|   |   |   |   |   |   +-- _polynomial_impl.py
|   |   |   |   |   |   +-- _polynomial_impl.pyi
|   |   |   |   |   |   +-- _scimath_impl.py
|   |   |   |   |   |   +-- _scimath_impl.pyi
|   |   |   |   |   |   +-- _shape_base_impl.py
|   |   |   |   |   |   +-- _shape_base_impl.pyi
|   |   |   |   |   |   +-- _stride_tricks_impl.py
|   |   |   |   |   |   +-- _stride_tricks_impl.pyi
|   |   |   |   |   |   +-- _twodim_base_impl.py
|   |   |   |   |   |   +-- _twodim_base_impl.pyi
|   |   |   |   |   |   +-- _type_check_impl.py
|   |   |   |   |   |   +-- _type_check_impl.pyi
|   |   |   |   |   |   +-- _ufunclike_impl.py
|   |   |   |   |   |   +-- _ufunclike_impl.pyi
|   |   |   |   |   |   +-- _user_array_impl.py
|   |   |   |   |   |   +-- _user_array_impl.pyi
|   |   |   |   |   |   +-- _utils_impl.py
|   |   |   |   |   |   +-- _utils_impl.pyi
|   |   |   |   |   |   +-- _version.py
|   |   |   |   |   |   +-- _version.pyi
|   |   |   |   |   |   +-- array_utils.py
|   |   |   |   |   |   +-- array_utils.pyi
|   |   |   |   |   |   +-- format.py
|   |   |   |   |   |   +-- format.pyi
|   |   |   |   |   |   +-- introspect.py
|   |   |   |   |   |   +-- introspect.pyi
|   |   |   |   |   |   +-- mixins.py
|   |   |   |   |   |   +-- mixins.pyi
|   |   |   |   |   |   +-- npyio.py
|   |   |   |   |   |   +-- npyio.pyi
|   |   |   |   |   |   +-- recfunctions.py
|   |   |   |   |   |   +-- recfunctions.pyi
|   |   |   |   |   |   +-- scimath.py
|   |   |   |   |   |   +-- scimath.pyi
|   |   |   |   |   |   +-- stride_tricks.py
|   |   |   |   |   |   +-- stride_tricks.pyi
|   |   |   |   |   |   +-- user_array.py
|   |   |   |   |   |   +-- user_array.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _array_utils_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _arraypad_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _arraysetops_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _arrayterator_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _datasource.cpython-311.pyc
|   |   |   |   |   |   |   +-- _format_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _function_base_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _histograms_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _index_tricks_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _iotools.cpython-311.pyc
|   |   |   |   |   |   |   +-- _nanfunctions_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _npyio_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _polynomial_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _scimath_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _shape_base_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _stride_tricks_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _twodim_base_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _type_check_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _ufunclike_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _user_array_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _utils_impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _version.cpython-311.pyc
|   |   |   |   |   |   |   +-- array_utils.cpython-311.pyc
|   |   |   |   |   |   |   +-- format.cpython-311.pyc
|   |   |   |   |   |   |   +-- introspect.cpython-311.pyc
|   |   |   |   |   |   |   +-- mixins.cpython-311.pyc
|   |   |   |   |   |   |   +-- npyio.cpython-311.pyc
|   |   |   |   |   |   |   +-- recfunctions.cpython-311.pyc
|   |   |   |   |   |   |   +-- scimath.cpython-311.pyc
|   |   |   |   |   |   |   +-- stride_tricks.cpython-311.pyc
|   |   |   |   |   |   |   +-- user_array.cpython-311.pyc
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test__datasource.py
|   |   |   |   |   |   |   +-- test__iotools.py
|   |   |   |   |   |   |   +-- test__version.py
|   |   |   |   |   |   |   +-- test_array_utils.py
|   |   |   |   |   |   |   +-- test_arraypad.py
|   |   |   |   |   |   |   +-- test_arraysetops.py
|   |   |   |   |   |   |   +-- test_arrayterator.py
|   |   |   |   |   |   |   +-- test_format.py
|   |   |   |   |   |   |   +-- test_function_base.py
|   |   |   |   |   |   |   +-- test_histograms.py
|   |   |   |   |   |   |   +-- test_index_tricks.py
|   |   |   |   |   |   |   +-- test_io.py
|   |   |   |   |   |   |   +-- test_loadtxt.py
|   |   |   |   |   |   |   +-- test_mixins.py
|   |   |   |   |   |   |   +-- test_nanfunctions.py
|   |   |   |   |   |   |   +-- test_packbits.py
|   |   |   |   |   |   |   +-- test_polynomial.py
|   |   |   |   |   |   |   +-- test_recfunctions.py
|   |   |   |   |   |   |   +-- test_regression.py
|   |   |   |   |   |   |   +-- test_shape_base.py
|   |   |   |   |   |   |   +-- test_stride_tricks.py
|   |   |   |   |   |   |   +-- test_twodim_base.py
|   |   |   |   |   |   |   +-- test_type_check.py
|   |   |   |   |   |   |   +-- test_ufunclike.py
|   |   |   |   |   |   |   +-- test_utils.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test__datasource.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test__iotools.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test__version.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_array_utils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_arraypad.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_arraysetops.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_arrayterator.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_format.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_function_base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_histograms.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_index_tricks.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_io.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_loadtxt.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_mixins.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_nanfunctions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_packbits.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_polynomial.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_recfunctions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_regression.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_shape_base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_stride_tricks.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_twodim_base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_type_check.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_ufunclike.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_utils.cpython-311.pyc
|   |   |   |   |   |   |   +-- data/
|   |   |   |   |   |   |   |   +-- py2-np0-objarr.npy
|   |   |   |   |   |   |   |   +-- py2-objarr.npy
|   |   |   |   |   |   |   |   +-- py2-objarr.npz
|   |   |   |   |   |   |   |   +-- py3-objarr.npy
|   |   |   |   |   |   |   |   +-- py3-objarr.npz
|   |   |   |   |   |   |   |   +-- python3.npy
|   |   |   |   |   |   |   |   +-- win64python2.npy
|   |   |   |   |   +-- linalg/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- _linalg.py
|   |   |   |   |   |   +-- _linalg.pyi
|   |   |   |   |   |   +-- _umath_linalg.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _umath_linalg.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _umath_linalg.pyi
|   |   |   |   |   |   +-- lapack_lite.cp311-win_amd64.lib
|   |   |   |   |   |   +-- lapack_lite.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- lapack_lite.pyi
|   |   |   |   |   |   +-- linalg.py
|   |   |   |   |   |   +-- linalg.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _linalg.cpython-311.pyc
|   |   |   |   |   |   |   +-- linalg.cpython-311.pyc
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_deprecations.py
|   |   |   |   |   |   |   +-- test_linalg.py
|   |   |   |   |   |   |   +-- test_regression.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_deprecations.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_linalg.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_regression.cpython-311.pyc
|   |   |   |   |   +-- ma/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- API_CHANGES.txt
|   |   |   |   |   |   +-- core.py
|   |   |   |   |   |   +-- core.pyi
|   |   |   |   |   |   +-- extras.py
|   |   |   |   |   |   +-- extras.pyi
|   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   +-- mrecords.py
|   |   |   |   |   |   +-- mrecords.pyi
|   |   |   |   |   |   +-- README.rst
|   |   |   |   |   |   +-- testutils.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- core.cpython-311.pyc
|   |   |   |   |   |   |   +-- extras.cpython-311.pyc
|   |   |   |   |   |   |   +-- mrecords.cpython-311.pyc
|   |   |   |   |   |   |   +-- testutils.cpython-311.pyc
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_arrayobject.py
|   |   |   |   |   |   |   +-- test_core.py
|   |   |   |   |   |   |   +-- test_deprecations.py
|   |   |   |   |   |   |   +-- test_extras.py
|   |   |   |   |   |   |   +-- test_mrecords.py
|   |   |   |   |   |   |   +-- test_old_ma.py
|   |   |   |   |   |   |   +-- test_regression.py
|   |   |   |   |   |   |   +-- test_subclassing.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_arrayobject.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_core.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_deprecations.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_extras.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_mrecords.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_old_ma.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_regression.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_subclassing.cpython-311.pyc
|   |   |   |   |   +-- matrixlib/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- defmatrix.py
|   |   |   |   |   |   +-- defmatrix.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- defmatrix.cpython-311.pyc
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_defmatrix.py
|   |   |   |   |   |   |   +-- test_interaction.py
|   |   |   |   |   |   |   +-- test_masked_matrix.py
|   |   |   |   |   |   |   +-- test_matrix_linalg.py
|   |   |   |   |   |   |   +-- test_multiarray.py
|   |   |   |   |   |   |   +-- test_numeric.py
|   |   |   |   |   |   |   +-- test_regression.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_defmatrix.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_interaction.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_masked_matrix.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_matrix_linalg.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_multiarray.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_numeric.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_regression.cpython-311.pyc
|   |   |   |   |   +-- polynomial/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- _polybase.py
|   |   |   |   |   |   +-- _polybase.pyi
|   |   |   |   |   |   +-- _polytypes.pyi
|   |   |   |   |   |   +-- chebyshev.py
|   |   |   |   |   |   +-- chebyshev.pyi
|   |   |   |   |   |   +-- hermite.py
|   |   |   |   |   |   +-- hermite.pyi
|   |   |   |   |   |   +-- hermite_e.py
|   |   |   |   |   |   +-- hermite_e.pyi
|   |   |   |   |   |   +-- laguerre.py
|   |   |   |   |   |   +-- laguerre.pyi
|   |   |   |   |   |   +-- legendre.py
|   |   |   |   |   |   +-- legendre.pyi
|   |   |   |   |   |   +-- polynomial.py
|   |   |   |   |   |   +-- polynomial.pyi
|   |   |   |   |   |   +-- polyutils.py
|   |   |   |   |   |   +-- polyutils.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _polybase.cpython-311.pyc
|   |   |   |   |   |   |   +-- chebyshev.cpython-311.pyc
|   |   |   |   |   |   |   +-- hermite.cpython-311.pyc
|   |   |   |   |   |   |   +-- hermite_e.cpython-311.pyc
|   |   |   |   |   |   |   +-- laguerre.cpython-311.pyc
|   |   |   |   |   |   |   +-- legendre.cpython-311.pyc
|   |   |   |   |   |   |   +-- polynomial.cpython-311.pyc
|   |   |   |   |   |   |   +-- polyutils.cpython-311.pyc
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_chebyshev.py
|   |   |   |   |   |   |   +-- test_classes.py
|   |   |   |   |   |   |   +-- test_hermite.py
|   |   |   |   |   |   |   +-- test_hermite_e.py
|   |   |   |   |   |   |   +-- test_laguerre.py
|   |   |   |   |   |   |   +-- test_legendre.py
|   |   |   |   |   |   |   +-- test_polynomial.py
|   |   |   |   |   |   |   +-- test_polyutils.py
|   |   |   |   |   |   |   +-- test_printing.py
|   |   |   |   |   |   |   +-- test_symbol.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_chebyshev.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_classes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_hermite.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_hermite_e.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_laguerre.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_legendre.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_polynomial.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_polyutils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_printing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_symbol.cpython-311.pyc
|   |   |   |   |   +-- random/
|   |   |   |   |   |   +-- __init__.pxd
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- _bounded_integers.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _bounded_integers.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _bounded_integers.pxd
|   |   |   |   |   |   +-- _bounded_integers.pyi
|   |   |   |   |   |   +-- _common.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _common.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _common.pxd
|   |   |   |   |   |   +-- _common.pyi
|   |   |   |   |   |   +-- _generator.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _generator.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _generator.pyi
|   |   |   |   |   |   +-- _mt19937.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _mt19937.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _mt19937.pyi
|   |   |   |   |   |   +-- _pcg64.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _pcg64.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _pcg64.pyi
|   |   |   |   |   |   +-- _philox.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _philox.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _philox.pyi
|   |   |   |   |   |   +-- _pickle.py
|   |   |   |   |   |   +-- _pickle.pyi
|   |   |   |   |   |   +-- _sfc64.cp311-win_amd64.lib
|   |   |   |   |   |   +-- _sfc64.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- _sfc64.pyi
|   |   |   |   |   |   +-- bit_generator.cp311-win_amd64.lib
|   |   |   |   |   |   +-- bit_generator.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- bit_generator.pxd
|   |   |   |   |   |   +-- bit_generator.pyi
|   |   |   |   |   |   +-- c_distributions.pxd
|   |   |   |   |   |   +-- LICENSE.md
|   |   |   |   |   |   +-- mtrand.cp311-win_amd64.lib
|   |   |   |   |   |   +-- mtrand.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- mtrand.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _pickle.cpython-311.pyc
|   |   |   |   |   |   +-- _examples/
|   |   |   |   |   |   |   +-- cffi/
|   |   |   |   |   |   |   |   +-- extending.py
|   |   |   |   |   |   |   |   +-- parse.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- extending.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- parse.cpython-311.pyc
|   |   |   |   |   |   |   +-- cython/
|   |   |   |   |   |   |   |   +-- extending.pyx
|   |   |   |   |   |   |   |   +-- extending_distributions.pyx
|   |   |   |   |   |   |   |   +-- meson.build
|   |   |   |   |   |   |   +-- numba/
|   |   |   |   |   |   |   |   +-- extending.py
|   |   |   |   |   |   |   |   +-- extending_distributions.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- extending.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- extending_distributions.cpython-311.pyc
|   |   |   |   |   |   +-- lib/
|   |   |   |   |   |   |   +-- npyrandom.lib
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_direct.py
|   |   |   |   |   |   |   +-- test_extending.py
|   |   |   |   |   |   |   +-- test_generator_mt19937.py
|   |   |   |   |   |   |   +-- test_generator_mt19937_regressions.py
|   |   |   |   |   |   |   +-- test_random.py
|   |   |   |   |   |   |   +-- test_randomstate.py
|   |   |   |   |   |   |   +-- test_randomstate_regression.py
|   |   |   |   |   |   |   +-- test_regression.py
|   |   |   |   |   |   |   +-- test_seed_sequence.py
|   |   |   |   |   |   |   +-- test_smoke.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_direct.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_extending.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_generator_mt19937.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_generator_mt19937_regressions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_random.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_randomstate.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_randomstate_regression.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_regression.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_seed_sequence.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_smoke.cpython-311.pyc
|   |   |   |   |   |   |   +-- data/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- generator_pcg64_np121.pkl.gz
|   |   |   |   |   |   |   |   +-- generator_pcg64_np126.pkl.gz
|   |   |   |   |   |   |   |   +-- mt19937-testset-1.csv
|   |   |   |   |   |   |   |   +-- mt19937-testset-2.csv
|   |   |   |   |   |   |   |   +-- pcg64dxsm-testset-1.csv
|   |   |   |   |   |   |   |   +-- pcg64dxsm-testset-2.csv
|   |   |   |   |   |   |   |   +-- pcg64-testset-1.csv
|   |   |   |   |   |   |   |   +-- pcg64-testset-2.csv
|   |   |   |   |   |   |   |   +-- philox-testset-1.csv
|   |   |   |   |   |   |   |   +-- philox-testset-2.csv
|   |   |   |   |   |   |   |   +-- sfc64_np126.pkl.gz
|   |   |   |   |   |   |   |   +-- sfc64-testset-1.csv
|   |   |   |   |   |   |   |   +-- sfc64-testset-2.csv
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- rec/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- strings/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- testing/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   +-- overrides.py
|   |   |   |   |   |   +-- overrides.pyi
|   |   |   |   |   |   +-- print_coercion_tables.py
|   |   |   |   |   |   +-- print_coercion_tables.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- overrides.cpython-311.pyc
|   |   |   |   |   |   |   +-- print_coercion_tables.cpython-311.pyc
|   |   |   |   |   |   +-- _private/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __init__.pyi
|   |   |   |   |   |   |   +-- extbuild.py
|   |   |   |   |   |   |   +-- extbuild.pyi
|   |   |   |   |   |   |   +-- utils.py
|   |   |   |   |   |   |   +-- utils.pyi
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- extbuild.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_utils.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_utils.cpython-311.pyc
|   |   |   |   |   +-- tests/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- test__all__.py
|   |   |   |   |   |   +-- test_configtool.py
|   |   |   |   |   |   +-- test_ctypeslib.py
|   |   |   |   |   |   +-- test_lazyloading.py
|   |   |   |   |   |   +-- test_matlib.py
|   |   |   |   |   |   +-- test_numpy_config.py
|   |   |   |   |   |   +-- test_numpy_version.py
|   |   |   |   |   |   +-- test_public_api.py
|   |   |   |   |   |   +-- test_reloading.py
|   |   |   |   |   |   +-- test_scripts.py
|   |   |   |   |   |   +-- test_warnings.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- test__all__.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_configtool.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_ctypeslib.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_lazyloading.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_matlib.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_numpy_config.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_numpy_version.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_public_api.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_reloading.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_scripts.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_warnings.cpython-311.pyc
|   |   |   |   |   +-- typing/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- mypy_plugin.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- mypy_plugin.cpython-311.pyc
|   |   |   |   |   |   +-- tests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_isfile.py
|   |   |   |   |   |   |   +-- test_runtime.py
|   |   |   |   |   |   |   +-- test_typing.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_isfile.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_runtime.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_typing.cpython-311.pyc
|   |   |   |   |   |   |   +-- data/
|   |   |   |   |   |   |   |   +-- mypy.ini
|   |   |   |   |   |   |   |   +-- fail/
|   |   |   |   |   |   |   |   |   +-- arithmetic.pyi
|   |   |   |   |   |   |   |   |   +-- array_constructors.pyi
|   |   |   |   |   |   |   |   |   +-- array_like.pyi
|   |   |   |   |   |   |   |   |   +-- array_pad.pyi
|   |   |   |   |   |   |   |   |   +-- arrayprint.pyi
|   |   |   |   |   |   |   |   |   +-- arrayterator.pyi
|   |   |   |   |   |   |   |   |   +-- bitwise_ops.pyi
|   |   |   |   |   |   |   |   |   +-- char.pyi
|   |   |   |   |   |   |   |   |   +-- chararray.pyi
|   |   |   |   |   |   |   |   |   +-- comparisons.pyi
|   |   |   |   |   |   |   |   |   +-- constants.pyi
|   |   |   |   |   |   |   |   |   +-- datasource.pyi
|   |   |   |   |   |   |   |   |   +-- dtype.pyi
|   |   |   |   |   |   |   |   |   +-- einsumfunc.pyi
|   |   |   |   |   |   |   |   |   +-- flatiter.pyi
|   |   |   |   |   |   |   |   |   +-- fromnumeric.pyi
|   |   |   |   |   |   |   |   |   +-- histograms.pyi
|   |   |   |   |   |   |   |   |   +-- index_tricks.pyi
|   |   |   |   |   |   |   |   |   +-- lib_function_base.pyi
|   |   |   |   |   |   |   |   |   +-- lib_polynomial.pyi
|   |   |   |   |   |   |   |   |   +-- lib_utils.pyi
|   |   |   |   |   |   |   |   |   +-- lib_version.pyi
|   |   |   |   |   |   |   |   |   +-- linalg.pyi
|   |   |   |   |   |   |   |   |   +-- ma.pyi
|   |   |   |   |   |   |   |   |   +-- memmap.pyi
|   |   |   |   |   |   |   |   |   +-- modules.pyi
|   |   |   |   |   |   |   |   |   +-- multiarray.pyi
|   |   |   |   |   |   |   |   |   +-- ndarray.pyi
|   |   |   |   |   |   |   |   |   +-- ndarray_misc.pyi
|   |   |   |   |   |   |   |   |   +-- nditer.pyi
|   |   |   |   |   |   |   |   |   +-- nested_sequence.pyi
|   |   |   |   |   |   |   |   |   +-- npyio.pyi
|   |   |   |   |   |   |   |   |   +-- numerictypes.pyi
|   |   |   |   |   |   |   |   |   +-- random.pyi
|   |   |   |   |   |   |   |   |   +-- rec.pyi
|   |   |   |   |   |   |   |   |   +-- scalars.pyi
|   |   |   |   |   |   |   |   |   +-- shape.pyi
|   |   |   |   |   |   |   |   |   +-- shape_base.pyi
|   |   |   |   |   |   |   |   |   +-- stride_tricks.pyi
|   |   |   |   |   |   |   |   |   +-- strings.pyi
|   |   |   |   |   |   |   |   |   +-- testing.pyi
|   |   |   |   |   |   |   |   |   +-- twodim_base.pyi
|   |   |   |   |   |   |   |   |   +-- type_check.pyi
|   |   |   |   |   |   |   |   |   +-- ufunc_config.pyi
|   |   |   |   |   |   |   |   |   +-- ufunclike.pyi
|   |   |   |   |   |   |   |   |   +-- ufuncs.pyi
|   |   |   |   |   |   |   |   |   +-- warnings_and_errors.pyi
|   |   |   |   |   |   |   |   +-- misc/
|   |   |   |   |   |   |   |   |   +-- extended_precision.pyi
|   |   |   |   |   |   |   |   +-- pass/
|   |   |   |   |   |   |   |   |   +-- arithmetic.py
|   |   |   |   |   |   |   |   |   +-- array_constructors.py
|   |   |   |   |   |   |   |   |   +-- array_like.py
|   |   |   |   |   |   |   |   |   +-- arrayprint.py
|   |   |   |   |   |   |   |   |   +-- arrayterator.py
|   |   |   |   |   |   |   |   |   +-- bitwise_ops.py
|   |   |   |   |   |   |   |   |   +-- comparisons.py
|   |   |   |   |   |   |   |   |   +-- dtype.py
|   |   |   |   |   |   |   |   |   +-- einsumfunc.py
|   |   |   |   |   |   |   |   |   +-- flatiter.py
|   |   |   |   |   |   |   |   |   +-- fromnumeric.py
|   |   |   |   |   |   |   |   |   +-- index_tricks.py
|   |   |   |   |   |   |   |   |   +-- lib_user_array.py
|   |   |   |   |   |   |   |   |   +-- lib_utils.py
|   |   |   |   |   |   |   |   |   +-- lib_version.py
|   |   |   |   |   |   |   |   |   +-- literal.py
|   |   |   |   |   |   |   |   |   +-- ma.py
|   |   |   |   |   |   |   |   |   +-- mod.py
|   |   |   |   |   |   |   |   |   +-- modules.py
|   |   |   |   |   |   |   |   |   +-- multiarray.py
|   |   |   |   |   |   |   |   |   +-- ndarray_conversion.py
|   |   |   |   |   |   |   |   |   +-- ndarray_misc.py
|   |   |   |   |   |   |   |   |   +-- ndarray_shape_manipulation.py
|   |   |   |   |   |   |   |   |   +-- nditer.py
|   |   |   |   |   |   |   |   |   +-- numeric.py
|   |   |   |   |   |   |   |   |   +-- numerictypes.py
|   |   |   |   |   |   |   |   |   +-- random.py
|   |   |   |   |   |   |   |   |   +-- recfunctions.py
|   |   |   |   |   |   |   |   |   +-- scalars.py
|   |   |   |   |   |   |   |   |   +-- shape.py
|   |   |   |   |   |   |   |   |   +-- simple.py
|   |   |   |   |   |   |   |   |   +-- simple_py3.py
|   |   |   |   |   |   |   |   |   +-- ufunc_config.py
|   |   |   |   |   |   |   |   |   +-- ufunclike.py
|   |   |   |   |   |   |   |   |   +-- ufuncs.py
|   |   |   |   |   |   |   |   |   +-- warnings_and_errors.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- array_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- array_like.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- arrayprint.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- arrayterator.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- bitwise_ops.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- comparisons.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- dtype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- einsumfunc.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- flatiter.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- fromnumeric.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- index_tricks.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- lib_user_array.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- lib_utils.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- lib_version.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- literal.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- ma.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- mod.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- modules.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- multiarray.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- ndarray_conversion.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- ndarray_misc.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- ndarray_shape_manipulation.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- nditer.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- numeric.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- numerictypes.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- random.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- recfunctions.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- scalars.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- shape.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- simple.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- simple_py3.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- ufunc_config.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- ufunclike.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- ufuncs.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- warnings_and_errors.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- reveal/
|   |   |   |   |   |   |   |   |   +-- arithmetic.pyi
|   |   |   |   |   |   |   |   |   +-- array_api_info.pyi
|   |   |   |   |   |   |   |   |   +-- array_constructors.pyi
|   |   |   |   |   |   |   |   |   +-- arraypad.pyi
|   |   |   |   |   |   |   |   |   +-- arrayprint.pyi
|   |   |   |   |   |   |   |   |   +-- arraysetops.pyi
|   |   |   |   |   |   |   |   |   +-- arrayterator.pyi
|   |   |   |   |   |   |   |   |   +-- bitwise_ops.pyi
|   |   |   |   |   |   |   |   |   +-- char.pyi
|   |   |   |   |   |   |   |   |   +-- chararray.pyi
|   |   |   |   |   |   |   |   |   +-- comparisons.pyi
|   |   |   |   |   |   |   |   |   +-- constants.pyi
|   |   |   |   |   |   |   |   |   +-- ctypeslib.pyi
|   |   |   |   |   |   |   |   |   +-- datasource.pyi
|   |   |   |   |   |   |   |   |   +-- dtype.pyi
|   |   |   |   |   |   |   |   |   +-- einsumfunc.pyi
|   |   |   |   |   |   |   |   |   +-- emath.pyi
|   |   |   |   |   |   |   |   |   +-- fft.pyi
|   |   |   |   |   |   |   |   |   +-- flatiter.pyi
|   |   |   |   |   |   |   |   |   +-- fromnumeric.pyi
|   |   |   |   |   |   |   |   |   +-- getlimits.pyi
|   |   |   |   |   |   |   |   |   +-- histograms.pyi
|   |   |   |   |   |   |   |   |   +-- index_tricks.pyi
|   |   |   |   |   |   |   |   |   +-- lib_function_base.pyi
|   |   |   |   |   |   |   |   |   +-- lib_polynomial.pyi
|   |   |   |   |   |   |   |   |   +-- lib_utils.pyi
|   |   |   |   |   |   |   |   |   +-- lib_version.pyi
|   |   |   |   |   |   |   |   |   +-- linalg.pyi
|   |   |   |   |   |   |   |   |   +-- ma.pyi
|   |   |   |   |   |   |   |   |   +-- matrix.pyi
|   |   |   |   |   |   |   |   |   +-- memmap.pyi
|   |   |   |   |   |   |   |   |   +-- mod.pyi
|   |   |   |   |   |   |   |   |   +-- modules.pyi
|   |   |   |   |   |   |   |   |   +-- multiarray.pyi
|   |   |   |   |   |   |   |   |   +-- nbit_base_example.pyi
|   |   |   |   |   |   |   |   |   +-- ndarray_assignability.pyi
|   |   |   |   |   |   |   |   |   +-- ndarray_conversion.pyi
|   |   |   |   |   |   |   |   |   +-- ndarray_misc.pyi
|   |   |   |   |   |   |   |   |   +-- ndarray_shape_manipulation.pyi
|   |   |   |   |   |   |   |   |   +-- nditer.pyi
|   |   |   |   |   |   |   |   |   +-- nested_sequence.pyi
|   |   |   |   |   |   |   |   |   +-- npyio.pyi
|   |   |   |   |   |   |   |   |   +-- numeric.pyi
|   |   |   |   |   |   |   |   |   +-- numerictypes.pyi
|   |   |   |   |   |   |   |   |   +-- polynomial_polybase.pyi
|   |   |   |   |   |   |   |   |   +-- polynomial_polyutils.pyi
|   |   |   |   |   |   |   |   |   +-- polynomial_series.pyi
|   |   |   |   |   |   |   |   |   +-- random.pyi
|   |   |   |   |   |   |   |   |   +-- rec.pyi
|   |   |   |   |   |   |   |   |   +-- scalars.pyi
|   |   |   |   |   |   |   |   |   +-- shape.pyi
|   |   |   |   |   |   |   |   |   +-- shape_base.pyi
|   |   |   |   |   |   |   |   |   +-- stride_tricks.pyi
|   |   |   |   |   |   |   |   |   +-- strings.pyi
|   |   |   |   |   |   |   |   |   +-- testing.pyi
|   |   |   |   |   |   |   |   |   +-- twodim_base.pyi
|   |   |   |   |   |   |   |   |   +-- type_check.pyi
|   |   |   |   |   |   |   |   |   +-- ufunc_config.pyi
|   |   |   |   |   |   |   |   |   +-- ufunclike.pyi
|   |   |   |   |   |   |   |   |   +-- ufuncs.pyi
|   |   |   |   |   |   |   |   |   +-- warnings_and_errors.pyi
|   |   |   |   +-- numpy.libs/
|   |   |   |   |   +-- libscipy_openblas64_-9e3e5a4229c1ca39f10dc82bba9e2b2b.dll
|   |   |   |   |   +-- msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
|   |   |   |   +-- numpy-2.3.5.dist-info/
|   |   |   |   |   +-- DELVEWHEEL
|   |   |   |   |   +-- entry_points.txt
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- openpyxl/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _constants.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _constants.cpython-311.pyc
|   |   |   |   |   +-- cell/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _writer.py
|   |   |   |   |   |   +-- cell.py
|   |   |   |   |   |   +-- read_only.py
|   |   |   |   |   |   +-- rich_text.py
|   |   |   |   |   |   +-- text.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _writer.cpython-311.pyc
|   |   |   |   |   |   |   +-- cell.cpython-311.pyc
|   |   |   |   |   |   |   +-- read_only.cpython-311.pyc
|   |   |   |   |   |   |   +-- rich_text.cpython-311.pyc
|   |   |   |   |   |   |   +-- text.cpython-311.pyc
|   |   |   |   |   +-- chart/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _3d.py
|   |   |   |   |   |   +-- _chart.py
|   |   |   |   |   |   +-- area_chart.py
|   |   |   |   |   |   +-- axis.py
|   |   |   |   |   |   +-- bar_chart.py
|   |   |   |   |   |   +-- bubble_chart.py
|   |   |   |   |   |   +-- chartspace.py
|   |   |   |   |   |   +-- data_source.py
|   |   |   |   |   |   +-- descriptors.py
|   |   |   |   |   |   +-- error_bar.py
|   |   |   |   |   |   +-- label.py
|   |   |   |   |   |   +-- layout.py
|   |   |   |   |   |   +-- legend.py
|   |   |   |   |   |   +-- line_chart.py
|   |   |   |   |   |   +-- marker.py
|   |   |   |   |   |   +-- picture.py
|   |   |   |   |   |   +-- pie_chart.py
|   |   |   |   |   |   +-- pivot.py
|   |   |   |   |   |   +-- plotarea.py
|   |   |   |   |   |   +-- print_settings.py
|   |   |   |   |   |   +-- radar_chart.py
|   |   |   |   |   |   +-- reader.py
|   |   |   |   |   |   +-- reference.py
|   |   |   |   |   |   +-- scatter_chart.py
|   |   |   |   |   |   +-- series.py
|   |   |   |   |   |   +-- series_factory.py
|   |   |   |   |   |   +-- shapes.py
|   |   |   |   |   |   +-- stock_chart.py
|   |   |   |   |   |   +-- surface_chart.py
|   |   |   |   |   |   +-- text.py
|   |   |   |   |   |   +-- title.py
|   |   |   |   |   |   +-- trendline.py
|   |   |   |   |   |   +-- updown_bars.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _3d.cpython-311.pyc
|   |   |   |   |   |   |   +-- _chart.cpython-311.pyc
|   |   |   |   |   |   |   +-- area_chart.cpython-311.pyc
|   |   |   |   |   |   |   +-- axis.cpython-311.pyc
|   |   |   |   |   |   |   +-- bar_chart.cpython-311.pyc
|   |   |   |   |   |   |   +-- bubble_chart.cpython-311.pyc
|   |   |   |   |   |   |   +-- chartspace.cpython-311.pyc
|   |   |   |   |   |   |   +-- data_source.cpython-311.pyc
|   |   |   |   |   |   |   +-- descriptors.cpython-311.pyc
|   |   |   |   |   |   |   +-- error_bar.cpython-311.pyc
|   |   |   |   |   |   |   +-- label.cpython-311.pyc
|   |   |   |   |   |   |   +-- layout.cpython-311.pyc
|   |   |   |   |   |   |   +-- legend.cpython-311.pyc
|   |   |   |   |   |   |   +-- line_chart.cpython-311.pyc
|   |   |   |   |   |   |   +-- marker.cpython-311.pyc
|   |   |   |   |   |   |   +-- picture.cpython-311.pyc
|   |   |   |   |   |   |   +-- pie_chart.cpython-311.pyc
|   |   |   |   |   |   |   +-- pivot.cpython-311.pyc
|   |   |   |   |   |   |   +-- plotarea.cpython-311.pyc
|   |   |   |   |   |   |   +-- print_settings.cpython-311.pyc
|   |   |   |   |   |   |   +-- radar_chart.cpython-311.pyc
|   |   |   |   |   |   |   +-- reader.cpython-311.pyc
|   |   |   |   |   |   |   +-- reference.cpython-311.pyc
|   |   |   |   |   |   |   +-- scatter_chart.cpython-311.pyc
|   |   |   |   |   |   |   +-- series.cpython-311.pyc
|   |   |   |   |   |   |   +-- series_factory.cpython-311.pyc
|   |   |   |   |   |   |   +-- shapes.cpython-311.pyc
|   |   |   |   |   |   |   +-- stock_chart.cpython-311.pyc
|   |   |   |   |   |   |   +-- surface_chart.cpython-311.pyc
|   |   |   |   |   |   |   +-- text.cpython-311.pyc
|   |   |   |   |   |   |   +-- title.cpython-311.pyc
|   |   |   |   |   |   |   +-- trendline.cpython-311.pyc
|   |   |   |   |   |   |   +-- updown_bars.cpython-311.pyc
|   |   |   |   |   +-- chartsheet/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- chartsheet.py
|   |   |   |   |   |   +-- custom.py
|   |   |   |   |   |   +-- properties.py
|   |   |   |   |   |   +-- protection.py
|   |   |   |   |   |   +-- publish.py
|   |   |   |   |   |   +-- relation.py
|   |   |   |   |   |   +-- views.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- chartsheet.cpython-311.pyc
|   |   |   |   |   |   |   +-- custom.cpython-311.pyc
|   |   |   |   |   |   |   +-- properties.cpython-311.pyc
|   |   |   |   |   |   |   +-- protection.cpython-311.pyc
|   |   |   |   |   |   |   +-- publish.cpython-311.pyc
|   |   |   |   |   |   |   +-- relation.cpython-311.pyc
|   |   |   |   |   |   |   +-- views.cpython-311.pyc
|   |   |   |   |   +-- comments/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- author.py
|   |   |   |   |   |   +-- comment_sheet.py
|   |   |   |   |   |   +-- comments.py
|   |   |   |   |   |   +-- shape_writer.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- author.cpython-311.pyc
|   |   |   |   |   |   |   +-- comment_sheet.cpython-311.pyc
|   |   |   |   |   |   |   +-- comments.cpython-311.pyc
|   |   |   |   |   |   |   +-- shape_writer.cpython-311.pyc
|   |   |   |   |   +-- compat/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- abc.py
|   |   |   |   |   |   +-- numbers.py
|   |   |   |   |   |   +-- product.py
|   |   |   |   |   |   +-- singleton.py
|   |   |   |   |   |   +-- strings.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- abc.cpython-311.pyc
|   |   |   |   |   |   |   +-- numbers.cpython-311.pyc
|   |   |   |   |   |   |   +-- product.cpython-311.pyc
|   |   |   |   |   |   |   +-- singleton.cpython-311.pyc
|   |   |   |   |   |   |   +-- strings.cpython-311.pyc
|   |   |   |   |   +-- descriptors/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   +-- container.py
|   |   |   |   |   |   +-- excel.py
|   |   |   |   |   |   +-- namespace.py
|   |   |   |   |   |   +-- nested.py
|   |   |   |   |   |   +-- sequence.py
|   |   |   |   |   |   +-- serialisable.py
|   |   |   |   |   |   +-- slots.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   +-- container.cpython-311.pyc
|   |   |   |   |   |   |   +-- excel.cpython-311.pyc
|   |   |   |   |   |   |   +-- namespace.cpython-311.pyc
|   |   |   |   |   |   |   +-- nested.cpython-311.pyc
|   |   |   |   |   |   |   +-- sequence.cpython-311.pyc
|   |   |   |   |   |   |   +-- serialisable.cpython-311.pyc
|   |   |   |   |   |   |   +-- slots.cpython-311.pyc
|   |   |   |   |   +-- drawing/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- colors.py
|   |   |   |   |   |   +-- connector.py
|   |   |   |   |   |   +-- drawing.py
|   |   |   |   |   |   +-- effect.py
|   |   |   |   |   |   +-- fill.py
|   |   |   |   |   |   +-- geometry.py
|   |   |   |   |   |   +-- graphic.py
|   |   |   |   |   |   +-- image.py
|   |   |   |   |   |   +-- line.py
|   |   |   |   |   |   +-- picture.py
|   |   |   |   |   |   +-- properties.py
|   |   |   |   |   |   +-- relation.py
|   |   |   |   |   |   +-- spreadsheet_drawing.py
|   |   |   |   |   |   +-- text.py
|   |   |   |   |   |   +-- xdr.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- colors.cpython-311.pyc
|   |   |   |   |   |   |   +-- connector.cpython-311.pyc
|   |   |   |   |   |   |   +-- drawing.cpython-311.pyc
|   |   |   |   |   |   |   +-- effect.cpython-311.pyc
|   |   |   |   |   |   |   +-- fill.cpython-311.pyc
|   |   |   |   |   |   |   +-- geometry.cpython-311.pyc
|   |   |   |   |   |   |   +-- graphic.cpython-311.pyc
|   |   |   |   |   |   |   +-- image.cpython-311.pyc
|   |   |   |   |   |   |   +-- line.cpython-311.pyc
|   |   |   |   |   |   |   +-- picture.cpython-311.pyc
|   |   |   |   |   |   |   +-- properties.cpython-311.pyc
|   |   |   |   |   |   |   +-- relation.cpython-311.pyc
|   |   |   |   |   |   |   +-- spreadsheet_drawing.cpython-311.pyc
|   |   |   |   |   |   |   +-- text.cpython-311.pyc
|   |   |   |   |   |   |   +-- xdr.cpython-311.pyc
|   |   |   |   |   +-- formatting/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- formatting.py
|   |   |   |   |   |   +-- rule.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- formatting.cpython-311.pyc
|   |   |   |   |   |   |   +-- rule.cpython-311.pyc
|   |   |   |   |   +-- formula/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- tokenizer.py
|   |   |   |   |   |   +-- translate.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- tokenizer.cpython-311.pyc
|   |   |   |   |   |   |   +-- translate.cpython-311.pyc
|   |   |   |   |   +-- packaging/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- core.py
|   |   |   |   |   |   +-- custom.py
|   |   |   |   |   |   +-- extended.py
|   |   |   |   |   |   +-- interface.py
|   |   |   |   |   |   +-- manifest.py
|   |   |   |   |   |   +-- relationship.py
|   |   |   |   |   |   +-- workbook.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- core.cpython-311.pyc
|   |   |   |   |   |   |   +-- custom.cpython-311.pyc
|   |   |   |   |   |   |   +-- extended.cpython-311.pyc
|   |   |   |   |   |   |   +-- interface.cpython-311.pyc
|   |   |   |   |   |   |   +-- manifest.cpython-311.pyc
|   |   |   |   |   |   |   +-- relationship.cpython-311.pyc
|   |   |   |   |   |   |   +-- workbook.cpython-311.pyc
|   |   |   |   |   +-- pivot/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- cache.py
|   |   |   |   |   |   +-- fields.py
|   |   |   |   |   |   +-- record.py
|   |   |   |   |   |   +-- table.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- cache.cpython-311.pyc
|   |   |   |   |   |   |   +-- fields.cpython-311.pyc
|   |   |   |   |   |   |   +-- record.cpython-311.pyc
|   |   |   |   |   |   |   +-- table.cpython-311.pyc
|   |   |   |   |   +-- reader/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- drawings.py
|   |   |   |   |   |   +-- excel.py
|   |   |   |   |   |   +-- strings.py
|   |   |   |   |   |   +-- workbook.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- drawings.cpython-311.pyc
|   |   |   |   |   |   |   +-- excel.cpython-311.pyc
|   |   |   |   |   |   |   +-- strings.cpython-311.pyc
|   |   |   |   |   |   |   +-- workbook.cpython-311.pyc
|   |   |   |   |   +-- styles/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- alignment.py
|   |   |   |   |   |   +-- borders.py
|   |   |   |   |   |   +-- builtins.py
|   |   |   |   |   |   +-- cell_style.py
|   |   |   |   |   |   +-- colors.py
|   |   |   |   |   |   +-- differential.py
|   |   |   |   |   |   +-- fills.py
|   |   |   |   |   |   +-- fonts.py
|   |   |   |   |   |   +-- named_styles.py
|   |   |   |   |   |   +-- numbers.py
|   |   |   |   |   |   +-- protection.py
|   |   |   |   |   |   +-- proxy.py
|   |   |   |   |   |   +-- styleable.py
|   |   |   |   |   |   +-- stylesheet.py
|   |   |   |   |   |   +-- table.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- alignment.cpython-311.pyc
|   |   |   |   |   |   |   +-- borders.cpython-311.pyc
|   |   |   |   |   |   |   +-- builtins.cpython-311.pyc
|   |   |   |   |   |   |   +-- cell_style.cpython-311.pyc
|   |   |   |   |   |   |   +-- colors.cpython-311.pyc
|   |   |   |   |   |   |   +-- differential.cpython-311.pyc
|   |   |   |   |   |   |   +-- fills.cpython-311.pyc
|   |   |   |   |   |   |   +-- fonts.cpython-311.pyc
|   |   |   |   |   |   |   +-- named_styles.cpython-311.pyc
|   |   |   |   |   |   |   +-- numbers.cpython-311.pyc
|   |   |   |   |   |   |   +-- protection.cpython-311.pyc
|   |   |   |   |   |   |   +-- proxy.cpython-311.pyc
|   |   |   |   |   |   |   +-- styleable.cpython-311.pyc
|   |   |   |   |   |   |   +-- stylesheet.cpython-311.pyc
|   |   |   |   |   |   |   +-- table.cpython-311.pyc
|   |   |   |   |   +-- utils/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- bound_dictionary.py
|   |   |   |   |   |   +-- cell.py
|   |   |   |   |   |   +-- dataframe.py
|   |   |   |   |   |   +-- datetime.py
|   |   |   |   |   |   +-- escape.py
|   |   |   |   |   |   +-- exceptions.py
|   |   |   |   |   |   +-- formulas.py
|   |   |   |   |   |   +-- indexed_list.py
|   |   |   |   |   |   +-- inference.py
|   |   |   |   |   |   +-- protection.py
|   |   |   |   |   |   +-- units.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- bound_dictionary.cpython-311.pyc
|   |   |   |   |   |   |   +-- cell.cpython-311.pyc
|   |   |   |   |   |   |   +-- dataframe.cpython-311.pyc
|   |   |   |   |   |   |   +-- datetime.cpython-311.pyc
|   |   |   |   |   |   |   +-- escape.cpython-311.pyc
|   |   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   |   +-- formulas.cpython-311.pyc
|   |   |   |   |   |   |   +-- indexed_list.cpython-311.pyc
|   |   |   |   |   |   |   +-- inference.cpython-311.pyc
|   |   |   |   |   |   |   +-- protection.cpython-311.pyc
|   |   |   |   |   |   |   +-- units.cpython-311.pyc
|   |   |   |   |   +-- workbook/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _writer.py
|   |   |   |   |   |   +-- child.py
|   |   |   |   |   |   +-- defined_name.py
|   |   |   |   |   |   +-- external_reference.py
|   |   |   |   |   |   +-- function_group.py
|   |   |   |   |   |   +-- properties.py
|   |   |   |   |   |   +-- protection.py
|   |   |   |   |   |   +-- smart_tags.py
|   |   |   |   |   |   +-- views.py
|   |   |   |   |   |   +-- web.py
|   |   |   |   |   |   +-- workbook.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _writer.cpython-311.pyc
|   |   |   |   |   |   |   +-- child.cpython-311.pyc
|   |   |   |   |   |   |   +-- defined_name.cpython-311.pyc
|   |   |   |   |   |   |   +-- external_reference.cpython-311.pyc
|   |   |   |   |   |   |   +-- function_group.cpython-311.pyc
|   |   |   |   |   |   |   +-- properties.cpython-311.pyc
|   |   |   |   |   |   |   +-- protection.cpython-311.pyc
|   |   |   |   |   |   |   +-- smart_tags.cpython-311.pyc
|   |   |   |   |   |   |   +-- views.cpython-311.pyc
|   |   |   |   |   |   |   +-- web.cpython-311.pyc
|   |   |   |   |   |   |   +-- workbook.cpython-311.pyc
|   |   |   |   |   |   +-- external_link/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- external.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- external.cpython-311.pyc
|   |   |   |   |   +-- worksheet/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _read_only.py
|   |   |   |   |   |   +-- _reader.py
|   |   |   |   |   |   +-- _write_only.py
|   |   |   |   |   |   +-- _writer.py
|   |   |   |   |   |   +-- cell_range.py
|   |   |   |   |   |   +-- cell_watch.py
|   |   |   |   |   |   +-- controls.py
|   |   |   |   |   |   +-- copier.py
|   |   |   |   |   |   +-- custom.py
|   |   |   |   |   |   +-- datavalidation.py
|   |   |   |   |   |   +-- dimensions.py
|   |   |   |   |   |   +-- drawing.py
|   |   |   |   |   |   +-- errors.py
|   |   |   |   |   |   +-- filters.py
|   |   |   |   |   |   +-- formula.py
|   |   |   |   |   |   +-- header_footer.py
|   |   |   |   |   |   +-- hyperlink.py
|   |   |   |   |   |   +-- merge.py
|   |   |   |   |   |   +-- ole.py
|   |   |   |   |   |   +-- page.py
|   |   |   |   |   |   +-- pagebreak.py
|   |   |   |   |   |   +-- picture.py
|   |   |   |   |   |   +-- print_settings.py
|   |   |   |   |   |   +-- properties.py
|   |   |   |   |   |   +-- protection.py
|   |   |   |   |   |   +-- related.py
|   |   |   |   |   |   +-- scenario.py
|   |   |   |   |   |   +-- smart_tag.py
|   |   |   |   |   |   +-- table.py
|   |   |   |   |   |   +-- views.py
|   |   |   |   |   |   +-- worksheet.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _read_only.cpython-311.pyc
|   |   |   |   |   |   |   +-- _reader.cpython-311.pyc
|   |   |   |   |   |   |   +-- _write_only.cpython-311.pyc
|   |   |   |   |   |   |   +-- _writer.cpython-311.pyc
|   |   |   |   |   |   |   +-- cell_range.cpython-311.pyc
|   |   |   |   |   |   |   +-- cell_watch.cpython-311.pyc
|   |   |   |   |   |   |   +-- controls.cpython-311.pyc
|   |   |   |   |   |   |   +-- copier.cpython-311.pyc
|   |   |   |   |   |   |   +-- custom.cpython-311.pyc
|   |   |   |   |   |   |   +-- datavalidation.cpython-311.pyc
|   |   |   |   |   |   |   +-- dimensions.cpython-311.pyc
|   |   |   |   |   |   |   +-- drawing.cpython-311.pyc
|   |   |   |   |   |   |   +-- errors.cpython-311.pyc
|   |   |   |   |   |   |   +-- filters.cpython-311.pyc
|   |   |   |   |   |   |   +-- formula.cpython-311.pyc
|   |   |   |   |   |   |   +-- header_footer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hyperlink.cpython-311.pyc
|   |   |   |   |   |   |   +-- merge.cpython-311.pyc
|   |   |   |   |   |   |   +-- ole.cpython-311.pyc
|   |   |   |   |   |   |   +-- page.cpython-311.pyc
|   |   |   |   |   |   |   +-- pagebreak.cpython-311.pyc
|   |   |   |   |   |   |   +-- picture.cpython-311.pyc
|   |   |   |   |   |   |   +-- print_settings.cpython-311.pyc
|   |   |   |   |   |   |   +-- properties.cpython-311.pyc
|   |   |   |   |   |   |   +-- protection.cpython-311.pyc
|   |   |   |   |   |   |   +-- related.cpython-311.pyc
|   |   |   |   |   |   |   +-- scenario.cpython-311.pyc
|   |   |   |   |   |   |   +-- smart_tag.cpython-311.pyc
|   |   |   |   |   |   |   +-- table.cpython-311.pyc
|   |   |   |   |   |   |   +-- views.cpython-311.pyc
|   |   |   |   |   |   |   +-- worksheet.cpython-311.pyc
|   |   |   |   |   +-- writer/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- excel.py
|   |   |   |   |   |   +-- theme.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- excel.cpython-311.pyc
|   |   |   |   |   |   |   +-- theme.cpython-311.pyc
|   |   |   |   |   +-- xml/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- constants.py
|   |   |   |   |   |   +-- functions.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- constants.cpython-311.pyc
|   |   |   |   |   |   |   +-- functions.cpython-311.pyc
|   |   |   |   +-- openpyxl-3.1.5.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENCE.rst
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- REQUESTED
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- ordlookup/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- oleaut32.py
|   |   |   |   |   +-- ws2_32.py
|   |   |   |   |   +-- wsock32.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- oleaut32.cpython-311.pyc
|   |   |   |   |   |   +-- ws2_32.cpython-311.pyc
|   |   |   |   |   |   +-- wsock32.cpython-311.pyc
|   |   |   |   +-- packaging/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _elffile.py
|   |   |   |   |   +-- _manylinux.py
|   |   |   |   |   +-- _musllinux.py
|   |   |   |   |   +-- _parser.py
|   |   |   |   |   +-- _structures.py
|   |   |   |   |   +-- _tokenizer.py
|   |   |   |   |   +-- markers.py
|   |   |   |   |   +-- metadata.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- requirements.py
|   |   |   |   |   +-- specifiers.py
|   |   |   |   |   +-- tags.py
|   |   |   |   |   +-- utils.py
|   |   |   |   |   +-- version.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _elffile.cpython-311.pyc
|   |   |   |   |   |   +-- _manylinux.cpython-311.pyc
|   |   |   |   |   |   +-- _musllinux.cpython-311.pyc
|   |   |   |   |   |   +-- _parser.cpython-311.pyc
|   |   |   |   |   |   +-- _structures.cpython-311.pyc
|   |   |   |   |   |   +-- _tokenizer.cpython-311.pyc
|   |   |   |   |   |   +-- markers.cpython-311.pyc
|   |   |   |   |   |   +-- metadata.cpython-311.pyc
|   |   |   |   |   |   +-- requirements.cpython-311.pyc
|   |   |   |   |   |   +-- specifiers.cpython-311.pyc
|   |   |   |   |   |   +-- tags.cpython-311.pyc
|   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   +-- version.cpython-311.pyc
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _spdx.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _spdx.cpython-311.pyc
|   |   |   |   +-- packaging-25.0.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   +-- LICENSE.APACHE
|   |   |   |   |   |   +-- LICENSE.BSD
|   |   |   |   +-- pandas/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _typing.py
|   |   |   |   |   +-- _version.py
|   |   |   |   |   +-- _version_meson.py
|   |   |   |   |   +-- conftest.py
|   |   |   |   |   +-- pyproject.toml
|   |   |   |   |   +-- testing.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _typing.cpython-311.pyc
|   |   |   |   |   |   +-- _version.cpython-311.pyc
|   |   |   |   |   |   +-- _version_meson.cpython-311.pyc
|   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   +-- testing.cpython-311.pyc
|   |   |   |   |   +-- _config/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- config.py
|   |   |   |   |   |   +-- dates.py
|   |   |   |   |   |   +-- display.py
|   |   |   |   |   |   +-- localization.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- config.cpython-311.pyc
|   |   |   |   |   |   |   +-- dates.cpython-311.pyc
|   |   |   |   |   |   |   +-- display.cpython-311.pyc
|   |   |   |   |   |   |   +-- localization.cpython-311.pyc
|   |   |   |   |   +-- _libs/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- algos.cp311-win_amd64.lib
|   |   |   |   |   |   +-- algos.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- algos.pyi
|   |   |   |   |   |   +-- arrays.cp311-win_amd64.lib
|   |   |   |   |   |   +-- arrays.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- arrays.pyi
|   |   |   |   |   |   +-- byteswap.cp311-win_amd64.lib
|   |   |   |   |   |   +-- byteswap.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- byteswap.pyi
|   |   |   |   |   |   +-- groupby.cp311-win_amd64.lib
|   |   |   |   |   |   +-- groupby.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- groupby.pyi
|   |   |   |   |   |   +-- hashing.cp311-win_amd64.lib
|   |   |   |   |   |   +-- hashing.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- hashing.pyi
|   |   |   |   |   |   +-- hashtable.cp311-win_amd64.lib
|   |   |   |   |   |   +-- hashtable.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- hashtable.pyi
|   |   |   |   |   |   +-- index.cp311-win_amd64.lib
|   |   |   |   |   |   +-- index.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- index.pyi
|   |   |   |   |   |   +-- indexing.cp311-win_amd64.lib
|   |   |   |   |   |   +-- indexing.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- indexing.pyi
|   |   |   |   |   |   +-- internals.cp311-win_amd64.lib
|   |   |   |   |   |   +-- internals.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- internals.pyi
|   |   |   |   |   |   +-- interval.cp311-win_amd64.lib
|   |   |   |   |   |   +-- interval.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- interval.pyi
|   |   |   |   |   |   +-- join.cp311-win_amd64.lib
|   |   |   |   |   |   +-- join.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- join.pyi
|   |   |   |   |   |   +-- json.cp311-win_amd64.lib
|   |   |   |   |   |   +-- json.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- json.pyi
|   |   |   |   |   |   +-- lib.cp311-win_amd64.lib
|   |   |   |   |   |   +-- lib.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- lib.pyi
|   |   |   |   |   |   +-- missing.cp311-win_amd64.lib
|   |   |   |   |   |   +-- missing.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- missing.pyi
|   |   |   |   |   |   +-- ops.cp311-win_amd64.lib
|   |   |   |   |   |   +-- ops.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- ops.pyi
|   |   |   |   |   |   +-- ops_dispatch.cp311-win_amd64.lib
|   |   |   |   |   |   +-- ops_dispatch.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- ops_dispatch.pyi
|   |   |   |   |   |   +-- pandas_datetime.cp311-win_amd64.lib
|   |   |   |   |   |   +-- pandas_datetime.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- pandas_parser.cp311-win_amd64.lib
|   |   |   |   |   |   +-- pandas_parser.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- parsers.cp311-win_amd64.lib
|   |   |   |   |   |   +-- parsers.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- parsers.pyi
|   |   |   |   |   |   +-- properties.cp311-win_amd64.lib
|   |   |   |   |   |   +-- properties.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- properties.pyi
|   |   |   |   |   |   +-- reshape.cp311-win_amd64.lib
|   |   |   |   |   |   +-- reshape.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- reshape.pyi
|   |   |   |   |   |   +-- sas.cp311-win_amd64.lib
|   |   |   |   |   |   +-- sas.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- sas.pyi
|   |   |   |   |   |   +-- sparse.cp311-win_amd64.lib
|   |   |   |   |   |   +-- sparse.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- sparse.pyi
|   |   |   |   |   |   +-- testing.cp311-win_amd64.lib
|   |   |   |   |   |   +-- testing.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- testing.pyi
|   |   |   |   |   |   +-- tslib.cp311-win_amd64.lib
|   |   |   |   |   |   +-- tslib.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- tslib.pyi
|   |   |   |   |   |   +-- writers.cp311-win_amd64.lib
|   |   |   |   |   |   +-- writers.cp311-win_amd64.pyd
|   |   |   |   |   |   +-- writers.pyi
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- tslibs/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- base.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- base.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- ccalendar.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- ccalendar.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- ccalendar.pyi
|   |   |   |   |   |   |   +-- conversion.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- conversion.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- conversion.pyi
|   |   |   |   |   |   |   +-- dtypes.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- dtypes.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- dtypes.pyi
|   |   |   |   |   |   |   +-- fields.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- fields.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- fields.pyi
|   |   |   |   |   |   |   +-- nattype.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- nattype.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- nattype.pyi
|   |   |   |   |   |   |   +-- np_datetime.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- np_datetime.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- np_datetime.pyi
|   |   |   |   |   |   |   +-- offsets.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- offsets.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- offsets.pyi
|   |   |   |   |   |   |   +-- parsing.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- parsing.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- parsing.pyi
|   |   |   |   |   |   |   +-- period.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- period.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- period.pyi
|   |   |   |   |   |   |   +-- strptime.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- strptime.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- strptime.pyi
|   |   |   |   |   |   |   +-- timedeltas.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- timedeltas.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- timedeltas.pyi
|   |   |   |   |   |   |   +-- timestamps.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- timestamps.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- timestamps.pyi
|   |   |   |   |   |   |   +-- timezones.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- timezones.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- timezones.pyi
|   |   |   |   |   |   |   +-- tzconversion.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- tzconversion.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- tzconversion.pyi
|   |   |   |   |   |   |   +-- vectorized.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- vectorized.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- vectorized.pyi
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- window/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- aggregations.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- aggregations.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- aggregations.pyi
|   |   |   |   |   |   |   +-- indexers.cp311-win_amd64.lib
|   |   |   |   |   |   |   +-- indexers.cp311-win_amd64.pyd
|   |   |   |   |   |   |   +-- indexers.pyi
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- _testing/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _hypothesis.py
|   |   |   |   |   |   +-- _io.py
|   |   |   |   |   |   +-- _warnings.py
|   |   |   |   |   |   +-- asserters.py
|   |   |   |   |   |   +-- compat.py
|   |   |   |   |   |   +-- contexts.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _hypothesis.cpython-311.pyc
|   |   |   |   |   |   |   +-- _io.cpython-311.pyc
|   |   |   |   |   |   |   +-- _warnings.cpython-311.pyc
|   |   |   |   |   |   |   +-- asserters.cpython-311.pyc
|   |   |   |   |   |   |   +-- compat.cpython-311.pyc
|   |   |   |   |   |   |   +-- contexts.cpython-311.pyc
|   |   |   |   |   +-- api/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- extensions/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- indexers/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- interchange/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- types/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- typing/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- arrays/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- compat/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _constants.py
|   |   |   |   |   |   +-- _optional.py
|   |   |   |   |   |   +-- compressors.py
|   |   |   |   |   |   +-- pickle_compat.py
|   |   |   |   |   |   +-- pyarrow.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _constants.cpython-311.pyc
|   |   |   |   |   |   |   +-- _optional.cpython-311.pyc
|   |   |   |   |   |   |   +-- compressors.cpython-311.pyc
|   |   |   |   |   |   |   +-- pickle_compat.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyarrow.cpython-311.pyc
|   |   |   |   |   |   +-- numpy/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- function.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- function.cpython-311.pyc
|   |   |   |   |   +-- core/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- accessor.py
|   |   |   |   |   |   +-- algorithms.py
|   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   +-- apply.py
|   |   |   |   |   |   +-- arraylike.py
|   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   +-- config_init.py
|   |   |   |   |   |   +-- construction.py
|   |   |   |   |   |   +-- flags.py
|   |   |   |   |   |   +-- frame.py
|   |   |   |   |   |   +-- generic.py
|   |   |   |   |   |   +-- indexing.py
|   |   |   |   |   |   +-- missing.py
|   |   |   |   |   |   +-- nanops.py
|   |   |   |   |   |   +-- resample.py
|   |   |   |   |   |   +-- roperator.py
|   |   |   |   |   |   +-- sample.py
|   |   |   |   |   |   +-- series.py
|   |   |   |   |   |   +-- shared_docs.py
|   |   |   |   |   |   +-- sorting.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- accessor.cpython-311.pyc
|   |   |   |   |   |   |   +-- algorithms.cpython-311.pyc
|   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   |   +-- apply.cpython-311.pyc
|   |   |   |   |   |   |   +-- arraylike.cpython-311.pyc
|   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   +-- config_init.cpython-311.pyc
|   |   |   |   |   |   |   +-- construction.cpython-311.pyc
|   |   |   |   |   |   |   +-- flags.cpython-311.pyc
|   |   |   |   |   |   |   +-- frame.cpython-311.pyc
|   |   |   |   |   |   |   +-- generic.cpython-311.pyc
|   |   |   |   |   |   |   +-- indexing.cpython-311.pyc
|   |   |   |   |   |   |   +-- missing.cpython-311.pyc
|   |   |   |   |   |   |   +-- nanops.cpython-311.pyc
|   |   |   |   |   |   |   +-- resample.cpython-311.pyc
|   |   |   |   |   |   |   +-- roperator.cpython-311.pyc
|   |   |   |   |   |   |   +-- sample.cpython-311.pyc
|   |   |   |   |   |   |   +-- series.cpython-311.pyc
|   |   |   |   |   |   |   +-- shared_docs.cpython-311.pyc
|   |   |   |   |   |   |   +-- sorting.cpython-311.pyc
|   |   |   |   |   |   +-- _numba/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- executor.py
|   |   |   |   |   |   |   +-- extensions.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- executor.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- extensions.cpython-311.pyc
|   |   |   |   |   |   |   +-- kernels/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- mean_.py
|   |   |   |   |   |   |   |   +-- min_max_.py
|   |   |   |   |   |   |   |   +-- shared.py
|   |   |   |   |   |   |   |   +-- sum_.py
|   |   |   |   |   |   |   |   +-- var_.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- mean_.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- min_max_.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- shared.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- sum_.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- var_.cpython-311.pyc
|   |   |   |   |   |   +-- array_algos/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- datetimelike_accumulations.py
|   |   |   |   |   |   |   +-- masked_accumulations.py
|   |   |   |   |   |   |   +-- masked_reductions.py
|   |   |   |   |   |   |   +-- putmask.py
|   |   |   |   |   |   |   +-- quantile.py
|   |   |   |   |   |   |   +-- replace.py
|   |   |   |   |   |   |   +-- take.py
|   |   |   |   |   |   |   +-- transforms.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- datetimelike_accumulations.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- masked_accumulations.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- masked_reductions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- putmask.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- quantile.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- replace.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- take.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- transforms.cpython-311.pyc
|   |   |   |   |   |   +-- arrays/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _arrow_string_mixins.py
|   |   |   |   |   |   |   +-- _mixins.py
|   |   |   |   |   |   |   +-- _ranges.py
|   |   |   |   |   |   |   +-- _utils.py
|   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   +-- boolean.py
|   |   |   |   |   |   |   +-- categorical.py
|   |   |   |   |   |   |   +-- datetimelike.py
|   |   |   |   |   |   |   +-- datetimes.py
|   |   |   |   |   |   |   +-- floating.py
|   |   |   |   |   |   |   +-- integer.py
|   |   |   |   |   |   |   +-- interval.py
|   |   |   |   |   |   |   +-- masked.py
|   |   |   |   |   |   |   +-- numeric.py
|   |   |   |   |   |   |   +-- numpy_.py
|   |   |   |   |   |   |   +-- period.py
|   |   |   |   |   |   |   +-- string_.py
|   |   |   |   |   |   |   +-- string_arrow.py
|   |   |   |   |   |   |   +-- timedeltas.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _arrow_string_mixins.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _mixins.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _ranges.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _utils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- boolean.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- categorical.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- datetimelike.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- datetimes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- floating.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- integer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- interval.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- masked.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- numeric.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- numpy_.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- period.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- string_.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- string_arrow.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- timedeltas.cpython-311.pyc
|   |   |   |   |   |   |   +-- arrow/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- _arrow_utils.py
|   |   |   |   |   |   |   |   +-- accessors.py
|   |   |   |   |   |   |   |   +-- array.py
|   |   |   |   |   |   |   |   +-- extension_types.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- _arrow_utils.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- accessors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- array.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- extension_types.cpython-311.pyc
|   |   |   |   |   |   |   +-- sparse/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- accessor.py
|   |   |   |   |   |   |   |   +-- array.py
|   |   |   |   |   |   |   |   +-- scipy_sparse.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- accessor.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- array.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- scipy_sparse.cpython-311.pyc
|   |   |   |   |   |   +-- computation/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- align.py
|   |   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   |   +-- check.py
|   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   +-- engines.py
|   |   |   |   |   |   |   +-- eval.py
|   |   |   |   |   |   |   +-- expr.py
|   |   |   |   |   |   |   +-- expressions.py
|   |   |   |   |   |   |   +-- ops.py
|   |   |   |   |   |   |   +-- parsing.py
|   |   |   |   |   |   |   +-- pytables.py
|   |   |   |   |   |   |   +-- scope.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- align.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- check.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- engines.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- eval.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- expr.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- expressions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- ops.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- parsing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pytables.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- scope.cpython-311.pyc
|   |   |   |   |   |   +-- dtypes/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   |   +-- astype.py
|   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   +-- cast.py
|   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   +-- concat.py
|   |   |   |   |   |   |   +-- dtypes.py
|   |   |   |   |   |   |   +-- generic.py
|   |   |   |   |   |   |   +-- inference.py
|   |   |   |   |   |   |   +-- missing.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- astype.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- cast.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- concat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- dtypes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- generic.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- inference.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- missing.cpython-311.pyc
|   |   |   |   |   |   +-- groupby/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   +-- categorical.py
|   |   |   |   |   |   |   +-- generic.py
|   |   |   |   |   |   |   +-- groupby.py
|   |   |   |   |   |   |   +-- grouper.py
|   |   |   |   |   |   |   +-- indexing.py
|   |   |   |   |   |   |   +-- numba_.py
|   |   |   |   |   |   |   +-- ops.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- categorical.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- generic.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- groupby.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- grouper.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- numba_.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- ops.cpython-311.pyc
|   |   |   |   |   |   +-- indexers/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- objects.py
|   |   |   |   |   |   |   +-- utils.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- objects.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   +-- indexes/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- accessors.py
|   |   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   +-- category.py
|   |   |   |   |   |   |   +-- datetimelike.py
|   |   |   |   |   |   |   +-- datetimes.py
|   |   |   |   |   |   |   +-- extension.py
|   |   |   |   |   |   |   +-- frozen.py
|   |   |   |   |   |   |   +-- interval.py
|   |   |   |   |   |   |   +-- multi.py
|   |   |   |   |   |   |   +-- period.py
|   |   |   |   |   |   |   +-- range.py
|   |   |   |   |   |   |   +-- timedeltas.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- accessors.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- category.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- datetimelike.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- datetimes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- extension.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- frozen.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- interval.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- multi.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- period.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- range.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- timedeltas.cpython-311.pyc
|   |   |   |   |   |   +-- interchange/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- buffer.py
|   |   |   |   |   |   |   +-- column.py
|   |   |   |   |   |   |   +-- dataframe.py
|   |   |   |   |   |   |   +-- dataframe_protocol.py
|   |   |   |   |   |   |   +-- from_dataframe.py
|   |   |   |   |   |   |   +-- utils.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- buffer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- column.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- dataframe.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- dataframe_protocol.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- from_dataframe.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   +-- internals/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   |   +-- array_manager.py
|   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   +-- blocks.py
|   |   |   |   |   |   |   +-- concat.py
|   |   |   |   |   |   |   +-- construction.py
|   |   |   |   |   |   |   +-- managers.py
|   |   |   |   |   |   |   +-- ops.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- array_manager.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- blocks.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- concat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- construction.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- managers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- ops.cpython-311.pyc
|   |   |   |   |   |   +-- methods/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- describe.py
|   |   |   |   |   |   |   +-- selectn.py
|   |   |   |   |   |   |   +-- to_dict.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- describe.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- selectn.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- to_dict.cpython-311.pyc
|   |   |   |   |   |   +-- ops/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- array_ops.py
|   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   +-- dispatch.py
|   |   |   |   |   |   |   +-- docstrings.py
|   |   |   |   |   |   |   +-- invalid.py
|   |   |   |   |   |   |   +-- mask_ops.py
|   |   |   |   |   |   |   +-- missing.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- array_ops.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- dispatch.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- docstrings.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- invalid.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- mask_ops.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- missing.cpython-311.pyc
|   |   |   |   |   |   +-- reshape/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   |   +-- concat.py
|   |   |   |   |   |   |   +-- encoding.py
|   |   |   |   |   |   |   +-- melt.py
|   |   |   |   |   |   |   +-- merge.py
|   |   |   |   |   |   |   +-- pivot.py
|   |   |   |   |   |   |   +-- reshape.py
|   |   |   |   |   |   |   +-- tile.py
|   |   |   |   |   |   |   +-- util.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- concat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- encoding.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- melt.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- merge.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pivot.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- reshape.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- tile.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- util.cpython-311.pyc
|   |   |   |   |   |   +-- sparse/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   +-- strings/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- accessor.py
|   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   +-- object_array.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- accessor.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- object_array.cpython-311.pyc
|   |   |   |   |   |   +-- tools/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- datetimes.py
|   |   |   |   |   |   |   +-- numeric.py
|   |   |   |   |   |   |   +-- timedeltas.py
|   |   |   |   |   |   |   +-- times.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- datetimes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- numeric.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- timedeltas.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- times.cpython-311.pyc
|   |   |   |   |   |   +-- util/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- hashing.py
|   |   |   |   |   |   |   +-- numba_.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hashing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- numba_.cpython-311.pyc
|   |   |   |   |   |   +-- window/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   +-- doc.py
|   |   |   |   |   |   |   +-- ewm.py
|   |   |   |   |   |   |   +-- expanding.py
|   |   |   |   |   |   |   +-- numba_.py
|   |   |   |   |   |   |   +-- online.py
|   |   |   |   |   |   |   +-- rolling.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- doc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- ewm.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- expanding.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- numba_.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- online.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- rolling.cpython-311.pyc
|   |   |   |   |   +-- errors/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- io/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _util.py
|   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   +-- clipboards.py
|   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   +-- feather_format.py
|   |   |   |   |   |   +-- gbq.py
|   |   |   |   |   |   +-- html.py
|   |   |   |   |   |   +-- orc.py
|   |   |   |   |   |   +-- parquet.py
|   |   |   |   |   |   +-- pickle.py
|   |   |   |   |   |   +-- pytables.py
|   |   |   |   |   |   +-- spss.py
|   |   |   |   |   |   +-- sql.py
|   |   |   |   |   |   +-- stata.py
|   |   |   |   |   |   +-- xml.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _util.cpython-311.pyc
|   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   |   +-- clipboards.cpython-311.pyc
|   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   +-- feather_format.cpython-311.pyc
|   |   |   |   |   |   |   +-- gbq.cpython-311.pyc
|   |   |   |   |   |   |   +-- html.cpython-311.pyc
|   |   |   |   |   |   |   +-- orc.cpython-311.pyc
|   |   |   |   |   |   |   +-- parquet.cpython-311.pyc
|   |   |   |   |   |   |   +-- pickle.cpython-311.pyc
|   |   |   |   |   |   |   +-- pytables.cpython-311.pyc
|   |   |   |   |   |   |   +-- spss.cpython-311.pyc
|   |   |   |   |   |   |   +-- sql.cpython-311.pyc
|   |   |   |   |   |   |   +-- stata.cpython-311.pyc
|   |   |   |   |   |   |   +-- xml.cpython-311.pyc
|   |   |   |   |   |   +-- clipboard/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- excel/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _base.py
|   |   |   |   |   |   |   +-- _calamine.py
|   |   |   |   |   |   |   +-- _odfreader.py
|   |   |   |   |   |   |   +-- _odswriter.py
|   |   |   |   |   |   |   +-- _openpyxl.py
|   |   |   |   |   |   |   +-- _pyxlsb.py
|   |   |   |   |   |   |   +-- _util.py
|   |   |   |   |   |   |   +-- _xlrd.py
|   |   |   |   |   |   |   +-- _xlsxwriter.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _calamine.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _odfreader.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _odswriter.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _openpyxl.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _pyxlsb.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _util.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _xlrd.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _xlsxwriter.cpython-311.pyc
|   |   |   |   |   |   +-- formats/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _color_data.py
|   |   |   |   |   |   |   +-- console.py
|   |   |   |   |   |   |   +-- css.py
|   |   |   |   |   |   |   +-- csvs.py
|   |   |   |   |   |   |   +-- excel.py
|   |   |   |   |   |   |   +-- format.py
|   |   |   |   |   |   |   +-- html.py
|   |   |   |   |   |   |   +-- info.py
|   |   |   |   |   |   |   +-- printing.py
|   |   |   |   |   |   |   +-- string.py
|   |   |   |   |   |   |   +-- style.py
|   |   |   |   |   |   |   +-- style_render.py
|   |   |   |   |   |   |   +-- xml.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _color_data.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- console.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- css.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- csvs.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- excel.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- format.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- html.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- info.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- printing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- string.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- style.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- style_render.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- xml.cpython-311.pyc
|   |   |   |   |   |   |   +-- templates/
|   |   |   |   |   |   |   |   +-- html.tpl
|   |   |   |   |   |   |   |   +-- html_style.tpl
|   |   |   |   |   |   |   |   +-- html_table.tpl
|   |   |   |   |   |   |   |   +-- latex.tpl
|   |   |   |   |   |   |   |   +-- latex_longtable.tpl
|   |   |   |   |   |   |   |   +-- latex_table.tpl
|   |   |   |   |   |   |   |   +-- string.tpl
|   |   |   |   |   |   +-- json/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _json.py
|   |   |   |   |   |   |   +-- _normalize.py
|   |   |   |   |   |   |   +-- _table_schema.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _json.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _normalize.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _table_schema.cpython-311.pyc
|   |   |   |   |   |   +-- parsers/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- arrow_parser_wrapper.py
|   |   |   |   |   |   |   +-- base_parser.py
|   |   |   |   |   |   |   +-- c_parser_wrapper.py
|   |   |   |   |   |   |   +-- python_parser.py
|   |   |   |   |   |   |   +-- readers.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- arrow_parser_wrapper.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- base_parser.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- c_parser_wrapper.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- python_parser.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- readers.cpython-311.pyc
|   |   |   |   |   |   +-- sas/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- sas_constants.py
|   |   |   |   |   |   |   +-- sas_xport.py
|   |   |   |   |   |   |   +-- sas7bdat.py
|   |   |   |   |   |   |   +-- sasreader.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- sas_constants.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- sas_xport.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- sas7bdat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- sasreader.cpython-311.pyc
|   |   |   |   |   +-- plotting/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _core.py
|   |   |   |   |   |   +-- _misc.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _core.cpython-311.pyc
|   |   |   |   |   |   |   +-- _misc.cpython-311.pyc
|   |   |   |   |   |   +-- _matplotlib/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- boxplot.py
|   |   |   |   |   |   |   +-- converter.py
|   |   |   |   |   |   |   +-- core.py
|   |   |   |   |   |   |   +-- groupby.py
|   |   |   |   |   |   |   +-- hist.py
|   |   |   |   |   |   |   +-- misc.py
|   |   |   |   |   |   |   +-- style.py
|   |   |   |   |   |   |   +-- timeseries.py
|   |   |   |   |   |   |   +-- tools.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- boxplot.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- converter.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- core.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- groupby.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hist.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- misc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- style.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- timeseries.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- tools.cpython-311.pyc
|   |   |   |   |   +-- tests/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- test_aggregation.py
|   |   |   |   |   |   +-- test_algos.py
|   |   |   |   |   |   +-- test_common.py
|   |   |   |   |   |   +-- test_downstream.py
|   |   |   |   |   |   +-- test_errors.py
|   |   |   |   |   |   +-- test_expressions.py
|   |   |   |   |   |   +-- test_flags.py
|   |   |   |   |   |   +-- test_multilevel.py
|   |   |   |   |   |   +-- test_nanops.py
|   |   |   |   |   |   +-- test_optional_dependency.py
|   |   |   |   |   |   +-- test_register_accessor.py
|   |   |   |   |   |   +-- test_sorting.py
|   |   |   |   |   |   +-- test_take.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_aggregation.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_algos.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_common.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_downstream.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_errors.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_expressions.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_flags.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_multilevel.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_nanops.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_optional_dependency.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_register_accessor.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_sorting.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_take.cpython-311.pyc
|   |   |   |   |   |   +-- api/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_api.py
|   |   |   |   |   |   |   +-- test_types.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_types.cpython-311.pyc
|   |   |   |   |   |   +-- apply/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   +-- test_frame_apply.py
|   |   |   |   |   |   |   +-- test_frame_apply_relabeling.py
|   |   |   |   |   |   |   +-- test_frame_transform.py
|   |   |   |   |   |   |   +-- test_invalid_arg.py
|   |   |   |   |   |   |   +-- test_numba.py
|   |   |   |   |   |   |   +-- test_series_apply.py
|   |   |   |   |   |   |   +-- test_series_apply_relabeling.py
|   |   |   |   |   |   |   +-- test_series_transform.py
|   |   |   |   |   |   |   +-- test_str.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_frame_apply.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_frame_apply_relabeling.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_frame_transform.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_invalid_arg.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_numba.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_series_apply.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_series_apply_relabeling.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_series_transform.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_str.cpython-311.pyc
|   |   |   |   |   |   +-- arithmetic/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   +-- test_array_ops.py
|   |   |   |   |   |   |   +-- test_categorical.py
|   |   |   |   |   |   |   +-- test_datetime64.py
|   |   |   |   |   |   |   +-- test_interval.py
|   |   |   |   |   |   |   +-- test_numeric.py
|   |   |   |   |   |   |   +-- test_object.py
|   |   |   |   |   |   |   +-- test_period.py
|   |   |   |   |   |   |   +-- test_timedelta64.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_array_ops.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_categorical.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_datetime64.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_interval.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_numeric.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_object.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_period.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_timedelta64.cpython-311.pyc
|   |   |   |   |   |   +-- arrays/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- masked_shared.py
|   |   |   |   |   |   |   +-- test_array.py
|   |   |   |   |   |   |   +-- test_datetimelike.py
|   |   |   |   |   |   |   +-- test_datetimes.py
|   |   |   |   |   |   |   +-- test_ndarray_backed.py
|   |   |   |   |   |   |   +-- test_period.py
|   |   |   |   |   |   |   +-- test_timedeltas.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- masked_shared.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_array.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_datetimelike.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_datetimes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_ndarray_backed.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_period.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_timedeltas.cpython-311.pyc
|   |   |   |   |   |   |   +-- boolean/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_arithmetic.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_comparison.py
|   |   |   |   |   |   |   |   +-- test_construction.py
|   |   |   |   |   |   |   |   +-- test_function.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_logical.py
|   |   |   |   |   |   |   |   +-- test_ops.py
|   |   |   |   |   |   |   |   +-- test_reduction.py
|   |   |   |   |   |   |   |   +-- test_repr.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_comparison.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_construction.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_function.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_logical.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_ops.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reduction.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_repr.cpython-311.pyc
|   |   |   |   |   |   |   +-- categorical/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_algos.py
|   |   |   |   |   |   |   |   +-- test_analytics.py
|   |   |   |   |   |   |   |   +-- test_api.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_dtypes.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_map.py
|   |   |   |   |   |   |   |   +-- test_missing.py
|   |   |   |   |   |   |   |   +-- test_operators.py
|   |   |   |   |   |   |   |   +-- test_replace.py
|   |   |   |   |   |   |   |   +-- test_repr.py
|   |   |   |   |   |   |   |   +-- test_sorting.py
|   |   |   |   |   |   |   |   +-- test_subclass.py
|   |   |   |   |   |   |   |   +-- test_take.py
|   |   |   |   |   |   |   |   +-- test_warnings.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_algos.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_analytics.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_api.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dtypes.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_map.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_missing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_operators.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_replace.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_repr.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sorting.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_subclass.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_take.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_warnings.cpython-311.pyc
|   |   |   |   |   |   |   +-- datetimes/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_cumulative.py
|   |   |   |   |   |   |   |   +-- test_reductions.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_cumulative.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reductions.cpython-311.pyc
|   |   |   |   |   |   |   +-- floating/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   |   +-- test_arithmetic.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_comparison.py
|   |   |   |   |   |   |   |   +-- test_concat.py
|   |   |   |   |   |   |   |   +-- test_construction.py
|   |   |   |   |   |   |   |   +-- test_contains.py
|   |   |   |   |   |   |   |   +-- test_function.py
|   |   |   |   |   |   |   |   +-- test_repr.py
|   |   |   |   |   |   |   |   +-- test_to_numpy.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_comparison.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_concat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_construction.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_contains.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_function.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_repr.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_numpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- integer/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   |   +-- test_arithmetic.py
|   |   |   |   |   |   |   |   +-- test_comparison.py
|   |   |   |   |   |   |   |   +-- test_concat.py
|   |   |   |   |   |   |   |   +-- test_construction.py
|   |   |   |   |   |   |   |   +-- test_dtypes.py
|   |   |   |   |   |   |   |   +-- test_function.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_reduction.py
|   |   |   |   |   |   |   |   +-- test_repr.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_comparison.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_concat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_construction.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dtypes.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_function.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reduction.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_repr.cpython-311.pyc
|   |   |   |   |   |   |   +-- interval/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_formats.py
|   |   |   |   |   |   |   |   +-- test_interval.py
|   |   |   |   |   |   |   |   +-- test_interval_pyarrow.py
|   |   |   |   |   |   |   |   +-- test_overlaps.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_formats.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_interval.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_interval_pyarrow.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_overlaps.cpython-311.pyc
|   |   |   |   |   |   |   +-- masked/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_arithmetic.py
|   |   |   |   |   |   |   |   +-- test_arrow_compat.py
|   |   |   |   |   |   |   |   +-- test_function.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arrow_compat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_function.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   +-- numpy_/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_numpy.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_numpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- period/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_arrow_compat.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_reductions.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arrow_compat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reductions.cpython-311.pyc
|   |   |   |   |   |   |   +-- sparse/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_accessor.py
|   |   |   |   |   |   |   |   +-- test_arithmetics.py
|   |   |   |   |   |   |   |   +-- test_array.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_combine_concat.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_dtype.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_libsparse.py
|   |   |   |   |   |   |   |   +-- test_reductions.py
|   |   |   |   |   |   |   |   +-- test_unary.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_accessor.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arithmetics.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_array.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_combine_concat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dtype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_libsparse.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reductions.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_unary.cpython-311.pyc
|   |   |   |   |   |   |   +-- string_/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_concat.py
|   |   |   |   |   |   |   |   +-- test_string.py
|   |   |   |   |   |   |   |   +-- test_string_arrow.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_concat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_string.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_string_arrow.cpython-311.pyc
|   |   |   |   |   |   |   +-- timedeltas/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_cumulative.py
|   |   |   |   |   |   |   |   +-- test_reductions.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_cumulative.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reductions.cpython-311.pyc
|   |   |   |   |   |   +-- base/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   +-- test_conversion.py
|   |   |   |   |   |   |   +-- test_fillna.py
|   |   |   |   |   |   |   +-- test_misc.py
|   |   |   |   |   |   |   +-- test_transpose.py
|   |   |   |   |   |   |   +-- test_unique.py
|   |   |   |   |   |   |   +-- test_value_counts.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_conversion.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_fillna.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_misc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_transpose.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_unique.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_value_counts.cpython-311.pyc
|   |   |   |   |   |   +-- computation/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_compat.py
|   |   |   |   |   |   |   +-- test_eval.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_compat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_eval.cpython-311.pyc
|   |   |   |   |   |   +-- config/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_config.py
|   |   |   |   |   |   |   +-- test_localization.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_config.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_localization.cpython-311.pyc
|   |   |   |   |   |   +-- construction/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_extract_array.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_extract_array.cpython-311.pyc
|   |   |   |   |   |   +-- copy_view/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_array.py
|   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   +-- test_chained_assignment_deprecation.py
|   |   |   |   |   |   |   +-- test_clip.py
|   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   +-- test_core_functionalities.py
|   |   |   |   |   |   |   +-- test_functions.py
|   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   +-- test_internals.py
|   |   |   |   |   |   |   +-- test_interp_fillna.py
|   |   |   |   |   |   |   +-- test_methods.py
|   |   |   |   |   |   |   +-- test_replace.py
|   |   |   |   |   |   |   +-- test_setitem.py
|   |   |   |   |   |   |   +-- test_util.py
|   |   |   |   |   |   |   +-- util.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_array.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_chained_assignment_deprecation.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_clip.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_core_functionalities.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_functions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_internals.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_interp_fillna.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_methods.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_replace.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_setitem.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_util.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- util.cpython-311.pyc
|   |   |   |   |   |   |   +-- index/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_datetimeindex.py
|   |   |   |   |   |   |   |   +-- test_index.py
|   |   |   |   |   |   |   |   +-- test_periodindex.py
|   |   |   |   |   |   |   |   +-- test_timedeltaindex.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_datetimeindex.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_index.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_periodindex.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_timedeltaindex.cpython-311.pyc
|   |   |   |   |   |   +-- dtypes/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_common.py
|   |   |   |   |   |   |   +-- test_concat.py
|   |   |   |   |   |   |   +-- test_dtypes.py
|   |   |   |   |   |   |   +-- test_generic.py
|   |   |   |   |   |   |   +-- test_inference.py
|   |   |   |   |   |   |   +-- test_missing.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_concat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_dtypes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_generic.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_inference.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_missing.cpython-311.pyc
|   |   |   |   |   |   |   +-- cast/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_can_hold_element.py
|   |   |   |   |   |   |   |   +-- test_construct_from_scalar.py
|   |   |   |   |   |   |   |   +-- test_construct_ndarray.py
|   |   |   |   |   |   |   |   +-- test_construct_object_arr.py
|   |   |   |   |   |   |   |   +-- test_dict_compat.py
|   |   |   |   |   |   |   |   +-- test_downcast.py
|   |   |   |   |   |   |   |   +-- test_find_common_type.py
|   |   |   |   |   |   |   |   +-- test_infer_datetimelike.py
|   |   |   |   |   |   |   |   +-- test_infer_dtype.py
|   |   |   |   |   |   |   |   +-- test_maybe_box_native.py
|   |   |   |   |   |   |   |   +-- test_promote.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_can_hold_element.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_construct_from_scalar.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_construct_ndarray.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_construct_object_arr.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dict_compat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_downcast.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_find_common_type.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_infer_datetimelike.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_infer_dtype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_maybe_box_native.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_promote.cpython-311.pyc
|   |   |   |   |   |   +-- extension/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   +-- test_arrow.py
|   |   |   |   |   |   |   +-- test_categorical.py
|   |   |   |   |   |   |   +-- test_common.py
|   |   |   |   |   |   |   +-- test_datetime.py
|   |   |   |   |   |   |   +-- test_extension.py
|   |   |   |   |   |   |   +-- test_interval.py
|   |   |   |   |   |   |   +-- test_masked.py
|   |   |   |   |   |   |   +-- test_numpy.py
|   |   |   |   |   |   |   +-- test_period.py
|   |   |   |   |   |   |   +-- test_sparse.py
|   |   |   |   |   |   |   +-- test_string.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_arrow.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_categorical.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_datetime.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_extension.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_interval.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_masked.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_numpy.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_period.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_sparse.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_string.cpython-311.pyc
|   |   |   |   |   |   |   +-- array_with_attr/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- array.py
|   |   |   |   |   |   |   |   +-- test_array_with_attr.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- array.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_array_with_attr.cpython-311.pyc
|   |   |   |   |   |   |   +-- base/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- accumulate.py
|   |   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   |   +-- casting.py
|   |   |   |   |   |   |   |   +-- constructors.py
|   |   |   |   |   |   |   |   +-- dim2.py
|   |   |   |   |   |   |   |   +-- dtype.py
|   |   |   |   |   |   |   |   +-- getitem.py
|   |   |   |   |   |   |   |   +-- groupby.py
|   |   |   |   |   |   |   |   +-- index.py
|   |   |   |   |   |   |   |   +-- interface.py
|   |   |   |   |   |   |   |   +-- io.py
|   |   |   |   |   |   |   |   +-- methods.py
|   |   |   |   |   |   |   |   +-- missing.py
|   |   |   |   |   |   |   |   +-- ops.py
|   |   |   |   |   |   |   |   +-- printing.py
|   |   |   |   |   |   |   |   +-- reduce.py
|   |   |   |   |   |   |   |   +-- reshaping.py
|   |   |   |   |   |   |   |   +-- setitem.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- accumulate.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- casting.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- dim2.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- dtype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- getitem.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- groupby.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- index.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- interface.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- io.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- methods.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- missing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- ops.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- printing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- reduce.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- reshaping.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- setitem.cpython-311.pyc
|   |   |   |   |   |   |   +-- date/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- array.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- array.cpython-311.pyc
|   |   |   |   |   |   |   +-- decimal/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- array.py
|   |   |   |   |   |   |   |   +-- test_decimal.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- array.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_decimal.cpython-311.pyc
|   |   |   |   |   |   |   +-- json/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- array.py
|   |   |   |   |   |   |   |   +-- test_json.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- array.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_json.cpython-311.pyc
|   |   |   |   |   |   |   +-- list/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- array.py
|   |   |   |   |   |   |   |   +-- test_list.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- array.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_list.cpython-311.pyc
|   |   |   |   |   |   +-- frame/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   +-- test_alter_axes.py
|   |   |   |   |   |   |   +-- test_api.py
|   |   |   |   |   |   |   +-- test_arithmetic.py
|   |   |   |   |   |   |   +-- test_arrow_interface.py
|   |   |   |   |   |   |   +-- test_block_internals.py
|   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   +-- test_cumulative.py
|   |   |   |   |   |   |   +-- test_iteration.py
|   |   |   |   |   |   |   +-- test_logical_ops.py
|   |   |   |   |   |   |   +-- test_nonunique_indexes.py
|   |   |   |   |   |   |   +-- test_npfuncs.py
|   |   |   |   |   |   |   +-- test_query_eval.py
|   |   |   |   |   |   |   +-- test_reductions.py
|   |   |   |   |   |   |   +-- test_repr.py
|   |   |   |   |   |   |   +-- test_stack_unstack.py
|   |   |   |   |   |   |   +-- test_subclass.py
|   |   |   |   |   |   |   +-- test_ufunc.py
|   |   |   |   |   |   |   +-- test_unary.py
|   |   |   |   |   |   |   +-- test_validate.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_alter_axes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_arrow_interface.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_block_internals.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_cumulative.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_iteration.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_logical_ops.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_nonunique_indexes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_npfuncs.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_query_eval.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_reductions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_repr.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_stack_unstack.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_subclass.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_ufunc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_unary.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_validate.cpython-311.pyc
|   |   |   |   |   |   |   +-- constructors/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_from_dict.py
|   |   |   |   |   |   |   |   +-- test_from_records.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_from_dict.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_from_records.cpython-311.pyc
|   |   |   |   |   |   |   +-- indexing/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_coercion.py
|   |   |   |   |   |   |   |   +-- test_delitem.py
|   |   |   |   |   |   |   |   +-- test_get.py
|   |   |   |   |   |   |   |   +-- test_get_value.py
|   |   |   |   |   |   |   |   +-- test_getitem.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_insert.py
|   |   |   |   |   |   |   |   +-- test_mask.py
|   |   |   |   |   |   |   |   +-- test_set_value.py
|   |   |   |   |   |   |   |   +-- test_setitem.py
|   |   |   |   |   |   |   |   +-- test_take.py
|   |   |   |   |   |   |   |   +-- test_where.py
|   |   |   |   |   |   |   |   +-- test_xs.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_coercion.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_delitem.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_get.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_get_value.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_getitem.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_insert.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_mask.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_set_value.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_setitem.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_take.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_where.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_xs.cpython-311.pyc
|   |   |   |   |   |   |   +-- methods/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_add_prefix_suffix.py
|   |   |   |   |   |   |   |   +-- test_align.py
|   |   |   |   |   |   |   |   +-- test_asfreq.py
|   |   |   |   |   |   |   |   +-- test_asof.py
|   |   |   |   |   |   |   |   +-- test_assign.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_at_time.py
|   |   |   |   |   |   |   |   +-- test_between_time.py
|   |   |   |   |   |   |   |   +-- test_clip.py
|   |   |   |   |   |   |   |   +-- test_combine.py
|   |   |   |   |   |   |   |   +-- test_combine_first.py
|   |   |   |   |   |   |   |   +-- test_compare.py
|   |   |   |   |   |   |   |   +-- test_convert_dtypes.py
|   |   |   |   |   |   |   |   +-- test_copy.py
|   |   |   |   |   |   |   |   +-- test_count.py
|   |   |   |   |   |   |   |   +-- test_cov_corr.py
|   |   |   |   |   |   |   |   +-- test_describe.py
|   |   |   |   |   |   |   |   +-- test_diff.py
|   |   |   |   |   |   |   |   +-- test_dot.py
|   |   |   |   |   |   |   |   +-- test_drop.py
|   |   |   |   |   |   |   |   +-- test_drop_duplicates.py
|   |   |   |   |   |   |   |   +-- test_droplevel.py
|   |   |   |   |   |   |   |   +-- test_dropna.py
|   |   |   |   |   |   |   |   +-- test_dtypes.py
|   |   |   |   |   |   |   |   +-- test_duplicated.py
|   |   |   |   |   |   |   |   +-- test_equals.py
|   |   |   |   |   |   |   |   +-- test_explode.py
|   |   |   |   |   |   |   |   +-- test_fillna.py
|   |   |   |   |   |   |   |   +-- test_filter.py
|   |   |   |   |   |   |   |   +-- test_first_and_last.py
|   |   |   |   |   |   |   |   +-- test_first_valid_index.py
|   |   |   |   |   |   |   |   +-- test_get_numeric_data.py
|   |   |   |   |   |   |   |   +-- test_head_tail.py
|   |   |   |   |   |   |   |   +-- test_infer_objects.py
|   |   |   |   |   |   |   |   +-- test_info.py
|   |   |   |   |   |   |   |   +-- test_interpolate.py
|   |   |   |   |   |   |   |   +-- test_is_homogeneous_dtype.py
|   |   |   |   |   |   |   |   +-- test_isetitem.py
|   |   |   |   |   |   |   |   +-- test_isin.py
|   |   |   |   |   |   |   |   +-- test_iterrows.py
|   |   |   |   |   |   |   |   +-- test_join.py
|   |   |   |   |   |   |   |   +-- test_map.py
|   |   |   |   |   |   |   |   +-- test_matmul.py
|   |   |   |   |   |   |   |   +-- test_nlargest.py
|   |   |   |   |   |   |   |   +-- test_pct_change.py
|   |   |   |   |   |   |   |   +-- test_pipe.py
|   |   |   |   |   |   |   |   +-- test_pop.py
|   |   |   |   |   |   |   |   +-- test_quantile.py
|   |   |   |   |   |   |   |   +-- test_rank.py
|   |   |   |   |   |   |   |   +-- test_reindex.py
|   |   |   |   |   |   |   |   +-- test_reindex_like.py
|   |   |   |   |   |   |   |   +-- test_rename.py
|   |   |   |   |   |   |   |   +-- test_rename_axis.py
|   |   |   |   |   |   |   |   +-- test_reorder_levels.py
|   |   |   |   |   |   |   |   +-- test_replace.py
|   |   |   |   |   |   |   |   +-- test_reset_index.py
|   |   |   |   |   |   |   |   +-- test_round.py
|   |   |   |   |   |   |   |   +-- test_sample.py
|   |   |   |   |   |   |   |   +-- test_select_dtypes.py
|   |   |   |   |   |   |   |   +-- test_set_axis.py
|   |   |   |   |   |   |   |   +-- test_set_index.py
|   |   |   |   |   |   |   |   +-- test_shift.py
|   |   |   |   |   |   |   |   +-- test_size.py
|   |   |   |   |   |   |   |   +-- test_sort_index.py
|   |   |   |   |   |   |   |   +-- test_sort_values.py
|   |   |   |   |   |   |   |   +-- test_swapaxes.py
|   |   |   |   |   |   |   |   +-- test_swaplevel.py
|   |   |   |   |   |   |   |   +-- test_to_csv.py
|   |   |   |   |   |   |   |   +-- test_to_dict.py
|   |   |   |   |   |   |   |   +-- test_to_dict_of_blocks.py
|   |   |   |   |   |   |   |   +-- test_to_numpy.py
|   |   |   |   |   |   |   |   +-- test_to_period.py
|   |   |   |   |   |   |   |   +-- test_to_records.py
|   |   |   |   |   |   |   |   +-- test_to_timestamp.py
|   |   |   |   |   |   |   |   +-- test_transpose.py
|   |   |   |   |   |   |   |   +-- test_truncate.py
|   |   |   |   |   |   |   |   +-- test_tz_convert.py
|   |   |   |   |   |   |   |   +-- test_tz_localize.py
|   |   |   |   |   |   |   |   +-- test_update.py
|   |   |   |   |   |   |   |   +-- test_value_counts.py
|   |   |   |   |   |   |   |   +-- test_values.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_add_prefix_suffix.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_align.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_asfreq.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_asof.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_assign.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_at_time.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_between_time.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_clip.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_combine.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_combine_first.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_compare.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_convert_dtypes.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_copy.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_count.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_cov_corr.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_describe.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_diff.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dot.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_drop.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_drop_duplicates.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_droplevel.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dropna.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dtypes.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_duplicated.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_equals.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_explode.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_fillna.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_filter.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_first_and_last.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_first_valid_index.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_get_numeric_data.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_head_tail.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_infer_objects.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_info.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_interpolate.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_is_homogeneous_dtype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_isetitem.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_isin.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_iterrows.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_join.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_map.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_matmul.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_nlargest.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pct_change.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pipe.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pop.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_quantile.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_rank.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reindex.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reindex_like.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_rename.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_rename_axis.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reorder_levels.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_replace.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reset_index.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_round.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sample.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_select_dtypes.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_set_axis.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_set_index.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_shift.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_size.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sort_index.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sort_values.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_swapaxes.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_swaplevel.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_csv.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_dict.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_dict_of_blocks.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_numpy.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_period.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_records.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_timestamp.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_transpose.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_truncate.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_tz_convert.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_tz_localize.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_update.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_value_counts.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_values.cpython-311.pyc
|   |   |   |   |   |   +-- generic/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_duplicate_labels.py
|   |   |   |   |   |   |   +-- test_finalize.py
|   |   |   |   |   |   |   +-- test_frame.py
|   |   |   |   |   |   |   +-- test_generic.py
|   |   |   |   |   |   |   +-- test_label_or_level_utils.py
|   |   |   |   |   |   |   +-- test_series.py
|   |   |   |   |   |   |   +-- test_to_xarray.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_duplicate_labels.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_finalize.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_frame.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_generic.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_label_or_level_utils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_series.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_to_xarray.cpython-311.pyc
|   |   |   |   |   |   +-- groupby/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   +-- test_all_methods.py
|   |   |   |   |   |   |   +-- test_api.py
|   |   |   |   |   |   |   +-- test_apply.py
|   |   |   |   |   |   |   +-- test_apply_mutate.py
|   |   |   |   |   |   |   +-- test_bin_groupby.py
|   |   |   |   |   |   |   +-- test_categorical.py
|   |   |   |   |   |   |   +-- test_counting.py
|   |   |   |   |   |   |   +-- test_cumulative.py
|   |   |   |   |   |   |   +-- test_filters.py
|   |   |   |   |   |   |   +-- test_groupby.py
|   |   |   |   |   |   |   +-- test_groupby_dropna.py
|   |   |   |   |   |   |   +-- test_groupby_subclass.py
|   |   |   |   |   |   |   +-- test_grouping.py
|   |   |   |   |   |   |   +-- test_index_as_string.py
|   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   +-- test_libgroupby.py
|   |   |   |   |   |   |   +-- test_missing.py
|   |   |   |   |   |   |   +-- test_numba.py
|   |   |   |   |   |   |   +-- test_numeric_only.py
|   |   |   |   |   |   |   +-- test_pipe.py
|   |   |   |   |   |   |   +-- test_raises.py
|   |   |   |   |   |   |   +-- test_reductions.py
|   |   |   |   |   |   |   +-- test_timegrouper.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_all_methods.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_apply.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_apply_mutate.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_bin_groupby.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_categorical.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_counting.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_cumulative.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_filters.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_groupby.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_groupby_dropna.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_groupby_subclass.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_grouping.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_index_as_string.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_libgroupby.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_missing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_numba.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_numeric_only.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_pipe.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_raises.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_reductions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_timegrouper.cpython-311.pyc
|   |   |   |   |   |   |   +-- aggregate/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_aggregate.py
|   |   |   |   |   |   |   |   +-- test_cython.py
|   |   |   |   |   |   |   |   +-- test_numba.py
|   |   |   |   |   |   |   |   +-- test_other.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_aggregate.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_cython.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_numba.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_other.cpython-311.pyc
|   |   |   |   |   |   |   +-- methods/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_corrwith.py
|   |   |   |   |   |   |   |   +-- test_describe.py
|   |   |   |   |   |   |   |   +-- test_groupby_shift_diff.py
|   |   |   |   |   |   |   |   +-- test_is_monotonic.py
|   |   |   |   |   |   |   |   +-- test_nlargest_nsmallest.py
|   |   |   |   |   |   |   |   +-- test_nth.py
|   |   |   |   |   |   |   |   +-- test_quantile.py
|   |   |   |   |   |   |   |   +-- test_rank.py
|   |   |   |   |   |   |   |   +-- test_sample.py
|   |   |   |   |   |   |   |   +-- test_size.py
|   |   |   |   |   |   |   |   +-- test_skew.py
|   |   |   |   |   |   |   |   +-- test_value_counts.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_corrwith.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_describe.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_groupby_shift_diff.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_is_monotonic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_nlargest_nsmallest.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_nth.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_quantile.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_rank.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sample.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_size.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_skew.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_value_counts.cpython-311.pyc
|   |   |   |   |   |   |   +-- transform/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_numba.py
|   |   |   |   |   |   |   |   +-- test_transform.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_numba.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_transform.cpython-311.pyc
|   |   |   |   |   |   +-- indexes/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   +-- test_any_index.py
|   |   |   |   |   |   |   +-- test_base.py
|   |   |   |   |   |   |   +-- test_common.py
|   |   |   |   |   |   |   +-- test_datetimelike.py
|   |   |   |   |   |   |   +-- test_engines.py
|   |   |   |   |   |   |   +-- test_frozen.py
|   |   |   |   |   |   |   +-- test_index_new.py
|   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   +-- test_numpy_compat.py
|   |   |   |   |   |   |   +-- test_old_base.py
|   |   |   |   |   |   |   +-- test_setops.py
|   |   |   |   |   |   |   +-- test_subclass.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_any_index.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_datetimelike.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_engines.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_frozen.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_index_new.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_numpy_compat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_old_base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_setops.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_subclass.cpython-311.pyc
|   |   |   |   |   |   |   +-- base_class/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_formats.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_pickle.py
|   |   |   |   |   |   |   |   +-- test_reshape.py
|   |   |   |   |   |   |   |   +-- test_setops.py
|   |   |   |   |   |   |   |   +-- test_where.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_formats.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pickle.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reshape.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_setops.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_where.cpython-311.pyc
|   |   |   |   |   |   |   +-- categorical/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_append.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_category.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_equals.py
|   |   |   |   |   |   |   |   +-- test_fillna.py
|   |   |   |   |   |   |   |   +-- test_formats.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_map.py
|   |   |   |   |   |   |   |   +-- test_reindex.py
|   |   |   |   |   |   |   |   +-- test_setops.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_append.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_category.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_equals.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_fillna.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_formats.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_map.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reindex.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_setops.cpython-311.pyc
|   |   |   |   |   |   |   +-- datetimelike_/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_drop_duplicates.py
|   |   |   |   |   |   |   |   +-- test_equals.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_is_monotonic.py
|   |   |   |   |   |   |   |   +-- test_nat.py
|   |   |   |   |   |   |   |   +-- test_sort_values.py
|   |   |   |   |   |   |   |   +-- test_value_counts.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_drop_duplicates.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_equals.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_is_monotonic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_nat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sort_values.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_value_counts.cpython-311.pyc
|   |   |   |   |   |   |   +-- datetimes/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_arithmetic.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_date_range.py
|   |   |   |   |   |   |   |   +-- test_datetime.py
|   |   |   |   |   |   |   |   +-- test_formats.py
|   |   |   |   |   |   |   |   +-- test_freq_attr.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_iter.py
|   |   |   |   |   |   |   |   +-- test_join.py
|   |   |   |   |   |   |   |   +-- test_npfuncs.py
|   |   |   |   |   |   |   |   +-- test_ops.py
|   |   |   |   |   |   |   |   +-- test_partial_slicing.py
|   |   |   |   |   |   |   |   +-- test_pickle.py
|   |   |   |   |   |   |   |   +-- test_reindex.py
|   |   |   |   |   |   |   |   +-- test_scalar_compat.py
|   |   |   |   |   |   |   |   +-- test_setops.py
|   |   |   |   |   |   |   |   +-- test_timezones.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_date_range.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_datetime.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_formats.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_freq_attr.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_iter.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_join.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_npfuncs.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_ops.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_partial_slicing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pickle.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reindex.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_scalar_compat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_setops.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_timezones.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- methods/
|   |   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   |   +-- test_asof.py
|   |   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   |   +-- test_delete.py
|   |   |   |   |   |   |   |   |   +-- test_factorize.py
|   |   |   |   |   |   |   |   |   +-- test_fillna.py
|   |   |   |   |   |   |   |   |   +-- test_insert.py
|   |   |   |   |   |   |   |   |   +-- test_isocalendar.py
|   |   |   |   |   |   |   |   |   +-- test_map.py
|   |   |   |   |   |   |   |   |   +-- test_normalize.py
|   |   |   |   |   |   |   |   |   +-- test_repeat.py
|   |   |   |   |   |   |   |   |   +-- test_resolution.py
|   |   |   |   |   |   |   |   |   +-- test_round.py
|   |   |   |   |   |   |   |   |   +-- test_shift.py
|   |   |   |   |   |   |   |   |   +-- test_snap.py
|   |   |   |   |   |   |   |   |   +-- test_to_frame.py
|   |   |   |   |   |   |   |   |   +-- test_to_julian_date.py
|   |   |   |   |   |   |   |   |   +-- test_to_period.py
|   |   |   |   |   |   |   |   |   +-- test_to_pydatetime.py
|   |   |   |   |   |   |   |   |   +-- test_to_series.py
|   |   |   |   |   |   |   |   |   +-- test_tz_convert.py
|   |   |   |   |   |   |   |   |   +-- test_tz_localize.py
|   |   |   |   |   |   |   |   |   +-- test_unique.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_asof.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_delete.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_factorize.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_fillna.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_insert.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_isocalendar.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_map.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_normalize.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_repeat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_resolution.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_round.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_shift.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_snap.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_to_frame.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_to_julian_date.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_to_period.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_to_pydatetime.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_to_series.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_tz_convert.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_tz_localize.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_unique.cpython-311.pyc
|   |   |   |   |   |   |   +-- interval/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_equals.py
|   |   |   |   |   |   |   |   +-- test_formats.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_interval.py
|   |   |   |   |   |   |   |   +-- test_interval_range.py
|   |   |   |   |   |   |   |   +-- test_interval_tree.py
|   |   |   |   |   |   |   |   +-- test_join.py
|   |   |   |   |   |   |   |   +-- test_pickle.py
|   |   |   |   |   |   |   |   +-- test_setops.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_equals.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_formats.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_interval.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_interval_range.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_interval_tree.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_join.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pickle.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_setops.cpython-311.pyc
|   |   |   |   |   |   |   +-- multi/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   |   +-- test_analytics.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_compat.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_conversion.py
|   |   |   |   |   |   |   |   +-- test_copy.py
|   |   |   |   |   |   |   |   +-- test_drop.py
|   |   |   |   |   |   |   |   +-- test_duplicates.py
|   |   |   |   |   |   |   |   +-- test_equivalence.py
|   |   |   |   |   |   |   |   +-- test_formats.py
|   |   |   |   |   |   |   |   +-- test_get_level_values.py
|   |   |   |   |   |   |   |   +-- test_get_set.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_integrity.py
|   |   |   |   |   |   |   |   +-- test_isin.py
|   |   |   |   |   |   |   |   +-- test_join.py
|   |   |   |   |   |   |   |   +-- test_lexsort.py
|   |   |   |   |   |   |   |   +-- test_missing.py
|   |   |   |   |   |   |   |   +-- test_monotonic.py
|   |   |   |   |   |   |   |   +-- test_names.py
|   |   |   |   |   |   |   |   +-- test_partial_indexing.py
|   |   |   |   |   |   |   |   +-- test_pickle.py
|   |   |   |   |   |   |   |   +-- test_reindex.py
|   |   |   |   |   |   |   |   +-- test_reshape.py
|   |   |   |   |   |   |   |   +-- test_setops.py
|   |   |   |   |   |   |   |   +-- test_sorting.py
|   |   |   |   |   |   |   |   +-- test_take.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_analytics.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_compat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_conversion.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_copy.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_drop.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_duplicates.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_equivalence.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_formats.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_get_level_values.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_get_set.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_integrity.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_isin.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_join.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_lexsort.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_missing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_monotonic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_names.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_partial_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pickle.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reindex.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reshape.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_setops.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sorting.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_take.cpython-311.pyc
|   |   |   |   |   |   |   +-- numeric/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_join.py
|   |   |   |   |   |   |   |   +-- test_numeric.py
|   |   |   |   |   |   |   |   +-- test_setops.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_join.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_numeric.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_setops.cpython-311.pyc
|   |   |   |   |   |   |   +-- object/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   +-- period/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_formats.py
|   |   |   |   |   |   |   |   +-- test_freq_attr.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_join.py
|   |   |   |   |   |   |   |   +-- test_monotonic.py
|   |   |   |   |   |   |   |   +-- test_partial_slicing.py
|   |   |   |   |   |   |   |   +-- test_period.py
|   |   |   |   |   |   |   |   +-- test_period_range.py
|   |   |   |   |   |   |   |   +-- test_pickle.py
|   |   |   |   |   |   |   |   +-- test_resolution.py
|   |   |   |   |   |   |   |   +-- test_scalar_compat.py
|   |   |   |   |   |   |   |   +-- test_searchsorted.py
|   |   |   |   |   |   |   |   +-- test_setops.py
|   |   |   |   |   |   |   |   +-- test_tools.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_formats.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_freq_attr.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_join.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_monotonic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_partial_slicing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_period.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_period_range.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pickle.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_resolution.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_scalar_compat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_searchsorted.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_setops.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_tools.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- methods/
|   |   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   |   +-- test_asfreq.py
|   |   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   |   +-- test_factorize.py
|   |   |   |   |   |   |   |   |   +-- test_fillna.py
|   |   |   |   |   |   |   |   |   +-- test_insert.py
|   |   |   |   |   |   |   |   |   +-- test_is_full.py
|   |   |   |   |   |   |   |   |   +-- test_repeat.py
|   |   |   |   |   |   |   |   |   +-- test_shift.py
|   |   |   |   |   |   |   |   |   +-- test_to_timestamp.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_asfreq.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_factorize.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_fillna.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_insert.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_is_full.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_repeat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_shift.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_to_timestamp.cpython-311.pyc
|   |   |   |   |   |   |   +-- ranges/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_join.py
|   |   |   |   |   |   |   |   +-- test_range.py
|   |   |   |   |   |   |   |   +-- test_setops.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_join.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_range.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_setops.cpython-311.pyc
|   |   |   |   |   |   |   +-- string/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   +-- timedeltas/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_arithmetic.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_delete.py
|   |   |   |   |   |   |   |   +-- test_formats.py
|   |   |   |   |   |   |   |   +-- test_freq_attr.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_join.py
|   |   |   |   |   |   |   |   +-- test_ops.py
|   |   |   |   |   |   |   |   +-- test_pickle.py
|   |   |   |   |   |   |   |   +-- test_scalar_compat.py
|   |   |   |   |   |   |   |   +-- test_searchsorted.py
|   |   |   |   |   |   |   |   +-- test_setops.py
|   |   |   |   |   |   |   |   +-- test_timedelta.py
|   |   |   |   |   |   |   |   +-- test_timedelta_range.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_delete.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_formats.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_freq_attr.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_join.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_ops.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pickle.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_scalar_compat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_searchsorted.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_setops.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_timedelta.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_timedelta_range.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- methods/
|   |   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   |   +-- test_factorize.py
|   |   |   |   |   |   |   |   |   +-- test_fillna.py
|   |   |   |   |   |   |   |   |   +-- test_insert.py
|   |   |   |   |   |   |   |   |   +-- test_repeat.py
|   |   |   |   |   |   |   |   |   +-- test_shift.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_factorize.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_fillna.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_insert.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_repeat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_shift.cpython-311.pyc
|   |   |   |   |   |   +-- indexing/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   +-- test_at.py
|   |   |   |   |   |   |   +-- test_categorical.py
|   |   |   |   |   |   |   +-- test_chaining_and_caching.py
|   |   |   |   |   |   |   +-- test_check_indexer.py
|   |   |   |   |   |   |   +-- test_coercion.py
|   |   |   |   |   |   |   +-- test_datetime.py
|   |   |   |   |   |   |   +-- test_floats.py
|   |   |   |   |   |   |   +-- test_iat.py
|   |   |   |   |   |   |   +-- test_iloc.py
|   |   |   |   |   |   |   +-- test_indexers.py
|   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   +-- test_loc.py
|   |   |   |   |   |   |   +-- test_na_indexing.py
|   |   |   |   |   |   |   +-- test_partial.py
|   |   |   |   |   |   |   +-- test_scalar.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_at.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_categorical.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_chaining_and_caching.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_check_indexer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_coercion.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_datetime.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_floats.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_iat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_iloc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_indexers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_loc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_na_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_partial.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_scalar.cpython-311.pyc
|   |   |   |   |   |   |   +-- interval/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_interval.py
|   |   |   |   |   |   |   |   +-- test_interval_new.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_interval.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_interval_new.cpython-311.pyc
|   |   |   |   |   |   |   +-- multiindex/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_chaining_and_caching.py
|   |   |   |   |   |   |   |   +-- test_datetime.py
|   |   |   |   |   |   |   |   +-- test_getitem.py
|   |   |   |   |   |   |   |   +-- test_iloc.py
|   |   |   |   |   |   |   |   +-- test_indexing_slow.py
|   |   |   |   |   |   |   |   +-- test_loc.py
|   |   |   |   |   |   |   |   +-- test_multiindex.py
|   |   |   |   |   |   |   |   +-- test_partial.py
|   |   |   |   |   |   |   |   +-- test_setitem.py
|   |   |   |   |   |   |   |   +-- test_slice.py
|   |   |   |   |   |   |   |   +-- test_sorted.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_chaining_and_caching.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_datetime.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_getitem.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_iloc.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing_slow.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_loc.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_multiindex.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_partial.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_setitem.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_slice.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sorted.cpython-311.pyc
|   |   |   |   |   |   +-- interchange/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_impl.py
|   |   |   |   |   |   |   +-- test_spec_conformance.py
|   |   |   |   |   |   |   +-- test_utils.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_impl.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_spec_conformance.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_utils.cpython-311.pyc
|   |   |   |   |   |   +-- internals/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_api.py
|   |   |   |   |   |   |   +-- test_internals.py
|   |   |   |   |   |   |   +-- test_managers.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_internals.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_managers.cpython-311.pyc
|   |   |   |   |   |   +-- io/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   +-- generate_legacy_storage_files.py
|   |   |   |   |   |   |   +-- test_clipboard.py
|   |   |   |   |   |   |   +-- test_common.py
|   |   |   |   |   |   |   +-- test_compression.py
|   |   |   |   |   |   |   +-- test_feather.py
|   |   |   |   |   |   |   +-- test_fsspec.py
|   |   |   |   |   |   |   +-- test_gbq.py
|   |   |   |   |   |   |   +-- test_gcs.py
|   |   |   |   |   |   |   +-- test_html.py
|   |   |   |   |   |   |   +-- test_http_headers.py
|   |   |   |   |   |   |   +-- test_orc.py
|   |   |   |   |   |   |   +-- test_parquet.py
|   |   |   |   |   |   |   +-- test_pickle.py
|   |   |   |   |   |   |   +-- test_s3.py
|   |   |   |   |   |   |   +-- test_spss.py
|   |   |   |   |   |   |   +-- test_sql.py
|   |   |   |   |   |   |   +-- test_stata.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- generate_legacy_storage_files.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_clipboard.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_compression.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_feather.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_fsspec.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_gbq.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_gcs.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_html.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_http_headers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_orc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_parquet.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_pickle.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_s3.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_spss.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_sql.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_stata.cpython-311.pyc
|   |   |   |   |   |   |   +-- excel/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_odf.py
|   |   |   |   |   |   |   |   +-- test_odswriter.py
|   |   |   |   |   |   |   |   +-- test_openpyxl.py
|   |   |   |   |   |   |   |   +-- test_readers.py
|   |   |   |   |   |   |   |   +-- test_style.py
|   |   |   |   |   |   |   |   +-- test_writers.py
|   |   |   |   |   |   |   |   +-- test_xlrd.py
|   |   |   |   |   |   |   |   +-- test_xlsxwriter.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_odf.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_odswriter.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_openpyxl.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_readers.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_style.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_writers.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_xlrd.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_xlsxwriter.cpython-311.pyc
|   |   |   |   |   |   |   +-- formats/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_console.py
|   |   |   |   |   |   |   |   +-- test_css.py
|   |   |   |   |   |   |   |   +-- test_eng_formatting.py
|   |   |   |   |   |   |   |   +-- test_format.py
|   |   |   |   |   |   |   |   +-- test_ipython_compat.py
|   |   |   |   |   |   |   |   +-- test_printing.py
|   |   |   |   |   |   |   |   +-- test_to_csv.py
|   |   |   |   |   |   |   |   +-- test_to_excel.py
|   |   |   |   |   |   |   |   +-- test_to_html.py
|   |   |   |   |   |   |   |   +-- test_to_latex.py
|   |   |   |   |   |   |   |   +-- test_to_markdown.py
|   |   |   |   |   |   |   |   +-- test_to_string.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_console.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_css.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_eng_formatting.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_format.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_ipython_compat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_printing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_csv.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_excel.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_html.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_latex.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_markdown.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_string.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- style/
|   |   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   |   +-- test_bar.py
|   |   |   |   |   |   |   |   |   +-- test_exceptions.py
|   |   |   |   |   |   |   |   |   +-- test_format.py
|   |   |   |   |   |   |   |   |   +-- test_highlight.py
|   |   |   |   |   |   |   |   |   +-- test_html.py
|   |   |   |   |   |   |   |   |   +-- test_matplotlib.py
|   |   |   |   |   |   |   |   |   +-- test_non_unique.py
|   |   |   |   |   |   |   |   |   +-- test_style.py
|   |   |   |   |   |   |   |   |   +-- test_to_latex.py
|   |   |   |   |   |   |   |   |   +-- test_to_string.py
|   |   |   |   |   |   |   |   |   +-- test_tooltip.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_bar.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_exceptions.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_format.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_highlight.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_html.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_matplotlib.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_non_unique.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_style.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_to_latex.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_to_string.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_tooltip.cpython-311.pyc
|   |   |   |   |   |   |   +-- json/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   |   +-- test_compression.py
|   |   |   |   |   |   |   |   +-- test_deprecated_kwargs.py
|   |   |   |   |   |   |   |   +-- test_json_table_schema.py
|   |   |   |   |   |   |   |   +-- test_json_table_schema_ext_dtype.py
|   |   |   |   |   |   |   |   +-- test_normalize.py
|   |   |   |   |   |   |   |   +-- test_pandas.py
|   |   |   |   |   |   |   |   +-- test_readlines.py
|   |   |   |   |   |   |   |   +-- test_ujson.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_compression.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_deprecated_kwargs.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_json_table_schema.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_json_table_schema_ext_dtype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_normalize.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pandas.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_readlines.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_ujson.cpython-311.pyc
|   |   |   |   |   |   |   +-- parser/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   |   +-- test_c_parser_only.py
|   |   |   |   |   |   |   |   +-- test_comment.py
|   |   |   |   |   |   |   |   +-- test_compression.py
|   |   |   |   |   |   |   |   +-- test_concatenate_chunks.py
|   |   |   |   |   |   |   |   +-- test_converters.py
|   |   |   |   |   |   |   |   +-- test_dialect.py
|   |   |   |   |   |   |   |   +-- test_encoding.py
|   |   |   |   |   |   |   |   +-- test_header.py
|   |   |   |   |   |   |   |   +-- test_index_col.py
|   |   |   |   |   |   |   |   +-- test_mangle_dupes.py
|   |   |   |   |   |   |   |   +-- test_multi_thread.py
|   |   |   |   |   |   |   |   +-- test_na_values.py
|   |   |   |   |   |   |   |   +-- test_network.py
|   |   |   |   |   |   |   |   +-- test_parse_dates.py
|   |   |   |   |   |   |   |   +-- test_python_parser_only.py
|   |   |   |   |   |   |   |   +-- test_quoting.py
|   |   |   |   |   |   |   |   +-- test_read_fwf.py
|   |   |   |   |   |   |   |   +-- test_skiprows.py
|   |   |   |   |   |   |   |   +-- test_textreader.py
|   |   |   |   |   |   |   |   +-- test_unsupported.py
|   |   |   |   |   |   |   |   +-- test_upcast.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_c_parser_only.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_comment.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_compression.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_concatenate_chunks.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_converters.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dialect.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_encoding.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_header.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_index_col.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_mangle_dupes.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_multi_thread.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_na_values.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_network.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_parse_dates.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_python_parser_only.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_quoting.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_read_fwf.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_skiprows.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_textreader.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_unsupported.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_upcast.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common/
|   |   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   |   +-- test_chunksize.py
|   |   |   |   |   |   |   |   |   +-- test_common_basic.py
|   |   |   |   |   |   |   |   |   +-- test_data_list.py
|   |   |   |   |   |   |   |   |   +-- test_decimal.py
|   |   |   |   |   |   |   |   |   +-- test_file_buffer_url.py
|   |   |   |   |   |   |   |   |   +-- test_float.py
|   |   |   |   |   |   |   |   |   +-- test_index.py
|   |   |   |   |   |   |   |   |   +-- test_inf.py
|   |   |   |   |   |   |   |   |   +-- test_ints.py
|   |   |   |   |   |   |   |   |   +-- test_iterator.py
|   |   |   |   |   |   |   |   |   +-- test_read_errors.py
|   |   |   |   |   |   |   |   |   +-- test_verbose.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_chunksize.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_common_basic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_data_list.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_decimal.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_file_buffer_url.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_float.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_index.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_inf.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_ints.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_iterator.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_read_errors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_verbose.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- dtypes/
|   |   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   |   +-- test_categorical.py
|   |   |   |   |   |   |   |   |   +-- test_dtypes_basic.py
|   |   |   |   |   |   |   |   |   +-- test_empty.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_categorical.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_dtypes_basic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_empty.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- usecols/
|   |   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   |   +-- test_parse_dates.py
|   |   |   |   |   |   |   |   |   +-- test_strings.py
|   |   |   |   |   |   |   |   |   +-- test_usecols_basic.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_parse_dates.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_strings.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_usecols_basic.cpython-311.pyc
|   |   |   |   |   |   |   +-- pytables/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   |   +-- test_append.py
|   |   |   |   |   |   |   |   +-- test_categorical.py
|   |   |   |   |   |   |   |   +-- test_compat.py
|   |   |   |   |   |   |   |   +-- test_complex.py
|   |   |   |   |   |   |   |   +-- test_errors.py
|   |   |   |   |   |   |   |   +-- test_file_handling.py
|   |   |   |   |   |   |   |   +-- test_keys.py
|   |   |   |   |   |   |   |   +-- test_put.py
|   |   |   |   |   |   |   |   +-- test_pytables_missing.py
|   |   |   |   |   |   |   |   +-- test_read.py
|   |   |   |   |   |   |   |   +-- test_retain_attributes.py
|   |   |   |   |   |   |   |   +-- test_round_trip.py
|   |   |   |   |   |   |   |   +-- test_select.py
|   |   |   |   |   |   |   |   +-- test_store.py
|   |   |   |   |   |   |   |   +-- test_subclass.py
|   |   |   |   |   |   |   |   +-- test_time_series.py
|   |   |   |   |   |   |   |   +-- test_timezones.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_append.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_categorical.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_compat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_complex.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_errors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_file_handling.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_keys.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_put.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pytables_missing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_read.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_retain_attributes.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_round_trip.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_select.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_store.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_subclass.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_time_series.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_timezones.cpython-311.pyc
|   |   |   |   |   |   |   +-- sas/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_byteswap.py
|   |   |   |   |   |   |   |   +-- test_sas.py
|   |   |   |   |   |   |   |   +-- test_sas7bdat.py
|   |   |   |   |   |   |   |   +-- test_xport.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_byteswap.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sas.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sas7bdat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_xport.cpython-311.pyc
|   |   |   |   |   |   |   +-- xml/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   |   +-- test_to_xml.py
|   |   |   |   |   |   |   |   +-- test_xml.py
|   |   |   |   |   |   |   |   +-- test_xml_dtypes.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_xml.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_xml.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_xml_dtypes.cpython-311.pyc
|   |   |   |   |   |   +-- libs/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_hashtable.py
|   |   |   |   |   |   |   +-- test_join.py
|   |   |   |   |   |   |   +-- test_lib.py
|   |   |   |   |   |   |   +-- test_libalgos.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_hashtable.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_join.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_lib.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_libalgos.cpython-311.pyc
|   |   |   |   |   |   +-- plotting/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   +-- test_backend.py
|   |   |   |   |   |   |   +-- test_boxplot_method.py
|   |   |   |   |   |   |   +-- test_common.py
|   |   |   |   |   |   |   +-- test_converter.py
|   |   |   |   |   |   |   +-- test_datetimelike.py
|   |   |   |   |   |   |   +-- test_groupby.py
|   |   |   |   |   |   |   +-- test_hist_method.py
|   |   |   |   |   |   |   +-- test_misc.py
|   |   |   |   |   |   |   +-- test_series.py
|   |   |   |   |   |   |   +-- test_style.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_backend.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_boxplot_method.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_converter.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_datetimelike.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_groupby.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_hist_method.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_misc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_series.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_style.cpython-311.pyc
|   |   |   |   |   |   |   +-- frame/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_frame.py
|   |   |   |   |   |   |   |   +-- test_frame_color.py
|   |   |   |   |   |   |   |   +-- test_frame_groupby.py
|   |   |   |   |   |   |   |   +-- test_frame_legend.py
|   |   |   |   |   |   |   |   +-- test_frame_subplots.py
|   |   |   |   |   |   |   |   +-- test_hist_box_by.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_frame.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_frame_color.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_frame_groupby.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_frame_legend.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_frame_subplots.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_hist_box_by.cpython-311.pyc
|   |   |   |   |   |   +-- reductions/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_reductions.py
|   |   |   |   |   |   |   +-- test_stat_reductions.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_reductions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_stat_reductions.cpython-311.pyc
|   |   |   |   |   |   +-- resample/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   +-- test_base.py
|   |   |   |   |   |   |   +-- test_datetime_index.py
|   |   |   |   |   |   |   +-- test_period_index.py
|   |   |   |   |   |   |   +-- test_resample_api.py
|   |   |   |   |   |   |   +-- test_resampler_grouper.py
|   |   |   |   |   |   |   +-- test_time_grouper.py
|   |   |   |   |   |   |   +-- test_timedelta.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_datetime_index.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_period_index.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_resample_api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_resampler_grouper.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_time_grouper.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_timedelta.cpython-311.pyc
|   |   |   |   |   |   +-- reshape/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_crosstab.py
|   |   |   |   |   |   |   +-- test_cut.py
|   |   |   |   |   |   |   +-- test_from_dummies.py
|   |   |   |   |   |   |   +-- test_get_dummies.py
|   |   |   |   |   |   |   +-- test_melt.py
|   |   |   |   |   |   |   +-- test_pivot.py
|   |   |   |   |   |   |   +-- test_pivot_multilevel.py
|   |   |   |   |   |   |   +-- test_qcut.py
|   |   |   |   |   |   |   +-- test_union_categoricals.py
|   |   |   |   |   |   |   +-- test_util.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_crosstab.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_cut.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_from_dummies.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_get_dummies.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_melt.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_pivot.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_pivot_multilevel.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_qcut.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_union_categoricals.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_util.cpython-311.pyc
|   |   |   |   |   |   |   +-- concat/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   |   +-- test_append.py
|   |   |   |   |   |   |   |   +-- test_append_common.py
|   |   |   |   |   |   |   |   +-- test_categorical.py
|   |   |   |   |   |   |   |   +-- test_concat.py
|   |   |   |   |   |   |   |   +-- test_dataframe.py
|   |   |   |   |   |   |   |   +-- test_datetimes.py
|   |   |   |   |   |   |   |   +-- test_empty.py
|   |   |   |   |   |   |   |   +-- test_index.py
|   |   |   |   |   |   |   |   +-- test_invalid.py
|   |   |   |   |   |   |   |   +-- test_series.py
|   |   |   |   |   |   |   |   +-- test_sort.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_append.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_append_common.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_categorical.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_concat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dataframe.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_datetimes.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_empty.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_index.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_invalid.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_series.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sort.cpython-311.pyc
|   |   |   |   |   |   |   +-- merge/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_join.py
|   |   |   |   |   |   |   |   +-- test_merge.py
|   |   |   |   |   |   |   |   +-- test_merge_asof.py
|   |   |   |   |   |   |   |   +-- test_merge_cross.py
|   |   |   |   |   |   |   |   +-- test_merge_index_as_string.py
|   |   |   |   |   |   |   |   +-- test_merge_ordered.py
|   |   |   |   |   |   |   |   +-- test_multi.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_join.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_merge.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_merge_asof.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_merge_cross.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_merge_index_as_string.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_merge_ordered.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_multi.cpython-311.pyc
|   |   |   |   |   |   +-- scalar/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_na_scalar.py
|   |   |   |   |   |   |   +-- test_nat.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_na_scalar.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_nat.cpython-311.pyc
|   |   |   |   |   |   |   +-- interval/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_arithmetic.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_contains.py
|   |   |   |   |   |   |   |   +-- test_formats.py
|   |   |   |   |   |   |   |   +-- test_interval.py
|   |   |   |   |   |   |   |   +-- test_overlaps.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_contains.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_formats.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_interval.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_overlaps.cpython-311.pyc
|   |   |   |   |   |   |   +-- period/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_arithmetic.py
|   |   |   |   |   |   |   |   +-- test_asfreq.py
|   |   |   |   |   |   |   |   +-- test_period.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_asfreq.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_period.cpython-311.pyc
|   |   |   |   |   |   |   +-- timedelta/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_arithmetic.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_formats.py
|   |   |   |   |   |   |   |   +-- test_timedelta.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_formats.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_timedelta.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- methods/
|   |   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   |   +-- test_as_unit.py
|   |   |   |   |   |   |   |   |   +-- test_round.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_as_unit.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_round.cpython-311.pyc
|   |   |   |   |   |   |   +-- timestamp/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_arithmetic.py
|   |   |   |   |   |   |   |   +-- test_comparisons.py
|   |   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   |   +-- test_formats.py
|   |   |   |   |   |   |   |   +-- test_timestamp.py
|   |   |   |   |   |   |   |   +-- test_timezones.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_comparisons.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_formats.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_timestamp.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_timezones.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- methods/
|   |   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   |   +-- test_as_unit.py
|   |   |   |   |   |   |   |   |   +-- test_normalize.py
|   |   |   |   |   |   |   |   |   +-- test_replace.py
|   |   |   |   |   |   |   |   |   +-- test_round.py
|   |   |   |   |   |   |   |   |   +-- test_timestamp_method.py
|   |   |   |   |   |   |   |   |   +-- test_to_julian_date.py
|   |   |   |   |   |   |   |   |   +-- test_to_pydatetime.py
|   |   |   |   |   |   |   |   |   +-- test_tz_convert.py
|   |   |   |   |   |   |   |   |   +-- test_tz_localize.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_as_unit.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_normalize.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_replace.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_round.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_timestamp_method.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_to_julian_date.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_to_pydatetime.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_tz_convert.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- test_tz_localize.cpython-311.pyc
|   |   |   |   |   |   +-- series/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_api.py
|   |   |   |   |   |   |   +-- test_arithmetic.py
|   |   |   |   |   |   |   +-- test_constructors.py
|   |   |   |   |   |   |   +-- test_cumulative.py
|   |   |   |   |   |   |   +-- test_formats.py
|   |   |   |   |   |   |   +-- test_iteration.py
|   |   |   |   |   |   |   +-- test_logical_ops.py
|   |   |   |   |   |   |   +-- test_missing.py
|   |   |   |   |   |   |   +-- test_npfuncs.py
|   |   |   |   |   |   |   +-- test_reductions.py
|   |   |   |   |   |   |   +-- test_subclass.py
|   |   |   |   |   |   |   +-- test_ufunc.py
|   |   |   |   |   |   |   +-- test_unary.py
|   |   |   |   |   |   |   +-- test_validate.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_arithmetic.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_cumulative.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_formats.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_iteration.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_logical_ops.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_missing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_npfuncs.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_reductions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_subclass.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_ufunc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_unary.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_validate.cpython-311.pyc
|   |   |   |   |   |   |   +-- accessors/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_cat_accessor.py
|   |   |   |   |   |   |   |   +-- test_dt_accessor.py
|   |   |   |   |   |   |   |   +-- test_list_accessor.py
|   |   |   |   |   |   |   |   +-- test_sparse_accessor.py
|   |   |   |   |   |   |   |   +-- test_str_accessor.py
|   |   |   |   |   |   |   |   +-- test_struct_accessor.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_cat_accessor.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dt_accessor.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_list_accessor.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sparse_accessor.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_str_accessor.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_struct_accessor.cpython-311.pyc
|   |   |   |   |   |   |   +-- indexing/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_datetime.py
|   |   |   |   |   |   |   |   +-- test_delitem.py
|   |   |   |   |   |   |   |   +-- test_get.py
|   |   |   |   |   |   |   |   +-- test_getitem.py
|   |   |   |   |   |   |   |   +-- test_indexing.py
|   |   |   |   |   |   |   |   +-- test_mask.py
|   |   |   |   |   |   |   |   +-- test_set_value.py
|   |   |   |   |   |   |   |   +-- test_setitem.py
|   |   |   |   |   |   |   |   +-- test_take.py
|   |   |   |   |   |   |   |   +-- test_where.py
|   |   |   |   |   |   |   |   +-- test_xs.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_datetime.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_delitem.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_get.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_getitem.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_indexing.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_mask.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_set_value.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_setitem.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_take.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_where.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_xs.cpython-311.pyc
|   |   |   |   |   |   |   +-- methods/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_add_prefix_suffix.py
|   |   |   |   |   |   |   |   +-- test_align.py
|   |   |   |   |   |   |   |   +-- test_argsort.py
|   |   |   |   |   |   |   |   +-- test_asof.py
|   |   |   |   |   |   |   |   +-- test_astype.py
|   |   |   |   |   |   |   |   +-- test_autocorr.py
|   |   |   |   |   |   |   |   +-- test_between.py
|   |   |   |   |   |   |   |   +-- test_case_when.py
|   |   |   |   |   |   |   |   +-- test_clip.py
|   |   |   |   |   |   |   |   +-- test_combine.py
|   |   |   |   |   |   |   |   +-- test_combine_first.py
|   |   |   |   |   |   |   |   +-- test_compare.py
|   |   |   |   |   |   |   |   +-- test_convert_dtypes.py
|   |   |   |   |   |   |   |   +-- test_copy.py
|   |   |   |   |   |   |   |   +-- test_count.py
|   |   |   |   |   |   |   |   +-- test_cov_corr.py
|   |   |   |   |   |   |   |   +-- test_describe.py
|   |   |   |   |   |   |   |   +-- test_diff.py
|   |   |   |   |   |   |   |   +-- test_drop.py
|   |   |   |   |   |   |   |   +-- test_drop_duplicates.py
|   |   |   |   |   |   |   |   +-- test_dropna.py
|   |   |   |   |   |   |   |   +-- test_dtypes.py
|   |   |   |   |   |   |   |   +-- test_duplicated.py
|   |   |   |   |   |   |   |   +-- test_equals.py
|   |   |   |   |   |   |   |   +-- test_explode.py
|   |   |   |   |   |   |   |   +-- test_fillna.py
|   |   |   |   |   |   |   |   +-- test_get_numeric_data.py
|   |   |   |   |   |   |   |   +-- test_head_tail.py
|   |   |   |   |   |   |   |   +-- test_infer_objects.py
|   |   |   |   |   |   |   |   +-- test_info.py
|   |   |   |   |   |   |   |   +-- test_interpolate.py
|   |   |   |   |   |   |   |   +-- test_is_monotonic.py
|   |   |   |   |   |   |   |   +-- test_is_unique.py
|   |   |   |   |   |   |   |   +-- test_isin.py
|   |   |   |   |   |   |   |   +-- test_isna.py
|   |   |   |   |   |   |   |   +-- test_item.py
|   |   |   |   |   |   |   |   +-- test_map.py
|   |   |   |   |   |   |   |   +-- test_matmul.py
|   |   |   |   |   |   |   |   +-- test_nlargest.py
|   |   |   |   |   |   |   |   +-- test_nunique.py
|   |   |   |   |   |   |   |   +-- test_pct_change.py
|   |   |   |   |   |   |   |   +-- test_pop.py
|   |   |   |   |   |   |   |   +-- test_quantile.py
|   |   |   |   |   |   |   |   +-- test_rank.py
|   |   |   |   |   |   |   |   +-- test_reindex.py
|   |   |   |   |   |   |   |   +-- test_reindex_like.py
|   |   |   |   |   |   |   |   +-- test_rename.py
|   |   |   |   |   |   |   |   +-- test_rename_axis.py
|   |   |   |   |   |   |   |   +-- test_repeat.py
|   |   |   |   |   |   |   |   +-- test_replace.py
|   |   |   |   |   |   |   |   +-- test_reset_index.py
|   |   |   |   |   |   |   |   +-- test_round.py
|   |   |   |   |   |   |   |   +-- test_searchsorted.py
|   |   |   |   |   |   |   |   +-- test_set_name.py
|   |   |   |   |   |   |   |   +-- test_size.py
|   |   |   |   |   |   |   |   +-- test_sort_index.py
|   |   |   |   |   |   |   |   +-- test_sort_values.py
|   |   |   |   |   |   |   |   +-- test_to_csv.py
|   |   |   |   |   |   |   |   +-- test_to_dict.py
|   |   |   |   |   |   |   |   +-- test_to_frame.py
|   |   |   |   |   |   |   |   +-- test_to_numpy.py
|   |   |   |   |   |   |   |   +-- test_tolist.py
|   |   |   |   |   |   |   |   +-- test_truncate.py
|   |   |   |   |   |   |   |   +-- test_tz_localize.py
|   |   |   |   |   |   |   |   +-- test_unique.py
|   |   |   |   |   |   |   |   +-- test_unstack.py
|   |   |   |   |   |   |   |   +-- test_update.py
|   |   |   |   |   |   |   |   +-- test_value_counts.py
|   |   |   |   |   |   |   |   +-- test_values.py
|   |   |   |   |   |   |   |   +-- test_view.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_add_prefix_suffix.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_align.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_argsort.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_asof.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_astype.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_autocorr.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_between.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_case_when.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_clip.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_combine.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_combine_first.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_compare.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_convert_dtypes.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_copy.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_count.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_cov_corr.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_describe.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_diff.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_drop.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_drop_duplicates.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dropna.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dtypes.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_duplicated.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_equals.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_explode.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_fillna.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_get_numeric_data.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_head_tail.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_infer_objects.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_info.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_interpolate.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_is_monotonic.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_is_unique.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_isin.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_isna.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_item.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_map.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_matmul.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_nlargest.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_nunique.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pct_change.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_pop.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_quantile.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_rank.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reindex.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reindex_like.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_rename.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_rename_axis.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_repeat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_replace.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_reset_index.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_round.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_searchsorted.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_set_name.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_size.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sort_index.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_sort_values.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_csv.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_dict.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_frame.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_to_numpy.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_tolist.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_truncate.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_tz_localize.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_unique.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_unstack.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_update.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_value_counts.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_values.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_view.cpython-311.pyc
|   |   |   |   |   |   +-- strings/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   +-- test_api.py
|   |   |   |   |   |   |   +-- test_case_justify.py
|   |   |   |   |   |   |   +-- test_cat.py
|   |   |   |   |   |   |   +-- test_extract.py
|   |   |   |   |   |   |   +-- test_find_replace.py
|   |   |   |   |   |   |   +-- test_get_dummies.py
|   |   |   |   |   |   |   +-- test_split_partition.py
|   |   |   |   |   |   |   +-- test_string_array.py
|   |   |   |   |   |   |   +-- test_strings.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_case_justify.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_cat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_extract.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_find_replace.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_get_dummies.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_split_partition.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_string_array.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_strings.cpython-311.pyc
|   |   |   |   |   |   +-- tools/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_to_datetime.py
|   |   |   |   |   |   |   +-- test_to_numeric.py
|   |   |   |   |   |   |   +-- test_to_time.py
|   |   |   |   |   |   |   +-- test_to_timedelta.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_to_datetime.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_to_numeric.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_to_time.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_to_timedelta.cpython-311.pyc
|   |   |   |   |   |   +-- tseries/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- frequencies/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_freq_code.py
|   |   |   |   |   |   |   |   +-- test_frequencies.py
|   |   |   |   |   |   |   |   +-- test_inference.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_freq_code.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_frequencies.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_inference.cpython-311.pyc
|   |   |   |   |   |   |   +-- holiday/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- test_calendar.py
|   |   |   |   |   |   |   |   +-- test_federal.py
|   |   |   |   |   |   |   |   +-- test_holiday.py
|   |   |   |   |   |   |   |   +-- test_observance.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_calendar.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_federal.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_holiday.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_observance.cpython-311.pyc
|   |   |   |   |   |   |   +-- offsets/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   |   +-- test_business_day.py
|   |   |   |   |   |   |   |   +-- test_business_hour.py
|   |   |   |   |   |   |   |   +-- test_business_month.py
|   |   |   |   |   |   |   |   +-- test_business_quarter.py
|   |   |   |   |   |   |   |   +-- test_business_year.py
|   |   |   |   |   |   |   |   +-- test_common.py
|   |   |   |   |   |   |   |   +-- test_custom_business_day.py
|   |   |   |   |   |   |   |   +-- test_custom_business_hour.py
|   |   |   |   |   |   |   |   +-- test_custom_business_month.py
|   |   |   |   |   |   |   |   +-- test_dst.py
|   |   |   |   |   |   |   |   +-- test_easter.py
|   |   |   |   |   |   |   |   +-- test_fiscal.py
|   |   |   |   |   |   |   |   +-- test_index.py
|   |   |   |   |   |   |   |   +-- test_month.py
|   |   |   |   |   |   |   |   +-- test_offsets.py
|   |   |   |   |   |   |   |   +-- test_offsets_properties.py
|   |   |   |   |   |   |   |   +-- test_quarter.py
|   |   |   |   |   |   |   |   +-- test_ticks.py
|   |   |   |   |   |   |   |   +-- test_week.py
|   |   |   |   |   |   |   |   +-- test_year.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_business_day.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_business_hour.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_business_month.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_business_quarter.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_business_year.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_common.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_custom_business_day.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_custom_business_hour.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_custom_business_month.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_dst.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_easter.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_fiscal.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_index.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_month.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_offsets.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_offsets_properties.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_quarter.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_ticks.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_week.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_year.cpython-311.pyc
|   |   |   |   |   |   +-- tslibs/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- test_api.py
|   |   |   |   |   |   |   +-- test_array_to_datetime.py
|   |   |   |   |   |   |   +-- test_ccalendar.py
|   |   |   |   |   |   |   +-- test_conversion.py
|   |   |   |   |   |   |   +-- test_fields.py
|   |   |   |   |   |   |   +-- test_libfrequencies.py
|   |   |   |   |   |   |   +-- test_liboffsets.py
|   |   |   |   |   |   |   +-- test_np_datetime.py
|   |   |   |   |   |   |   +-- test_npy_units.py
|   |   |   |   |   |   |   +-- test_parse_iso8601.py
|   |   |   |   |   |   |   +-- test_parsing.py
|   |   |   |   |   |   |   +-- test_period.py
|   |   |   |   |   |   |   +-- test_resolution.py
|   |   |   |   |   |   |   +-- test_strptime.py
|   |   |   |   |   |   |   +-- test_timedeltas.py
|   |   |   |   |   |   |   +-- test_timezones.py
|   |   |   |   |   |   |   +-- test_to_offset.py
|   |   |   |   |   |   |   +-- test_tzconversion.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_array_to_datetime.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_ccalendar.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_conversion.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_fields.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_libfrequencies.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_liboffsets.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_np_datetime.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_npy_units.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_parse_iso8601.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_parsing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_period.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_resolution.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_strptime.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_timedeltas.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_timezones.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_to_offset.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_tzconversion.cpython-311.pyc
|   |   |   |   |   |   +-- util/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   +-- test_assert_almost_equal.py
|   |   |   |   |   |   |   +-- test_assert_attr_equal.py
|   |   |   |   |   |   |   +-- test_assert_categorical_equal.py
|   |   |   |   |   |   |   +-- test_assert_extension_array_equal.py
|   |   |   |   |   |   |   +-- test_assert_frame_equal.py
|   |   |   |   |   |   |   +-- test_assert_index_equal.py
|   |   |   |   |   |   |   +-- test_assert_interval_array_equal.py
|   |   |   |   |   |   |   +-- test_assert_numpy_array_equal.py
|   |   |   |   |   |   |   +-- test_assert_produces_warning.py
|   |   |   |   |   |   |   +-- test_assert_series_equal.py
|   |   |   |   |   |   |   +-- test_deprecate.py
|   |   |   |   |   |   |   +-- test_deprecate_kwarg.py
|   |   |   |   |   |   |   +-- test_deprecate_nonkeyword_arguments.py
|   |   |   |   |   |   |   +-- test_doc.py
|   |   |   |   |   |   |   +-- test_hashing.py
|   |   |   |   |   |   |   +-- test_numba.py
|   |   |   |   |   |   |   +-- test_rewrite_warning.py
|   |   |   |   |   |   |   +-- test_shares_memory.py
|   |   |   |   |   |   |   +-- test_show_versions.py
|   |   |   |   |   |   |   +-- test_util.py
|   |   |   |   |   |   |   +-- test_validate_args.py
|   |   |   |   |   |   |   +-- test_validate_args_and_kwargs.py
|   |   |   |   |   |   |   +-- test_validate_inclusive.py
|   |   |   |   |   |   |   +-- test_validate_kwargs.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_assert_almost_equal.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_assert_attr_equal.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_assert_categorical_equal.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_assert_extension_array_equal.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_assert_frame_equal.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_assert_index_equal.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_assert_interval_array_equal.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_assert_numpy_array_equal.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_assert_produces_warning.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_assert_series_equal.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_deprecate.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_deprecate_kwarg.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_deprecate_nonkeyword_arguments.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_doc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_hashing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_numba.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_rewrite_warning.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_shares_memory.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_show_versions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_util.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_validate_args.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_validate_args_and_kwargs.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_validate_inclusive.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_validate_kwargs.cpython-311.pyc
|   |   |   |   |   |   +-- window/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   +-- test_api.py
|   |   |   |   |   |   |   +-- test_apply.py
|   |   |   |   |   |   |   +-- test_base_indexer.py
|   |   |   |   |   |   |   +-- test_cython_aggregations.py
|   |   |   |   |   |   |   +-- test_dtypes.py
|   |   |   |   |   |   |   +-- test_ewm.py
|   |   |   |   |   |   |   +-- test_expanding.py
|   |   |   |   |   |   |   +-- test_groupby.py
|   |   |   |   |   |   |   +-- test_numba.py
|   |   |   |   |   |   |   +-- test_online.py
|   |   |   |   |   |   |   +-- test_pairwise.py
|   |   |   |   |   |   |   +-- test_rolling.py
|   |   |   |   |   |   |   +-- test_rolling_functions.py
|   |   |   |   |   |   |   +-- test_rolling_quantile.py
|   |   |   |   |   |   |   +-- test_rolling_skew_kurt.py
|   |   |   |   |   |   |   +-- test_timeseries_window.py
|   |   |   |   |   |   |   +-- test_win_type.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_apply.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_base_indexer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_cython_aggregations.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_dtypes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_ewm.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_expanding.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_groupby.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_numba.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_online.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_pairwise.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_rolling.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_rolling_functions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_rolling_quantile.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_rolling_skew_kurt.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_timeseries_window.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- test_win_type.cpython-311.pyc
|   |   |   |   |   |   |   +-- moments/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   |   |   +-- test_moments_consistency_ewm.py
|   |   |   |   |   |   |   |   +-- test_moments_consistency_expanding.py
|   |   |   |   |   |   |   |   +-- test_moments_consistency_rolling.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_moments_consistency_ewm.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_moments_consistency_expanding.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- test_moments_consistency_rolling.cpython-311.pyc
|   |   |   |   |   +-- tseries/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   +-- frequencies.py
|   |   |   |   |   |   +-- holiday.py
|   |   |   |   |   |   +-- offsets.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   |   +-- frequencies.cpython-311.pyc
|   |   |   |   |   |   |   +-- holiday.cpython-311.pyc
|   |   |   |   |   |   |   +-- offsets.cpython-311.pyc
|   |   |   |   |   +-- util/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _decorators.py
|   |   |   |   |   |   +-- _doctools.py
|   |   |   |   |   |   +-- _exceptions.py
|   |   |   |   |   |   +-- _print_versions.py
|   |   |   |   |   |   +-- _test_decorators.py
|   |   |   |   |   |   +-- _tester.py
|   |   |   |   |   |   +-- _validators.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _decorators.cpython-311.pyc
|   |   |   |   |   |   |   +-- _doctools.cpython-311.pyc
|   |   |   |   |   |   |   +-- _exceptions.cpython-311.pyc
|   |   |   |   |   |   |   +-- _print_versions.cpython-311.pyc
|   |   |   |   |   |   |   +-- _test_decorators.cpython-311.pyc
|   |   |   |   |   |   |   +-- _tester.cpython-311.pyc
|   |   |   |   |   |   |   +-- _validators.cpython-311.pyc
|   |   |   |   |   |   +-- version/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   +-- pandas.libs/
|   |   |   |   |   +-- msvcp140-a4c2229bdc2a2a630acdc095b4d86008.dll
|   |   |   |   +-- pandas-2.3.3.dist-info/
|   |   |   |   |   +-- DELVEWHEEL
|   |   |   |   |   +-- entry_points.txt
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- REQUESTED
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- pefile-2024.8.26.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- PIL/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- __main__.py
|   |   |   |   |   +-- _avif.cp311-win_amd64.pyd
|   |   |   |   |   +-- _avif.pyi
|   |   |   |   |   +-- _binary.py
|   |   |   |   |   +-- _deprecate.py
|   |   |   |   |   +-- _imaging.cp311-win_amd64.pyd
|   |   |   |   |   +-- _imaging.pyi
|   |   |   |   |   +-- _imagingcms.cp311-win_amd64.pyd
|   |   |   |   |   +-- _imagingcms.pyi
|   |   |   |   |   +-- _imagingft.cp311-win_amd64.pyd
|   |   |   |   |   +-- _imagingft.pyi
|   |   |   |   |   +-- _imagingmath.cp311-win_amd64.pyd
|   |   |   |   |   +-- _imagingmath.pyi
|   |   |   |   |   +-- _imagingmorph.cp311-win_amd64.pyd
|   |   |   |   |   +-- _imagingmorph.pyi
|   |   |   |   |   +-- _imagingtk.cp311-win_amd64.pyd
|   |   |   |   |   +-- _imagingtk.pyi
|   |   |   |   |   +-- _tkinter_finder.py
|   |   |   |   |   +-- _typing.py
|   |   |   |   |   +-- _util.py
|   |   |   |   |   +-- _version.py
|   |   |   |   |   +-- _webp.cp311-win_amd64.pyd
|   |   |   |   |   +-- _webp.pyi
|   |   |   |   |   +-- AvifImagePlugin.py
|   |   |   |   |   +-- BdfFontFile.py
|   |   |   |   |   +-- BlpImagePlugin.py
|   |   |   |   |   +-- BmpImagePlugin.py
|   |   |   |   |   +-- BufrStubImagePlugin.py
|   |   |   |   |   +-- ContainerIO.py
|   |   |   |   |   +-- CurImagePlugin.py
|   |   |   |   |   +-- DcxImagePlugin.py
|   |   |   |   |   +-- DdsImagePlugin.py
|   |   |   |   |   +-- EpsImagePlugin.py
|   |   |   |   |   +-- ExifTags.py
|   |   |   |   |   +-- features.py
|   |   |   |   |   +-- FitsImagePlugin.py
|   |   |   |   |   +-- FliImagePlugin.py
|   |   |   |   |   +-- FontFile.py
|   |   |   |   |   +-- FpxImagePlugin.py
|   |   |   |   |   +-- FtexImagePlugin.py
|   |   |   |   |   +-- GbrImagePlugin.py
|   |   |   |   |   +-- GdImageFile.py
|   |   |   |   |   +-- GifImagePlugin.py
|   |   |   |   |   +-- GimpGradientFile.py
|   |   |   |   |   +-- GimpPaletteFile.py
|   |   |   |   |   +-- GribStubImagePlugin.py
|   |   |   |   |   +-- Hdf5StubImagePlugin.py
|   |   |   |   |   +-- IcnsImagePlugin.py
|   |   |   |   |   +-- IcoImagePlugin.py
|   |   |   |   |   +-- Image.py
|   |   |   |   |   +-- ImageChops.py
|   |   |   |   |   +-- ImageCms.py
|   |   |   |   |   +-- ImageColor.py
|   |   |   |   |   +-- ImageDraw.py
|   |   |   |   |   +-- ImageDraw2.py
|   |   |   |   |   +-- ImageEnhance.py
|   |   |   |   |   +-- ImageFile.py
|   |   |   |   |   +-- ImageFilter.py
|   |   |   |   |   +-- ImageFont.py
|   |   |   |   |   +-- ImageGrab.py
|   |   |   |   |   +-- ImageMath.py
|   |   |   |   |   +-- ImageMode.py
|   |   |   |   |   +-- ImageMorph.py
|   |   |   |   |   +-- ImageOps.py
|   |   |   |   |   +-- ImagePalette.py
|   |   |   |   |   +-- ImagePath.py
|   |   |   |   |   +-- ImageQt.py
|   |   |   |   |   +-- ImageSequence.py
|   |   |   |   |   +-- ImageShow.py
|   |   |   |   |   +-- ImageStat.py
|   |   |   |   |   +-- ImageText.py
|   |   |   |   |   +-- ImageTk.py
|   |   |   |   |   +-- ImageTransform.py
|   |   |   |   |   +-- ImageWin.py
|   |   |   |   |   +-- ImImagePlugin.py
|   |   |   |   |   +-- ImtImagePlugin.py
|   |   |   |   |   +-- IptcImagePlugin.py
|   |   |   |   |   +-- Jpeg2KImagePlugin.py
|   |   |   |   |   +-- JpegImagePlugin.py
|   |   |   |   |   +-- JpegPresets.py
|   |   |   |   |   +-- McIdasImagePlugin.py
|   |   |   |   |   +-- MicImagePlugin.py
|   |   |   |   |   +-- MpegImagePlugin.py
|   |   |   |   |   +-- MpoImagePlugin.py
|   |   |   |   |   +-- MspImagePlugin.py
|   |   |   |   |   +-- PaletteFile.py
|   |   |   |   |   +-- PalmImagePlugin.py
|   |   |   |   |   +-- PcdImagePlugin.py
|   |   |   |   |   +-- PcfFontFile.py
|   |   |   |   |   +-- PcxImagePlugin.py
|   |   |   |   |   +-- PdfImagePlugin.py
|   |   |   |   |   +-- PdfParser.py
|   |   |   |   |   +-- PixarImagePlugin.py
|   |   |   |   |   +-- PngImagePlugin.py
|   |   |   |   |   +-- PpmImagePlugin.py
|   |   |   |   |   +-- PsdImagePlugin.py
|   |   |   |   |   +-- PSDraw.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- QoiImagePlugin.py
|   |   |   |   |   +-- report.py
|   |   |   |   |   +-- SgiImagePlugin.py
|   |   |   |   |   +-- SpiderImagePlugin.py
|   |   |   |   |   +-- SunImagePlugin.py
|   |   |   |   |   +-- TarIO.py
|   |   |   |   |   +-- TgaImagePlugin.py
|   |   |   |   |   +-- TiffImagePlugin.py
|   |   |   |   |   +-- TiffTags.py
|   |   |   |   |   +-- WalImageFile.py
|   |   |   |   |   +-- WebPImagePlugin.py
|   |   |   |   |   +-- WmfImagePlugin.py
|   |   |   |   |   +-- XbmImagePlugin.py
|   |   |   |   |   +-- XpmImagePlugin.py
|   |   |   |   |   +-- XVThumbImagePlugin.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   +-- _binary.cpython-311.pyc
|   |   |   |   |   |   +-- _deprecate.cpython-311.pyc
|   |   |   |   |   |   +-- _tkinter_finder.cpython-311.pyc
|   |   |   |   |   |   +-- _typing.cpython-311.pyc
|   |   |   |   |   |   +-- _util.cpython-311.pyc
|   |   |   |   |   |   +-- _version.cpython-311.pyc
|   |   |   |   |   |   +-- AvifImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- BdfFontFile.cpython-311.pyc
|   |   |   |   |   |   +-- BlpImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- BmpImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- BufrStubImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- ContainerIO.cpython-311.pyc
|   |   |   |   |   |   +-- CurImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- DcxImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- DdsImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- EpsImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- ExifTags.cpython-311.pyc
|   |   |   |   |   |   +-- features.cpython-311.pyc
|   |   |   |   |   |   +-- FitsImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- FliImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- FontFile.cpython-311.pyc
|   |   |   |   |   |   +-- FpxImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- FtexImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- GbrImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- GdImageFile.cpython-311.pyc
|   |   |   |   |   |   +-- GifImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- GimpGradientFile.cpython-311.pyc
|   |   |   |   |   |   +-- GimpPaletteFile.cpython-311.pyc
|   |   |   |   |   |   +-- GribStubImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- Hdf5StubImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- IcnsImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- IcoImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- Image.cpython-311.pyc
|   |   |   |   |   |   +-- ImageChops.cpython-311.pyc
|   |   |   |   |   |   +-- ImageCms.cpython-311.pyc
|   |   |   |   |   |   +-- ImageColor.cpython-311.pyc
|   |   |   |   |   |   +-- ImageDraw.cpython-311.pyc
|   |   |   |   |   |   +-- ImageDraw2.cpython-311.pyc
|   |   |   |   |   |   +-- ImageEnhance.cpython-311.pyc
|   |   |   |   |   |   +-- ImageFile.cpython-311.pyc
|   |   |   |   |   |   +-- ImageFilter.cpython-311.pyc
|   |   |   |   |   |   +-- ImageFont.cpython-311.pyc
|   |   |   |   |   |   +-- ImageGrab.cpython-311.pyc
|   |   |   |   |   |   +-- ImageMath.cpython-311.pyc
|   |   |   |   |   |   +-- ImageMode.cpython-311.pyc
|   |   |   |   |   |   +-- ImageMorph.cpython-311.pyc
|   |   |   |   |   |   +-- ImageOps.cpython-311.pyc
|   |   |   |   |   |   +-- ImagePalette.cpython-311.pyc
|   |   |   |   |   |   +-- ImagePath.cpython-311.pyc
|   |   |   |   |   |   +-- ImageQt.cpython-311.pyc
|   |   |   |   |   |   +-- ImageSequence.cpython-311.pyc
|   |   |   |   |   |   +-- ImageShow.cpython-311.pyc
|   |   |   |   |   |   +-- ImageStat.cpython-311.pyc
|   |   |   |   |   |   +-- ImageText.cpython-311.pyc
|   |   |   |   |   |   +-- ImageTk.cpython-311.pyc
|   |   |   |   |   |   +-- ImageTransform.cpython-311.pyc
|   |   |   |   |   |   +-- ImageWin.cpython-311.pyc
|   |   |   |   |   |   +-- ImImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- ImtImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- IptcImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- Jpeg2KImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- JpegImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- JpegPresets.cpython-311.pyc
|   |   |   |   |   |   +-- McIdasImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- MicImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- MpegImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- MpoImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- MspImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- PaletteFile.cpython-311.pyc
|   |   |   |   |   |   +-- PalmImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- PcdImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- PcfFontFile.cpython-311.pyc
|   |   |   |   |   |   +-- PcxImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- PdfImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- PdfParser.cpython-311.pyc
|   |   |   |   |   |   +-- PixarImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- PngImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- PpmImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- PsdImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- PSDraw.cpython-311.pyc
|   |   |   |   |   |   +-- QoiImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- report.cpython-311.pyc
|   |   |   |   |   |   +-- SgiImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- SpiderImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- SunImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- TarIO.cpython-311.pyc
|   |   |   |   |   |   +-- TgaImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- TiffImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- TiffTags.cpython-311.pyc
|   |   |   |   |   |   +-- WalImageFile.cpython-311.pyc
|   |   |   |   |   |   +-- WebPImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- WmfImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- XbmImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- XpmImagePlugin.cpython-311.pyc
|   |   |   |   |   |   +-- XVThumbImagePlugin.cpython-311.pyc
|   |   |   |   +-- pillow-12.0.0.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- REQUESTED
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- zip-safe
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE
|   |   |   |   +-- pip/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- __main__.py
|   |   |   |   |   +-- __pip-runner__.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   +-- __pip-runner__.cpython-311.pyc
|   |   |   |   |   +-- _internal/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- build_env.py
|   |   |   |   |   |   +-- cache.py
|   |   |   |   |   |   +-- configuration.py
|   |   |   |   |   |   +-- exceptions.py
|   |   |   |   |   |   +-- main.py
|   |   |   |   |   |   +-- pyproject.py
|   |   |   |   |   |   +-- self_outdated_check.py
|   |   |   |   |   |   +-- wheel_builder.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- build_env.cpython-311.pyc
|   |   |   |   |   |   |   +-- cache.cpython-311.pyc
|   |   |   |   |   |   |   +-- configuration.cpython-311.pyc
|   |   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   |   +-- main.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyproject.cpython-311.pyc
|   |   |   |   |   |   |   +-- self_outdated_check.cpython-311.pyc
|   |   |   |   |   |   |   +-- wheel_builder.cpython-311.pyc
|   |   |   |   |   |   +-- cli/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- autocompletion.py
|   |   |   |   |   |   |   +-- base_command.py
|   |   |   |   |   |   |   +-- cmdoptions.py
|   |   |   |   |   |   |   +-- command_context.py
|   |   |   |   |   |   |   +-- index_command.py
|   |   |   |   |   |   |   +-- main.py
|   |   |   |   |   |   |   +-- main_parser.py
|   |   |   |   |   |   |   +-- parser.py
|   |   |   |   |   |   |   +-- progress_bars.py
|   |   |   |   |   |   |   +-- req_command.py
|   |   |   |   |   |   |   +-- spinners.py
|   |   |   |   |   |   |   +-- status_codes.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- autocompletion.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- base_command.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- cmdoptions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- command_context.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- index_command.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- main.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- main_parser.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- parser.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- progress_bars.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- req_command.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- spinners.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- status_codes.cpython-311.pyc
|   |   |   |   |   |   +-- commands/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- cache.py
|   |   |   |   |   |   |   +-- check.py
|   |   |   |   |   |   |   +-- completion.py
|   |   |   |   |   |   |   +-- configuration.py
|   |   |   |   |   |   |   +-- debug.py
|   |   |   |   |   |   |   +-- download.py
|   |   |   |   |   |   |   +-- freeze.py
|   |   |   |   |   |   |   +-- hash.py
|   |   |   |   |   |   |   +-- help.py
|   |   |   |   |   |   |   +-- index.py
|   |   |   |   |   |   |   +-- inspect.py
|   |   |   |   |   |   |   +-- install.py
|   |   |   |   |   |   |   +-- list.py
|   |   |   |   |   |   |   +-- lock.py
|   |   |   |   |   |   |   +-- search.py
|   |   |   |   |   |   |   +-- show.py
|   |   |   |   |   |   |   +-- uninstall.py
|   |   |   |   |   |   |   +-- wheel.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- cache.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- check.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- completion.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- configuration.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- debug.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- download.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- freeze.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hash.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- help.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- index.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- inspect.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- install.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- list.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- lock.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- search.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- show.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- uninstall.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- wheel.cpython-311.pyc
|   |   |   |   |   |   +-- distributions/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   +-- installed.py
|   |   |   |   |   |   |   +-- sdist.py
|   |   |   |   |   |   |   +-- wheel.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- installed.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- sdist.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- wheel.cpython-311.pyc
|   |   |   |   |   |   +-- index/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- collector.py
|   |   |   |   |   |   |   +-- package_finder.py
|   |   |   |   |   |   |   +-- sources.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- collector.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- package_finder.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- sources.cpython-311.pyc
|   |   |   |   |   |   +-- locations/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _distutils.py
|   |   |   |   |   |   |   +-- _sysconfig.py
|   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _distutils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _sysconfig.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   +-- metadata/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _json.py
|   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   +-- pkg_resources.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _json.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pkg_resources.cpython-311.pyc
|   |   |   |   |   |   |   +-- importlib/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- _compat.py
|   |   |   |   |   |   |   |   +-- _dists.py
|   |   |   |   |   |   |   |   +-- _envs.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- _compat.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- _dists.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- _envs.cpython-311.pyc
|   |   |   |   |   |   +-- models/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- candidate.py
|   |   |   |   |   |   |   +-- direct_url.py
|   |   |   |   |   |   |   +-- format_control.py
|   |   |   |   |   |   |   +-- index.py
|   |   |   |   |   |   |   +-- installation_report.py
|   |   |   |   |   |   |   +-- link.py
|   |   |   |   |   |   |   +-- pylock.py
|   |   |   |   |   |   |   +-- scheme.py
|   |   |   |   |   |   |   +-- search_scope.py
|   |   |   |   |   |   |   +-- selection_prefs.py
|   |   |   |   |   |   |   +-- target_python.py
|   |   |   |   |   |   |   +-- wheel.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- candidate.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- direct_url.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- format_control.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- index.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- installation_report.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- link.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pylock.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- scheme.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- search_scope.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- selection_prefs.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- target_python.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- wheel.cpython-311.pyc
|   |   |   |   |   |   +-- network/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- auth.py
|   |   |   |   |   |   |   +-- cache.py
|   |   |   |   |   |   |   +-- download.py
|   |   |   |   |   |   |   +-- lazy_wheel.py
|   |   |   |   |   |   |   +-- session.py
|   |   |   |   |   |   |   +-- utils.py
|   |   |   |   |   |   |   +-- xmlrpc.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- auth.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- cache.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- download.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- lazy_wheel.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- session.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- xmlrpc.cpython-311.pyc
|   |   |   |   |   |   +-- operations/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- check.py
|   |   |   |   |   |   |   +-- freeze.py
|   |   |   |   |   |   |   +-- prepare.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- check.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- freeze.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- prepare.cpython-311.pyc
|   |   |   |   |   |   |   +-- build/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- build_tracker.py
|   |   |   |   |   |   |   |   +-- metadata.py
|   |   |   |   |   |   |   |   +-- metadata_editable.py
|   |   |   |   |   |   |   |   +-- wheel.py
|   |   |   |   |   |   |   |   +-- wheel_editable.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- build_tracker.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- metadata.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- metadata_editable.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- wheel.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- wheel_editable.cpython-311.pyc
|   |   |   |   |   |   |   +-- install/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- wheel.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- wheel.cpython-311.pyc
|   |   |   |   |   |   +-- req/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- constructors.py
|   |   |   |   |   |   |   +-- req_dependency_group.py
|   |   |   |   |   |   |   +-- req_file.py
|   |   |   |   |   |   |   +-- req_install.py
|   |   |   |   |   |   |   +-- req_set.py
|   |   |   |   |   |   |   +-- req_uninstall.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- constructors.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- req_dependency_group.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- req_file.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- req_install.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- req_set.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- req_uninstall.cpython-311.pyc
|   |   |   |   |   |   +-- resolution/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   +-- legacy/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- resolver.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- resolver.cpython-311.pyc
|   |   |   |   |   |   |   +-- resolvelib/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   |   +-- candidates.py
|   |   |   |   |   |   |   |   +-- factory.py
|   |   |   |   |   |   |   |   +-- found_candidates.py
|   |   |   |   |   |   |   |   +-- provider.py
|   |   |   |   |   |   |   |   +-- reporter.py
|   |   |   |   |   |   |   |   +-- requirements.py
|   |   |   |   |   |   |   |   +-- resolver.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- candidates.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- factory.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- found_candidates.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- provider.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- reporter.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- requirements.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- resolver.cpython-311.pyc
|   |   |   |   |   |   +-- utils/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _jaraco_text.py
|   |   |   |   |   |   |   +-- _log.py
|   |   |   |   |   |   |   +-- appdirs.py
|   |   |   |   |   |   |   +-- compat.py
|   |   |   |   |   |   |   +-- compatibility_tags.py
|   |   |   |   |   |   |   +-- datetime.py
|   |   |   |   |   |   |   +-- deprecation.py
|   |   |   |   |   |   |   +-- direct_url_helpers.py
|   |   |   |   |   |   |   +-- egg_link.py
|   |   |   |   |   |   |   +-- entrypoints.py
|   |   |   |   |   |   |   +-- filesystem.py
|   |   |   |   |   |   |   +-- filetypes.py
|   |   |   |   |   |   |   +-- glibc.py
|   |   |   |   |   |   |   +-- hashes.py
|   |   |   |   |   |   |   +-- logging.py
|   |   |   |   |   |   |   +-- misc.py
|   |   |   |   |   |   |   +-- packaging.py
|   |   |   |   |   |   |   +-- retry.py
|   |   |   |   |   |   |   +-- subprocess.py
|   |   |   |   |   |   |   +-- temp_dir.py
|   |   |   |   |   |   |   +-- unpacking.py
|   |   |   |   |   |   |   +-- urls.py
|   |   |   |   |   |   |   +-- virtualenv.py
|   |   |   |   |   |   |   +-- wheel.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _jaraco_text.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _log.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- appdirs.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- compat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- compatibility_tags.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- datetime.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- deprecation.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- direct_url_helpers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- egg_link.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- entrypoints.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- filesystem.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- filetypes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- glibc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hashes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- logging.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- misc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- packaging.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- retry.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- subprocess.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- temp_dir.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- unpacking.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- urls.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- virtualenv.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- wheel.cpython-311.pyc
|   |   |   |   |   |   +-- vcs/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- bazaar.py
|   |   |   |   |   |   |   +-- git.py
|   |   |   |   |   |   |   +-- mercurial.py
|   |   |   |   |   |   |   +-- subversion.py
|   |   |   |   |   |   |   +-- versioncontrol.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- bazaar.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- git.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- mercurial.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- subversion.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- versioncontrol.cpython-311.pyc
|   |   |   |   |   +-- _vendor/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- README.rst
|   |   |   |   |   |   +-- vendor.txt
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- cachecontrol/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _cmd.py
|   |   |   |   |   |   |   +-- adapter.py
|   |   |   |   |   |   |   +-- cache.py
|   |   |   |   |   |   |   +-- controller.py
|   |   |   |   |   |   |   +-- filewrapper.py
|   |   |   |   |   |   |   +-- heuristics.py
|   |   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- serialize.py
|   |   |   |   |   |   |   +-- wrapper.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _cmd.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- adapter.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- cache.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- controller.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- filewrapper.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- heuristics.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- serialize.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- wrapper.cpython-311.pyc
|   |   |   |   |   |   |   +-- caches/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- file_cache.py
|   |   |   |   |   |   |   |   +-- redis_cache.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- file_cache.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- redis_cache.cpython-311.pyc
|   |   |   |   |   |   +-- certifi/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __main__.py
|   |   |   |   |   |   |   +-- cacert.pem
|   |   |   |   |   |   |   +-- core.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- core.cpython-311.pyc
|   |   |   |   |   |   +-- dependency_groups/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __main__.py
|   |   |   |   |   |   |   +-- _implementation.py
|   |   |   |   |   |   |   +-- _lint_dependency_groups.py
|   |   |   |   |   |   |   +-- _pip_wrapper.py
|   |   |   |   |   |   |   +-- _toml_compat.py
|   |   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _implementation.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _lint_dependency_groups.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _pip_wrapper.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _toml_compat.cpython-311.pyc
|   |   |   |   |   |   +-- distlib/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- compat.py
|   |   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   |   |   +-- resources.py
|   |   |   |   |   |   |   +-- scripts.py
|   |   |   |   |   |   |   +-- t32.exe
|   |   |   |   |   |   |   +-- t64.exe
|   |   |   |   |   |   |   +-- t64-arm.exe
|   |   |   |   |   |   |   +-- util.py
|   |   |   |   |   |   |   +-- w32.exe
|   |   |   |   |   |   |   +-- w64.exe
|   |   |   |   |   |   |   +-- w64-arm.exe
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- compat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- resources.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- scripts.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- util.cpython-311.pyc
|   |   |   |   |   |   +-- distro/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __main__.py
|   |   |   |   |   |   |   +-- distro.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- distro.cpython-311.pyc
|   |   |   |   |   |   +-- idna/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- codec.py
|   |   |   |   |   |   |   +-- compat.py
|   |   |   |   |   |   |   +-- core.py
|   |   |   |   |   |   |   +-- idnadata.py
|   |   |   |   |   |   |   +-- intranges.py
|   |   |   |   |   |   |   +-- LICENSE.md
|   |   |   |   |   |   |   +-- package_data.py
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- uts46data.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- codec.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- compat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- core.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- idnadata.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- intranges.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- package_data.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- uts46data.cpython-311.pyc
|   |   |   |   |   |   +-- msgpack/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- COPYING
|   |   |   |   |   |   |   +-- exceptions.py
|   |   |   |   |   |   |   +-- ext.py
|   |   |   |   |   |   |   +-- fallback.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- ext.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- fallback.cpython-311.pyc
|   |   |   |   |   |   +-- packaging/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _elffile.py
|   |   |   |   |   |   |   +-- _manylinux.py
|   |   |   |   |   |   |   +-- _musllinux.py
|   |   |   |   |   |   |   +-- _parser.py
|   |   |   |   |   |   |   +-- _structures.py
|   |   |   |   |   |   |   +-- _tokenizer.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- LICENSE.APACHE
|   |   |   |   |   |   |   +-- LICENSE.BSD
|   |   |   |   |   |   |   +-- markers.py
|   |   |   |   |   |   |   +-- metadata.py
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- requirements.py
|   |   |   |   |   |   |   +-- specifiers.py
|   |   |   |   |   |   |   +-- tags.py
|   |   |   |   |   |   |   +-- utils.py
|   |   |   |   |   |   |   +-- version.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _elffile.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _manylinux.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _musllinux.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _parser.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _structures.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _tokenizer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- markers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- metadata.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- requirements.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- specifiers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- tags.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- version.cpython-311.pyc
|   |   |   |   |   |   |   +-- licenses/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- _spdx.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- _spdx.cpython-311.pyc
|   |   |   |   |   |   +-- pkg_resources/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- platformdirs/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __main__.py
|   |   |   |   |   |   |   +-- android.py
|   |   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- macos.py
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- unix.py
|   |   |   |   |   |   |   +-- version.py
|   |   |   |   |   |   |   +-- windows.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- android.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- macos.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- unix.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- version.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- windows.cpython-311.pyc
|   |   |   |   |   |   +-- pygments/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __main__.py
|   |   |   |   |   |   |   +-- console.py
|   |   |   |   |   |   |   +-- filter.py
|   |   |   |   |   |   |   +-- formatter.py
|   |   |   |   |   |   |   +-- lexer.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- modeline.py
|   |   |   |   |   |   |   +-- plugin.py
|   |   |   |   |   |   |   +-- regexopt.py
|   |   |   |   |   |   |   +-- scanner.py
|   |   |   |   |   |   |   +-- sphinxext.py
|   |   |   |   |   |   |   +-- style.py
|   |   |   |   |   |   |   +-- token.py
|   |   |   |   |   |   |   +-- unistring.py
|   |   |   |   |   |   |   +-- util.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- console.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- filter.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- formatter.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- lexer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- modeline.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- plugin.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- regexopt.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- scanner.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- sphinxext.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- style.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- token.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- unistring.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- util.cpython-311.pyc
|   |   |   |   |   |   |   +-- filters/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- formatters/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- _mapping.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- _mapping.cpython-311.pyc
|   |   |   |   |   |   |   +-- lexers/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- _mapping.py
|   |   |   |   |   |   |   |   +-- python.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- _mapping.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- python.cpython-311.pyc
|   |   |   |   |   |   |   +-- styles/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- _mapping.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- _mapping.cpython-311.pyc
|   |   |   |   |   |   +-- pyproject_hooks/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _impl.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _impl.cpython-311.pyc
|   |   |   |   |   |   |   +-- _in_process/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- _in_process.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- _in_process.cpython-311.pyc
|   |   |   |   |   |   +-- requests/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __version__.py
|   |   |   |   |   |   |   +-- _internal_utils.py
|   |   |   |   |   |   |   +-- adapters.py
|   |   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   |   +-- auth.py
|   |   |   |   |   |   |   +-- certs.py
|   |   |   |   |   |   |   +-- compat.py
|   |   |   |   |   |   |   +-- cookies.py
|   |   |   |   |   |   |   +-- exceptions.py
|   |   |   |   |   |   |   +-- help.py
|   |   |   |   |   |   |   +-- hooks.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- models.py
|   |   |   |   |   |   |   +-- packages.py
|   |   |   |   |   |   |   +-- sessions.py
|   |   |   |   |   |   |   +-- status_codes.py
|   |   |   |   |   |   |   +-- structures.py
|   |   |   |   |   |   |   +-- utils.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- __version__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _internal_utils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- adapters.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- auth.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- certs.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- compat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- cookies.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- help.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hooks.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- models.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- packages.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- sessions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- status_codes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- structures.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   +-- resolvelib/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- providers.py
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- reporters.py
|   |   |   |   |   |   |   +-- structs.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- providers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- reporters.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- structs.cpython-311.pyc
|   |   |   |   |   |   |   +-- resolvers/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- abstract.py
|   |   |   |   |   |   |   |   +-- criterion.py
|   |   |   |   |   |   |   |   +-- exceptions.py
|   |   |   |   |   |   |   |   +-- resolution.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- abstract.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- criterion.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- resolution.cpython-311.pyc
|   |   |   |   |   |   +-- rich/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __main__.py
|   |   |   |   |   |   |   +-- _cell_widths.py
|   |   |   |   |   |   |   +-- _emoji_codes.py
|   |   |   |   |   |   |   +-- _emoji_replace.py
|   |   |   |   |   |   |   +-- _export_format.py
|   |   |   |   |   |   |   +-- _extension.py
|   |   |   |   |   |   |   +-- _fileno.py
|   |   |   |   |   |   |   +-- _inspect.py
|   |   |   |   |   |   |   +-- _log_render.py
|   |   |   |   |   |   |   +-- _loop.py
|   |   |   |   |   |   |   +-- _null_file.py
|   |   |   |   |   |   |   +-- _palettes.py
|   |   |   |   |   |   |   +-- _pick.py
|   |   |   |   |   |   |   +-- _ratio.py
|   |   |   |   |   |   |   +-- _spinners.py
|   |   |   |   |   |   |   +-- _stack.py
|   |   |   |   |   |   |   +-- _timer.py
|   |   |   |   |   |   |   +-- _win32_console.py
|   |   |   |   |   |   |   +-- _windows.py
|   |   |   |   |   |   |   +-- _windows_renderer.py
|   |   |   |   |   |   |   +-- _wrap.py
|   |   |   |   |   |   |   +-- abc.py
|   |   |   |   |   |   |   +-- align.py
|   |   |   |   |   |   |   +-- ansi.py
|   |   |   |   |   |   |   +-- bar.py
|   |   |   |   |   |   |   +-- box.py
|   |   |   |   |   |   |   +-- cells.py
|   |   |   |   |   |   |   +-- color.py
|   |   |   |   |   |   |   +-- color_triplet.py
|   |   |   |   |   |   |   +-- columns.py
|   |   |   |   |   |   |   +-- console.py
|   |   |   |   |   |   |   +-- constrain.py
|   |   |   |   |   |   |   +-- containers.py
|   |   |   |   |   |   |   +-- control.py
|   |   |   |   |   |   |   +-- default_styles.py
|   |   |   |   |   |   |   +-- diagnose.py
|   |   |   |   |   |   |   +-- emoji.py
|   |   |   |   |   |   |   +-- errors.py
|   |   |   |   |   |   |   +-- file_proxy.py
|   |   |   |   |   |   |   +-- filesize.py
|   |   |   |   |   |   |   +-- highlighter.py
|   |   |   |   |   |   |   +-- json.py
|   |   |   |   |   |   |   +-- jupyter.py
|   |   |   |   |   |   |   +-- layout.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- live.py
|   |   |   |   |   |   |   +-- live_render.py
|   |   |   |   |   |   |   +-- logging.py
|   |   |   |   |   |   |   +-- markup.py
|   |   |   |   |   |   |   +-- measure.py
|   |   |   |   |   |   |   +-- padding.py
|   |   |   |   |   |   |   +-- pager.py
|   |   |   |   |   |   |   +-- palette.py
|   |   |   |   |   |   |   +-- panel.py
|   |   |   |   |   |   |   +-- pretty.py
|   |   |   |   |   |   |   +-- progress.py
|   |   |   |   |   |   |   +-- progress_bar.py
|   |   |   |   |   |   |   +-- prompt.py
|   |   |   |   |   |   |   +-- protocol.py
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- region.py
|   |   |   |   |   |   |   +-- repr.py
|   |   |   |   |   |   |   +-- rule.py
|   |   |   |   |   |   |   +-- scope.py
|   |   |   |   |   |   |   +-- screen.py
|   |   |   |   |   |   |   +-- segment.py
|   |   |   |   |   |   |   +-- spinner.py
|   |   |   |   |   |   |   +-- status.py
|   |   |   |   |   |   |   +-- style.py
|   |   |   |   |   |   |   +-- styled.py
|   |   |   |   |   |   |   +-- syntax.py
|   |   |   |   |   |   |   +-- table.py
|   |   |   |   |   |   |   +-- terminal_theme.py
|   |   |   |   |   |   |   +-- text.py
|   |   |   |   |   |   |   +-- theme.py
|   |   |   |   |   |   |   +-- themes.py
|   |   |   |   |   |   |   +-- traceback.py
|   |   |   |   |   |   |   +-- tree.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _cell_widths.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _emoji_codes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _emoji_replace.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _export_format.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _extension.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _fileno.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _inspect.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _log_render.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _loop.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _null_file.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _palettes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _pick.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _ratio.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _spinners.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _stack.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _timer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _win32_console.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _windows.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _windows_renderer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _wrap.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- abc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- align.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- ansi.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- bar.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- box.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- cells.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- color.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- color_triplet.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- columns.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- console.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- constrain.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- containers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- control.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- default_styles.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- diagnose.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- emoji.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- errors.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- file_proxy.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- filesize.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- highlighter.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- json.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- jupyter.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- layout.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- live.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- live_render.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- logging.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- markup.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- measure.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- padding.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pager.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- palette.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- panel.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pretty.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- progress.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- progress_bar.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- prompt.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- protocol.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- region.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- repr.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- rule.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- scope.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- screen.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- segment.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- spinner.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- status.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- style.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- styled.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- syntax.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- table.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- terminal_theme.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- text.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- theme.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- themes.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- traceback.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- tree.cpython-311.pyc
|   |   |   |   |   |   +-- tomli/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _parser.py
|   |   |   |   |   |   |   +-- _re.py
|   |   |   |   |   |   |   +-- _types.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _parser.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _re.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _types.cpython-311.pyc
|   |   |   |   |   |   +-- tomli_w/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _writer.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _writer.cpython-311.pyc
|   |   |   |   |   |   +-- truststore/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _api.py
|   |   |   |   |   |   |   +-- _macos.py
|   |   |   |   |   |   |   +-- _openssl.py
|   |   |   |   |   |   |   +-- _ssl_constants.py
|   |   |   |   |   |   |   +-- _windows.py
|   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   +-- py.typed
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _api.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _macos.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _openssl.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _ssl_constants.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _windows.cpython-311.pyc
|   |   |   |   |   |   +-- urllib3/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _collections.py
|   |   |   |   |   |   |   +-- _version.py
|   |   |   |   |   |   |   +-- connection.py
|   |   |   |   |   |   |   +-- connectionpool.py
|   |   |   |   |   |   |   +-- exceptions.py
|   |   |   |   |   |   |   +-- fields.py
|   |   |   |   |   |   |   +-- filepost.py
|   |   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   |   |   +-- poolmanager.py
|   |   |   |   |   |   |   +-- request.py
|   |   |   |   |   |   |   +-- response.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _collections.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _version.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- connection.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- connectionpool.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- fields.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- filepost.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- poolmanager.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- request.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- response.cpython-311.pyc
|   |   |   |   |   |   |   +-- contrib/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- _appengine_environ.py
|   |   |   |   |   |   |   |   +-- appengine.py
|   |   |   |   |   |   |   |   +-- ntlmpool.py
|   |   |   |   |   |   |   |   +-- pyopenssl.py
|   |   |   |   |   |   |   |   +-- securetransport.py
|   |   |   |   |   |   |   |   +-- socks.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- _appengine_environ.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- appengine.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- ntlmpool.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- pyopenssl.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- securetransport.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- socks.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _securetransport/
|   |   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   |   +-- bindings.py
|   |   |   |   |   |   |   |   |   +-- low_level.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- bindings.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- low_level.cpython-311.pyc
|   |   |   |   |   |   |   +-- packages/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- six.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- six.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- backports/
|   |   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   |   +-- makefile.py
|   |   |   |   |   |   |   |   |   +-- weakref_finalize.py
|   |   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- makefile.cpython-311.pyc
|   |   |   |   |   |   |   |   |   |   +-- weakref_finalize.cpython-311.pyc
|   |   |   |   |   |   |   +-- util/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- connection.py
|   |   |   |   |   |   |   |   +-- proxy.py
|   |   |   |   |   |   |   |   +-- queue.py
|   |   |   |   |   |   |   |   +-- request.py
|   |   |   |   |   |   |   |   +-- response.py
|   |   |   |   |   |   |   |   +-- retry.py
|   |   |   |   |   |   |   |   +-- ssl_.py
|   |   |   |   |   |   |   |   +-- ssl_match_hostname.py
|   |   |   |   |   |   |   |   +-- ssltransport.py
|   |   |   |   |   |   |   |   +-- timeout.py
|   |   |   |   |   |   |   |   +-- url.py
|   |   |   |   |   |   |   |   +-- wait.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- connection.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- proxy.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- queue.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- request.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- response.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- retry.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- ssl_.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- ssl_match_hostname.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- ssltransport.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- timeout.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- url.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- wait.cpython-311.pyc
|   |   |   |   +-- pip-25.3.dist-info/
|   |   |   |   |   +-- entry_points.txt
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- REQUESTED
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- AUTHORS.txt
|   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   |   +-- src/
|   |   |   |   |   |   |   +-- pip/
|   |   |   |   |   |   |   |   +-- _vendor/
|   |   |   |   |   |   |   |   |   +-- cachecontrol/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   |   |   |   |   +-- certifi/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   +-- dependency_groups/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   |   |   |   |   +-- distlib/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   |   |   |   |   +-- distro/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   +-- idna/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE.md
|   |   |   |   |   |   |   |   |   +-- msgpack/
|   |   |   |   |   |   |   |   |   |   +-- COPYING
|   |   |   |   |   |   |   |   |   +-- packaging/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   |   +-- LICENSE.APACHE
|   |   |   |   |   |   |   |   |   |   +-- LICENSE.BSD
|   |   |   |   |   |   |   |   |   +-- pkg_resources/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   +-- platformdirs/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   +-- pygments/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   +-- pyproject_hooks/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   +-- requests/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   +-- resolvelib/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   +-- rich/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   +-- tomli/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   +-- tomli_w/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   +-- truststore/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   |   |   |   +-- urllib3/
|   |   |   |   |   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   +-- pkg_resources/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- _vendor/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- appdirs.py
|   |   |   |   |   |   +-- zipp.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- appdirs.cpython-311.pyc
|   |   |   |   |   |   |   +-- zipp.cpython-311.pyc
|   |   |   |   |   |   +-- importlib_resources/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _adapters.py
|   |   |   |   |   |   |   +-- _common.py
|   |   |   |   |   |   |   +-- _compat.py
|   |   |   |   |   |   |   +-- _itertools.py
|   |   |   |   |   |   |   +-- _legacy.py
|   |   |   |   |   |   |   +-- abc.py
|   |   |   |   |   |   |   +-- readers.py
|   |   |   |   |   |   |   +-- simple.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _adapters.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _compat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _itertools.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _legacy.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- abc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- readers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- simple.cpython-311.pyc
|   |   |   |   |   |   +-- jaraco/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- context.py
|   |   |   |   |   |   |   +-- functools.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- context.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- functools.cpython-311.pyc
|   |   |   |   |   |   |   +-- text/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- more_itertools/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- more.py
|   |   |   |   |   |   |   +-- recipes.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- more.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- recipes.cpython-311.pyc
|   |   |   |   |   |   +-- packaging/
|   |   |   |   |   |   |   +-- __about__.py
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _manylinux.py
|   |   |   |   |   |   |   +-- _musllinux.py
|   |   |   |   |   |   |   +-- _structures.py
|   |   |   |   |   |   |   +-- markers.py
|   |   |   |   |   |   |   +-- requirements.py
|   |   |   |   |   |   |   +-- specifiers.py
|   |   |   |   |   |   |   +-- tags.py
|   |   |   |   |   |   |   +-- utils.py
|   |   |   |   |   |   |   +-- version.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __about__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _manylinux.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _musllinux.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _structures.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- markers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- requirements.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- specifiers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- tags.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- version.cpython-311.pyc
|   |   |   |   |   |   +-- pyparsing/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- actions.py
|   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   +-- core.py
|   |   |   |   |   |   |   +-- exceptions.py
|   |   |   |   |   |   |   +-- helpers.py
|   |   |   |   |   |   |   +-- results.py
|   |   |   |   |   |   |   +-- testing.py
|   |   |   |   |   |   |   +-- unicode.py
|   |   |   |   |   |   |   +-- util.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- actions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- core.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- helpers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- results.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- testing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- unicode.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- util.cpython-311.pyc
|   |   |   |   |   |   |   +-- diagram/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- extern/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   +-- psutil/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _common.py
|   |   |   |   |   +-- _psaix.py
|   |   |   |   |   +-- _psbsd.py
|   |   |   |   |   +-- _pslinux.py
|   |   |   |   |   +-- _psosx.py
|   |   |   |   |   +-- _psposix.py
|   |   |   |   |   +-- _pssunos.py
|   |   |   |   |   +-- _psutil_windows.pyd
|   |   |   |   |   +-- _pswindows.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _common.cpython-311.pyc
|   |   |   |   |   |   +-- _psaix.cpython-311.pyc
|   |   |   |   |   |   +-- _psbsd.cpython-311.pyc
|   |   |   |   |   |   +-- _pslinux.cpython-311.pyc
|   |   |   |   |   |   +-- _psosx.cpython-311.pyc
|   |   |   |   |   |   +-- _psposix.cpython-311.pyc
|   |   |   |   |   |   +-- _pssunos.cpython-311.pyc
|   |   |   |   |   |   +-- _pswindows.cpython-311.pyc
|   |   |   |   |   +-- tests/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __main__.py
|   |   |   |   |   |   +-- test_aix.py
|   |   |   |   |   |   +-- test_bsd.py
|   |   |   |   |   |   +-- test_connections.py
|   |   |   |   |   |   +-- test_contracts.py
|   |   |   |   |   |   +-- test_linux.py
|   |   |   |   |   |   +-- test_memleaks.py
|   |   |   |   |   |   +-- test_misc.py
|   |   |   |   |   |   +-- test_osx.py
|   |   |   |   |   |   +-- test_posix.py
|   |   |   |   |   |   +-- test_process.py
|   |   |   |   |   |   +-- test_process_all.py
|   |   |   |   |   |   +-- test_scripts.py
|   |   |   |   |   |   +-- test_sudo.py
|   |   |   |   |   |   +-- test_sunos.py
|   |   |   |   |   |   +-- test_system.py
|   |   |   |   |   |   +-- test_testutils.py
|   |   |   |   |   |   +-- test_unicode.py
|   |   |   |   |   |   +-- test_windows.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_aix.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_bsd.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_connections.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_contracts.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_linux.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_memleaks.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_misc.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_osx.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_posix.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_process.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_process_all.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_scripts.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_sudo.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_sunos.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_system.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_testutils.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_unicode.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_windows.cpython-311.pyc
|   |   |   |   +-- psutil-7.1.3.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- REQUESTED
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- PyInstaller/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- __main__.py
|   |   |   |   |   +-- _recursion_too_deep_message.py
|   |   |   |   |   +-- _shared_with_waf.py
|   |   |   |   |   +-- compat.py
|   |   |   |   |   +-- config.py
|   |   |   |   |   +-- configure.py
|   |   |   |   |   +-- exceptions.py
|   |   |   |   |   +-- log.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   +-- _recursion_too_deep_message.cpython-311.pyc
|   |   |   |   |   |   +-- _shared_with_waf.cpython-311.pyc
|   |   |   |   |   |   +-- compat.cpython-311.pyc
|   |   |   |   |   |   +-- config.cpython-311.pyc
|   |   |   |   |   |   +-- configure.cpython-311.pyc
|   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   +-- log.cpython-311.pyc
|   |   |   |   |   +-- archive/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- pyz_crypto.py
|   |   |   |   |   |   +-- readers.py
|   |   |   |   |   |   +-- writers.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyz_crypto.cpython-311.pyc
|   |   |   |   |   |   |   +-- readers.cpython-311.pyc
|   |   |   |   |   |   |   +-- writers.cpython-311.pyc
|   |   |   |   |   +-- bootloader/
|   |   |   |   |   |   +-- images/
|   |   |   |   |   |   |   +-- icon-console.ico
|   |   |   |   |   |   |   +-- icon-windowed.ico
|   |   |   |   |   |   +-- Windows-64bit-intel/
|   |   |   |   |   |   |   +-- run.exe
|   |   |   |   |   |   |   +-- run_d.exe
|   |   |   |   |   |   |   +-- runw.exe
|   |   |   |   |   |   |   +-- runw_d.exe
|   |   |   |   |   +-- building/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   +-- build_main.py
|   |   |   |   |   |   +-- datastruct.py
|   |   |   |   |   |   +-- icon.py
|   |   |   |   |   |   +-- makespec.py
|   |   |   |   |   |   +-- osx.py
|   |   |   |   |   |   +-- splash.py
|   |   |   |   |   |   +-- splash_templates.py
|   |   |   |   |   |   +-- templates.py
|   |   |   |   |   |   +-- utils.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   |   +-- build_main.cpython-311.pyc
|   |   |   |   |   |   |   +-- datastruct.cpython-311.pyc
|   |   |   |   |   |   |   +-- icon.cpython-311.pyc
|   |   |   |   |   |   |   +-- makespec.cpython-311.pyc
|   |   |   |   |   |   |   +-- osx.cpython-311.pyc
|   |   |   |   |   |   |   +-- splash.cpython-311.pyc
|   |   |   |   |   |   |   +-- splash_templates.cpython-311.pyc
|   |   |   |   |   |   |   +-- templates.cpython-311.pyc
|   |   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   +-- depend/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- analysis.py
|   |   |   |   |   |   +-- bindepend.py
|   |   |   |   |   |   +-- bytecode.py
|   |   |   |   |   |   +-- dylib.py
|   |   |   |   |   |   +-- imphook.py
|   |   |   |   |   |   +-- imphookapi.py
|   |   |   |   |   |   +-- utils.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- analysis.cpython-311.pyc
|   |   |   |   |   |   |   +-- bindepend.cpython-311.pyc
|   |   |   |   |   |   |   +-- bytecode.cpython-311.pyc
|   |   |   |   |   |   |   +-- dylib.cpython-311.pyc
|   |   |   |   |   |   |   +-- imphook.cpython-311.pyc
|   |   |   |   |   |   |   +-- imphookapi.cpython-311.pyc
|   |   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   +-- fake-modules/
|   |   |   |   |   |   +-- pyi_splash.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- pyi_splash.cpython-311.pyc
|   |   |   |   |   |   +-- _pyi_rth_utils/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _win32.py
|   |   |   |   |   |   |   +-- qt.py
|   |   |   |   |   |   |   +-- tempfile.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _win32.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- qt.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- tempfile.cpython-311.pyc
|   |   |   |   |   +-- hooks/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- hook-_ctypes.py
|   |   |   |   |   |   +-- hook-_osx_support.py
|   |   |   |   |   |   +-- hook-_pyi_rth_utils.py
|   |   |   |   |   |   +-- hook-_tkinter.py
|   |   |   |   |   |   +-- hook-babel.py
|   |   |   |   |   |   +-- hook-difflib.py
|   |   |   |   |   |   +-- hook-distutils.command.check.py
|   |   |   |   |   |   +-- hook-distutils.py
|   |   |   |   |   |   +-- hook-distutils.util.py
|   |   |   |   |   |   +-- hook-django.contrib.sessions.py
|   |   |   |   |   |   +-- hook-django.core.cache.py
|   |   |   |   |   |   +-- hook-django.core.mail.py
|   |   |   |   |   |   +-- hook-django.core.management.py
|   |   |   |   |   |   +-- hook-django.db.backends.mysql.base.py
|   |   |   |   |   |   +-- hook-django.db.backends.oracle.base.py
|   |   |   |   |   |   +-- hook-django.db.backends.py
|   |   |   |   |   |   +-- hook-django.py
|   |   |   |   |   |   +-- hook-django.template.loaders.py
|   |   |   |   |   |   +-- hook-encodings.py
|   |   |   |   |   |   +-- hook-gevent.py
|   |   |   |   |   |   +-- hook-gi.py
|   |   |   |   |   |   +-- hook-gi.repository.Adw.py
|   |   |   |   |   |   +-- hook-gi.repository.AppIndicator3.py
|   |   |   |   |   |   +-- hook-gi.repository.Atk.py
|   |   |   |   |   |   +-- hook-gi.repository.AyatanaAppIndicator3.py
|   |   |   |   |   |   +-- hook-gi.repository.cairo.py
|   |   |   |   |   |   +-- hook-gi.repository.Champlain.py
|   |   |   |   |   |   +-- hook-gi.repository.Clutter.py
|   |   |   |   |   |   +-- hook-gi.repository.DBus.py
|   |   |   |   |   |   +-- hook-gi.repository.freetype2.py
|   |   |   |   |   |   +-- hook-gi.repository.Gdk.py
|   |   |   |   |   |   +-- hook-gi.repository.GdkPixbuf.py
|   |   |   |   |   |   +-- hook-gi.repository.Gio.py
|   |   |   |   |   |   +-- hook-gi.repository.GIRepository.py
|   |   |   |   |   |   +-- hook-gi.repository.GLib.py
|   |   |   |   |   |   +-- hook-gi.repository.GModule.py
|   |   |   |   |   |   +-- hook-gi.repository.GObject.py
|   |   |   |   |   |   +-- hook-gi.repository.Graphene.py
|   |   |   |   |   |   +-- hook-gi.repository.Gsk.py
|   |   |   |   |   |   +-- hook-gi.repository.Gst.py
|   |   |   |   |   |   +-- hook-gi.repository.GstAllocators.py
|   |   |   |   |   |   +-- hook-gi.repository.GstApp.py
|   |   |   |   |   |   +-- hook-gi.repository.GstAudio.py
|   |   |   |   |   |   +-- hook-gi.repository.GstBadAudio.py
|   |   |   |   |   |   +-- hook-gi.repository.GstBase.py
|   |   |   |   |   |   +-- hook-gi.repository.GstCheck.py
|   |   |   |   |   |   +-- hook-gi.repository.GstCodecs.py
|   |   |   |   |   |   +-- hook-gi.repository.GstController.py
|   |   |   |   |   |   +-- hook-gi.repository.GstGL.py
|   |   |   |   |   |   +-- hook-gi.repository.GstGLEGL.py
|   |   |   |   |   |   +-- hook-gi.repository.GstGLWayland.py
|   |   |   |   |   |   +-- hook-gi.repository.GstGLX11.py
|   |   |   |   |   |   +-- hook-gi.repository.GstInsertBin.py
|   |   |   |   |   |   +-- hook-gi.repository.GstMpegts.py
|   |   |   |   |   |   +-- hook-gi.repository.GstNet.py
|   |   |   |   |   |   +-- hook-gi.repository.GstPbutils.py
|   |   |   |   |   |   +-- hook-gi.repository.GstPlay.py
|   |   |   |   |   |   +-- hook-gi.repository.GstPlayer.py
|   |   |   |   |   |   +-- hook-gi.repository.GstRtp.py
|   |   |   |   |   |   +-- hook-gi.repository.GstRtsp.py
|   |   |   |   |   |   +-- hook-gi.repository.GstRtspServer.py
|   |   |   |   |   |   +-- hook-gi.repository.GstSdp.py
|   |   |   |   |   |   +-- hook-gi.repository.GstTag.py
|   |   |   |   |   |   +-- hook-gi.repository.GstTranscoder.py
|   |   |   |   |   |   +-- hook-gi.repository.GstVideo.py
|   |   |   |   |   |   +-- hook-gi.repository.GstVulkan.py
|   |   |   |   |   |   +-- hook-gi.repository.GstVulkanWayland.py
|   |   |   |   |   |   +-- hook-gi.repository.GstVulkanXCB.py
|   |   |   |   |   |   +-- hook-gi.repository.GstWebRTC.py
|   |   |   |   |   |   +-- hook-gi.repository.Gtk.py
|   |   |   |   |   |   +-- hook-gi.repository.GtkChamplain.py
|   |   |   |   |   |   +-- hook-gi.repository.GtkClutter.py
|   |   |   |   |   |   +-- hook-gi.repository.GtkosxApplication.py
|   |   |   |   |   |   +-- hook-gi.repository.GtkSource.py
|   |   |   |   |   |   +-- hook-gi.repository.HarfBuzz.py
|   |   |   |   |   |   +-- hook-gi.repository.OsmGpsMap.py
|   |   |   |   |   |   +-- hook-gi.repository.Pango.py
|   |   |   |   |   |   +-- hook-gi.repository.PangoCairo.py
|   |   |   |   |   |   +-- hook-gi.repository.Rsvg.py
|   |   |   |   |   |   +-- hook-gi.repository.xlib.py
|   |   |   |   |   |   +-- hook-heapq.py
|   |   |   |   |   |   +-- hook-idlelib.py
|   |   |   |   |   |   +-- hook-importlib_metadata.py
|   |   |   |   |   |   +-- hook-importlib_resources.py
|   |   |   |   |   |   +-- hook-keyring.py
|   |   |   |   |   |   +-- hook-kivy.py
|   |   |   |   |   |   +-- hook-lib2to3.py
|   |   |   |   |   |   +-- hook-matplotlib.backend_bases.py
|   |   |   |   |   |   +-- hook-matplotlib.backends.backend_qtagg.py
|   |   |   |   |   |   +-- hook-matplotlib.backends.backend_qtcairo.py
|   |   |   |   |   |   +-- hook-matplotlib.backends.py
|   |   |   |   |   |   +-- hook-matplotlib.backends.qt_compat.py
|   |   |   |   |   |   +-- hook-matplotlib.numerix.py
|   |   |   |   |   |   +-- hook-matplotlib.py
|   |   |   |   |   |   +-- hook-matplotlib.pyplot.py
|   |   |   |   |   |   +-- hook-multiprocessing.util.py
|   |   |   |   |   |   +-- hook-numpy.py
|   |   |   |   |   |   +-- hook-pandas.io.clipboard.py
|   |   |   |   |   |   +-- hook-pandas.io.formats.style.py
|   |   |   |   |   |   +-- hook-pandas.plotting.py
|   |   |   |   |   |   +-- hook-pandas.py
|   |   |   |   |   |   +-- hook-pickle.py
|   |   |   |   |   |   +-- hook-PIL.Image.py
|   |   |   |   |   |   +-- hook-PIL.ImageFilter.py
|   |   |   |   |   |   +-- hook-PIL.py
|   |   |   |   |   |   +-- hook-PIL.SpiderImagePlugin.py
|   |   |   |   |   |   +-- hook-pkg_resources.py
|   |   |   |   |   |   +-- hook-platform.py
|   |   |   |   |   |   +-- hook-pygments.py
|   |   |   |   |   |   +-- hook-PyQt5.py
|   |   |   |   |   |   +-- hook-PyQt5.QAxContainer.py
|   |   |   |   |   |   +-- hook-PyQt5.Qsci.py
|   |   |   |   |   |   +-- hook-PyQt5.Qt.py
|   |   |   |   |   |   +-- hook-PyQt5.Qt3DAnimation.py
|   |   |   |   |   |   +-- hook-PyQt5.Qt3DCore.py
|   |   |   |   |   |   +-- hook-PyQt5.Qt3DExtras.py
|   |   |   |   |   |   +-- hook-PyQt5.Qt3DInput.py
|   |   |   |   |   |   +-- hook-PyQt5.Qt3DLogic.py
|   |   |   |   |   |   +-- hook-PyQt5.Qt3DRender.py
|   |   |   |   |   |   +-- hook-PyQt5.QtBluetooth.py
|   |   |   |   |   |   +-- hook-PyQt5.QtChart.py
|   |   |   |   |   |   +-- hook-PyQt5.QtCore.py
|   |   |   |   |   |   +-- hook-PyQt5.QtDataVisualization.py
|   |   |   |   |   |   +-- hook-PyQt5.QtDBus.py
|   |   |   |   |   |   +-- hook-PyQt5.QtDesigner.py
|   |   |   |   |   |   +-- hook-PyQt5.QtGui.py
|   |   |   |   |   |   +-- hook-PyQt5.QtHelp.py
|   |   |   |   |   |   +-- hook-PyQt5.QtLocation.py
|   |   |   |   |   |   +-- hook-PyQt5.QtMacExtras.py
|   |   |   |   |   |   +-- hook-PyQt5.QtMultimedia.py
|   |   |   |   |   |   +-- hook-PyQt5.QtMultimediaWidgets.py
|   |   |   |   |   |   +-- hook-PyQt5.QtNetwork.py
|   |   |   |   |   |   +-- hook-PyQt5.QtNetworkAuth.py
|   |   |   |   |   |   +-- hook-PyQt5.QtNfc.py
|   |   |   |   |   |   +-- hook-PyQt5.QtOpenGL.py
|   |   |   |   |   |   +-- hook-PyQt5.QtPositioning.py
|   |   |   |   |   |   +-- hook-PyQt5.QtPrintSupport.py
|   |   |   |   |   |   +-- hook-PyQt5.QtPurchasing.py
|   |   |   |   |   |   +-- hook-PyQt5.QtQml.py
|   |   |   |   |   |   +-- hook-PyQt5.QtQuick.py
|   |   |   |   |   |   +-- hook-PyQt5.QtQuick3D.py
|   |   |   |   |   |   +-- hook-PyQt5.QtQuickWidgets.py
|   |   |   |   |   |   +-- hook-PyQt5.QtRemoteObjects.py
|   |   |   |   |   |   +-- hook-PyQt5.QtScript.py
|   |   |   |   |   |   +-- hook-PyQt5.QtSensors.py
|   |   |   |   |   |   +-- hook-PyQt5.QtSerialPort.py
|   |   |   |   |   |   +-- hook-PyQt5.QtSql.py
|   |   |   |   |   |   +-- hook-PyQt5.QtSvg.py
|   |   |   |   |   |   +-- hook-PyQt5.QtTest.py
|   |   |   |   |   |   +-- hook-PyQt5.QtTextToSpeech.py
|   |   |   |   |   |   +-- hook-PyQt5.QtWebChannel.py
|   |   |   |   |   |   +-- hook-PyQt5.QtWebEngine.py
|   |   |   |   |   |   +-- hook-PyQt5.QtWebEngineCore.py
|   |   |   |   |   |   +-- hook-PyQt5.QtWebEngineWidgets.py
|   |   |   |   |   |   +-- hook-PyQt5.QtWebKit.py
|   |   |   |   |   |   +-- hook-PyQt5.QtWebKitWidgets.py
|   |   |   |   |   |   +-- hook-PyQt5.QtWebSockets.py
|   |   |   |   |   |   +-- hook-PyQt5.QtWidgets.py
|   |   |   |   |   |   +-- hook-PyQt5.QtWinExtras.py
|   |   |   |   |   |   +-- hook-PyQt5.QtX11Extras.py
|   |   |   |   |   |   +-- hook-PyQt5.QtXml.py
|   |   |   |   |   |   +-- hook-PyQt5.QtXmlPatterns.py
|   |   |   |   |   |   +-- hook-PyQt5.uic.py
|   |   |   |   |   |   +-- hook-PyQt6.py
|   |   |   |   |   |   +-- hook-PyQt6.QAxContainer.py
|   |   |   |   |   |   +-- hook-PyQt6.Qsci.py
|   |   |   |   |   |   +-- hook-PyQt6.Qt3DAnimation.py
|   |   |   |   |   |   +-- hook-PyQt6.Qt3DCore.py
|   |   |   |   |   |   +-- hook-PyQt6.Qt3DExtras.py
|   |   |   |   |   |   +-- hook-PyQt6.Qt3DInput.py
|   |   |   |   |   |   +-- hook-PyQt6.Qt3DLogic.py
|   |   |   |   |   |   +-- hook-PyQt6.Qt3DRender.py
|   |   |   |   |   |   +-- hook-PyQt6.QtBluetooth.py
|   |   |   |   |   |   +-- hook-PyQt6.QtCharts.py
|   |   |   |   |   |   +-- hook-PyQt6.QtCore.py
|   |   |   |   |   |   +-- hook-PyQt6.QtDataVisualization.py
|   |   |   |   |   |   +-- hook-PyQt6.QtDBus.py
|   |   |   |   |   |   +-- hook-PyQt6.QtDesigner.py
|   |   |   |   |   |   +-- hook-PyQt6.QtGraphs.py
|   |   |   |   |   |   +-- hook-PyQt6.QtGraphsWidgets.py
|   |   |   |   |   |   +-- hook-PyQt6.QtGui.py
|   |   |   |   |   |   +-- hook-PyQt6.QtHelp.py
|   |   |   |   |   |   +-- hook-PyQt6.QtMultimedia.py
|   |   |   |   |   |   +-- hook-PyQt6.QtMultimediaWidgets.py
|   |   |   |   |   |   +-- hook-PyQt6.QtNetwork.py
|   |   |   |   |   |   +-- hook-PyQt6.QtNetworkAuth.py
|   |   |   |   |   |   +-- hook-PyQt6.QtNfc.py
|   |   |   |   |   |   +-- hook-PyQt6.QtOpenGL.py
|   |   |   |   |   |   +-- hook-PyQt6.QtOpenGLWidgets.py
|   |   |   |   |   |   +-- hook-PyQt6.QtPdf.py
|   |   |   |   |   |   +-- hook-PyQt6.QtPdfWidgets.py
|   |   |   |   |   |   +-- hook-PyQt6.QtPositioning.py
|   |   |   |   |   |   +-- hook-PyQt6.QtPrintSupport.py
|   |   |   |   |   |   +-- hook-PyQt6.QtQml.py
|   |   |   |   |   |   +-- hook-PyQt6.QtQuick.py
|   |   |   |   |   |   +-- hook-PyQt6.QtQuick3D.py
|   |   |   |   |   |   +-- hook-PyQt6.QtQuickWidgets.py
|   |   |   |   |   |   +-- hook-PyQt6.QtRemoteObjects.py
|   |   |   |   |   |   +-- hook-PyQt6.QtSensors.py
|   |   |   |   |   |   +-- hook-PyQt6.QtSerialPort.py
|   |   |   |   |   |   +-- hook-PyQt6.QtSpatialAudio.py
|   |   |   |   |   |   +-- hook-PyQt6.QtSql.py
|   |   |   |   |   |   +-- hook-PyQt6.QtStateMachine.py
|   |   |   |   |   |   +-- hook-PyQt6.QtSvg.py
|   |   |   |   |   |   +-- hook-PyQt6.QtSvgWidgets.py
|   |   |   |   |   |   +-- hook-PyQt6.QtTest.py
|   |   |   |   |   |   +-- hook-PyQt6.QtTextToSpeech.py
|   |   |   |   |   |   +-- hook-PyQt6.QtWebChannel.py
|   |   |   |   |   |   +-- hook-PyQt6.QtWebEngineCore.py
|   |   |   |   |   |   +-- hook-PyQt6.QtWebEngineQuick.py
|   |   |   |   |   |   +-- hook-PyQt6.QtWebEngineWidgets.py
|   |   |   |   |   |   +-- hook-PyQt6.QtWebSockets.py
|   |   |   |   |   |   +-- hook-PyQt6.QtWidgets.py
|   |   |   |   |   |   +-- hook-PyQt6.QtXml.py
|   |   |   |   |   |   +-- hook-PyQt6.uic.py
|   |   |   |   |   |   +-- hook-PySide2.py
|   |   |   |   |   |   +-- hook-PySide2.Qt3DAnimation.py
|   |   |   |   |   |   +-- hook-PySide2.Qt3DCore.py
|   |   |   |   |   |   +-- hook-PySide2.Qt3DExtras.py
|   |   |   |   |   |   +-- hook-PySide2.Qt3DInput.py
|   |   |   |   |   |   +-- hook-PySide2.Qt3DLogic.py
|   |   |   |   |   |   +-- hook-PySide2.Qt3DRender.py
|   |   |   |   |   |   +-- hook-PySide2.QtAxContainer.py
|   |   |   |   |   |   +-- hook-PySide2.QtCharts.py
|   |   |   |   |   |   +-- hook-PySide2.QtConcurrent.py
|   |   |   |   |   |   +-- hook-PySide2.QtCore.py
|   |   |   |   |   |   +-- hook-PySide2.QtDataVisualization.py
|   |   |   |   |   |   +-- hook-PySide2.QtGui.py
|   |   |   |   |   |   +-- hook-PySide2.QtHelp.py
|   |   |   |   |   |   +-- hook-PySide2.QtLocation.py
|   |   |   |   |   |   +-- hook-PySide2.QtMacExtras.py
|   |   |   |   |   |   +-- hook-PySide2.QtMultimedia.py
|   |   |   |   |   |   +-- hook-PySide2.QtMultimediaWidgets.py
|   |   |   |   |   |   +-- hook-PySide2.QtNetwork.py
|   |   |   |   |   |   +-- hook-PySide2.QtOpenGL.py
|   |   |   |   |   |   +-- hook-PySide2.QtOpenGLFunctions.py
|   |   |   |   |   |   +-- hook-PySide2.QtPositioning.py
|   |   |   |   |   |   +-- hook-PySide2.QtPrintSupport.py
|   |   |   |   |   |   +-- hook-PySide2.QtQml.py
|   |   |   |   |   |   +-- hook-PySide2.QtQuick.py
|   |   |   |   |   |   +-- hook-PySide2.QtQuickControls2.py
|   |   |   |   |   |   +-- hook-PySide2.QtQuickWidgets.py
|   |   |   |   |   |   +-- hook-PySide2.QtRemoteObjects.py
|   |   |   |   |   |   +-- hook-PySide2.QtScript.py
|   |   |   |   |   |   +-- hook-PySide2.QtScriptTools.py
|   |   |   |   |   |   +-- hook-PySide2.QtScxml.py
|   |   |   |   |   |   +-- hook-PySide2.QtSensors.py
|   |   |   |   |   |   +-- hook-PySide2.QtSerialPort.py
|   |   |   |   |   |   +-- hook-PySide2.QtSql.py
|   |   |   |   |   |   +-- hook-PySide2.QtSvg.py
|   |   |   |   |   |   +-- hook-PySide2.QtTest.py
|   |   |   |   |   |   +-- hook-PySide2.QtTextToSpeech.py
|   |   |   |   |   |   +-- hook-PySide2.QtUiTools.py
|   |   |   |   |   |   +-- hook-PySide2.QtWebChannel.py
|   |   |   |   |   |   +-- hook-PySide2.QtWebEngine.py
|   |   |   |   |   |   +-- hook-PySide2.QtWebEngineCore.py
|   |   |   |   |   |   +-- hook-PySide2.QtWebEngineWidgets.py
|   |   |   |   |   |   +-- hook-PySide2.QtWebKit.py
|   |   |   |   |   |   +-- hook-PySide2.QtWebKitWidgets.py
|   |   |   |   |   |   +-- hook-PySide2.QtWebSockets.py
|   |   |   |   |   |   +-- hook-PySide2.QtWidgets.py
|   |   |   |   |   |   +-- hook-PySide2.QtWinExtras.py
|   |   |   |   |   |   +-- hook-PySide2.QtX11Extras.py
|   |   |   |   |   |   +-- hook-PySide2.QtXml.py
|   |   |   |   |   |   +-- hook-PySide2.QtXmlPatterns.py
|   |   |   |   |   |   +-- hook-PySide2.Qwt5.py
|   |   |   |   |   |   +-- hook-PySide6.py
|   |   |   |   |   |   +-- hook-PySide6.Qt3DAnimation.py
|   |   |   |   |   |   +-- hook-PySide6.Qt3DCore.py
|   |   |   |   |   |   +-- hook-PySide6.Qt3DExtras.py
|   |   |   |   |   |   +-- hook-PySide6.Qt3DInput.py
|   |   |   |   |   |   +-- hook-PySide6.Qt3DLogic.py
|   |   |   |   |   |   +-- hook-PySide6.Qt3DRender.py
|   |   |   |   |   |   +-- hook-PySide6.QtAxContainer.py
|   |   |   |   |   |   +-- hook-PySide6.QtBluetooth.py
|   |   |   |   |   |   +-- hook-PySide6.QtCharts.py
|   |   |   |   |   |   +-- hook-PySide6.QtConcurrent.py
|   |   |   |   |   |   +-- hook-PySide6.QtCore.py
|   |   |   |   |   |   +-- hook-PySide6.QtDataVisualization.py
|   |   |   |   |   |   +-- hook-PySide6.QtDBus.py
|   |   |   |   |   |   +-- hook-PySide6.QtDesigner.py
|   |   |   |   |   |   +-- hook-PySide6.QtGraphs.py
|   |   |   |   |   |   +-- hook-PySide6.QtGraphsWidgets.py
|   |   |   |   |   |   +-- hook-PySide6.QtGui.py
|   |   |   |   |   |   +-- hook-PySide6.QtHelp.py
|   |   |   |   |   |   +-- hook-PySide6.QtHttpServer.py
|   |   |   |   |   |   +-- hook-PySide6.QtLocation.py
|   |   |   |   |   |   +-- hook-PySide6.QtMultimedia.py
|   |   |   |   |   |   +-- hook-PySide6.QtMultimediaWidgets.py
|   |   |   |   |   |   +-- hook-PySide6.QtNetwork.py
|   |   |   |   |   |   +-- hook-PySide6.QtNetworkAuth.py
|   |   |   |   |   |   +-- hook-PySide6.QtNfc.py
|   |   |   |   |   |   +-- hook-PySide6.QtOpenGL.py
|   |   |   |   |   |   +-- hook-PySide6.QtOpenGLWidgets.py
|   |   |   |   |   |   +-- hook-PySide6.QtPdf.py
|   |   |   |   |   |   +-- hook-PySide6.QtPdfWidgets.py
|   |   |   |   |   |   +-- hook-PySide6.QtPositioning.py
|   |   |   |   |   |   +-- hook-PySide6.QtPrintSupport.py
|   |   |   |   |   |   +-- hook-PySide6.QtQml.py
|   |   |   |   |   |   +-- hook-PySide6.QtQuick.py
|   |   |   |   |   |   +-- hook-PySide6.QtQuick3D.py
|   |   |   |   |   |   +-- hook-PySide6.QtQuickControls2.py
|   |   |   |   |   |   +-- hook-PySide6.QtQuickWidgets.py
|   |   |   |   |   |   +-- hook-PySide6.QtRemoteObjects.py
|   |   |   |   |   |   +-- hook-PySide6.QtScxml.py
|   |   |   |   |   |   +-- hook-PySide6.QtSensors.py
|   |   |   |   |   |   +-- hook-PySide6.QtSerialBus.py
|   |   |   |   |   |   +-- hook-PySide6.QtSerialPort.py
|   |   |   |   |   |   +-- hook-PySide6.QtSpatialAudio.py
|   |   |   |   |   |   +-- hook-PySide6.QtSql.py
|   |   |   |   |   |   +-- hook-PySide6.QtStateMachine.py
|   |   |   |   |   |   +-- hook-PySide6.QtSvg.py
|   |   |   |   |   |   +-- hook-PySide6.QtSvgWidgets.py
|   |   |   |   |   |   +-- hook-PySide6.QtTest.py
|   |   |   |   |   |   +-- hook-PySide6.QtTextToSpeech.py
|   |   |   |   |   |   +-- hook-PySide6.QtUiTools.py
|   |   |   |   |   |   +-- hook-PySide6.QtWebChannel.py
|   |   |   |   |   |   +-- hook-PySide6.QtWebEngineCore.py
|   |   |   |   |   |   +-- hook-PySide6.QtWebEngineQuick.py
|   |   |   |   |   |   +-- hook-PySide6.QtWebEngineWidgets.py
|   |   |   |   |   |   +-- hook-PySide6.QtWebSockets.py
|   |   |   |   |   |   +-- hook-PySide6.QtWidgets.py
|   |   |   |   |   |   +-- hook-PySide6.QtXml.py
|   |   |   |   |   |   +-- hook-pytz.py
|   |   |   |   |   |   +-- hook-pytzdata.py
|   |   |   |   |   |   +-- hook-qtawesome.py
|   |   |   |   |   |   +-- hook-qtpy.py
|   |   |   |   |   |   +-- hook-scapy.layers.all.py
|   |   |   |   |   |   +-- hook-scipy.io.matlab.py
|   |   |   |   |   |   +-- hook-scipy.linalg.py
|   |   |   |   |   |   +-- hook-scipy.py
|   |   |   |   |   |   +-- hook-scipy.sparse.csgraph.py
|   |   |   |   |   |   +-- hook-scipy.spatial._ckdtree.py
|   |   |   |   |   |   +-- hook-scipy.spatial.transform.rotation.py
|   |   |   |   |   |   +-- hook-scipy.special._ellip_harm_2.py
|   |   |   |   |   |   +-- hook-scipy.special._ufuncs.py
|   |   |   |   |   |   +-- hook-scipy.stats._stats.py
|   |   |   |   |   |   +-- hook-scrapy.py
|   |   |   |   |   |   +-- hook-setuptools._vendor.importlib_metadata.py
|   |   |   |   |   |   +-- hook-setuptools._vendor.jaraco.text.py
|   |   |   |   |   |   +-- hook-setuptools.py
|   |   |   |   |   |   +-- hook-shelve.py
|   |   |   |   |   |   +-- hook-shiboken6.py
|   |   |   |   |   |   +-- hook-sphinx.py
|   |   |   |   |   |   +-- hook-sqlalchemy.py
|   |   |   |   |   |   +-- hook-sqlite3.py
|   |   |   |   |   |   +-- hook-sysconfig.py
|   |   |   |   |   |   +-- hook-wcwidth.py
|   |   |   |   |   |   +-- hook-win32ctypes.core.py
|   |   |   |   |   |   +-- hook-xml.dom.domreg.py
|   |   |   |   |   |   +-- hook-xml.etree.cElementTree.py
|   |   |   |   |   |   +-- hook-xml.py
|   |   |   |   |   |   +-- hook-zope.interface.py
|   |   |   |   |   |   +-- rthooks.dat
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-_ctypes.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-_osx_support.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-_pyi_rth_utils.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-_tkinter.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-babel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-difflib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-distutils.command.check.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-distutils.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-distutils.util.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-django.contrib.sessions.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-django.core.cache.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-django.core.mail.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-django.core.management.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-django.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-django.db.backends.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-django.db.backends.mysql.base.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-django.db.backends.oracle.base.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-django.template.loaders.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-encodings.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gevent.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.Adw.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.AppIndicator3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.Atk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.AyatanaAppIndicator3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.cairo.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.Champlain.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.Clutter.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.DBus.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.freetype2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.Gdk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GdkPixbuf.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.Gio.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GIRepository.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GLib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GModule.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GObject.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.Graphene.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.Gsk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.Gst.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstAllocators.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstApp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstAudio.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstBadAudio.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstBase.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstCheck.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstCodecs.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstController.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstGL.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstGLEGL.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstGLWayland.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstGLX11.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstInsertBin.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstMpegts.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstNet.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstPbutils.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstPlay.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstPlayer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstRtp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstRtsp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstRtspServer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstSdp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstTag.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstTranscoder.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstVideo.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstVulkan.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstVulkanWayland.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstVulkanXCB.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GstWebRTC.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.Gtk.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GtkChamplain.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GtkClutter.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GtkosxApplication.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.GtkSource.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.HarfBuzz.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.OsmGpsMap.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.Pango.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.PangoCairo.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.Rsvg.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-gi.repository.xlib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-heapq.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-idlelib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-importlib_metadata.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-importlib_resources.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-keyring.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-kivy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-lib2to3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-matplotlib.backend_bases.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-matplotlib.backends.backend_qtagg.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-matplotlib.backends.backend_qtcairo.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-matplotlib.backends.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-matplotlib.backends.qt_compat.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-matplotlib.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-matplotlib.numerix.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-matplotlib.pyplot.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-multiprocessing.util.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-numpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pandas.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pandas.io.clipboard.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pandas.io.formats.style.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pandas.plotting.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pickle.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PIL.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PIL.Image.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PIL.ImageFilter.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PIL.SpiderImagePlugin.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pkg_resources.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-platform.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pygments.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QAxContainer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.Qsci.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.Qt.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.Qt3DAnimation.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.Qt3DCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.Qt3DExtras.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.Qt3DInput.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.Qt3DLogic.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.Qt3DRender.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtBluetooth.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtChart.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtDataVisualization.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtDBus.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtDesigner.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtGui.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtHelp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtLocation.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtMacExtras.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtMultimedia.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtMultimediaWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtNetwork.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtNetworkAuth.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtNfc.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtOpenGL.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtPositioning.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtPrintSupport.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtPurchasing.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtQml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtQuick.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtQuick3D.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtQuickWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtRemoteObjects.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtScript.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtSensors.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtSerialPort.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtSql.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtSvg.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtTest.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtTextToSpeech.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtWebChannel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtWebEngine.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtWebEngineCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtWebEngineWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtWebKit.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtWebKitWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtWebSockets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtWinExtras.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtX11Extras.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtXml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.QtXmlPatterns.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt5.uic.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QAxContainer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.Qsci.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.Qt3DAnimation.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.Qt3DCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.Qt3DExtras.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.Qt3DInput.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.Qt3DLogic.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.Qt3DRender.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtBluetooth.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtCharts.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtDataVisualization.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtDBus.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtDesigner.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtGraphs.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtGraphsWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtGui.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtHelp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtMultimedia.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtMultimediaWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtNetwork.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtNetworkAuth.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtNfc.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtOpenGL.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtOpenGLWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtPdf.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtPdfWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtPositioning.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtPrintSupport.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtQml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtQuick.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtQuick3D.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtQuickWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtRemoteObjects.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtSensors.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtSerialPort.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtSpatialAudio.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtSql.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtStateMachine.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtSvg.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtSvgWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtTest.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtTextToSpeech.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtWebChannel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtWebEngineCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtWebEngineQuick.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtWebEngineWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtWebSockets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.QtXml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PyQt6.uic.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.Qt3DAnimation.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.Qt3DCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.Qt3DExtras.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.Qt3DInput.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.Qt3DLogic.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.Qt3DRender.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtAxContainer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtCharts.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtConcurrent.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtDataVisualization.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtGui.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtHelp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtLocation.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtMacExtras.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtMultimedia.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtMultimediaWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtNetwork.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtOpenGL.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtOpenGLFunctions.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtPositioning.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtPrintSupport.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtQml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtQuick.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtQuickControls2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtQuickWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtRemoteObjects.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtScript.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtScriptTools.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtScxml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtSensors.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtSerialPort.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtSql.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtSvg.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtTest.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtTextToSpeech.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtUiTools.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtWebChannel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtWebEngine.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtWebEngineCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtWebEngineWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtWebKit.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtWebKitWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtWebSockets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtWinExtras.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtX11Extras.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtXml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.QtXmlPatterns.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide2.Qwt5.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.Qt3DAnimation.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.Qt3DCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.Qt3DExtras.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.Qt3DInput.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.Qt3DLogic.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.Qt3DRender.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtAxContainer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtBluetooth.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtCharts.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtConcurrent.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtDataVisualization.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtDBus.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtDesigner.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtGraphs.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtGraphsWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtGui.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtHelp.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtHttpServer.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtLocation.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtMultimedia.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtMultimediaWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtNetwork.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtNetworkAuth.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtNfc.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtOpenGL.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtOpenGLWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtPdf.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtPdfWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtPositioning.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtPrintSupport.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtQml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtQuick.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtQuick3D.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtQuickControls2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtQuickWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtRemoteObjects.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtScxml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtSensors.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtSerialBus.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtSerialPort.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtSpatialAudio.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtSql.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtStateMachine.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtSvg.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtSvgWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtTest.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtTextToSpeech.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtUiTools.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtWebChannel.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtWebEngineCore.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtWebEngineQuick.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtWebEngineWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtWebSockets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtWidgets.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-PySide6.QtXml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pytz.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-pytzdata.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-qtawesome.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-qtpy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-scapy.layers.all.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-scipy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-scipy.io.matlab.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-scipy.linalg.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-scipy.sparse.csgraph.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-scipy.spatial._ckdtree.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-scipy.spatial.transform.rotation.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-scipy.special._ellip_harm_2.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-scipy.special._ufuncs.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-scipy.stats._stats.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-scrapy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-setuptools._vendor.importlib_metadata.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-setuptools._vendor.jaraco.text.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-setuptools.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-shelve.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-shiboken6.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sphinx.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sqlalchemy.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sqlite3.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-sysconfig.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-wcwidth.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-win32ctypes.core.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-xml.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-xml.dom.domreg.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-xml.etree.cElementTree.cpython-311.pyc
|   |   |   |   |   |   |   +-- hook-zope.interface.cpython-311.pyc
|   |   |   |   |   |   +-- pre_find_module_path/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- hook-_pyi_rth_utils.py
|   |   |   |   |   |   |   +-- hook-distutils.py
|   |   |   |   |   |   |   +-- hook-pyi_splash.py
|   |   |   |   |   |   |   +-- hook-PyQt5.uic.port_v2.py
|   |   |   |   |   |   |   +-- hook-tkinter.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-_pyi_rth_utils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-distutils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-pyi_splash.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-PyQt5.uic.port_v2.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-tkinter.cpython-311.pyc
|   |   |   |   |   |   +-- pre_safe_import_module/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- hook-autocommand.py
|   |   |   |   |   |   |   +-- hook-backports.py
|   |   |   |   |   |   |   +-- hook-backports.tarfile.py
|   |   |   |   |   |   |   +-- hook-distutils.py
|   |   |   |   |   |   |   +-- hook-gi.overrides.py
|   |   |   |   |   |   |   +-- hook-gi.py
|   |   |   |   |   |   |   +-- hook-gi.repository.Adw.py
|   |   |   |   |   |   |   +-- hook-gi.repository.AppIndicator3.py
|   |   |   |   |   |   |   +-- hook-gi.repository.Atk.py
|   |   |   |   |   |   |   +-- hook-gi.repository.AyatanaAppIndicator3.py
|   |   |   |   |   |   |   +-- hook-gi.repository.cairo.py
|   |   |   |   |   |   |   +-- hook-gi.repository.Champlain.py
|   |   |   |   |   |   |   +-- hook-gi.repository.Clutter.py
|   |   |   |   |   |   |   +-- hook-gi.repository.DBus.py
|   |   |   |   |   |   |   +-- hook-gi.repository.freetype2.py
|   |   |   |   |   |   |   +-- hook-gi.repository.Gdk.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GdkPixbuf.py
|   |   |   |   |   |   |   +-- hook-gi.repository.Gio.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GIRepository.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GLib.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GModule.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GObject.py
|   |   |   |   |   |   |   +-- hook-gi.repository.Graphene.py
|   |   |   |   |   |   |   +-- hook-gi.repository.Gsk.py
|   |   |   |   |   |   |   +-- hook-gi.repository.Gst.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstAllocators.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstApp.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstAudio.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstBadAudio.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstBase.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstCheck.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstCodecs.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstController.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstGL.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstGLEGL.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstGLWayland.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstGLX11.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstInsertBin.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstMpegts.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstNet.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstPbutils.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstPlay.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstPlayer.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstRtp.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstRtsp.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstRtspServer.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstSdp.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstTag.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstTranscoder.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstVideo.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstVulkan.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstVulkanWayland.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstVulkanXCB.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GstWebRTC.py
|   |   |   |   |   |   |   +-- hook-gi.repository.Gtk.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GtkChamplain.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GtkClutter.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GtkosxApplication.py
|   |   |   |   |   |   |   +-- hook-gi.repository.GtkSource.py
|   |   |   |   |   |   |   +-- hook-gi.repository.HarfBuzz.py
|   |   |   |   |   |   |   +-- hook-gi.repository.OsmGpsMap.py
|   |   |   |   |   |   |   +-- hook-gi.repository.Pango.py
|   |   |   |   |   |   |   +-- hook-gi.repository.PangoCairo.py
|   |   |   |   |   |   |   +-- hook-gi.repository.Rsvg.py
|   |   |   |   |   |   |   +-- hook-gi.repository.xlib.py
|   |   |   |   |   |   |   +-- hook-importlib_metadata.py
|   |   |   |   |   |   |   +-- hook-importlib_resources.py
|   |   |   |   |   |   |   +-- hook-inflect.py
|   |   |   |   |   |   |   +-- hook-jaraco.context.py
|   |   |   |   |   |   |   +-- hook-jaraco.functools.py
|   |   |   |   |   |   |   +-- hook-jaraco.py
|   |   |   |   |   |   |   +-- hook-jaraco.text.py
|   |   |   |   |   |   |   +-- hook-more_itertools.py
|   |   |   |   |   |   |   +-- hook-ordered_set.py
|   |   |   |   |   |   |   +-- hook-packaging.py
|   |   |   |   |   |   |   +-- hook-platformdirs.py
|   |   |   |   |   |   |   +-- hook-setuptools.extern.six.moves.py
|   |   |   |   |   |   |   +-- hook-six.moves.py
|   |   |   |   |   |   |   +-- hook-tomli.py
|   |   |   |   |   |   |   +-- hook-typeguard.py
|   |   |   |   |   |   |   +-- hook-typing_extensions.py
|   |   |   |   |   |   |   +-- hook-urllib3.packages.six.moves.py
|   |   |   |   |   |   |   +-- hook-wheel.py
|   |   |   |   |   |   |   +-- hook-zipp.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-autocommand.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-backports.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-backports.tarfile.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-distutils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.overrides.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.Adw.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.AppIndicator3.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.Atk.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.AyatanaAppIndicator3.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.cairo.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.Champlain.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.Clutter.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.DBus.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.freetype2.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.Gdk.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GdkPixbuf.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.Gio.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GIRepository.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GLib.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GModule.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GObject.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.Graphene.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.Gsk.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.Gst.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstAllocators.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstApp.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstAudio.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstBadAudio.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstBase.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstCheck.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstCodecs.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstController.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstGL.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstGLEGL.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstGLWayland.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstGLX11.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstInsertBin.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstMpegts.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstNet.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstPbutils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstPlay.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstPlayer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstRtp.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstRtsp.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstRtspServer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstSdp.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstTag.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstTranscoder.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstVideo.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstVulkan.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstVulkanWayland.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstVulkanXCB.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GstWebRTC.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.Gtk.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GtkChamplain.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GtkClutter.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GtkosxApplication.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.GtkSource.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.HarfBuzz.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.OsmGpsMap.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.Pango.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.PangoCairo.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.Rsvg.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-gi.repository.xlib.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-importlib_metadata.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-importlib_resources.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-inflect.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-jaraco.context.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-jaraco.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-jaraco.functools.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-jaraco.text.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-more_itertools.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-ordered_set.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-packaging.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-platformdirs.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-setuptools.extern.six.moves.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-six.moves.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-tomli.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-typeguard.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-typing_extensions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-urllib3.packages.six.moves.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-wheel.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- hook-zipp.cpython-311.pyc
|   |   |   |   |   |   +-- rthooks/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- pyi_rth__tkinter.py
|   |   |   |   |   |   |   +-- pyi_rth_django.py
|   |   |   |   |   |   |   +-- pyi_rth_gdkpixbuf.py
|   |   |   |   |   |   |   +-- pyi_rth_gi.py
|   |   |   |   |   |   |   +-- pyi_rth_gio.py
|   |   |   |   |   |   |   +-- pyi_rth_glib.py
|   |   |   |   |   |   |   +-- pyi_rth_gstreamer.py
|   |   |   |   |   |   |   +-- pyi_rth_gtk.py
|   |   |   |   |   |   |   +-- pyi_rth_inspect.py
|   |   |   |   |   |   |   +-- pyi_rth_kivy.py
|   |   |   |   |   |   |   +-- pyi_rth_mplconfig.py
|   |   |   |   |   |   |   +-- pyi_rth_multiprocessing.py
|   |   |   |   |   |   |   +-- pyi_rth_pkgres.py
|   |   |   |   |   |   |   +-- pyi_rth_pkgutil.py
|   |   |   |   |   |   |   +-- pyi_rth_pyqt5.py
|   |   |   |   |   |   |   +-- pyi_rth_pyqt6.py
|   |   |   |   |   |   |   +-- pyi_rth_pyside2.py
|   |   |   |   |   |   |   +-- pyi_rth_pyside6.py
|   |   |   |   |   |   |   +-- pyi_rth_setuptools.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth__tkinter.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_django.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_gdkpixbuf.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_gi.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_gio.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_glib.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_gstreamer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_gtk.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_inspect.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_kivy.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_mplconfig.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_multiprocessing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_pkgres.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_pkgutil.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_pyqt5.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_pyqt6.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_pyside2.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_pyside6.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- pyi_rth_setuptools.cpython-311.pyc
|   |   |   |   |   +-- isolated/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _child.py
|   |   |   |   |   |   +-- _parent.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _child.cpython-311.pyc
|   |   |   |   |   |   |   +-- _parent.cpython-311.pyc
|   |   |   |   |   +-- lib/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- README.rst
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- modulegraph/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- __main__.py
|   |   |   |   |   |   |   +-- find_modules.py
|   |   |   |   |   |   |   +-- modulegraph.py
|   |   |   |   |   |   |   +-- util.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- __main__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- find_modules.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- modulegraph.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- util.cpython-311.pyc
|   |   |   |   |   +-- loader/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- pyiboot01_bootstrap.py
|   |   |   |   |   |   +-- pyimod01_archive.py
|   |   |   |   |   |   +-- pyimod02_importers.py
|   |   |   |   |   |   +-- pyimod03_ctypes.py
|   |   |   |   |   |   +-- pyimod04_pywin32.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyiboot01_bootstrap.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyimod01_archive.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyimod02_importers.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyimod03_ctypes.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyimod04_pywin32.cpython-311.pyc
|   |   |   |   |   +-- utils/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- conftest.py
|   |   |   |   |   |   +-- misc.py
|   |   |   |   |   |   +-- osx.py
|   |   |   |   |   |   +-- run_tests.py
|   |   |   |   |   |   +-- tests.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- conftest.cpython-311.pyc
|   |   |   |   |   |   |   +-- misc.cpython-311.pyc
|   |   |   |   |   |   |   +-- osx.cpython-311.pyc
|   |   |   |   |   |   |   +-- run_tests.cpython-311.pyc
|   |   |   |   |   |   |   +-- tests.cpython-311.pyc
|   |   |   |   |   |   +-- cliutils/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- archive_viewer.py
|   |   |   |   |   |   |   +-- bindepend.py
|   |   |   |   |   |   |   +-- grab_version.py
|   |   |   |   |   |   |   +-- makespec.py
|   |   |   |   |   |   |   +-- set_version.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- archive_viewer.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- bindepend.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- grab_version.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- makespec.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- set_version.cpython-311.pyc
|   |   |   |   |   |   +-- hooks/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- conda.py
|   |   |   |   |   |   |   +-- django.py
|   |   |   |   |   |   |   +-- gi.py
|   |   |   |   |   |   |   +-- setuptools.py
|   |   |   |   |   |   |   +-- tcl_tk.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- conda.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- django.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- gi.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- setuptools.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- tcl_tk.cpython-311.pyc
|   |   |   |   |   |   |   +-- qt/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- _modules_info.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- _modules_info.cpython-311.pyc
|   |   |   |   |   |   +-- win32/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- icon.py
|   |   |   |   |   |   |   +-- versioninfo.py
|   |   |   |   |   |   |   +-- winmanifest.py
|   |   |   |   |   |   |   +-- winresource.py
|   |   |   |   |   |   |   +-- winutils.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- icon.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- versioninfo.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- winmanifest.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- winresource.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- winutils.cpython-311.pyc
|   |   |   |   +-- pyinstaller_hooks_contrib-2025.10.dist-info/
|   |   |   |   |   +-- entry_points.txt
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE
|   |   |   |   +-- pyinstaller-6.17.0.dist-info/
|   |   |   |   |   +-- entry_points.txt
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- REQUESTED
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- COPYING.txt
|   |   |   |   +-- python_dateutil-2.9.0.post0.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- zip-safe
|   |   |   |   +-- pytz/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- exceptions.py
|   |   |   |   |   +-- lazy.py
|   |   |   |   |   +-- reference.py
|   |   |   |   |   +-- tzfile.py
|   |   |   |   |   +-- tzinfo.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   +-- lazy.cpython-311.pyc
|   |   |   |   |   |   +-- reference.cpython-311.pyc
|   |   |   |   |   |   +-- tzfile.cpython-311.pyc
|   |   |   |   |   |   +-- tzinfo.cpython-311.pyc
|   |   |   |   |   +-- zoneinfo/
|   |   |   |   |   |   +-- CET
|   |   |   |   |   |   +-- CST6CDT
|   |   |   |   |   |   +-- Cuba
|   |   |   |   |   |   +-- EET
|   |   |   |   |   |   +-- Egypt
|   |   |   |   |   |   +-- Eire
|   |   |   |   |   |   +-- EST
|   |   |   |   |   |   +-- EST5EDT
|   |   |   |   |   |   +-- Factory
|   |   |   |   |   |   +-- GB
|   |   |   |   |   |   +-- GB-Eire
|   |   |   |   |   |   +-- GMT
|   |   |   |   |   |   +-- GMT+0
|   |   |   |   |   |   +-- GMT0
|   |   |   |   |   |   +-- GMT-0
|   |   |   |   |   |   +-- Greenwich
|   |   |   |   |   |   +-- Hongkong
|   |   |   |   |   |   +-- HST
|   |   |   |   |   |   +-- Iceland
|   |   |   |   |   |   +-- Iran
|   |   |   |   |   |   +-- iso3166.tab
|   |   |   |   |   |   +-- Israel
|   |   |   |   |   |   +-- Jamaica
|   |   |   |   |   |   +-- Japan
|   |   |   |   |   |   +-- Kwajalein
|   |   |   |   |   |   +-- leapseconds
|   |   |   |   |   |   +-- Libya
|   |   |   |   |   |   +-- MET
|   |   |   |   |   |   +-- MST
|   |   |   |   |   |   +-- MST7MDT
|   |   |   |   |   |   +-- Navajo
|   |   |   |   |   |   +-- NZ
|   |   |   |   |   |   +-- NZ-CHAT
|   |   |   |   |   |   +-- Poland
|   |   |   |   |   |   +-- Portugal
|   |   |   |   |   |   +-- PRC
|   |   |   |   |   |   +-- PST8PDT
|   |   |   |   |   |   +-- ROC
|   |   |   |   |   |   +-- ROK
|   |   |   |   |   |   +-- Singapore
|   |   |   |   |   |   +-- Turkey
|   |   |   |   |   |   +-- tzdata.zi
|   |   |   |   |   |   +-- UCT
|   |   |   |   |   |   +-- Universal
|   |   |   |   |   |   +-- UTC
|   |   |   |   |   |   +-- WET
|   |   |   |   |   |   +-- W-SU
|   |   |   |   |   |   +-- zone.tab
|   |   |   |   |   |   +-- zone1970.tab
|   |   |   |   |   |   +-- zonenow.tab
|   |   |   |   |   |   +-- Zulu
|   |   |   |   |   |   +-- Africa/
|   |   |   |   |   |   |   +-- Abidjan
|   |   |   |   |   |   |   +-- Accra
|   |   |   |   |   |   |   +-- Addis_Ababa
|   |   |   |   |   |   |   +-- Algiers
|   |   |   |   |   |   |   +-- Asmara
|   |   |   |   |   |   |   +-- Asmera
|   |   |   |   |   |   |   +-- Bamako
|   |   |   |   |   |   |   +-- Bangui
|   |   |   |   |   |   |   +-- Banjul
|   |   |   |   |   |   |   +-- Bissau
|   |   |   |   |   |   |   +-- Blantyre
|   |   |   |   |   |   |   +-- Brazzaville
|   |   |   |   |   |   |   +-- Bujumbura
|   |   |   |   |   |   |   +-- Cairo
|   |   |   |   |   |   |   +-- Casablanca
|   |   |   |   |   |   |   +-- Ceuta
|   |   |   |   |   |   |   +-- Conakry
|   |   |   |   |   |   |   +-- Dakar
|   |   |   |   |   |   |   +-- Dar_es_Salaam
|   |   |   |   |   |   |   +-- Djibouti
|   |   |   |   |   |   |   +-- Douala
|   |   |   |   |   |   |   +-- El_Aaiun
|   |   |   |   |   |   |   +-- Freetown
|   |   |   |   |   |   |   +-- Gaborone
|   |   |   |   |   |   |   +-- Harare
|   |   |   |   |   |   |   +-- Johannesburg
|   |   |   |   |   |   |   +-- Juba
|   |   |   |   |   |   |   +-- Kampala
|   |   |   |   |   |   |   +-- Khartoum
|   |   |   |   |   |   |   +-- Kigali
|   |   |   |   |   |   |   +-- Kinshasa
|   |   |   |   |   |   |   +-- Lagos
|   |   |   |   |   |   |   +-- Libreville
|   |   |   |   |   |   |   +-- Lome
|   |   |   |   |   |   |   +-- Luanda
|   |   |   |   |   |   |   +-- Lubumbashi
|   |   |   |   |   |   |   +-- Lusaka
|   |   |   |   |   |   |   +-- Malabo
|   |   |   |   |   |   |   +-- Maputo
|   |   |   |   |   |   |   +-- Maseru
|   |   |   |   |   |   |   +-- Mbabane
|   |   |   |   |   |   |   +-- Mogadishu
|   |   |   |   |   |   |   +-- Monrovia
|   |   |   |   |   |   |   +-- Nairobi
|   |   |   |   |   |   |   +-- Ndjamena
|   |   |   |   |   |   |   +-- Niamey
|   |   |   |   |   |   |   +-- Nouakchott
|   |   |   |   |   |   |   +-- Ouagadougou
|   |   |   |   |   |   |   +-- Porto-Novo
|   |   |   |   |   |   |   +-- Sao_Tome
|   |   |   |   |   |   |   +-- Timbuktu
|   |   |   |   |   |   |   +-- Tripoli
|   |   |   |   |   |   |   +-- Tunis
|   |   |   |   |   |   |   +-- Windhoek
|   |   |   |   |   |   +-- America/
|   |   |   |   |   |   |   +-- Adak
|   |   |   |   |   |   |   +-- Anchorage
|   |   |   |   |   |   |   +-- Anguilla
|   |   |   |   |   |   |   +-- Antigua
|   |   |   |   |   |   |   +-- Araguaina
|   |   |   |   |   |   |   +-- Aruba
|   |   |   |   |   |   |   +-- Asuncion
|   |   |   |   |   |   |   +-- Atikokan
|   |   |   |   |   |   |   +-- Atka
|   |   |   |   |   |   |   +-- Bahia
|   |   |   |   |   |   |   +-- Bahia_Banderas
|   |   |   |   |   |   |   +-- Barbados
|   |   |   |   |   |   |   +-- Belem
|   |   |   |   |   |   |   +-- Belize
|   |   |   |   |   |   |   +-- Blanc-Sablon
|   |   |   |   |   |   |   +-- Boa_Vista
|   |   |   |   |   |   |   +-- Bogota
|   |   |   |   |   |   |   +-- Boise
|   |   |   |   |   |   |   +-- Buenos_Aires
|   |   |   |   |   |   |   +-- Cambridge_Bay
|   |   |   |   |   |   |   +-- Campo_Grande
|   |   |   |   |   |   |   +-- Cancun
|   |   |   |   |   |   |   +-- Caracas
|   |   |   |   |   |   |   +-- Catamarca
|   |   |   |   |   |   |   +-- Cayenne
|   |   |   |   |   |   |   +-- Cayman
|   |   |   |   |   |   |   +-- Chicago
|   |   |   |   |   |   |   +-- Chihuahua
|   |   |   |   |   |   |   +-- Ciudad_Juarez
|   |   |   |   |   |   |   +-- Coral_Harbour
|   |   |   |   |   |   |   +-- Cordoba
|   |   |   |   |   |   |   +-- Costa_Rica
|   |   |   |   |   |   |   +-- Coyhaique
|   |   |   |   |   |   |   +-- Creston
|   |   |   |   |   |   |   +-- Cuiaba
|   |   |   |   |   |   |   +-- Curacao
|   |   |   |   |   |   |   +-- Danmarkshavn
|   |   |   |   |   |   |   +-- Dawson
|   |   |   |   |   |   |   +-- Dawson_Creek
|   |   |   |   |   |   |   +-- Denver
|   |   |   |   |   |   |   +-- Detroit
|   |   |   |   |   |   |   +-- Dominica
|   |   |   |   |   |   |   +-- Edmonton
|   |   |   |   |   |   |   +-- Eirunepe
|   |   |   |   |   |   |   +-- El_Salvador
|   |   |   |   |   |   |   +-- Ensenada
|   |   |   |   |   |   |   +-- Fort_Nelson
|   |   |   |   |   |   |   +-- Fort_Wayne
|   |   |   |   |   |   |   +-- Fortaleza
|   |   |   |   |   |   |   +-- Glace_Bay
|   |   |   |   |   |   |   +-- Godthab
|   |   |   |   |   |   |   +-- Goose_Bay
|   |   |   |   |   |   |   +-- Grand_Turk
|   |   |   |   |   |   |   +-- Grenada
|   |   |   |   |   |   |   +-- Guadeloupe
|   |   |   |   |   |   |   +-- Guatemala
|   |   |   |   |   |   |   +-- Guayaquil
|   |   |   |   |   |   |   +-- Guyana
|   |   |   |   |   |   |   +-- Halifax
|   |   |   |   |   |   |   +-- Havana
|   |   |   |   |   |   |   +-- Hermosillo
|   |   |   |   |   |   |   +-- Indianapolis
|   |   |   |   |   |   |   +-- Inuvik
|   |   |   |   |   |   |   +-- Iqaluit
|   |   |   |   |   |   |   +-- Jamaica
|   |   |   |   |   |   |   +-- Jujuy
|   |   |   |   |   |   |   +-- Juneau
|   |   |   |   |   |   |   +-- Knox_IN
|   |   |   |   |   |   |   +-- Kralendijk
|   |   |   |   |   |   |   +-- La_Paz
|   |   |   |   |   |   |   +-- Lima
|   |   |   |   |   |   |   +-- Los_Angeles
|   |   |   |   |   |   |   +-- Louisville
|   |   |   |   |   |   |   +-- Lower_Princes
|   |   |   |   |   |   |   +-- Maceio
|   |   |   |   |   |   |   +-- Managua
|   |   |   |   |   |   |   +-- Manaus
|   |   |   |   |   |   |   +-- Marigot
|   |   |   |   |   |   |   +-- Martinique
|   |   |   |   |   |   |   +-- Matamoros
|   |   |   |   |   |   |   +-- Mazatlan
|   |   |   |   |   |   |   +-- Mendoza
|   |   |   |   |   |   |   +-- Menominee
|   |   |   |   |   |   |   +-- Merida
|   |   |   |   |   |   |   +-- Metlakatla
|   |   |   |   |   |   |   +-- Mexico_City
|   |   |   |   |   |   |   +-- Miquelon
|   |   |   |   |   |   |   +-- Moncton
|   |   |   |   |   |   |   +-- Monterrey
|   |   |   |   |   |   |   +-- Montevideo
|   |   |   |   |   |   |   +-- Montreal
|   |   |   |   |   |   |   +-- Montserrat
|   |   |   |   |   |   |   +-- Nassau
|   |   |   |   |   |   |   +-- New_York
|   |   |   |   |   |   |   +-- Nipigon
|   |   |   |   |   |   |   +-- Nome
|   |   |   |   |   |   |   +-- Noronha
|   |   |   |   |   |   |   +-- Nuuk
|   |   |   |   |   |   |   +-- Ojinaga
|   |   |   |   |   |   |   +-- Panama
|   |   |   |   |   |   |   +-- Pangnirtung
|   |   |   |   |   |   |   +-- Paramaribo
|   |   |   |   |   |   |   +-- Phoenix
|   |   |   |   |   |   |   +-- Port_of_Spain
|   |   |   |   |   |   |   +-- Port-au-Prince
|   |   |   |   |   |   |   +-- Porto_Acre
|   |   |   |   |   |   |   +-- Porto_Velho
|   |   |   |   |   |   |   +-- Puerto_Rico
|   |   |   |   |   |   |   +-- Punta_Arenas
|   |   |   |   |   |   |   +-- Rainy_River
|   |   |   |   |   |   |   +-- Rankin_Inlet
|   |   |   |   |   |   |   +-- Recife
|   |   |   |   |   |   |   +-- Regina
|   |   |   |   |   |   |   +-- Resolute
|   |   |   |   |   |   |   +-- Rio_Branco
|   |   |   |   |   |   |   +-- Rosario
|   |   |   |   |   |   |   +-- Santa_Isabel
|   |   |   |   |   |   |   +-- Santarem
|   |   |   |   |   |   |   +-- Santiago
|   |   |   |   |   |   |   +-- Santo_Domingo
|   |   |   |   |   |   |   +-- Sao_Paulo
|   |   |   |   |   |   |   +-- Scoresbysund
|   |   |   |   |   |   |   +-- Shiprock
|   |   |   |   |   |   |   +-- Sitka
|   |   |   |   |   |   |   +-- St_Barthelemy
|   |   |   |   |   |   |   +-- St_Johns
|   |   |   |   |   |   |   +-- St_Kitts
|   |   |   |   |   |   |   +-- St_Lucia
|   |   |   |   |   |   |   +-- St_Thomas
|   |   |   |   |   |   |   +-- St_Vincent
|   |   |   |   |   |   |   +-- Swift_Current
|   |   |   |   |   |   |   +-- Tegucigalpa
|   |   |   |   |   |   |   +-- Thule
|   |   |   |   |   |   |   +-- Thunder_Bay
|   |   |   |   |   |   |   +-- Tijuana
|   |   |   |   |   |   |   +-- Toronto
|   |   |   |   |   |   |   +-- Tortola
|   |   |   |   |   |   |   +-- Vancouver
|   |   |   |   |   |   |   +-- Virgin
|   |   |   |   |   |   |   +-- Whitehorse
|   |   |   |   |   |   |   +-- Winnipeg
|   |   |   |   |   |   |   +-- Yakutat
|   |   |   |   |   |   |   +-- Yellowknife
|   |   |   |   |   |   |   +-- Argentina/
|   |   |   |   |   |   |   |   +-- Buenos_Aires
|   |   |   |   |   |   |   |   +-- Catamarca
|   |   |   |   |   |   |   |   +-- ComodRivadavia
|   |   |   |   |   |   |   |   +-- Cordoba
|   |   |   |   |   |   |   |   +-- Jujuy
|   |   |   |   |   |   |   |   +-- La_Rioja
|   |   |   |   |   |   |   |   +-- Mendoza
|   |   |   |   |   |   |   |   +-- Rio_Gallegos
|   |   |   |   |   |   |   |   +-- Salta
|   |   |   |   |   |   |   |   +-- San_Juan
|   |   |   |   |   |   |   |   +-- San_Luis
|   |   |   |   |   |   |   |   +-- Tucuman
|   |   |   |   |   |   |   |   +-- Ushuaia
|   |   |   |   |   |   |   +-- Indiana/
|   |   |   |   |   |   |   |   +-- Indianapolis
|   |   |   |   |   |   |   |   +-- Knox
|   |   |   |   |   |   |   |   +-- Marengo
|   |   |   |   |   |   |   |   +-- Petersburg
|   |   |   |   |   |   |   |   +-- Tell_City
|   |   |   |   |   |   |   |   +-- Vevay
|   |   |   |   |   |   |   |   +-- Vincennes
|   |   |   |   |   |   |   |   +-- Winamac
|   |   |   |   |   |   |   +-- Kentucky/
|   |   |   |   |   |   |   |   +-- Louisville
|   |   |   |   |   |   |   |   +-- Monticello
|   |   |   |   |   |   |   +-- North_Dakota/
|   |   |   |   |   |   |   |   +-- Beulah
|   |   |   |   |   |   |   |   +-- Center
|   |   |   |   |   |   |   |   +-- New_Salem
|   |   |   |   |   |   +-- Antarctica/
|   |   |   |   |   |   |   +-- Casey
|   |   |   |   |   |   |   +-- Davis
|   |   |   |   |   |   |   +-- DumontDUrville
|   |   |   |   |   |   |   +-- Macquarie
|   |   |   |   |   |   |   +-- Mawson
|   |   |   |   |   |   |   +-- McMurdo
|   |   |   |   |   |   |   +-- Palmer
|   |   |   |   |   |   |   +-- Rothera
|   |   |   |   |   |   |   +-- South_Pole
|   |   |   |   |   |   |   +-- Syowa
|   |   |   |   |   |   |   +-- Troll
|   |   |   |   |   |   |   +-- Vostok
|   |   |   |   |   |   +-- Arctic/
|   |   |   |   |   |   |   +-- Longyearbyen
|   |   |   |   |   |   +-- Asia/
|   |   |   |   |   |   |   +-- Aden
|   |   |   |   |   |   |   +-- Almaty
|   |   |   |   |   |   |   +-- Amman
|   |   |   |   |   |   |   +-- Anadyr
|   |   |   |   |   |   |   +-- Aqtau
|   |   |   |   |   |   |   +-- Aqtobe
|   |   |   |   |   |   |   +-- Ashgabat
|   |   |   |   |   |   |   +-- Ashkhabad
|   |   |   |   |   |   |   +-- Atyrau
|   |   |   |   |   |   |   +-- Baghdad
|   |   |   |   |   |   |   +-- Bahrain
|   |   |   |   |   |   |   +-- Baku
|   |   |   |   |   |   |   +-- Bangkok
|   |   |   |   |   |   |   +-- Barnaul
|   |   |   |   |   |   |   +-- Beirut
|   |   |   |   |   |   |   +-- Bishkek
|   |   |   |   |   |   |   +-- Brunei
|   |   |   |   |   |   |   +-- Calcutta
|   |   |   |   |   |   |   +-- Chita
|   |   |   |   |   |   |   +-- Choibalsan
|   |   |   |   |   |   |   +-- Chongqing
|   |   |   |   |   |   |   +-- Chungking
|   |   |   |   |   |   |   +-- Colombo
|   |   |   |   |   |   |   +-- Dacca
|   |   |   |   |   |   |   +-- Damascus
|   |   |   |   |   |   |   +-- Dhaka
|   |   |   |   |   |   |   +-- Dili
|   |   |   |   |   |   |   +-- Dubai
|   |   |   |   |   |   |   +-- Dushanbe
|   |   |   |   |   |   |   +-- Famagusta
|   |   |   |   |   |   |   +-- Gaza
|   |   |   |   |   |   |   +-- Harbin
|   |   |   |   |   |   |   +-- Hebron
|   |   |   |   |   |   |   +-- Ho_Chi_Minh
|   |   |   |   |   |   |   +-- Hong_Kong
|   |   |   |   |   |   |   +-- Hovd
|   |   |   |   |   |   |   +-- Irkutsk
|   |   |   |   |   |   |   +-- Istanbul
|   |   |   |   |   |   |   +-- Jakarta
|   |   |   |   |   |   |   +-- Jayapura
|   |   |   |   |   |   |   +-- Jerusalem
|   |   |   |   |   |   |   +-- Kabul
|   |   |   |   |   |   |   +-- Kamchatka
|   |   |   |   |   |   |   +-- Karachi
|   |   |   |   |   |   |   +-- Kashgar
|   |   |   |   |   |   |   +-- Kathmandu
|   |   |   |   |   |   |   +-- Katmandu
|   |   |   |   |   |   |   +-- Khandyga
|   |   |   |   |   |   |   +-- Kolkata
|   |   |   |   |   |   |   +-- Krasnoyarsk
|   |   |   |   |   |   |   +-- Kuala_Lumpur
|   |   |   |   |   |   |   +-- Kuching
|   |   |   |   |   |   |   +-- Kuwait
|   |   |   |   |   |   |   +-- Macao
|   |   |   |   |   |   |   +-- Macau
|   |   |   |   |   |   |   +-- Magadan
|   |   |   |   |   |   |   +-- Makassar
|   |   |   |   |   |   |   +-- Manila
|   |   |   |   |   |   |   +-- Muscat
|   |   |   |   |   |   |   +-- Nicosia
|   |   |   |   |   |   |   +-- Novokuznetsk
|   |   |   |   |   |   |   +-- Novosibirsk
|   |   |   |   |   |   |   +-- Omsk
|   |   |   |   |   |   |   +-- Oral
|   |   |   |   |   |   |   +-- Phnom_Penh
|   |   |   |   |   |   |   +-- Pontianak
|   |   |   |   |   |   |   +-- Pyongyang
|   |   |   |   |   |   |   +-- Qatar
|   |   |   |   |   |   |   +-- Qostanay
|   |   |   |   |   |   |   +-- Qyzylorda
|   |   |   |   |   |   |   +-- Rangoon
|   |   |   |   |   |   |   +-- Riyadh
|   |   |   |   |   |   |   +-- Saigon
|   |   |   |   |   |   |   +-- Sakhalin
|   |   |   |   |   |   |   +-- Samarkand
|   |   |   |   |   |   |   +-- Seoul
|   |   |   |   |   |   |   +-- Shanghai
|   |   |   |   |   |   |   +-- Singapore
|   |   |   |   |   |   |   +-- Srednekolymsk
|   |   |   |   |   |   |   +-- Taipei
|   |   |   |   |   |   |   +-- Tashkent
|   |   |   |   |   |   |   +-- Tbilisi
|   |   |   |   |   |   |   +-- Tehran
|   |   |   |   |   |   |   +-- Tel_Aviv
|   |   |   |   |   |   |   +-- Thimbu
|   |   |   |   |   |   |   +-- Thimphu
|   |   |   |   |   |   |   +-- Tokyo
|   |   |   |   |   |   |   +-- Tomsk
|   |   |   |   |   |   |   +-- Ujung_Pandang
|   |   |   |   |   |   |   +-- Ulaanbaatar
|   |   |   |   |   |   |   +-- Ulan_Bator
|   |   |   |   |   |   |   +-- Urumqi
|   |   |   |   |   |   |   +-- Ust-Nera
|   |   |   |   |   |   |   +-- Vientiane
|   |   |   |   |   |   |   +-- Vladivostok
|   |   |   |   |   |   |   +-- Yakutsk
|   |   |   |   |   |   |   +-- Yangon
|   |   |   |   |   |   |   +-- Yekaterinburg
|   |   |   |   |   |   |   +-- Yerevan
|   |   |   |   |   |   +-- Atlantic/
|   |   |   |   |   |   |   +-- Azores
|   |   |   |   |   |   |   +-- Bermuda
|   |   |   |   |   |   |   +-- Canary
|   |   |   |   |   |   |   +-- Cape_Verde
|   |   |   |   |   |   |   +-- Faeroe
|   |   |   |   |   |   |   +-- Faroe
|   |   |   |   |   |   |   +-- Jan_Mayen
|   |   |   |   |   |   |   +-- Madeira
|   |   |   |   |   |   |   +-- Reykjavik
|   |   |   |   |   |   |   +-- South_Georgia
|   |   |   |   |   |   |   +-- St_Helena
|   |   |   |   |   |   |   +-- Stanley
|   |   |   |   |   |   +-- Australia/
|   |   |   |   |   |   |   +-- ACT
|   |   |   |   |   |   |   +-- Adelaide
|   |   |   |   |   |   |   +-- Brisbane
|   |   |   |   |   |   |   +-- Broken_Hill
|   |   |   |   |   |   |   +-- Canberra
|   |   |   |   |   |   |   +-- Currie
|   |   |   |   |   |   |   +-- Darwin
|   |   |   |   |   |   |   +-- Eucla
|   |   |   |   |   |   |   +-- Hobart
|   |   |   |   |   |   |   +-- LHI
|   |   |   |   |   |   |   +-- Lindeman
|   |   |   |   |   |   |   +-- Lord_Howe
|   |   |   |   |   |   |   +-- Melbourne
|   |   |   |   |   |   |   +-- North
|   |   |   |   |   |   |   +-- NSW
|   |   |   |   |   |   |   +-- Perth
|   |   |   |   |   |   |   +-- Queensland
|   |   |   |   |   |   |   +-- South
|   |   |   |   |   |   |   +-- Sydney
|   |   |   |   |   |   |   +-- Tasmania
|   |   |   |   |   |   |   +-- Victoria
|   |   |   |   |   |   |   +-- West
|   |   |   |   |   |   |   +-- Yancowinna
|   |   |   |   |   |   +-- Brazil/
|   |   |   |   |   |   |   +-- Acre
|   |   |   |   |   |   |   +-- DeNoronha
|   |   |   |   |   |   |   +-- East
|   |   |   |   |   |   |   +-- West
|   |   |   |   |   |   +-- Canada/
|   |   |   |   |   |   |   +-- Atlantic
|   |   |   |   |   |   |   +-- Central
|   |   |   |   |   |   |   +-- Eastern
|   |   |   |   |   |   |   +-- Mountain
|   |   |   |   |   |   |   +-- Newfoundland
|   |   |   |   |   |   |   +-- Pacific
|   |   |   |   |   |   |   +-- Saskatchewan
|   |   |   |   |   |   |   +-- Yukon
|   |   |   |   |   |   +-- Chile/
|   |   |   |   |   |   |   +-- Continental
|   |   |   |   |   |   |   +-- EasterIsland
|   |   |   |   |   |   +-- Etc/
|   |   |   |   |   |   |   +-- GMT
|   |   |   |   |   |   |   +-- GMT+0
|   |   |   |   |   |   |   +-- GMT+1
|   |   |   |   |   |   |   +-- GMT+10
|   |   |   |   |   |   |   +-- GMT+11
|   |   |   |   |   |   |   +-- GMT+12
|   |   |   |   |   |   |   +-- GMT+2
|   |   |   |   |   |   |   +-- GMT+3
|   |   |   |   |   |   |   +-- GMT+4
|   |   |   |   |   |   |   +-- GMT+5
|   |   |   |   |   |   |   +-- GMT+6
|   |   |   |   |   |   |   +-- GMT+7
|   |   |   |   |   |   |   +-- GMT+8
|   |   |   |   |   |   |   +-- GMT+9
|   |   |   |   |   |   |   +-- GMT0
|   |   |   |   |   |   |   +-- GMT-0
|   |   |   |   |   |   |   +-- GMT-1
|   |   |   |   |   |   |   +-- GMT-10
|   |   |   |   |   |   |   +-- GMT-11
|   |   |   |   |   |   |   +-- GMT-12
|   |   |   |   |   |   |   +-- GMT-13
|   |   |   |   |   |   |   +-- GMT-14
|   |   |   |   |   |   |   +-- GMT-2
|   |   |   |   |   |   |   +-- GMT-3
|   |   |   |   |   |   |   +-- GMT-4
|   |   |   |   |   |   |   +-- GMT-5
|   |   |   |   |   |   |   +-- GMT-6
|   |   |   |   |   |   |   +-- GMT-7
|   |   |   |   |   |   |   +-- GMT-8
|   |   |   |   |   |   |   +-- GMT-9
|   |   |   |   |   |   |   +-- Greenwich
|   |   |   |   |   |   |   +-- UCT
|   |   |   |   |   |   |   +-- Universal
|   |   |   |   |   |   |   +-- UTC
|   |   |   |   |   |   |   +-- Zulu
|   |   |   |   |   |   +-- Europe/
|   |   |   |   |   |   |   +-- Amsterdam
|   |   |   |   |   |   |   +-- Andorra
|   |   |   |   |   |   |   +-- Astrakhan
|   |   |   |   |   |   |   +-- Athens
|   |   |   |   |   |   |   +-- Belfast
|   |   |   |   |   |   |   +-- Belgrade
|   |   |   |   |   |   |   +-- Berlin
|   |   |   |   |   |   |   +-- Bratislava
|   |   |   |   |   |   |   +-- Brussels
|   |   |   |   |   |   |   +-- Bucharest
|   |   |   |   |   |   |   +-- Budapest
|   |   |   |   |   |   |   +-- Busingen
|   |   |   |   |   |   |   +-- Chisinau
|   |   |   |   |   |   |   +-- Copenhagen
|   |   |   |   |   |   |   +-- Dublin
|   |   |   |   |   |   |   +-- Gibraltar
|   |   |   |   |   |   |   +-- Guernsey
|   |   |   |   |   |   |   +-- Helsinki
|   |   |   |   |   |   |   +-- Isle_of_Man
|   |   |   |   |   |   |   +-- Istanbul
|   |   |   |   |   |   |   +-- Jersey
|   |   |   |   |   |   |   +-- Kaliningrad
|   |   |   |   |   |   |   +-- Kiev
|   |   |   |   |   |   |   +-- Kirov
|   |   |   |   |   |   |   +-- Kyiv
|   |   |   |   |   |   |   +-- Lisbon
|   |   |   |   |   |   |   +-- Ljubljana
|   |   |   |   |   |   |   +-- London
|   |   |   |   |   |   |   +-- Luxembourg
|   |   |   |   |   |   |   +-- Madrid
|   |   |   |   |   |   |   +-- Malta
|   |   |   |   |   |   |   +-- Mariehamn
|   |   |   |   |   |   |   +-- Minsk
|   |   |   |   |   |   |   +-- Monaco
|   |   |   |   |   |   |   +-- Moscow
|   |   |   |   |   |   |   +-- Nicosia
|   |   |   |   |   |   |   +-- Oslo
|   |   |   |   |   |   |   +-- Paris
|   |   |   |   |   |   |   +-- Podgorica
|   |   |   |   |   |   |   +-- Prague
|   |   |   |   |   |   |   +-- Riga
|   |   |   |   |   |   |   +-- Rome
|   |   |   |   |   |   |   +-- Samara
|   |   |   |   |   |   |   +-- San_Marino
|   |   |   |   |   |   |   +-- Sarajevo
|   |   |   |   |   |   |   +-- Saratov
|   |   |   |   |   |   |   +-- Simferopol
|   |   |   |   |   |   |   +-- Skopje
|   |   |   |   |   |   |   +-- Sofia
|   |   |   |   |   |   |   +-- Stockholm
|   |   |   |   |   |   |   +-- Tallinn
|   |   |   |   |   |   |   +-- Tirane
|   |   |   |   |   |   |   +-- Tiraspol
|   |   |   |   |   |   |   +-- Ulyanovsk
|   |   |   |   |   |   |   +-- Uzhgorod
|   |   |   |   |   |   |   +-- Vaduz
|   |   |   |   |   |   |   +-- Vatican
|   |   |   |   |   |   |   +-- Vienna
|   |   |   |   |   |   |   +-- Vilnius
|   |   |   |   |   |   |   +-- Volgograd
|   |   |   |   |   |   |   +-- Warsaw
|   |   |   |   |   |   |   +-- Zagreb
|   |   |   |   |   |   |   +-- Zaporozhye
|   |   |   |   |   |   |   +-- Zurich
|   |   |   |   |   |   +-- Indian/
|   |   |   |   |   |   |   +-- Antananarivo
|   |   |   |   |   |   |   +-- Chagos
|   |   |   |   |   |   |   +-- Christmas
|   |   |   |   |   |   |   +-- Cocos
|   |   |   |   |   |   |   +-- Comoro
|   |   |   |   |   |   |   +-- Kerguelen
|   |   |   |   |   |   |   +-- Mahe
|   |   |   |   |   |   |   +-- Maldives
|   |   |   |   |   |   |   +-- Mauritius
|   |   |   |   |   |   |   +-- Mayotte
|   |   |   |   |   |   |   +-- Reunion
|   |   |   |   |   |   +-- Mexico/
|   |   |   |   |   |   |   +-- BajaNorte
|   |   |   |   |   |   |   +-- BajaSur
|   |   |   |   |   |   |   +-- General
|   |   |   |   |   |   +-- Pacific/
|   |   |   |   |   |   |   +-- Apia
|   |   |   |   |   |   |   +-- Auckland
|   |   |   |   |   |   |   +-- Bougainville
|   |   |   |   |   |   |   +-- Chatham
|   |   |   |   |   |   |   +-- Chuuk
|   |   |   |   |   |   |   +-- Easter
|   |   |   |   |   |   |   +-- Efate
|   |   |   |   |   |   |   +-- Enderbury
|   |   |   |   |   |   |   +-- Fakaofo
|   |   |   |   |   |   |   +-- Fiji
|   |   |   |   |   |   |   +-- Funafuti
|   |   |   |   |   |   |   +-- Galapagos
|   |   |   |   |   |   |   +-- Gambier
|   |   |   |   |   |   |   +-- Guadalcanal
|   |   |   |   |   |   |   +-- Guam
|   |   |   |   |   |   |   +-- Honolulu
|   |   |   |   |   |   |   +-- Johnston
|   |   |   |   |   |   |   +-- Kanton
|   |   |   |   |   |   |   +-- Kiritimati
|   |   |   |   |   |   |   +-- Kosrae
|   |   |   |   |   |   |   +-- Kwajalein
|   |   |   |   |   |   |   +-- Majuro
|   |   |   |   |   |   |   +-- Marquesas
|   |   |   |   |   |   |   +-- Midway
|   |   |   |   |   |   |   +-- Nauru
|   |   |   |   |   |   |   +-- Niue
|   |   |   |   |   |   |   +-- Norfolk
|   |   |   |   |   |   |   +-- Noumea
|   |   |   |   |   |   |   +-- Pago_Pago
|   |   |   |   |   |   |   +-- Palau
|   |   |   |   |   |   |   +-- Pitcairn
|   |   |   |   |   |   |   +-- Pohnpei
|   |   |   |   |   |   |   +-- Ponape
|   |   |   |   |   |   |   +-- Port_Moresby
|   |   |   |   |   |   |   +-- Rarotonga
|   |   |   |   |   |   |   +-- Saipan
|   |   |   |   |   |   |   +-- Samoa
|   |   |   |   |   |   |   +-- Tahiti
|   |   |   |   |   |   |   +-- Tarawa
|   |   |   |   |   |   |   +-- Tongatapu
|   |   |   |   |   |   |   +-- Truk
|   |   |   |   |   |   |   +-- Wake
|   |   |   |   |   |   |   +-- Wallis
|   |   |   |   |   |   |   +-- Yap
|   |   |   |   |   |   +-- US/
|   |   |   |   |   |   |   +-- Alaska
|   |   |   |   |   |   |   +-- Aleutian
|   |   |   |   |   |   |   +-- Arizona
|   |   |   |   |   |   |   +-- Central
|   |   |   |   |   |   |   +-- Eastern
|   |   |   |   |   |   |   +-- East-Indiana
|   |   |   |   |   |   |   +-- Hawaii
|   |   |   |   |   |   |   +-- Indiana-Starke
|   |   |   |   |   |   |   +-- Michigan
|   |   |   |   |   |   |   +-- Mountain
|   |   |   |   |   |   |   +-- Pacific
|   |   |   |   |   |   |   +-- Samoa
|   |   |   |   +-- pytz-2025.2.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- zip-safe
|   |   |   |   +-- pywin32_ctypes-0.2.3.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE.txt
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- qrcode/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- base.py
|   |   |   |   |   +-- console_scripts.py
|   |   |   |   |   +-- constants.py
|   |   |   |   |   +-- exceptions.py
|   |   |   |   |   +-- LUT.py
|   |   |   |   |   +-- main.py
|   |   |   |   |   +-- release.py
|   |   |   |   |   +-- util.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   +-- console_scripts.cpython-311.pyc
|   |   |   |   |   |   +-- constants.cpython-311.pyc
|   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   +-- LUT.cpython-311.pyc
|   |   |   |   |   |   +-- main.cpython-311.pyc
|   |   |   |   |   |   +-- release.cpython-311.pyc
|   |   |   |   |   |   +-- util.cpython-311.pyc
|   |   |   |   |   +-- compat/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- etree.py
|   |   |   |   |   |   +-- png.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- etree.cpython-311.pyc
|   |   |   |   |   |   |   +-- png.cpython-311.pyc
|   |   |   |   |   +-- image/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   +-- pil.py
|   |   |   |   |   |   +-- pure.py
|   |   |   |   |   |   +-- styledpil.py
|   |   |   |   |   |   +-- svg.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   +-- pil.cpython-311.pyc
|   |   |   |   |   |   |   +-- pure.cpython-311.pyc
|   |   |   |   |   |   |   +-- styledpil.cpython-311.pyc
|   |   |   |   |   |   |   +-- svg.cpython-311.pyc
|   |   |   |   |   |   +-- styles/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- colormasks.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- colormasks.cpython-311.pyc
|   |   |   |   |   |   |   +-- moduledrawers/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- base.py
|   |   |   |   |   |   |   |   +-- pil.py
|   |   |   |   |   |   |   |   +-- svg.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- base.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- pil.cpython-311.pyc
|   |   |   |   |   |   |   |   |   +-- svg.cpython-311.pyc
|   |   |   |   |   +-- tests/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- consts.py
|   |   |   |   |   |   +-- test_example.py
|   |   |   |   |   |   +-- test_qrcode.py
|   |   |   |   |   |   +-- test_qrcode_pil.py
|   |   |   |   |   |   +-- test_qrcode_pypng.py
|   |   |   |   |   |   +-- test_qrcode_svg.py
|   |   |   |   |   |   +-- test_release.py
|   |   |   |   |   |   +-- test_script.py
|   |   |   |   |   |   +-- test_util.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- consts.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_example.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_qrcode.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_qrcode_pil.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_qrcode_pypng.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_qrcode_svg.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_release.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_script.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_util.cpython-311.pyc
|   |   |   |   +-- qrcode-8.2.dist-info/
|   |   |   |   |   +-- entry_points.txt
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- REQUESTED
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- requests/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- __version__.py
|   |   |   |   |   +-- _internal_utils.py
|   |   |   |   |   +-- adapters.py
|   |   |   |   |   +-- api.py
|   |   |   |   |   +-- auth.py
|   |   |   |   |   +-- certs.py
|   |   |   |   |   +-- compat.py
|   |   |   |   |   +-- cookies.py
|   |   |   |   |   +-- exceptions.py
|   |   |   |   |   +-- help.py
|   |   |   |   |   +-- hooks.py
|   |   |   |   |   +-- models.py
|   |   |   |   |   +-- packages.py
|   |   |   |   |   +-- sessions.py
|   |   |   |   |   +-- status_codes.py
|   |   |   |   |   +-- structures.py
|   |   |   |   |   +-- utils.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- __version__.cpython-311.pyc
|   |   |   |   |   |   +-- _internal_utils.cpython-311.pyc
|   |   |   |   |   |   +-- adapters.cpython-311.pyc
|   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   +-- auth.cpython-311.pyc
|   |   |   |   |   |   +-- certs.cpython-311.pyc
|   |   |   |   |   |   +-- compat.cpython-311.pyc
|   |   |   |   |   |   +-- cookies.cpython-311.pyc
|   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   +-- help.cpython-311.pyc
|   |   |   |   |   |   +-- hooks.cpython-311.pyc
|   |   |   |   |   |   +-- models.cpython-311.pyc
|   |   |   |   |   |   +-- packages.cpython-311.pyc
|   |   |   |   |   |   +-- sessions.cpython-311.pyc
|   |   |   |   |   |   +-- status_codes.cpython-311.pyc
|   |   |   |   |   |   +-- structures.cpython-311.pyc
|   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   +-- requests-2.32.5.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- REQUESTED
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE
|   |   |   |   +-- setuptools/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _deprecation_warning.py
|   |   |   |   |   +-- _entry_points.py
|   |   |   |   |   +-- _imp.py
|   |   |   |   |   +-- _importlib.py
|   |   |   |   |   +-- _itertools.py
|   |   |   |   |   +-- _path.py
|   |   |   |   |   +-- _reqs.py
|   |   |   |   |   +-- archive_util.py
|   |   |   |   |   +-- build_meta.py
|   |   |   |   |   +-- cli.exe
|   |   |   |   |   +-- cli-32.exe
|   |   |   |   |   +-- cli-64.exe
|   |   |   |   |   +-- cli-arm64.exe
|   |   |   |   |   +-- dep_util.py
|   |   |   |   |   +-- depends.py
|   |   |   |   |   +-- discovery.py
|   |   |   |   |   +-- dist.py
|   |   |   |   |   +-- errors.py
|   |   |   |   |   +-- extension.py
|   |   |   |   |   +-- glob.py
|   |   |   |   |   +-- gui.exe
|   |   |   |   |   +-- gui-32.exe
|   |   |   |   |   +-- gui-64.exe
|   |   |   |   |   +-- gui-arm64.exe
|   |   |   |   |   +-- installer.py
|   |   |   |   |   +-- launch.py
|   |   |   |   |   +-- logging.py
|   |   |   |   |   +-- monkey.py
|   |   |   |   |   +-- msvc.py
|   |   |   |   |   +-- namespaces.py
|   |   |   |   |   +-- package_index.py
|   |   |   |   |   +-- py34compat.py
|   |   |   |   |   +-- sandbox.py
|   |   |   |   |   +-- script (dev).tmpl
|   |   |   |   |   +-- script.tmpl
|   |   |   |   |   +-- unicode_utils.py
|   |   |   |   |   +-- version.py
|   |   |   |   |   +-- wheel.py
|   |   |   |   |   +-- windows_support.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _deprecation_warning.cpython-311.pyc
|   |   |   |   |   |   +-- _entry_points.cpython-311.pyc
|   |   |   |   |   |   +-- _imp.cpython-311.pyc
|   |   |   |   |   |   +-- _importlib.cpython-311.pyc
|   |   |   |   |   |   +-- _itertools.cpython-311.pyc
|   |   |   |   |   |   +-- _path.cpython-311.pyc
|   |   |   |   |   |   +-- _reqs.cpython-311.pyc
|   |   |   |   |   |   +-- archive_util.cpython-311.pyc
|   |   |   |   |   |   +-- build_meta.cpython-311.pyc
|   |   |   |   |   |   +-- dep_util.cpython-311.pyc
|   |   |   |   |   |   +-- depends.cpython-311.pyc
|   |   |   |   |   |   +-- discovery.cpython-311.pyc
|   |   |   |   |   |   +-- dist.cpython-311.pyc
|   |   |   |   |   |   +-- errors.cpython-311.pyc
|   |   |   |   |   |   +-- extension.cpython-311.pyc
|   |   |   |   |   |   +-- glob.cpython-311.pyc
|   |   |   |   |   |   +-- installer.cpython-311.pyc
|   |   |   |   |   |   +-- launch.cpython-311.pyc
|   |   |   |   |   |   +-- logging.cpython-311.pyc
|   |   |   |   |   |   +-- monkey.cpython-311.pyc
|   |   |   |   |   |   +-- msvc.cpython-311.pyc
|   |   |   |   |   |   +-- namespaces.cpython-311.pyc
|   |   |   |   |   |   +-- package_index.cpython-311.pyc
|   |   |   |   |   |   +-- py34compat.cpython-311.pyc
|   |   |   |   |   |   +-- sandbox.cpython-311.pyc
|   |   |   |   |   |   +-- unicode_utils.cpython-311.pyc
|   |   |   |   |   |   +-- version.cpython-311.pyc
|   |   |   |   |   |   +-- wheel.cpython-311.pyc
|   |   |   |   |   |   +-- windows_support.cpython-311.pyc
|   |   |   |   |   +-- _distutils/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _collections.py
|   |   |   |   |   |   +-- _functools.py
|   |   |   |   |   |   +-- _macos_compat.py
|   |   |   |   |   |   +-- _msvccompiler.py
|   |   |   |   |   |   +-- archive_util.py
|   |   |   |   |   |   +-- bcppcompiler.py
|   |   |   |   |   |   +-- ccompiler.py
|   |   |   |   |   |   +-- cmd.py
|   |   |   |   |   |   +-- config.py
|   |   |   |   |   |   +-- core.py
|   |   |   |   |   |   +-- cygwinccompiler.py
|   |   |   |   |   |   +-- debug.py
|   |   |   |   |   |   +-- dep_util.py
|   |   |   |   |   |   +-- dir_util.py
|   |   |   |   |   |   +-- dist.py
|   |   |   |   |   |   +-- errors.py
|   |   |   |   |   |   +-- extension.py
|   |   |   |   |   |   +-- fancy_getopt.py
|   |   |   |   |   |   +-- file_util.py
|   |   |   |   |   |   +-- filelist.py
|   |   |   |   |   |   +-- log.py
|   |   |   |   |   |   +-- msvc9compiler.py
|   |   |   |   |   |   +-- msvccompiler.py
|   |   |   |   |   |   +-- py38compat.py
|   |   |   |   |   |   +-- py39compat.py
|   |   |   |   |   |   +-- spawn.py
|   |   |   |   |   |   +-- sysconfig.py
|   |   |   |   |   |   +-- text_file.py
|   |   |   |   |   |   +-- unixccompiler.py
|   |   |   |   |   |   +-- util.py
|   |   |   |   |   |   +-- version.py
|   |   |   |   |   |   +-- versionpredicate.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _collections.cpython-311.pyc
|   |   |   |   |   |   |   +-- _functools.cpython-311.pyc
|   |   |   |   |   |   |   +-- _macos_compat.cpython-311.pyc
|   |   |   |   |   |   |   +-- _msvccompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- archive_util.cpython-311.pyc
|   |   |   |   |   |   |   +-- bcppcompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- ccompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- cmd.cpython-311.pyc
|   |   |   |   |   |   |   +-- config.cpython-311.pyc
|   |   |   |   |   |   |   +-- core.cpython-311.pyc
|   |   |   |   |   |   |   +-- cygwinccompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- debug.cpython-311.pyc
|   |   |   |   |   |   |   +-- dep_util.cpython-311.pyc
|   |   |   |   |   |   |   +-- dir_util.cpython-311.pyc
|   |   |   |   |   |   |   +-- dist.cpython-311.pyc
|   |   |   |   |   |   |   +-- errors.cpython-311.pyc
|   |   |   |   |   |   |   +-- extension.cpython-311.pyc
|   |   |   |   |   |   |   +-- fancy_getopt.cpython-311.pyc
|   |   |   |   |   |   |   +-- file_util.cpython-311.pyc
|   |   |   |   |   |   |   +-- filelist.cpython-311.pyc
|   |   |   |   |   |   |   +-- log.cpython-311.pyc
|   |   |   |   |   |   |   +-- msvc9compiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- msvccompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- py38compat.cpython-311.pyc
|   |   |   |   |   |   |   +-- py39compat.cpython-311.pyc
|   |   |   |   |   |   |   +-- spawn.cpython-311.pyc
|   |   |   |   |   |   |   +-- sysconfig.cpython-311.pyc
|   |   |   |   |   |   |   +-- text_file.cpython-311.pyc
|   |   |   |   |   |   |   +-- unixccompiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- util.cpython-311.pyc
|   |   |   |   |   |   |   +-- version.cpython-311.pyc
|   |   |   |   |   |   |   +-- versionpredicate.cpython-311.pyc
|   |   |   |   |   |   +-- command/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _framework_compat.py
|   |   |   |   |   |   |   +-- bdist.py
|   |   |   |   |   |   |   +-- bdist_dumb.py
|   |   |   |   |   |   |   +-- bdist_rpm.py
|   |   |   |   |   |   |   +-- build.py
|   |   |   |   |   |   |   +-- build_clib.py
|   |   |   |   |   |   |   +-- build_ext.py
|   |   |   |   |   |   |   +-- build_py.py
|   |   |   |   |   |   |   +-- build_scripts.py
|   |   |   |   |   |   |   +-- check.py
|   |   |   |   |   |   |   +-- clean.py
|   |   |   |   |   |   |   +-- config.py
|   |   |   |   |   |   |   +-- install.py
|   |   |   |   |   |   |   +-- install_data.py
|   |   |   |   |   |   |   +-- install_egg_info.py
|   |   |   |   |   |   |   +-- install_headers.py
|   |   |   |   |   |   |   +-- install_lib.py
|   |   |   |   |   |   |   +-- install_scripts.py
|   |   |   |   |   |   |   +-- py37compat.py
|   |   |   |   |   |   |   +-- register.py
|   |   |   |   |   |   |   +-- sdist.py
|   |   |   |   |   |   |   +-- upload.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _framework_compat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- bdist.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- bdist_dumb.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- bdist_rpm.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- build.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- build_clib.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- build_ext.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- build_py.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- build_scripts.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- check.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- clean.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- config.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- install.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- install_data.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- install_egg_info.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- install_headers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- install_lib.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- install_scripts.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- py37compat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- register.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- sdist.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- upload.cpython-311.pyc
|   |   |   |   |   +-- _vendor/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- ordered_set.py
|   |   |   |   |   |   +-- typing_extensions.py
|   |   |   |   |   |   +-- zipp.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- ordered_set.cpython-311.pyc
|   |   |   |   |   |   |   +-- typing_extensions.cpython-311.pyc
|   |   |   |   |   |   |   +-- zipp.cpython-311.pyc
|   |   |   |   |   |   +-- importlib_metadata/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _adapters.py
|   |   |   |   |   |   |   +-- _collections.py
|   |   |   |   |   |   |   +-- _compat.py
|   |   |   |   |   |   |   +-- _functools.py
|   |   |   |   |   |   |   +-- _itertools.py
|   |   |   |   |   |   |   +-- _meta.py
|   |   |   |   |   |   |   +-- _text.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _adapters.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _collections.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _compat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _functools.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _itertools.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _meta.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _text.cpython-311.pyc
|   |   |   |   |   |   +-- importlib_resources/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _adapters.py
|   |   |   |   |   |   |   +-- _common.py
|   |   |   |   |   |   |   +-- _compat.py
|   |   |   |   |   |   |   +-- _itertools.py
|   |   |   |   |   |   |   +-- _legacy.py
|   |   |   |   |   |   |   +-- abc.py
|   |   |   |   |   |   |   +-- readers.py
|   |   |   |   |   |   |   +-- simple.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _adapters.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _compat.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _itertools.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _legacy.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- abc.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- readers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- simple.cpython-311.pyc
|   |   |   |   |   |   +-- jaraco/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- context.py
|   |   |   |   |   |   |   +-- functools.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- context.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- functools.cpython-311.pyc
|   |   |   |   |   |   |   +-- text/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- more_itertools/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- more.py
|   |   |   |   |   |   |   +-- recipes.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- more.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- recipes.cpython-311.pyc
|   |   |   |   |   |   +-- packaging/
|   |   |   |   |   |   |   +-- __about__.py
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _manylinux.py
|   |   |   |   |   |   |   +-- _musllinux.py
|   |   |   |   |   |   |   +-- _structures.py
|   |   |   |   |   |   |   +-- markers.py
|   |   |   |   |   |   |   +-- requirements.py
|   |   |   |   |   |   |   +-- specifiers.py
|   |   |   |   |   |   |   +-- tags.py
|   |   |   |   |   |   |   +-- utils.py
|   |   |   |   |   |   |   +-- version.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __about__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _manylinux.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _musllinux.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _structures.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- markers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- requirements.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- specifiers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- tags.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- version.cpython-311.pyc
|   |   |   |   |   |   +-- pyparsing/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- actions.py
|   |   |   |   |   |   |   +-- common.py
|   |   |   |   |   |   |   +-- core.py
|   |   |   |   |   |   |   +-- exceptions.py
|   |   |   |   |   |   |   +-- helpers.py
|   |   |   |   |   |   |   +-- results.py
|   |   |   |   |   |   |   +-- testing.py
|   |   |   |   |   |   |   +-- unicode.py
|   |   |   |   |   |   |   +-- util.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- actions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- core.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- helpers.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- results.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- testing.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- unicode.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- util.cpython-311.pyc
|   |   |   |   |   |   |   +-- diagram/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- tomli/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _parser.py
|   |   |   |   |   |   |   +-- _re.py
|   |   |   |   |   |   |   +-- _types.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _parser.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _re.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _types.cpython-311.pyc
|   |   |   |   |   +-- command/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- alias.py
|   |   |   |   |   |   +-- bdist_egg.py
|   |   |   |   |   |   +-- bdist_rpm.py
|   |   |   |   |   |   +-- build.py
|   |   |   |   |   |   +-- build_clib.py
|   |   |   |   |   |   +-- build_ext.py
|   |   |   |   |   |   +-- build_py.py
|   |   |   |   |   |   +-- develop.py
|   |   |   |   |   |   +-- dist_info.py
|   |   |   |   |   |   +-- easy_install.py
|   |   |   |   |   |   +-- editable_wheel.py
|   |   |   |   |   |   +-- egg_info.py
|   |   |   |   |   |   +-- install.py
|   |   |   |   |   |   +-- install_egg_info.py
|   |   |   |   |   |   +-- install_lib.py
|   |   |   |   |   |   +-- install_scripts.py
|   |   |   |   |   |   +-- launcher manifest.xml
|   |   |   |   |   |   +-- py36compat.py
|   |   |   |   |   |   +-- register.py
|   |   |   |   |   |   +-- rotate.py
|   |   |   |   |   |   +-- saveopts.py
|   |   |   |   |   |   +-- sdist.py
|   |   |   |   |   |   +-- setopt.py
|   |   |   |   |   |   +-- test.py
|   |   |   |   |   |   +-- upload.py
|   |   |   |   |   |   +-- upload_docs.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- alias.cpython-311.pyc
|   |   |   |   |   |   |   +-- bdist_egg.cpython-311.pyc
|   |   |   |   |   |   |   +-- bdist_rpm.cpython-311.pyc
|   |   |   |   |   |   |   +-- build.cpython-311.pyc
|   |   |   |   |   |   |   +-- build_clib.cpython-311.pyc
|   |   |   |   |   |   |   +-- build_ext.cpython-311.pyc
|   |   |   |   |   |   |   +-- build_py.cpython-311.pyc
|   |   |   |   |   |   |   +-- develop.cpython-311.pyc
|   |   |   |   |   |   |   +-- dist_info.cpython-311.pyc
|   |   |   |   |   |   |   +-- easy_install.cpython-311.pyc
|   |   |   |   |   |   |   +-- editable_wheel.cpython-311.pyc
|   |   |   |   |   |   |   +-- egg_info.cpython-311.pyc
|   |   |   |   |   |   |   +-- install.cpython-311.pyc
|   |   |   |   |   |   |   +-- install_egg_info.cpython-311.pyc
|   |   |   |   |   |   |   +-- install_lib.cpython-311.pyc
|   |   |   |   |   |   |   +-- install_scripts.cpython-311.pyc
|   |   |   |   |   |   |   +-- py36compat.cpython-311.pyc
|   |   |   |   |   |   |   +-- register.cpython-311.pyc
|   |   |   |   |   |   |   +-- rotate.cpython-311.pyc
|   |   |   |   |   |   |   +-- saveopts.cpython-311.pyc
|   |   |   |   |   |   |   +-- sdist.cpython-311.pyc
|   |   |   |   |   |   |   +-- setopt.cpython-311.pyc
|   |   |   |   |   |   |   +-- test.cpython-311.pyc
|   |   |   |   |   |   |   +-- upload.cpython-311.pyc
|   |   |   |   |   |   |   +-- upload_docs.cpython-311.pyc
|   |   |   |   |   +-- config/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _apply_pyprojecttoml.py
|   |   |   |   |   |   +-- expand.py
|   |   |   |   |   |   +-- pyprojecttoml.py
|   |   |   |   |   |   +-- setupcfg.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _apply_pyprojecttoml.cpython-311.pyc
|   |   |   |   |   |   |   +-- expand.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyprojecttoml.cpython-311.pyc
|   |   |   |   |   |   |   +-- setupcfg.cpython-311.pyc
|   |   |   |   |   |   +-- _validate_pyproject/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- error_reporting.py
|   |   |   |   |   |   |   +-- extra_validations.py
|   |   |   |   |   |   |   +-- fastjsonschema_exceptions.py
|   |   |   |   |   |   |   +-- fastjsonschema_validations.py
|   |   |   |   |   |   |   +-- formats.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- error_reporting.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- extra_validations.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- fastjsonschema_exceptions.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- fastjsonschema_validations.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- formats.cpython-311.pyc
|   |   |   |   |   +-- extern/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   +-- setuptools-65.5.0.dist-info/
|   |   |   |   |   +-- entry_points.txt
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- REQUESTED
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- six-1.17.0.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- tk/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- structure/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- Tensor.py
|   |   |   |   |   |   +-- TensorMap.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- Tensor.cpython-311.pyc
|   |   |   |   |   |   |   +-- TensorMap.cpython-311.pyc
|   |   |   |   +-- tk-0.1.0.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- REQUESTED
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- tzdata/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- zones
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- zoneinfo/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- CET
|   |   |   |   |   |   +-- CST6CDT
|   |   |   |   |   |   +-- Cuba
|   |   |   |   |   |   +-- EET
|   |   |   |   |   |   +-- Egypt
|   |   |   |   |   |   +-- Eire
|   |   |   |   |   |   +-- EST
|   |   |   |   |   |   +-- EST5EDT
|   |   |   |   |   |   +-- Factory
|   |   |   |   |   |   +-- GB
|   |   |   |   |   |   +-- GB-Eire
|   |   |   |   |   |   +-- GMT
|   |   |   |   |   |   +-- GMT+0
|   |   |   |   |   |   +-- GMT0
|   |   |   |   |   |   +-- GMT-0
|   |   |   |   |   |   +-- Greenwich
|   |   |   |   |   |   +-- Hongkong
|   |   |   |   |   |   +-- HST
|   |   |   |   |   |   +-- Iceland
|   |   |   |   |   |   +-- Iran
|   |   |   |   |   |   +-- iso3166.tab
|   |   |   |   |   |   +-- Israel
|   |   |   |   |   |   +-- Jamaica
|   |   |   |   |   |   +-- Japan
|   |   |   |   |   |   +-- Kwajalein
|   |   |   |   |   |   +-- leapseconds
|   |   |   |   |   |   +-- Libya
|   |   |   |   |   |   +-- MET
|   |   |   |   |   |   +-- MST
|   |   |   |   |   |   +-- MST7MDT
|   |   |   |   |   |   +-- Navajo
|   |   |   |   |   |   +-- NZ
|   |   |   |   |   |   +-- NZ-CHAT
|   |   |   |   |   |   +-- Poland
|   |   |   |   |   |   +-- Portugal
|   |   |   |   |   |   +-- PRC
|   |   |   |   |   |   +-- PST8PDT
|   |   |   |   |   |   +-- ROC
|   |   |   |   |   |   +-- ROK
|   |   |   |   |   |   +-- Singapore
|   |   |   |   |   |   +-- Turkey
|   |   |   |   |   |   +-- tzdata.zi
|   |   |   |   |   |   +-- UCT
|   |   |   |   |   |   +-- Universal
|   |   |   |   |   |   +-- UTC
|   |   |   |   |   |   +-- WET
|   |   |   |   |   |   +-- W-SU
|   |   |   |   |   |   +-- zone.tab
|   |   |   |   |   |   +-- zone1970.tab
|   |   |   |   |   |   +-- zonenow.tab
|   |   |   |   |   |   +-- Zulu
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Africa/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Abidjan
|   |   |   |   |   |   |   +-- Accra
|   |   |   |   |   |   |   +-- Addis_Ababa
|   |   |   |   |   |   |   +-- Algiers
|   |   |   |   |   |   |   +-- Asmara
|   |   |   |   |   |   |   +-- Asmera
|   |   |   |   |   |   |   +-- Bamako
|   |   |   |   |   |   |   +-- Bangui
|   |   |   |   |   |   |   +-- Banjul
|   |   |   |   |   |   |   +-- Bissau
|   |   |   |   |   |   |   +-- Blantyre
|   |   |   |   |   |   |   +-- Brazzaville
|   |   |   |   |   |   |   +-- Bujumbura
|   |   |   |   |   |   |   +-- Cairo
|   |   |   |   |   |   |   +-- Casablanca
|   |   |   |   |   |   |   +-- Ceuta
|   |   |   |   |   |   |   +-- Conakry
|   |   |   |   |   |   |   +-- Dakar
|   |   |   |   |   |   |   +-- Dar_es_Salaam
|   |   |   |   |   |   |   +-- Djibouti
|   |   |   |   |   |   |   +-- Douala
|   |   |   |   |   |   |   +-- El_Aaiun
|   |   |   |   |   |   |   +-- Freetown
|   |   |   |   |   |   |   +-- Gaborone
|   |   |   |   |   |   |   +-- Harare
|   |   |   |   |   |   |   +-- Johannesburg
|   |   |   |   |   |   |   +-- Juba
|   |   |   |   |   |   |   +-- Kampala
|   |   |   |   |   |   |   +-- Khartoum
|   |   |   |   |   |   |   +-- Kigali
|   |   |   |   |   |   |   +-- Kinshasa
|   |   |   |   |   |   |   +-- Lagos
|   |   |   |   |   |   |   +-- Libreville
|   |   |   |   |   |   |   +-- Lome
|   |   |   |   |   |   |   +-- Luanda
|   |   |   |   |   |   |   +-- Lubumbashi
|   |   |   |   |   |   |   +-- Lusaka
|   |   |   |   |   |   |   +-- Malabo
|   |   |   |   |   |   |   +-- Maputo
|   |   |   |   |   |   |   +-- Maseru
|   |   |   |   |   |   |   +-- Mbabane
|   |   |   |   |   |   |   +-- Mogadishu
|   |   |   |   |   |   |   +-- Monrovia
|   |   |   |   |   |   |   +-- Nairobi
|   |   |   |   |   |   |   +-- Ndjamena
|   |   |   |   |   |   |   +-- Niamey
|   |   |   |   |   |   |   +-- Nouakchott
|   |   |   |   |   |   |   +-- Ouagadougou
|   |   |   |   |   |   |   +-- Porto-Novo
|   |   |   |   |   |   |   +-- Sao_Tome
|   |   |   |   |   |   |   +-- Timbuktu
|   |   |   |   |   |   |   +-- Tripoli
|   |   |   |   |   |   |   +-- Tunis
|   |   |   |   |   |   |   +-- Windhoek
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- America/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Adak
|   |   |   |   |   |   |   +-- Anchorage
|   |   |   |   |   |   |   +-- Anguilla
|   |   |   |   |   |   |   +-- Antigua
|   |   |   |   |   |   |   +-- Araguaina
|   |   |   |   |   |   |   +-- Aruba
|   |   |   |   |   |   |   +-- Asuncion
|   |   |   |   |   |   |   +-- Atikokan
|   |   |   |   |   |   |   +-- Atka
|   |   |   |   |   |   |   +-- Bahia
|   |   |   |   |   |   |   +-- Bahia_Banderas
|   |   |   |   |   |   |   +-- Barbados
|   |   |   |   |   |   |   +-- Belem
|   |   |   |   |   |   |   +-- Belize
|   |   |   |   |   |   |   +-- Blanc-Sablon
|   |   |   |   |   |   |   +-- Boa_Vista
|   |   |   |   |   |   |   +-- Bogota
|   |   |   |   |   |   |   +-- Boise
|   |   |   |   |   |   |   +-- Buenos_Aires
|   |   |   |   |   |   |   +-- Cambridge_Bay
|   |   |   |   |   |   |   +-- Campo_Grande
|   |   |   |   |   |   |   +-- Cancun
|   |   |   |   |   |   |   +-- Caracas
|   |   |   |   |   |   |   +-- Catamarca
|   |   |   |   |   |   |   +-- Cayenne
|   |   |   |   |   |   |   +-- Cayman
|   |   |   |   |   |   |   +-- Chicago
|   |   |   |   |   |   |   +-- Chihuahua
|   |   |   |   |   |   |   +-- Ciudad_Juarez
|   |   |   |   |   |   |   +-- Coral_Harbour
|   |   |   |   |   |   |   +-- Cordoba
|   |   |   |   |   |   |   +-- Costa_Rica
|   |   |   |   |   |   |   +-- Coyhaique
|   |   |   |   |   |   |   +-- Creston
|   |   |   |   |   |   |   +-- Cuiaba
|   |   |   |   |   |   |   +-- Curacao
|   |   |   |   |   |   |   +-- Danmarkshavn
|   |   |   |   |   |   |   +-- Dawson
|   |   |   |   |   |   |   +-- Dawson_Creek
|   |   |   |   |   |   |   +-- Denver
|   |   |   |   |   |   |   +-- Detroit
|   |   |   |   |   |   |   +-- Dominica
|   |   |   |   |   |   |   +-- Edmonton
|   |   |   |   |   |   |   +-- Eirunepe
|   |   |   |   |   |   |   +-- El_Salvador
|   |   |   |   |   |   |   +-- Ensenada
|   |   |   |   |   |   |   +-- Fort_Nelson
|   |   |   |   |   |   |   +-- Fort_Wayne
|   |   |   |   |   |   |   +-- Fortaleza
|   |   |   |   |   |   |   +-- Glace_Bay
|   |   |   |   |   |   |   +-- Godthab
|   |   |   |   |   |   |   +-- Goose_Bay
|   |   |   |   |   |   |   +-- Grand_Turk
|   |   |   |   |   |   |   +-- Grenada
|   |   |   |   |   |   |   +-- Guadeloupe
|   |   |   |   |   |   |   +-- Guatemala
|   |   |   |   |   |   |   +-- Guayaquil
|   |   |   |   |   |   |   +-- Guyana
|   |   |   |   |   |   |   +-- Halifax
|   |   |   |   |   |   |   +-- Havana
|   |   |   |   |   |   |   +-- Hermosillo
|   |   |   |   |   |   |   +-- Indianapolis
|   |   |   |   |   |   |   +-- Inuvik
|   |   |   |   |   |   |   +-- Iqaluit
|   |   |   |   |   |   |   +-- Jamaica
|   |   |   |   |   |   |   +-- Jujuy
|   |   |   |   |   |   |   +-- Juneau
|   |   |   |   |   |   |   +-- Knox_IN
|   |   |   |   |   |   |   +-- Kralendijk
|   |   |   |   |   |   |   +-- La_Paz
|   |   |   |   |   |   |   +-- Lima
|   |   |   |   |   |   |   +-- Los_Angeles
|   |   |   |   |   |   |   +-- Louisville
|   |   |   |   |   |   |   +-- Lower_Princes
|   |   |   |   |   |   |   +-- Maceio
|   |   |   |   |   |   |   +-- Managua
|   |   |   |   |   |   |   +-- Manaus
|   |   |   |   |   |   |   +-- Marigot
|   |   |   |   |   |   |   +-- Martinique
|   |   |   |   |   |   |   +-- Matamoros
|   |   |   |   |   |   |   +-- Mazatlan
|   |   |   |   |   |   |   +-- Mendoza
|   |   |   |   |   |   |   +-- Menominee
|   |   |   |   |   |   |   +-- Merida
|   |   |   |   |   |   |   +-- Metlakatla
|   |   |   |   |   |   |   +-- Mexico_City
|   |   |   |   |   |   |   +-- Miquelon
|   |   |   |   |   |   |   +-- Moncton
|   |   |   |   |   |   |   +-- Monterrey
|   |   |   |   |   |   |   +-- Montevideo
|   |   |   |   |   |   |   +-- Montreal
|   |   |   |   |   |   |   +-- Montserrat
|   |   |   |   |   |   |   +-- Nassau
|   |   |   |   |   |   |   +-- New_York
|   |   |   |   |   |   |   +-- Nipigon
|   |   |   |   |   |   |   +-- Nome
|   |   |   |   |   |   |   +-- Noronha
|   |   |   |   |   |   |   +-- Nuuk
|   |   |   |   |   |   |   +-- Ojinaga
|   |   |   |   |   |   |   +-- Panama
|   |   |   |   |   |   |   +-- Pangnirtung
|   |   |   |   |   |   |   +-- Paramaribo
|   |   |   |   |   |   |   +-- Phoenix
|   |   |   |   |   |   |   +-- Port_of_Spain
|   |   |   |   |   |   |   +-- Port-au-Prince
|   |   |   |   |   |   |   +-- Porto_Acre
|   |   |   |   |   |   |   +-- Porto_Velho
|   |   |   |   |   |   |   +-- Puerto_Rico
|   |   |   |   |   |   |   +-- Punta_Arenas
|   |   |   |   |   |   |   +-- Rainy_River
|   |   |   |   |   |   |   +-- Rankin_Inlet
|   |   |   |   |   |   |   +-- Recife
|   |   |   |   |   |   |   +-- Regina
|   |   |   |   |   |   |   +-- Resolute
|   |   |   |   |   |   |   +-- Rio_Branco
|   |   |   |   |   |   |   +-- Rosario
|   |   |   |   |   |   |   +-- Santa_Isabel
|   |   |   |   |   |   |   +-- Santarem
|   |   |   |   |   |   |   +-- Santiago
|   |   |   |   |   |   |   +-- Santo_Domingo
|   |   |   |   |   |   |   +-- Sao_Paulo
|   |   |   |   |   |   |   +-- Scoresbysund
|   |   |   |   |   |   |   +-- Shiprock
|   |   |   |   |   |   |   +-- Sitka
|   |   |   |   |   |   |   +-- St_Barthelemy
|   |   |   |   |   |   |   +-- St_Johns
|   |   |   |   |   |   |   +-- St_Kitts
|   |   |   |   |   |   |   +-- St_Lucia
|   |   |   |   |   |   |   +-- St_Thomas
|   |   |   |   |   |   |   +-- St_Vincent
|   |   |   |   |   |   |   +-- Swift_Current
|   |   |   |   |   |   |   +-- Tegucigalpa
|   |   |   |   |   |   |   +-- Thule
|   |   |   |   |   |   |   +-- Thunder_Bay
|   |   |   |   |   |   |   +-- Tijuana
|   |   |   |   |   |   |   +-- Toronto
|   |   |   |   |   |   |   +-- Tortola
|   |   |   |   |   |   |   +-- Vancouver
|   |   |   |   |   |   |   +-- Virgin
|   |   |   |   |   |   |   +-- Whitehorse
|   |   |   |   |   |   |   +-- Winnipeg
|   |   |   |   |   |   |   +-- Yakutat
|   |   |   |   |   |   |   +-- Yellowknife
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- Argentina/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- Buenos_Aires
|   |   |   |   |   |   |   |   +-- Catamarca
|   |   |   |   |   |   |   |   +-- ComodRivadavia
|   |   |   |   |   |   |   |   +-- Cordoba
|   |   |   |   |   |   |   |   +-- Jujuy
|   |   |   |   |   |   |   |   +-- La_Rioja
|   |   |   |   |   |   |   |   +-- Mendoza
|   |   |   |   |   |   |   |   +-- Rio_Gallegos
|   |   |   |   |   |   |   |   +-- Salta
|   |   |   |   |   |   |   |   +-- San_Juan
|   |   |   |   |   |   |   |   +-- San_Luis
|   |   |   |   |   |   |   |   +-- Tucuman
|   |   |   |   |   |   |   |   +-- Ushuaia
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- Indiana/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- Indianapolis
|   |   |   |   |   |   |   |   +-- Knox
|   |   |   |   |   |   |   |   +-- Marengo
|   |   |   |   |   |   |   |   +-- Petersburg
|   |   |   |   |   |   |   |   +-- Tell_City
|   |   |   |   |   |   |   |   +-- Vevay
|   |   |   |   |   |   |   |   +-- Vincennes
|   |   |   |   |   |   |   |   +-- Winamac
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- Kentucky/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- Louisville
|   |   |   |   |   |   |   |   +-- Monticello
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- North_Dakota/
|   |   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   |   +-- Beulah
|   |   |   |   |   |   |   |   +-- Center
|   |   |   |   |   |   |   |   +-- New_Salem
|   |   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Antarctica/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Casey
|   |   |   |   |   |   |   +-- Davis
|   |   |   |   |   |   |   +-- DumontDUrville
|   |   |   |   |   |   |   +-- Macquarie
|   |   |   |   |   |   |   +-- Mawson
|   |   |   |   |   |   |   +-- McMurdo
|   |   |   |   |   |   |   +-- Palmer
|   |   |   |   |   |   |   +-- Rothera
|   |   |   |   |   |   |   +-- South_Pole
|   |   |   |   |   |   |   +-- Syowa
|   |   |   |   |   |   |   +-- Troll
|   |   |   |   |   |   |   +-- Vostok
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Arctic/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Longyearbyen
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Asia/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Aden
|   |   |   |   |   |   |   +-- Almaty
|   |   |   |   |   |   |   +-- Amman
|   |   |   |   |   |   |   +-- Anadyr
|   |   |   |   |   |   |   +-- Aqtau
|   |   |   |   |   |   |   +-- Aqtobe
|   |   |   |   |   |   |   +-- Ashgabat
|   |   |   |   |   |   |   +-- Ashkhabad
|   |   |   |   |   |   |   +-- Atyrau
|   |   |   |   |   |   |   +-- Baghdad
|   |   |   |   |   |   |   +-- Bahrain
|   |   |   |   |   |   |   +-- Baku
|   |   |   |   |   |   |   +-- Bangkok
|   |   |   |   |   |   |   +-- Barnaul
|   |   |   |   |   |   |   +-- Beirut
|   |   |   |   |   |   |   +-- Bishkek
|   |   |   |   |   |   |   +-- Brunei
|   |   |   |   |   |   |   +-- Calcutta
|   |   |   |   |   |   |   +-- Chita
|   |   |   |   |   |   |   +-- Choibalsan
|   |   |   |   |   |   |   +-- Chongqing
|   |   |   |   |   |   |   +-- Chungking
|   |   |   |   |   |   |   +-- Colombo
|   |   |   |   |   |   |   +-- Dacca
|   |   |   |   |   |   |   +-- Damascus
|   |   |   |   |   |   |   +-- Dhaka
|   |   |   |   |   |   |   +-- Dili
|   |   |   |   |   |   |   +-- Dubai
|   |   |   |   |   |   |   +-- Dushanbe
|   |   |   |   |   |   |   +-- Famagusta
|   |   |   |   |   |   |   +-- Gaza
|   |   |   |   |   |   |   +-- Harbin
|   |   |   |   |   |   |   +-- Hebron
|   |   |   |   |   |   |   +-- Ho_Chi_Minh
|   |   |   |   |   |   |   +-- Hong_Kong
|   |   |   |   |   |   |   +-- Hovd
|   |   |   |   |   |   |   +-- Irkutsk
|   |   |   |   |   |   |   +-- Istanbul
|   |   |   |   |   |   |   +-- Jakarta
|   |   |   |   |   |   |   +-- Jayapura
|   |   |   |   |   |   |   +-- Jerusalem
|   |   |   |   |   |   |   +-- Kabul
|   |   |   |   |   |   |   +-- Kamchatka
|   |   |   |   |   |   |   +-- Karachi
|   |   |   |   |   |   |   +-- Kashgar
|   |   |   |   |   |   |   +-- Kathmandu
|   |   |   |   |   |   |   +-- Katmandu
|   |   |   |   |   |   |   +-- Khandyga
|   |   |   |   |   |   |   +-- Kolkata
|   |   |   |   |   |   |   +-- Krasnoyarsk
|   |   |   |   |   |   |   +-- Kuala_Lumpur
|   |   |   |   |   |   |   +-- Kuching
|   |   |   |   |   |   |   +-- Kuwait
|   |   |   |   |   |   |   +-- Macao
|   |   |   |   |   |   |   +-- Macau
|   |   |   |   |   |   |   +-- Magadan
|   |   |   |   |   |   |   +-- Makassar
|   |   |   |   |   |   |   +-- Manila
|   |   |   |   |   |   |   +-- Muscat
|   |   |   |   |   |   |   +-- Nicosia
|   |   |   |   |   |   |   +-- Novokuznetsk
|   |   |   |   |   |   |   +-- Novosibirsk
|   |   |   |   |   |   |   +-- Omsk
|   |   |   |   |   |   |   +-- Oral
|   |   |   |   |   |   |   +-- Phnom_Penh
|   |   |   |   |   |   |   +-- Pontianak
|   |   |   |   |   |   |   +-- Pyongyang
|   |   |   |   |   |   |   +-- Qatar
|   |   |   |   |   |   |   +-- Qostanay
|   |   |   |   |   |   |   +-- Qyzylorda
|   |   |   |   |   |   |   +-- Rangoon
|   |   |   |   |   |   |   +-- Riyadh
|   |   |   |   |   |   |   +-- Saigon
|   |   |   |   |   |   |   +-- Sakhalin
|   |   |   |   |   |   |   +-- Samarkand
|   |   |   |   |   |   |   +-- Seoul
|   |   |   |   |   |   |   +-- Shanghai
|   |   |   |   |   |   |   +-- Singapore
|   |   |   |   |   |   |   +-- Srednekolymsk
|   |   |   |   |   |   |   +-- Taipei
|   |   |   |   |   |   |   +-- Tashkent
|   |   |   |   |   |   |   +-- Tbilisi
|   |   |   |   |   |   |   +-- Tehran
|   |   |   |   |   |   |   +-- Tel_Aviv
|   |   |   |   |   |   |   +-- Thimbu
|   |   |   |   |   |   |   +-- Thimphu
|   |   |   |   |   |   |   +-- Tokyo
|   |   |   |   |   |   |   +-- Tomsk
|   |   |   |   |   |   |   +-- Ujung_Pandang
|   |   |   |   |   |   |   +-- Ulaanbaatar
|   |   |   |   |   |   |   +-- Ulan_Bator
|   |   |   |   |   |   |   +-- Urumqi
|   |   |   |   |   |   |   +-- Ust-Nera
|   |   |   |   |   |   |   +-- Vientiane
|   |   |   |   |   |   |   +-- Vladivostok
|   |   |   |   |   |   |   +-- Yakutsk
|   |   |   |   |   |   |   +-- Yangon
|   |   |   |   |   |   |   +-- Yekaterinburg
|   |   |   |   |   |   |   +-- Yerevan
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Atlantic/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Azores
|   |   |   |   |   |   |   +-- Bermuda
|   |   |   |   |   |   |   +-- Canary
|   |   |   |   |   |   |   +-- Cape_Verde
|   |   |   |   |   |   |   +-- Faeroe
|   |   |   |   |   |   |   +-- Faroe
|   |   |   |   |   |   |   +-- Jan_Mayen
|   |   |   |   |   |   |   +-- Madeira
|   |   |   |   |   |   |   +-- Reykjavik
|   |   |   |   |   |   |   +-- South_Georgia
|   |   |   |   |   |   |   +-- St_Helena
|   |   |   |   |   |   |   +-- Stanley
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Australia/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- ACT
|   |   |   |   |   |   |   +-- Adelaide
|   |   |   |   |   |   |   +-- Brisbane
|   |   |   |   |   |   |   +-- Broken_Hill
|   |   |   |   |   |   |   +-- Canberra
|   |   |   |   |   |   |   +-- Currie
|   |   |   |   |   |   |   +-- Darwin
|   |   |   |   |   |   |   +-- Eucla
|   |   |   |   |   |   |   +-- Hobart
|   |   |   |   |   |   |   +-- LHI
|   |   |   |   |   |   |   +-- Lindeman
|   |   |   |   |   |   |   +-- Lord_Howe
|   |   |   |   |   |   |   +-- Melbourne
|   |   |   |   |   |   |   +-- North
|   |   |   |   |   |   |   +-- NSW
|   |   |   |   |   |   |   +-- Perth
|   |   |   |   |   |   |   +-- Queensland
|   |   |   |   |   |   |   +-- South
|   |   |   |   |   |   |   +-- Sydney
|   |   |   |   |   |   |   +-- Tasmania
|   |   |   |   |   |   |   +-- Victoria
|   |   |   |   |   |   |   +-- West
|   |   |   |   |   |   |   +-- Yancowinna
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Brazil/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Acre
|   |   |   |   |   |   |   +-- DeNoronha
|   |   |   |   |   |   |   +-- East
|   |   |   |   |   |   |   +-- West
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Canada/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Atlantic
|   |   |   |   |   |   |   +-- Central
|   |   |   |   |   |   |   +-- Eastern
|   |   |   |   |   |   |   +-- Mountain
|   |   |   |   |   |   |   +-- Newfoundland
|   |   |   |   |   |   |   +-- Pacific
|   |   |   |   |   |   |   +-- Saskatchewan
|   |   |   |   |   |   |   +-- Yukon
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Chile/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Continental
|   |   |   |   |   |   |   +-- EasterIsland
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Etc/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- GMT
|   |   |   |   |   |   |   +-- GMT+0
|   |   |   |   |   |   |   +-- GMT+1
|   |   |   |   |   |   |   +-- GMT+10
|   |   |   |   |   |   |   +-- GMT+11
|   |   |   |   |   |   |   +-- GMT+12
|   |   |   |   |   |   |   +-- GMT+2
|   |   |   |   |   |   |   +-- GMT+3
|   |   |   |   |   |   |   +-- GMT+4
|   |   |   |   |   |   |   +-- GMT+5
|   |   |   |   |   |   |   +-- GMT+6
|   |   |   |   |   |   |   +-- GMT+7
|   |   |   |   |   |   |   +-- GMT+8
|   |   |   |   |   |   |   +-- GMT+9
|   |   |   |   |   |   |   +-- GMT0
|   |   |   |   |   |   |   +-- GMT-0
|   |   |   |   |   |   |   +-- GMT-1
|   |   |   |   |   |   |   +-- GMT-10
|   |   |   |   |   |   |   +-- GMT-11
|   |   |   |   |   |   |   +-- GMT-12
|   |   |   |   |   |   |   +-- GMT-13
|   |   |   |   |   |   |   +-- GMT-14
|   |   |   |   |   |   |   +-- GMT-2
|   |   |   |   |   |   |   +-- GMT-3
|   |   |   |   |   |   |   +-- GMT-4
|   |   |   |   |   |   |   +-- GMT-5
|   |   |   |   |   |   |   +-- GMT-6
|   |   |   |   |   |   |   +-- GMT-7
|   |   |   |   |   |   |   +-- GMT-8
|   |   |   |   |   |   |   +-- GMT-9
|   |   |   |   |   |   |   +-- Greenwich
|   |   |   |   |   |   |   +-- UCT
|   |   |   |   |   |   |   +-- Universal
|   |   |   |   |   |   |   +-- UTC
|   |   |   |   |   |   |   +-- Zulu
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Europe/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Amsterdam
|   |   |   |   |   |   |   +-- Andorra
|   |   |   |   |   |   |   +-- Astrakhan
|   |   |   |   |   |   |   +-- Athens
|   |   |   |   |   |   |   +-- Belfast
|   |   |   |   |   |   |   +-- Belgrade
|   |   |   |   |   |   |   +-- Berlin
|   |   |   |   |   |   |   +-- Bratislava
|   |   |   |   |   |   |   +-- Brussels
|   |   |   |   |   |   |   +-- Bucharest
|   |   |   |   |   |   |   +-- Budapest
|   |   |   |   |   |   |   +-- Busingen
|   |   |   |   |   |   |   +-- Chisinau
|   |   |   |   |   |   |   +-- Copenhagen
|   |   |   |   |   |   |   +-- Dublin
|   |   |   |   |   |   |   +-- Gibraltar
|   |   |   |   |   |   |   +-- Guernsey
|   |   |   |   |   |   |   +-- Helsinki
|   |   |   |   |   |   |   +-- Isle_of_Man
|   |   |   |   |   |   |   +-- Istanbul
|   |   |   |   |   |   |   +-- Jersey
|   |   |   |   |   |   |   +-- Kaliningrad
|   |   |   |   |   |   |   +-- Kiev
|   |   |   |   |   |   |   +-- Kirov
|   |   |   |   |   |   |   +-- Kyiv
|   |   |   |   |   |   |   +-- Lisbon
|   |   |   |   |   |   |   +-- Ljubljana
|   |   |   |   |   |   |   +-- London
|   |   |   |   |   |   |   +-- Luxembourg
|   |   |   |   |   |   |   +-- Madrid
|   |   |   |   |   |   |   +-- Malta
|   |   |   |   |   |   |   +-- Mariehamn
|   |   |   |   |   |   |   +-- Minsk
|   |   |   |   |   |   |   +-- Monaco
|   |   |   |   |   |   |   +-- Moscow
|   |   |   |   |   |   |   +-- Nicosia
|   |   |   |   |   |   |   +-- Oslo
|   |   |   |   |   |   |   +-- Paris
|   |   |   |   |   |   |   +-- Podgorica
|   |   |   |   |   |   |   +-- Prague
|   |   |   |   |   |   |   +-- Riga
|   |   |   |   |   |   |   +-- Rome
|   |   |   |   |   |   |   +-- Samara
|   |   |   |   |   |   |   +-- San_Marino
|   |   |   |   |   |   |   +-- Sarajevo
|   |   |   |   |   |   |   +-- Saratov
|   |   |   |   |   |   |   +-- Simferopol
|   |   |   |   |   |   |   +-- Skopje
|   |   |   |   |   |   |   +-- Sofia
|   |   |   |   |   |   |   +-- Stockholm
|   |   |   |   |   |   |   +-- Tallinn
|   |   |   |   |   |   |   +-- Tirane
|   |   |   |   |   |   |   +-- Tiraspol
|   |   |   |   |   |   |   +-- Ulyanovsk
|   |   |   |   |   |   |   +-- Uzhgorod
|   |   |   |   |   |   |   +-- Vaduz
|   |   |   |   |   |   |   +-- Vatican
|   |   |   |   |   |   |   +-- Vienna
|   |   |   |   |   |   |   +-- Vilnius
|   |   |   |   |   |   |   +-- Volgograd
|   |   |   |   |   |   |   +-- Warsaw
|   |   |   |   |   |   |   +-- Zagreb
|   |   |   |   |   |   |   +-- Zaporozhye
|   |   |   |   |   |   |   +-- Zurich
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Indian/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Antananarivo
|   |   |   |   |   |   |   +-- Chagos
|   |   |   |   |   |   |   +-- Christmas
|   |   |   |   |   |   |   +-- Cocos
|   |   |   |   |   |   |   +-- Comoro
|   |   |   |   |   |   |   +-- Kerguelen
|   |   |   |   |   |   |   +-- Mahe
|   |   |   |   |   |   |   +-- Maldives
|   |   |   |   |   |   |   +-- Mauritius
|   |   |   |   |   |   |   +-- Mayotte
|   |   |   |   |   |   |   +-- Reunion
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Mexico/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- BajaNorte
|   |   |   |   |   |   |   +-- BajaSur
|   |   |   |   |   |   |   +-- General
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- Pacific/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Apia
|   |   |   |   |   |   |   +-- Auckland
|   |   |   |   |   |   |   +-- Bougainville
|   |   |   |   |   |   |   +-- Chatham
|   |   |   |   |   |   |   +-- Chuuk
|   |   |   |   |   |   |   +-- Easter
|   |   |   |   |   |   |   +-- Efate
|   |   |   |   |   |   |   +-- Enderbury
|   |   |   |   |   |   |   +-- Fakaofo
|   |   |   |   |   |   |   +-- Fiji
|   |   |   |   |   |   |   +-- Funafuti
|   |   |   |   |   |   |   +-- Galapagos
|   |   |   |   |   |   |   +-- Gambier
|   |   |   |   |   |   |   +-- Guadalcanal
|   |   |   |   |   |   |   +-- Guam
|   |   |   |   |   |   |   +-- Honolulu
|   |   |   |   |   |   |   +-- Johnston
|   |   |   |   |   |   |   +-- Kanton
|   |   |   |   |   |   |   +-- Kiritimati
|   |   |   |   |   |   |   +-- Kosrae
|   |   |   |   |   |   |   +-- Kwajalein
|   |   |   |   |   |   |   +-- Majuro
|   |   |   |   |   |   |   +-- Marquesas
|   |   |   |   |   |   |   +-- Midway
|   |   |   |   |   |   |   +-- Nauru
|   |   |   |   |   |   |   +-- Niue
|   |   |   |   |   |   |   +-- Norfolk
|   |   |   |   |   |   |   +-- Noumea
|   |   |   |   |   |   |   +-- Pago_Pago
|   |   |   |   |   |   |   +-- Palau
|   |   |   |   |   |   |   +-- Pitcairn
|   |   |   |   |   |   |   +-- Pohnpei
|   |   |   |   |   |   |   +-- Ponape
|   |   |   |   |   |   |   +-- Port_Moresby
|   |   |   |   |   |   |   +-- Rarotonga
|   |   |   |   |   |   |   +-- Saipan
|   |   |   |   |   |   |   +-- Samoa
|   |   |   |   |   |   |   +-- Tahiti
|   |   |   |   |   |   |   +-- Tarawa
|   |   |   |   |   |   |   +-- Tongatapu
|   |   |   |   |   |   |   +-- Truk
|   |   |   |   |   |   |   +-- Wake
|   |   |   |   |   |   |   +-- Wallis
|   |   |   |   |   |   |   +-- Yap
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- US/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- Alaska
|   |   |   |   |   |   |   +-- Aleutian
|   |   |   |   |   |   |   +-- Arizona
|   |   |   |   |   |   |   +-- Central
|   |   |   |   |   |   |   +-- Eastern
|   |   |   |   |   |   |   +-- East-Indiana
|   |   |   |   |   |   |   +-- Hawaii
|   |   |   |   |   |   |   +-- Indiana-Starke
|   |   |   |   |   |   |   +-- Michigan
|   |   |   |   |   |   |   +-- Mountain
|   |   |   |   |   |   |   +-- Pacific
|   |   |   |   |   |   |   +-- Samoa
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   +-- tzdata-2025.2.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE
|   |   |   |   |   |   +-- licenses/
|   |   |   |   |   |   |   +-- LICENSE_APACHE
|   |   |   |   +-- urllib3/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _base_connection.py
|   |   |   |   |   +-- _collections.py
|   |   |   |   |   +-- _request_methods.py
|   |   |   |   |   +-- _version.py
|   |   |   |   |   +-- connection.py
|   |   |   |   |   +-- connectionpool.py
|   |   |   |   |   +-- exceptions.py
|   |   |   |   |   +-- fields.py
|   |   |   |   |   +-- filepost.py
|   |   |   |   |   +-- poolmanager.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- response.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _base_connection.cpython-311.pyc
|   |   |   |   |   |   +-- _collections.cpython-311.pyc
|   |   |   |   |   |   +-- _request_methods.cpython-311.pyc
|   |   |   |   |   |   +-- _version.cpython-311.pyc
|   |   |   |   |   |   +-- connection.cpython-311.pyc
|   |   |   |   |   |   +-- connectionpool.cpython-311.pyc
|   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   +-- fields.cpython-311.pyc
|   |   |   |   |   |   +-- filepost.cpython-311.pyc
|   |   |   |   |   |   +-- poolmanager.cpython-311.pyc
|   |   |   |   |   |   +-- response.cpython-311.pyc
|   |   |   |   |   +-- contrib/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- pyopenssl.py
|   |   |   |   |   |   +-- socks.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- pyopenssl.cpython-311.pyc
|   |   |   |   |   |   |   +-- socks.cpython-311.pyc
|   |   |   |   |   |   +-- emscripten/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- connection.py
|   |   |   |   |   |   |   +-- emscripten_fetch_worker.js
|   |   |   |   |   |   |   +-- fetch.py
|   |   |   |   |   |   |   +-- request.py
|   |   |   |   |   |   |   +-- response.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- connection.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- fetch.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- request.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- response.cpython-311.pyc
|   |   |   |   |   +-- http2/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- connection.py
|   |   |   |   |   |   +-- probe.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- connection.cpython-311.pyc
|   |   |   |   |   |   |   +-- probe.cpython-311.pyc
|   |   |   |   |   +-- util/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- connection.py
|   |   |   |   |   |   +-- proxy.py
|   |   |   |   |   |   +-- request.py
|   |   |   |   |   |   +-- response.py
|   |   |   |   |   |   +-- retry.py
|   |   |   |   |   |   +-- ssl_.py
|   |   |   |   |   |   +-- ssl_match_hostname.py
|   |   |   |   |   |   +-- ssltransport.py
|   |   |   |   |   |   +-- timeout.py
|   |   |   |   |   |   +-- url.py
|   |   |   |   |   |   +-- util.py
|   |   |   |   |   |   +-- wait.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- connection.cpython-311.pyc
|   |   |   |   |   |   |   +-- proxy.cpython-311.pyc
|   |   |   |   |   |   |   +-- request.cpython-311.pyc
|   |   |   |   |   |   |   +-- response.cpython-311.pyc
|   |   |   |   |   |   |   +-- retry.cpython-311.pyc
|   |   |   |   |   |   |   +-- ssl_.cpython-311.pyc
|   |   |   |   |   |   |   +-- ssl_match_hostname.cpython-311.pyc
|   |   |   |   |   |   |   +-- ssltransport.cpython-311.pyc
|   |   |   |   |   |   |   +-- timeout.cpython-311.pyc
|   |   |   |   |   |   |   +-- url.cpython-311.pyc
|   |   |   |   |   |   |   +-- util.cpython-311.pyc
|   |   |   |   |   |   |   +-- wait.cpython-311.pyc
|   |   |   |   +-- urllib3-2.5.0.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   +-- watchdog/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- events.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- version.py
|   |   |   |   |   +-- watchmedo.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- events.cpython-311.pyc
|   |   |   |   |   |   +-- version.cpython-311.pyc
|   |   |   |   |   |   +-- watchmedo.cpython-311.pyc
|   |   |   |   |   +-- observers/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- api.py
|   |   |   |   |   |   +-- fsevents.py
|   |   |   |   |   |   +-- fsevents2.py
|   |   |   |   |   |   +-- inotify.py
|   |   |   |   |   |   +-- inotify_buffer.py
|   |   |   |   |   |   +-- inotify_c.py
|   |   |   |   |   |   +-- kqueue.py
|   |   |   |   |   |   +-- polling.py
|   |   |   |   |   |   +-- read_directory_changes.py
|   |   |   |   |   |   +-- winapi.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- api.cpython-311.pyc
|   |   |   |   |   |   |   +-- fsevents.cpython-311.pyc
|   |   |   |   |   |   |   +-- fsevents2.cpython-311.pyc
|   |   |   |   |   |   |   +-- inotify.cpython-311.pyc
|   |   |   |   |   |   |   +-- inotify_buffer.cpython-311.pyc
|   |   |   |   |   |   |   +-- inotify_c.cpython-311.pyc
|   |   |   |   |   |   |   +-- kqueue.cpython-311.pyc
|   |   |   |   |   |   |   +-- polling.cpython-311.pyc
|   |   |   |   |   |   |   +-- read_directory_changes.cpython-311.pyc
|   |   |   |   |   |   |   +-- winapi.cpython-311.pyc
|   |   |   |   |   +-- tricks/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   +-- utils/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- bricks.py
|   |   |   |   |   |   +-- delayed_queue.py
|   |   |   |   |   |   +-- dirsnapshot.py
|   |   |   |   |   |   +-- echo.py
|   |   |   |   |   |   +-- event_debouncer.py
|   |   |   |   |   |   +-- patterns.py
|   |   |   |   |   |   +-- platform.py
|   |   |   |   |   |   +-- process_watcher.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- bricks.cpython-311.pyc
|   |   |   |   |   |   |   +-- delayed_queue.cpython-311.pyc
|   |   |   |   |   |   |   +-- dirsnapshot.cpython-311.pyc
|   |   |   |   |   |   |   +-- echo.cpython-311.pyc
|   |   |   |   |   |   |   +-- event_debouncer.cpython-311.pyc
|   |   |   |   |   |   |   +-- patterns.cpython-311.pyc
|   |   |   |   |   |   |   +-- platform.cpython-311.pyc
|   |   |   |   |   |   |   +-- process_watcher.cpython-311.pyc
|   |   |   |   +-- watchdog-6.0.0.dist-info/
|   |   |   |   |   +-- AUTHORS
|   |   |   |   |   +-- COPYING
|   |   |   |   |   +-- entry_points.txt
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- LICENSE
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- REQUESTED
|   |   |   |   |   +-- top_level.txt
|   |   |   |   |   +-- WHEEL
|   |   |   |   +-- werkzeug/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- _internal.py
|   |   |   |   |   +-- _reloader.py
|   |   |   |   |   +-- exceptions.py
|   |   |   |   |   +-- formparser.py
|   |   |   |   |   +-- http.py
|   |   |   |   |   +-- local.py
|   |   |   |   |   +-- py.typed
|   |   |   |   |   +-- security.py
|   |   |   |   |   +-- serving.py
|   |   |   |   |   +-- test.py
|   |   |   |   |   +-- testapp.py
|   |   |   |   |   +-- urls.py
|   |   |   |   |   +-- user_agent.py
|   |   |   |   |   +-- utils.py
|   |   |   |   |   +-- wsgi.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- _internal.cpython-311.pyc
|   |   |   |   |   |   +-- _reloader.cpython-311.pyc
|   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   +-- formparser.cpython-311.pyc
|   |   |   |   |   |   +-- http.cpython-311.pyc
|   |   |   |   |   |   +-- local.cpython-311.pyc
|   |   |   |   |   |   +-- security.cpython-311.pyc
|   |   |   |   |   |   +-- serving.cpython-311.pyc
|   |   |   |   |   |   +-- test.cpython-311.pyc
|   |   |   |   |   |   +-- testapp.cpython-311.pyc
|   |   |   |   |   |   +-- urls.cpython-311.pyc
|   |   |   |   |   |   +-- user_agent.cpython-311.pyc
|   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   |   +-- wsgi.cpython-311.pyc
|   |   |   |   |   +-- datastructures/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- accept.py
|   |   |   |   |   |   +-- auth.py
|   |   |   |   |   |   +-- cache_control.py
|   |   |   |   |   |   +-- csp.py
|   |   |   |   |   |   +-- etag.py
|   |   |   |   |   |   +-- file_storage.py
|   |   |   |   |   |   +-- headers.py
|   |   |   |   |   |   +-- mixins.py
|   |   |   |   |   |   +-- range.py
|   |   |   |   |   |   +-- structures.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- accept.cpython-311.pyc
|   |   |   |   |   |   |   +-- auth.cpython-311.pyc
|   |   |   |   |   |   |   +-- cache_control.cpython-311.pyc
|   |   |   |   |   |   |   +-- csp.cpython-311.pyc
|   |   |   |   |   |   |   +-- etag.cpython-311.pyc
|   |   |   |   |   |   |   +-- file_storage.cpython-311.pyc
|   |   |   |   |   |   |   +-- headers.cpython-311.pyc
|   |   |   |   |   |   |   +-- mixins.cpython-311.pyc
|   |   |   |   |   |   |   +-- range.cpython-311.pyc
|   |   |   |   |   |   |   +-- structures.cpython-311.pyc
|   |   |   |   |   +-- debug/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- console.py
|   |   |   |   |   |   +-- repr.py
|   |   |   |   |   |   +-- tbtools.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- console.cpython-311.pyc
|   |   |   |   |   |   |   +-- repr.cpython-311.pyc
|   |   |   |   |   |   |   +-- tbtools.cpython-311.pyc
|   |   |   |   |   |   +-- shared/
|   |   |   |   |   |   |   +-- console.png
|   |   |   |   |   |   |   +-- debugger.js
|   |   |   |   |   |   |   +-- ICON_LICENSE.md
|   |   |   |   |   |   |   +-- less.png
|   |   |   |   |   |   |   +-- more.png
|   |   |   |   |   |   |   +-- style.css
|   |   |   |   |   +-- middleware/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- dispatcher.py
|   |   |   |   |   |   +-- http_proxy.py
|   |   |   |   |   |   +-- lint.py
|   |   |   |   |   |   +-- profiler.py
|   |   |   |   |   |   +-- proxy_fix.py
|   |   |   |   |   |   +-- shared_data.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- dispatcher.cpython-311.pyc
|   |   |   |   |   |   |   +-- http_proxy.cpython-311.pyc
|   |   |   |   |   |   |   +-- lint.cpython-311.pyc
|   |   |   |   |   |   |   +-- profiler.cpython-311.pyc
|   |   |   |   |   |   |   +-- proxy_fix.cpython-311.pyc
|   |   |   |   |   |   |   +-- shared_data.cpython-311.pyc
|   |   |   |   |   +-- routing/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- converters.py
|   |   |   |   |   |   +-- exceptions.py
|   |   |   |   |   |   +-- map.py
|   |   |   |   |   |   +-- matcher.py
|   |   |   |   |   |   +-- rules.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- converters.cpython-311.pyc
|   |   |   |   |   |   |   +-- exceptions.cpython-311.pyc
|   |   |   |   |   |   |   +-- map.cpython-311.pyc
|   |   |   |   |   |   |   +-- matcher.cpython-311.pyc
|   |   |   |   |   |   |   +-- rules.cpython-311.pyc
|   |   |   |   |   +-- sansio/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- http.py
|   |   |   |   |   |   +-- multipart.py
|   |   |   |   |   |   +-- request.py
|   |   |   |   |   |   +-- response.py
|   |   |   |   |   |   +-- utils.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- http.cpython-311.pyc
|   |   |   |   |   |   |   +-- multipart.cpython-311.pyc
|   |   |   |   |   |   |   +-- request.cpython-311.pyc
|   |   |   |   |   |   |   +-- response.cpython-311.pyc
|   |   |   |   |   |   |   +-- utils.cpython-311.pyc
|   |   |   |   |   +-- wrappers/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- request.py
|   |   |   |   |   |   +-- response.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- request.cpython-311.pyc
|   |   |   |   |   |   |   +-- response.cpython-311.pyc
|   |   |   |   +-- werkzeug-3.1.4.dist-info/
|   |   |   |   |   +-- INSTALLER
|   |   |   |   |   +-- METADATA
|   |   |   |   |   +-- RECORD
|   |   |   |   |   +-- WHEEL
|   |   |   |   |   +-- licenses/
|   |   |   |   |   |   +-- LICENSE.txt
|   |   |   |   +-- win32ctypes/
|   |   |   |   |   +-- __init__.py
|   |   |   |   |   +-- pywintypes.py
|   |   |   |   |   +-- version.py
|   |   |   |   |   +-- win32api.py
|   |   |   |   |   +-- win32cred.py
|   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   +-- pywintypes.cpython-311.pyc
|   |   |   |   |   |   +-- version.cpython-311.pyc
|   |   |   |   |   |   +-- win32api.cpython-311.pyc
|   |   |   |   |   |   +-- win32cred.cpython-311.pyc
|   |   |   |   |   +-- core/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- _winerrors.py
|   |   |   |   |   |   +-- compat.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- _winerrors.cpython-311.pyc
|   |   |   |   |   |   |   +-- compat.cpython-311.pyc
|   |   |   |   |   |   +-- cffi/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _authentication.py
|   |   |   |   |   |   |   +-- _common.py
|   |   |   |   |   |   |   +-- _dll.py
|   |   |   |   |   |   |   +-- _nl_support.py
|   |   |   |   |   |   |   +-- _resource.py
|   |   |   |   |   |   |   +-- _system_information.py
|   |   |   |   |   |   |   +-- _time.py
|   |   |   |   |   |   |   +-- _util.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _authentication.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _dll.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _nl_support.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _resource.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _system_information.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _time.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _util.cpython-311.pyc
|   |   |   |   |   |   +-- ctypes/
|   |   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   |   +-- _authentication.py
|   |   |   |   |   |   |   +-- _common.py
|   |   |   |   |   |   |   +-- _dll.py
|   |   |   |   |   |   |   +-- _nl_support.py
|   |   |   |   |   |   |   +-- _resource.py
|   |   |   |   |   |   |   +-- _system_information.py
|   |   |   |   |   |   |   +-- _time.py
|   |   |   |   |   |   |   +-- _util.py
|   |   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _authentication.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _common.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _dll.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _nl_support.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _resource.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _system_information.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _time.cpython-311.pyc
|   |   |   |   |   |   |   |   +-- _util.cpython-311.pyc
|   |   |   |   |   +-- pywin32/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- pywintypes.py
|   |   |   |   |   |   +-- win32api.py
|   |   |   |   |   |   +-- win32cred.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- pywintypes.cpython-311.pyc
|   |   |   |   |   |   |   +-- win32api.cpython-311.pyc
|   |   |   |   |   |   |   +-- win32cred.cpython-311.pyc
|   |   |   |   |   +-- tests/
|   |   |   |   |   |   +-- __init__.py
|   |   |   |   |   |   +-- test_backends.py
|   |   |   |   |   |   +-- test_win32api.py
|   |   |   |   |   |   +-- test_win32cred.py
|   |   |   |   |   |   +-- __pycache__/
|   |   |   |   |   |   |   +-- __init__.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_backends.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_win32api.cpython-311.pyc
|   |   |   |   |   |   |   +-- test_win32cred.cpython-311.pyc
|   |   +-- Scripts/
|   |   |   +-- activate
|   |   |   +-- activate.bat
|   |   |   +-- Activate.ps1
|   |   |   +-- deactivate.bat
|   |   |   +-- f2py.exe
|   |   |   +-- flask.exe
|   |   |   +-- normalizer.exe
|   |   |   +-- numpy-config.exe
|   |   |   +-- pip.exe
|   |   |   +-- pip3.11.exe
|   |   |   +-- pip3.exe
|   |   |   +-- pyi-archive_viewer.exe
|   |   |   +-- pyi-bindepend.exe
|   |   |   +-- pyi-grab_version.exe
|   |   |   +-- pyi-makespec.exe
|   |   |   +-- pyinstaller.exe
|   |   |   +-- pyi-set_version.exe
|   |   |   +-- python.exe
|   |   |   +-- pythonw.exe
|   |   |   +-- qr.exe
|   |   |   +-- watchmedo.exe
+-- Installer/
|   +-- QR_Attendance_Standalone_Setup.exe


---

## Requirements

- Python 3.x
- Packages (if any, see requirements.txt)

---

## Installation & Usage

1. Clone the repository:

git clone https://github.com/Snoozzee1027/AttendanceSystemIDSC.git
cd f4

2. Install dependencies:

pip install -r requirements.txt

3. Run the main program:

python main.py
> Replace 'main.py' with your actual main script if different.

---

## License

This project is for personal or educational use.
