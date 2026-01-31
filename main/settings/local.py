load_dotenv(BASE_DIR / 'local.env')

from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# Storage
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            "connection_string": os.getenv("AZURE_STORAGE_CONNECTION_STRING"),
            "container_name": os.getenv("AZURE_STORAGE_CONTAINER"),
            "custom_domain": os.getenv("AZURE_CUSTOM_DOMAIN"),
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

