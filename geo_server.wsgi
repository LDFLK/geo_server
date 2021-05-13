# geo_server.wsgi
import sys
sys.path.append('/usr/local/var/www/geo_server')
sys.path.append('/var/www/html/geo_server')

from geo_server import app as application
