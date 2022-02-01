# Default settings file for the website
PORT = 80
ENABLE_HTTPS = False
ENABLE_LOGGING = False
LOG_TO_FILE = False
ENABLE_TESTPAGE = False
SERVE_STATIC = False
SERVE_STORAGE = False
SERVE_JS = False
CERT_DIR = 'path/to/cert'
CERT_ROOT = 'CERT_ROOT'
TARGET_HOST = 'hiden64.duckdns.org'

# Import settings from settings_local.py. If settings_local.py is not present, terminate
try:
	from settings_local import *
except ImportError:
	raise Exception("settings_local.py not found, please create it.")