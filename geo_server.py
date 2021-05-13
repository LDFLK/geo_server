"""GeoServer."""
from flask import Flask
from flask_caching import Cache

from utils.sysx import log_metrics
from geo import geodata

DEFAULT_CACHE_TIMEOUT = 1

log_metrics()
app = Flask(__name__)
cache = Cache(config={'CACHE_TYPE': 'NullCache'})
cache.init_app(app)


@app.route('/')
@cache.cached(timeout=DEFAULT_CACHE_TIMEOUT)
def index():
    """Index."""
    log_metrics()
    return '''
<html>
    <h1>GeoServer</h1>
</html>
    '''


@app.route('/latlng_to_region/<string:latlng_str>')
@cache.cached(timeout=DEFAULT_CACHE_TIMEOUT)
def latlng_to_region(latlng_str):
    """Get region from latlng."""
    lat, _, lng = latlng_str.partition(',')
    lat_lng = (float)(lat), (float)(lng)
    return geodata.get_latlng_regions(lat_lng)


@app.route('/region_geo/<string:region_id>')
@cache.cached(timeout=DEFAULT_CACHE_TIMEOUT)
def region_geo(region_id):
    """Get region."""
    return geodata.get_region_geo(region_id)
