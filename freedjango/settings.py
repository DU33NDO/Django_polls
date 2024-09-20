"""
Django settings for freedjango project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#g-84&bph@pj@qoq@i4rsr&k-b$8v=5br9vs^m+j32i6mg)7d&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "users.apps.UsersConfig",
    "polygraphy.apps.PolygraphyConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "kaspi",
    "polls",
    "social_django",
    "bootstrap4",
    "rest_framework",
    "corsheaders",
    "rest_framework_simplejwt",
    # "userprofile",
]
AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.instagram.InstagramOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_URL_NAMESPACE = "social"
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "AIzaSyD37WOn_vZzfPQE3l38SizKzZQe5eQp_jo"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "R_9x9eTV6uooV_JysalVTlNpLUA"


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "django.middleware.cache.UpdateCacheMiddleware",
    # "django.middleware.common.CommonMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",
    "freedjango.middleware.atr_middleware",
    "freedjango.middleware.CustomMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = "freedjango.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["MyTemplates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
            "libraries": {"filtersandtags": "freedjango.templatetags.filtersandtags"},
        },
    },
]

WSGI_APPLICATION = "freedjango.wsgi.application"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # "DEFAULT_PERMISSION_CLASSES": [
    #     "rest_framework.permissions.IsAuthenticated",
    # ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10),
    # "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "secondForClassWorkDjango",
#         "USER": "postgres",
#         "PASSWORD": "MAL123",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {"()": "django.utils.log.RequireDebugTrue"},
    },
    "formatters": {
        "simple": {
            "format": "[%(asctime)s] %(levelname)s: %(message)s",
            "datefmt": "%Y.%m.%d %H:%M:%S",
        }
    },
    "handlers": {
        "console_dev": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "filters": ["require_debug_true"],
        },
        "console_prod": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "ERROR",
            "filters": ["require_debug_false"],
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "../django-site.log",
            "maxBytes": 1048576,
            "backupCount": 10,
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console_dev", "console_prod"],
        },
        "django.server": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

IS_HEROKU_APP = "DYNO" in os.environ and not "CI" in os.environ

if not IS_HEROKU_APP:
    DEBUG = True

if IS_HEROKU_APP:
    # In production on Heroku the database configuration is derived from the `DATABASE_URL`
    # environment variable by the dj-database-url package. `DATABASE_URL` will be set
    # automatically by Heroku when a database addon is attached to your Heroku app. See:
    # https://devcenter.heroku.com/articles/provisioning-heroku-postgres#application-config-vars
    # https://github.com/jazzband/dj-database-url
    DATABASES = {
        "default": dj_database_url.config(
            env="DATABASE_URL",
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True,
        ),
    }
else:
    # When running locally in development or in CI, a sqlite database file will be used instead
    # to simplify initial setup. Longer term it's recommended to use Postgres locally too.
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis-14726.c302.asia-northeast1-1.gce.redns.redis-cloud.com:14726",
        "OPTIONS": {
            "PASSWORD": "JaCqTWn1FdtsgoL9Bt35Ht50GKmRztAm",
        },
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_CACHE_ALIAS = 'session_storage'

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 30
CACHE_MIDDLEWARE_KEY_PREFIX = "my-prefix"

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
