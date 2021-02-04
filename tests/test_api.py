import unittest

from hetznerdns.api import *
from hetznerdns.exceptions import *

class TestZones(unittest.TestCase):
    zone_name = "example-test-test.com"
    zone_ttl = 3600

    def test_create_get_delete(self):
        create_zone(self.zone_name, self.zone_ttl)
        zone = get_zone_by_name(self.zone_name)
        self.assertEqual(zone["name"], self.zone_name)
        self.assertEqual(zone["ttl"], self.zone_ttl)
        delete_zone_by_name(self.zone_name)
        with self.assertRaises(ZoneNotExistException):
            get_zone_by_name(self.zone_name)

class TestRecords(unittest.TestCase):
    record_value = "127.0.0.1"
    record_type = "A"
    record_ttl = 3600
    record_name = "www"
    zone_name = "example-test-test2.com"
    zone_ttl = 3600
    
    def setUp(self):
        # Create testing zone
        create_zone(self.zone_name, self.zone_ttl)
    
    def test_create_get_delete(self):
        create_record(
            name=self.record_name,
            value=self.record_value,
            _type=self.record_type,
            ttl=self.record_ttl,
            zone_name=self.zone_name
        )
        record = get_record_by_name(self.record_name)
        self.assertEqual(record['type'], self.record_type)
        self.assertEqual(record['name'], self.record_name)
        self.assertEqual(record['value'], self.record_value)
        self.assertEqual(record['ttl'], self.record_ttl)
        delete_record_by_name(self.record_name)
        with self.assertRaises(RecordNotExistException):
            get_record_by_name(self.record_name)

    def tearDown(self):
        # Delete testing zone
        delete_zone_by_name(self.zone_name)