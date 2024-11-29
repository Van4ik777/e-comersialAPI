from config.settings.base import *# NOQA
import os

SECRET_KEY = "django-insecure-^at&*_lw2l40k&syn3wy2!i7o*jko_yp3i@(vx3(h%kiteb9tc"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += []
MIDDLEWARE += []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', 5432),
    }
}

STATIC_URL = "static/"


SECRET_KEY = "django-insecure-^at&*_lw2l40k&syn3wy2!i7o*jko_yp3i@(vx3(h%kiteb9tc"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += []
MIDDLEWARE += []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST", "eComersial"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

STATIC_URL = "static/"
