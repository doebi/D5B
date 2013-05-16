import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'bottletracker.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

sys.path.append('/home/devlol')
sys.path.append('/home/devlol/D5B')
sys.path.append('/home/devlol/D5B/bottletracker')
