import json
import logging
import requests
import requests.status_codes

from .config import get_api_auth_token, HETZNER_DNS_ENDPOINT
from .exceptions import *

logger = logging.getLogger(__name__)

class ApiRequest:
    __instance = None
    api_key = get_api_auth_token()
    headers = {
        "Content-Type": "application/json",
        "Auth-API-Token": api_key
    }

    def __init__(self):
        """Virtually private constructor. """
        if ApiRequest.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ApiRequest.__instance = self
    @staticmethod 
    def get_instance():
        """Static access method. """
        if ApiRequest.__instance == None:
            ApiRequest()
        return ApiRequest.__instance
    def get(self, endpoint, params=None):
        url = "%s%s" % (HETZNER_DNS_ENDPOINT, endpoint)
        req = requests.get(url, headers=self.headers)
        if req.status_code / 100 != 2:
            logger.error("Status exit code: %s" %(req.status_code))
            raise GetRequestException("GET Request failed: %s" % (url))
        return req.json()
    def post(self, endpoint, json=None):
        url = "%s%s" % (HETZNER_DNS_ENDPOINT, endpoint)
        req = requests.post(url, headers=self.headers, json=json)
        if req.status_code / 100 != 2:
            logger.error("Status exit code: %s" %(req.status_code))
            raise PostRequestException("POST Request failed: %s" % (url))            
        return req.json()
    def delete(self, endpoint):
        url = '%s%s' % (HETZNER_DNS_ENDPOINT, endpoint)
        req = requests.delete(url, headers=self.headers)
        if req.status_code / 100 != 2:
            logger.error("Status exit code: %s" %(req.status_code))
            raise DeleteRequestException("DELETE Request failed: %s" % (url))
        return req
   
request = ApiRequest.get_instance()

#########
# ZONES #
#########

def get_all_zones():
    return request.get("/zones")

def get_zone_by_id(_id):
    return request.get("/zones/%s" % (_id))

def get_zone_by_name(name):
    zones = get_all_zones().get("zones")
    for zone in zones:
        if zone["name"] == name:
            return zone
    raise ZoneNotExistException("Zone %s does not exist." % (name))
    
def get_zone_id_by_name(name):
    zone = get_zone_by_name(name)
    return zone["id"]

def create_zone(name, ttl):
    _json = {
        "name": name,
        "ttl": ttl
    }
    return request.post("/zones", json=_json)

def delete_zone_by_id(_id):
    return request.delete("/zones/%s" % (_id))

def delete_zone_by_name(name):
    _id = get_zone_id_by_name(name)
    return delete_zone_by_id(_id)

###########
# RECORDS #
###########

def get_all_records():
    return request.get("/records")

def get_record_by_name(name, zone_name):
    zone_id = get_zone_id_by_name(zone_name)
    records = get_all_records().get("records")
    for record in records:
        if record["name"] == name and record["zone_id"] == zone_id:
            return record
    raise RecordNotExistException("Record %s does not exist." % (name))

def get_record_id_by_name(name, zone_name):
    record = get_record_by_name(name, zone_name)
    return record["id"]

def get_record_by_id(_id):
    return request.get("/records/%s" % (record_id), "GET")

def create_record(name=None, _type=None, value=None, ttl=3600, zone_name=None):
    zone_id = get_zone_id_by_name(zone_name)
    _json = {
        "value": value, # e.g. ip address
        "type": _type, # A, AAAA, NS etc
        "ttl": ttl, # default is 86400
        "name": name, # e.g. www
        "zone_id": zone_id
    }
    req = request.post("/records", json=_json)
    return req

def delete_record_by_id(_id):
    return request.delete("/records/%s" % (_id))

def delete_record_by_name(name, zone_name):
    _id = get_record_id_by_name(name, zone_name)
    return delete_record_by_id(_id)
