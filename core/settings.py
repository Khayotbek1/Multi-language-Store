from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yx5!=re^sm44wz+p-m&hq21+ep(jg-mb%co%(1$@y&885u$j*_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #apps
    'main.apps.MainConfig',
    #packeges
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'en-us'
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('uz', _('Uzbek')),
    ('ru', _('Russian')),
]


LOCALE_PATHS = (
    BASE_DIR / 'locale',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
JAZZMIN_SETTINGS = {
    'site_title': _('Store'),
    'site_header': _('Store'),
    'site_brand': _('Store'),
    'welcome': _('Welcome'),
    "language_chooser": True,
"show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "your_app"],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "your_app.Product": "fas fa-box-open",
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    "topmenu_links": [
        {"name": "Bosh sahifa",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"app": "your_app"},
    ],

    "usermenu_links": [
        {"name": "Google", "url": "https://google.com", "new_window": True},
    ],

    "show_ui_builder": True,
    "changeform_format": "collapsible",
    "related_modal_active": True,

}

JAZZMIN_UI_TWEAKS = {

    "theme": "minty",
    "dark_mode_theme": "light",


    "body_small_text": False,
    "body_bg": None,
    "brand_colour": "navbar-danger",
    "accent": "accent-info",


    "sidebar": "sidebar-light-danger",
    "sidebar_icon": "fas fa-users",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "sidebar_fixed": True,


    "navbar": "navbar-dark navbar-dark",
    "navbar_fixed": True,
    "navbar_small_text": False,


    "footer_fixed": False,
    "footer_small_text": True,


    "button_classes": {
        "primary": "btn btn-primary",
        "secondary": "btn btn-secondary",
        "success": "btn btn-success",
        "info": "btn btn-info",
        "warning": "btn btn-warning",
        "danger": "btn btn-danger",
    },


    "form_classes": {
        "default": "form-control",
        "checkbox": "form-check-input",
        "radio": "form-check-input",
        "select": "form-select",
    },
    "actions_sticky_top": True,
    "text_muted": False,
    "small_text": False,
}

