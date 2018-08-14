from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dev_secret'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

MEDIA_ROOT = '{}/assets/uploads/'.format(os.environ['PROJECT_HOME'])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sc2w',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'mysql',
        'PORT': '3306',
        'OPTIONS': {
             'init_command': 'SET foreign_key_checks = 0;',
        }
    }
    
}
