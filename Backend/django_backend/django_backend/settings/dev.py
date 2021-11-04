
import environ
from .base import *

DEBUG = True

env = environ.Env()
# reading env file
environ.Env.read_env()

SECRET_KEY= env("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': 'database',
        'PORT': '3306',
    }
}


CORS_ORIGIN_ALLOW_ALL = True

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "http://0.0.0.0:3000",
#     "http://127.0.0.1:3000"
# ]

# STRIPE_PUBLIC_KEY=env("STRIPE_PUBLIC_KEY")
# STRIPE_SECRET_KEY=env("STRIPE_SECRET_KEY")
