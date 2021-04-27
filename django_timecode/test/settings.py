
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

ROOT_URLCONF = 'django_timecode.test.urls'

INSTALLED_APPS = [
    'django_timecode',
    'django_timecode.test',
]

SECRET_KEY = 'abcd'
