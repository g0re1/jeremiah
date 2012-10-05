import os
import sys
import django.core.handlers.wsgi


sys.path.append("/home/gore/apps/jeremiah")
sys.path.append("/home/gore/apps")


os.environ['DJANGO_SETTINGS_MODULE']='jeremiah.settings'


application = django.core.handlers.wsgi.WSGIHandler()


