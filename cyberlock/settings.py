# Django settings for cyberlock project.

import os
from pathlib import Path
from decouple import config

from dotenv import load_dotenv
load_dotenv()

# Import the environment variables
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()  


# Quick-start development settings - unsuitable for production


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
# Get values from the environment
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Parse ALLOWED_HOSTS as a list
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'coreapp', 
    'crispy_forms',
    'ckeditor',
    'jazzmin',
    'axes',
    'widget_tweaks',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',  # Optional: For social authentication
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.twitter',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
    # Required for django-allauth
    'allauth.account.middleware.AccountMiddleware',
]


ROOT_URLCONF = 'cyberlock.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR /'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'cyberlock.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# WhiteNoise configuration
# Enable WhiteNoise compression and caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# database connection setup for postgresql server
'''

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
'''

# allauth configuration settings
SITE_ID = 1

# Authentication backends
# settings.py
ACCOUNT_SIGNUP_FIELDS = ['email', 'password1', 'password2']  # Require email for registration
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Verify email addresses
ACCOUNT_LOGIN_METHODS = ['email']  # Use email for authentication
ACCOUNT_UNIQUE_EMAIL = True  # Ensure emails are unique
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1', 'password2']  # Do not require a username
LOGIN_REDIRECT_URL = '/'  # Redirect after login
LOGOUT_REDIRECT_URL = '/'  # Redirect after logout



# social account settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    },
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    },
    'github': {
        'SCOPE': ['user:email'],
    },
    'twitter': {
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'include_email': 'true'},
        'VERIFIED_EMAIL': False,
    },
}


# Secure cookie congiration settings Set up secure cookies and HSTS # Disable SSL for local development
SECURE_SSL_REDIRECT = True if not DEBUG else False
SESSION_COOKIE_SECURE = True if not DEBUG else False
CSRF_COOKIE_SECURE = True if not DEBUG else False
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
FRAME_OPTIONS = 'DENY'
CURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Assuming the 'static' directory is at the project root
]

# For production use, ensure you set up staticfiles storage correctly
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


# When collecting static files, for production use,
STATIC_ROOT = BASE_DIR / 'staticfiles'



# URL to access media files via the browser
MEDIA_URL = '/media/'

# Absolute path to the directory where media files are stored
MEDIA_ROOT = BASE_DIR / 'media'



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# The default login redirect path
LOGIN_URL = '/login/'


# The default redirect url
LOGOUT_REDIRECT_URL = 'home'  # Change 'home' to the desired URL name

#ckeditor upload path
CKEDITOR_UPLOAD_PATH="uploads/"

# The default django mailing system configuration
#Email backend for password reset (use console for testing)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # For testing
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # For production


# The default django mailing system configuration
# Get email configurations from .env file

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')  # Use SMTP backend
EMAIL_HOST = env('EMAIL_HOST')  # SMTP host, e.g., 'smtp.cyberlocktech.com'
EMAIL_PORT = env.int('EMAIL_PORT', 465)  # Default to 465 if not specified
EMAIL_USE_SSL = env.bool('EMAIL_USE_SSL', True)  # True or False
EMAIL_USE_TLS = False  # If SSL is enabled, TLS should be False
EMAIL_HOST_USER = env('EMAIL_HOST_USER')  # 'Email address to use for sending emails'
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')  # Email password
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')  # Default 'From' email address



'''
# content displayed and styled from backend using ckeditor framework
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',  # Use the custom toolbar
        'height': 300,
        'width': 'auto',
        'resize_enabled': False,
        'extraPlugins': 'highlight',  # Add highlight plugin
        'toolbar_Custom': [  # Define custom toolbar
            ['Bold', 'Italic', 'Underline', 'Highlight'],  # Text formatting
            ['BulletedList', 'NumberedList'],  # Lists
            ['Link', 'Unlink', 'Image', 'Table'],  # Links, media, and tables
            ['Source'],  # Source editor
        ],
    }
}

'''

# jazzmin configuration settings
JAZZMIN_SETTINGS = {

 # title of the window (Will default to current_admin_site.site_title if absent or None)
    
    'site_title': 'Cyberlock Admin',
    'site_header': 'Cyberlock Admin',
    'site_logo': 'static/images/logo.png',
    'welcome_sign': 'Welcome to Cyberlock Admin',
    'theme': 'dark',
    #'copyright': 'Cyberlock Technologies',

    # language settings
   # 'language_chooser': True,

   # related modal popups 
   "related_modal_active": True,


    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,
    

    ################################
    #                              #
    #       Side Menu              #
    #                              #
    ################################

    'show_sidebar': True,  # Whether to hide the sidebar.
    'sidebar_collapse_text': 'Collapse Sidebar',  # Text for the sidebar collapse button.
    'sidebar_expand_text': 'Expand Sidebar',  # Text for the sidebar expand button.
    'display_sidebar_settings': True,  # Whether to display the sidebar settings button.
    'display_sidebar_menu': True,  # Whether to display the sidebar menu.
    'display_sidebar_brand': True,  # Whether to display the sidebar brand.
    'display_sidebar_user_menu': True,  # Whether to display the user menu in the sidebar.

    'display_sidebar_search': False,  # Whether to display the sidebar search input.
    'sidebar_nav_style': 'accordion',  # 'accordion' (default) or 'nested
    'navigation_expanded': True,  # Whether to expand the navigation by default.
    'navigation_style':'vertical',  # 'horizontal' (default) or'vertical'
    'navigation_icon_style': 'circle',  # 'default' (default), 'circle' or 'square'
    'navigation_auto_collapse': True,  # Whether to automatically collapse the navigation on small screens.

    ################################
    'navigation_collapse_text': 'Collapse',  # Text for the collapse button.
    'navigation_expand_text': 'Expand',  # Text for the expand button.
    'display_footer': True,  # Whether to display the footer at the bottom of the page.
    'display_brand': True,  # Whether to display the brand name at the top of the page.
    'display_search': False,  # Whether to display the global search bar.

    ################
    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # show ui builder
    "show_ui_builder": True,
    # show function list on dashboard
    "show_function_list": True,


    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"}
    ],

    ############
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",


    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],
    }


# jazzmin UI tweaks
JAZZMIN_UI_TWEAKS = {
    
    "theme": "darkly",
    "dark_mode_theme": "darkly",
}


# Django Axes configuration settings
# Set the number of login attempts before blocking the user
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',  # Add this line
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# AXE backend settings Configuration
AXES_FAILURE_LIMIT = 5  # Number of failed login attempts before lockout
AXES_COOLOFF_TIME = 1  # Lockout duration in hours


# Track user login sessions and login failed sessions attempts
# The default django logging system configuration
# ERROR LOG IN DJANGO
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'django_error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
