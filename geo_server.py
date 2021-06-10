"""GeoServer."""
from flask import Flask
from flask_caching import Cache
from flask_cors import CORS
from waitress import serve


from utils.sysx import log_metrics
from geo import alt, geodata

DEFAULT_CACHE_TIMEOUT = 1


def _warmup():
    geodata.get_latlng_regions([0, 0])


log_metrics()
_warmup()
app = Flask(__name__)
CORS(app)
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)


@app.route('/status')
@cache.cached(timeout=DEFAULT_CACHE_TIMEOUT)
def status():
    """Index."""
    return log_metrics() | {'server': 'geo_server'}


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


@app.route('/altitude/<string:latlng_str>')
@cache.cached(timeout=DEFAULT_CACHE_TIMEOUT)
def altitude(latlng_str):
    """Get altitude for latlng."""
    lat, _, lng = latlng_str.partition(',')
    lat_lng = (float)(lat), (float)(lng)
    return {
        'altitude': alt.get_altitude(lat_lng),
    }


if __name__ == '__main__':
    PORT = 4002
    HOST = '0.0.0.0'
    print('Starting geo_server on %s:%d...' % (HOST, PORT))
    serve(
        app,
        host=HOST,
        port=PORT,
        threads=32,
    )
