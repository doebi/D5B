import site
site.addsitedir('/home/web/.envs/d5b/lib/python2.7/site-packages')
import os
import sys


path = '/home/web/d5b.doebi.at'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'bottletracker.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


import bottletracker.monitor
bottletracker.monitor.start(interval=1.0)
