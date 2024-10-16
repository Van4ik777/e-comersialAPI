from config.settings.base import INSTALLED_APPS, MIDDLEWARE, BASE_DIR  # NOQA

SECRET_KEY = "django-insecure-^at&*_lw2l40k&syn3wy2!i7o*jko_yp3i@(vx3(h%kiteb9tc"

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += []
MIDDLEWARE += []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"
