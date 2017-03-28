# Django settings for forexsys project.

DEBUG = True

ADMINS = (
    ('Jianing YANG', 'jianingy.yang@gmail.com'),
    ('yuting', 'tingle2008@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'forexsys',
        'USER': 'forexsys',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#TIME_ZONE = 'Asia/Shanghai'
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = ''
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '5yu1mfyetw&amp;5g^r-($e(f1iki6$wt1z@o*v$38rgr$f4-585is'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
] 


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'forexsys.urls'

WSGI_APPLICATION = 'forexsys.wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    'debug_toolbar',
    'django_tables2',
    'forexsys',
    'accounts',
    'tradesys',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


SESSION_ENGINE = (
    "django.contrib.sessions.backends.signed_cookies"
    )

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

INTERNAL_IPS = ('192.168.155.6')


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

STATIC_DOC_ROOT = '/home/yuting/project/turbo-daytrader/forexsys/tradesys/static'
IMAGE_ARCHIVE_DIR  = '/home/forexchart/forextools/html/forexsys/images/Archive'

# Forexsys Settings

IMAGE_BASE_URL = 'http://www.gao-yang.com:55580/static/images/'
