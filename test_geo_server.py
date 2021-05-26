"""Test."""
import sys
import os
import unittest
import time

from utils.flask import FlaskClient

N_SAMPLES = 5

SERVER_NAME, HOST, PORT = None, '127.0.0.1', 5000
# SERVER_NAME, HOST, PORT = 'geo', '0.0.0.0', 8080
# SERVER_NAME, HOST, PORT = 'geo', '18.209.43.63', 80


class TestGeoServer(unittest.TestCase):
    """Tests."""

    def setUp(self):
        """Init test."""
        if not SERVER_NAME:
            os.system('./local_flask_stop.sh')
            print('Starting flask...')
            os.system('./local_flask_start.sh &')
            time.sleep(2)
        self.__client = FlaskClient(SERVER_NAME, HOST, PORT)

    def tearDown(self):
        """Teardown test."""
        if not SERVER_NAME:
            print('Stopping flask...')
            os.system('./local_flask_stop.sh')

    def test_latlng_to_region(self):
        """Test."""
        latlng_str_1 = '6.9157,79.8636'
        regions = self.__client.run('latlng_to_region', [latlng_str_1])
        self.assertEqual(
            regions,
            {
                'province': 'LK-1',
                'district': 'LK-11',
                'dsd': 'LK-1127',
                'gnd': 'LK-1127015',
            },
        )

        latlng_str_2 = '20,20'
        regions = self.__client.run('latlng_to_region', [latlng_str_2])
        self.assertEqual(
            regions,
            {},
        )

    def test_region_geo(self):
        """Test."""
        geo = self.__client.run('region_geo', ['LK-11'])
        self.assertEqual(
            geo['type'],
            'MultiPolygon',
        )
        geo = self.__client.run('region_geo', ['LK-15'])
        self.assertEqual(
            geo,
            {},
        )

    def test_altitude(self):
        """Test."""
        latlng_str_1 = '6.9157,79.8636'
        alt = self.__client.run('altitude', [latlng_str_1])
        self.assertEqual(
            alt,
            {'altitude': 12},
        )


if __name__ == '__main__':
    unittest.main()
