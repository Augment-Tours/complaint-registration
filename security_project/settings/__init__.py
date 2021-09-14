from firebase_admin import credentials
import firebase_admin
import os

ENV_KEY = 'HEROKU_PROJECT'
PROD_APPLICATION_ID = 'security-backend-prod'

if os.getenv(ENV_KEY, None) == PROD_APPLICATION_ID:
    from .production import *
else:
    # TODO: change to testing
    from .testing import *


cred = credentials.Certificate(os.path.join(
    BASE_DIR, 'settings/firebase_key.json'))
default_app = firebase_admin.initialize_app(cred)
