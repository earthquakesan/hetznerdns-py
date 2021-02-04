import os

from .exceptions import ApiTokenNotSetException

HETZNER_DNS_TOKEN_ENV = "HETZNER_DNS_TOKEN"
HETZNER_DNS_ENDPOINT = "https://dns.hetzner.com/api/v1"

def get_api_auth_token():
    api_auth_token = os.environ.get(HETZNER_DNS_TOKEN_ENV, "")
    if api_auth_token == "":
        raise ApiTokenNotSetException("%s environment variable is not set" % HETZNER_DNS_TOKEN_ENV)
    return api_auth_token
