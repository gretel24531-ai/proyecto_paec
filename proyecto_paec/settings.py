from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-t@@^p%&4c(5o*gavg5h7l7qnrb-2s#2p)^f8=cuagtw7t_$%kw'

DEBUG = False

ALLOWED_HOSTS = [
    'dari21.pythonanywhere.com',
    '.onrender.com',
    '127.0.0.1',
    'localhost',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # ⚠️ OBLIGATORIO PARA RENDER
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto_paec.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Django buscará en templates/ y en webapp/templates/
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

WSGI_APPLICATION = 'proyecto_paec.wsgi.application'


# -------------------------
# DATABASE
# -------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -------------------------
# PASSWORDS
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -------------------------
# INTERNACIONALIZACIÓN
# -------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -------------------------
# STATIC FILES (Render + WhiteNoise)
# -------------------------

# URL pública
STATIC_URL = '/static/'

# Carpeta donde Django recolecta archivos al ejecutar collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Carpeta donde tú guardas tus archivos estáticos
STATICFILES_DIRS = [
    BASE_DIR / 'static',   # Asegúrate de que existe
]

# WhiteNoise: servir archivos optimizados
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
