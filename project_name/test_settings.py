import warnings
warnings.simplefilter('always')

from .settings import *  # noqa

SECRET_KEY = 'test secret key'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
EMAIL_HOST = 'dummy'
MEDIA_ROOT = os.path.join(HERE, 'test_media')
