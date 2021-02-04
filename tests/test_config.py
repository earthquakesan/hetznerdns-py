import unittest
import os

from hetznerdns import config
from hetznerdns.exceptions import ApiTokenNotSetException

class TestConfig(unittest.TestCase):
    test_value = "test"
  
    def test_get_api_auth_key(self):
        os.environ[config.HETZNER_DNS_TOKEN_ENV] = self.test_value
        self.assertEqual(config.get_api_auth_token(), self.test_value)

    def test_get_api_auth_key_fail(self):
        os.environ[config.HETZNER_DNS_TOKEN_ENV] = ""
        with self.assertRaises(ApiTokenNotSetException):
            config.get_api_auth_token()
