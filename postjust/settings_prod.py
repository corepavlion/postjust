DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {}
}
import dj_database_url
DATABASES['default'] =  dj_database_url.config()