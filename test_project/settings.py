from pathlib import Path, os
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

MYAPPS = [
    "apps.booking_app",
    "apps.authentication_app"
]

THIRDPARTYAPPS = [
    "rest_framework",
    "drf_spectacular",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + MYAPPS\
    + THIRDPARTYAPPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'test_project.wsgi.application'

DBconfig = os.getenv('DB')

if DBconfig == "development":
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DB_ENGINE'),
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'), 
            'PORT': os.getenv('DB_PORT'),    
        }
    }
elif DBconfig == "production":
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('PRO_DB_ENGINE'),
            'NAME': os.getenv('PRO_DB_NAME'),
            'USER': os.getenv('PRO_DB_USER'),
            'PASSWORD': os.getenv('PRO_DB_PASSWORD'),
            'HOST': os.getenv('PRO_DB_HOST'), 
            'PORT': os.getenv('PRO_DB_PORT'),    
        }
    }
else:
    print("Please setup the Database") 

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SPECTACULAR_SETTINGS = {
    "TITLE": "Anakin Assignment",
    "DESCRIPTION":"##############################"
}


# overrided JWT Auth decoder
REST_FRAMEWORK = {
    # athentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # if want default authentication like middleware we comment out thiline
        # 'apps.authentication_app.jwt_processor.decode_jwt_token',
    ],
    # permissions
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    # throttling
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ],  comment this if dont want global
    'DEFAULT_THROTTLE_RATES': {
        'anon': '3/day',
        'user': '1000/day'
        # 'contacts': '1000/day', scope based trotling
    },
    # Swagger
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
