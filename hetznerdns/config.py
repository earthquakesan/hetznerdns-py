import os

from .exceptions import ApiTokenNotSetException

HETZNER_DNS_TOKEN_ENV = "HETZNER_DNS_TOKEN"

def get_api_auth_key():
    api_auth_key = os.environ.get(HETZNER_DNS_TOKEN_ENV, "")
    if api_auth_key == "":
        raise ApiTokenNotSetException("%s environment variable is not set" % HETZNER_DNS_TOKEN_ENV)
    return api_auth_key