#!/usr/bin/env python3

import json, urllib.request
from gcp_config import gcp_api_key

API_KEY = gcp_api_key
GEOCODE_BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

def geocode(address):
    params = urllib.parse.urlencode({'address': address, 'key': API_KEY,})
    url = f'{GEOCODE_BASE_URL}?{params}'

    result = json.load(urllib.request.urlopen(url))

    if result['status'] in ['OK', 'ZERO_RESULTS']:
        return result['results']
