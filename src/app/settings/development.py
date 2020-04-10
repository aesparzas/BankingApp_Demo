from .base import *


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'banking_database',
            'USER': 'root',
            'PASSWORD': '100Tacvbo.',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
