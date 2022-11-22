# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hutz6kk9r3ki7k!d)6etwgb^tj*=@cv$n(98d#aeufa0zdup0a'



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'supers_database',
        'Host': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}