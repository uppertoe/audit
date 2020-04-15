from .base import *
from .secret_settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = prod_secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['anaesthesiology.pythonanywhere.com',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}