import sys
import site
import os

site.addsitedir('/var/www/172.20.128.63/env/lib/python3.13/site-packages')

sys.path.insert(0, '/var/www/172.20.128.63')

os.chdir('/var/www/172.20.128.63')

os.environ['VIRTUAL_ENV'] = '/var/www/172.20.128.63/env'
os.environ['PATH'] = '/var/www/172.20.128.63/env/bin:' + os.environ['PATH']

from app import app as application