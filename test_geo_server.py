"""Test."""
import unittest
import geo_server


class TestGeoServer(unittest.TestCase):
    """Tests."""

    def test_latlng_to_region(self):
        """Test."""
        regions = geo_server.latlng_to_region('6.9157,79.8636')
        self.assertEqual(
            regions,
            {
                'province': 'LK-1',
                'district': 'LK-11',
                'dsd': 'LK-1127',
                'gnd': 'LK-1127015',
            },
        )

        regions = geo_server.latlng_to_region('20,20')
        self.assertEqual(
            regions,
            {},
        )

    def test_region_geo(self):
        """Test."""
        geo = geo_server.region_geo('LK-11')
        self.assertEqual(
            geo['type'],
            'MultiPolygon',
        )
        geo = geo_server.region_geo('LK-15')
        self.assertEqual(
            geo,
            {},
        )

    def test_altitude(self):
        """Test."""
        alt = geo_server.altitude('6.9157,79.8636')
        self.assertEqual(
            alt,
            {'altitude': 12},
        )


if __name__ == '__main__':
    unittest.main()
