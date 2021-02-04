import unittest

from hetznerdns.api import *

class TestZones(unittest.TestCase):
    zone_name = "example-test-test.com"
    zone_ttl = 3600

    def test_create_get_delete(self):
        create_zone(self.zone_name, self.zone_ttl)
        zone = get_zone_by_name(self.zone_name)
        self.assertEqual(zone["name"], self.zone_name)
        self.assertEqual(zone["ttl"], self.zone_ttl)
        delete_zone_by_name(self.zone_name)
