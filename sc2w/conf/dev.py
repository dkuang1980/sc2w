from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dev_secret'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sc2w',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'mysql',  
        'PORT': '3306',
    }
}