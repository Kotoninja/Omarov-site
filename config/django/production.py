from .base import *
from config.env import env

DEBUG = False

ALLOWED_HOSTS = env.list("DJANGO_ALLOWES_HOSTS", default=[])
