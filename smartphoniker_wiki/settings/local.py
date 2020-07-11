from .base import *

DEBUG = True


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


for template_engine in TEMPLATES:
    template_engine["OPTIONS"]["debug"] = True