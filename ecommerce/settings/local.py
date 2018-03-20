from .base import *

MEDIA_URL='/media/'
MEDIA_ROOT='media'
STATIC_URL = '/static/'
STATIC_ROOT='staticfiles'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'