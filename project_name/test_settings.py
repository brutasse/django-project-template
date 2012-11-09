import warnings
warnings.simplefilter('always')

from .settings import *  # noqa

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
EMAIL_HOST = 'dummy'
MEDIA_ROOT = os.path.join(HERE, 'test_media')

INSTALLED_APPS += (
    'tests',
)
