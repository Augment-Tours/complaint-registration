import os

ENV_KEY = 'HEROKU_PROJECT'
PROD_APPLICATION_ID = 'security-backend-prod'

if os.getenv(ENV_KEY, None) == PROD_APPLICATION_ID:
    from .production import *
else:
    # TODO: change to testing
    from .testing import *
