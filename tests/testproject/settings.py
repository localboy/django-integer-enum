# This is minimal Django settings for test project.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

INSTALLED_APPS = ('testapp',)

SECRET_KEY = 'supersecretkey'