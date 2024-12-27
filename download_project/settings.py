from pathlib import Path
import os # Biblioteca para manipulação do sistema de arquivos

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-p^36(=840b8icf8&mas!fenn_hbx269)@t8#xn83l*j4+koqw&'

DEBUG = True

ALLOWED_HOSTS = []

# Aplicativos instalados no projeto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'download', # Aplicativo personalizado do projeto
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'download_project.urls'

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

WSGI_APPLICATION = 'download_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

# URL base para arquivos estáticos
STATIC_URL = '/static/'

# Diretórios adicionais para busca de arquivos estáticos
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Direciona para o diretório "static" na raiz do projeto
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações para arquivos de mídia (uploads de usuários)
MEDIA_URL = '/media/' # URL base para acessar arquivos de mídia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Diretório onde os arquivos de mídia serão armazenados
