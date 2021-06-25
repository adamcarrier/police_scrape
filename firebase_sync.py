#!/usr/bin/env python3
# https://firebase.google.com/docs/database/admin/save-data

import json, hashlib, firebase_admin
from firebase_admin import credentials, db
from firebase_config import service_account_key, firebase_database_url
from gcp_geocoding import geocode

def init_db():
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate(service_account_key)

    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': firebase_database_url
    })

def save_offense(agency_id, location, incident):
    # JSON to Python
    incidentJSON = json.loads(incident)

    # Get a database reference
    ref = db.reference('police/agency/' + agency_id)

    # Set the destination firebase node
    node_ref = ref.child('offense')

    # Generate a hexadecimal MD5 hash from the JSON to use as a unique incident key.
    # This prevents duplicate incidents from being added to Firebase.
    hash = hashlib.md5(str(incidentJSON).encode())
    hashkey = hash.hexdigest()

    # Geocode the address
    results = geocode(incidentJSON['Address'] + ', ' + location)
    formatted_address = get_string(json.dumps([s['formatted_address'] for s in results]))
    latitude = get_string(json.dumps([s['geometry']['location']['lat'] for s in results]))
    longitude = get_string(json.dumps([s['geometry']['location']['lng'] for s in results]))

    # Save each item individually
    node_ref.child(hashkey).set({
        'Precinct': incidentJSON['Precinct'],
        'Date': incidentJSON['Date'],
        'Location': incidentJSON['Location'],
        'Address': incidentJSON['Address'],
        'FormattedAddress': formatted_address,
        'Latitude': latitude,
        'Longitude': longitude,
        'Crime': incidentJSON['Crime'],
        'CaseStatus': incidentJSON['CaseStatus'],
        'Disposition': incidentJSON['Disposition'],
        'Beat': incidentJSON['Beat'],
        'RptArea': incidentJSON['RptArea'],
        'CaseAssignedTo': incidentJSON['CaseAssignedTo'],
        'ReportNumber': incidentJSON['ReportNumber']
    })

def save_arrest(agency_id, location, incident):
    # JSON to Python
    incidentJSON = json.loads(incident)

    # Get a database reference
    ref = db.reference('police/agency/' + agency_id)

    # Set the destination firebase node
    node_ref = ref.child('arrest')

    # Generate a hexadecimal MD5 hash from the JSON to use as a unique incident key.
    # This prevents duplicate incidents from being added to Firebase.
    hash = hashlib.md5(str(incidentJSON).encode())
    hashkey = hash.hexdigest()

    # Geocode the address
    results = geocode(incidentJSON['ArrestLocation'] + ', ' + location)
    formatted_address = get_string(json.dumps([s['formatted_address'] for s in results]))
    latitude = get_string(json.dumps([s['geometry']['location']['lat'] for s in results]))
    longitude = get_string(json.dumps([s['geometry']['location']['lng'] for s in results]))

    # Save each item individually
    node_ref.child(hashkey).set({
        'Date': incidentJSON['Date'],
        'Offender': incidentJSON['Offender'],
        'Age': incidentJSON['Age'],
        'TimeOfArrest': incidentJSON['TimeOfArrest'],
        'ArrestLocation': incidentJSON['ArrestLocation'],
        'FormattedAddress': formatted_address,
        'Latitude': latitude,
        'Longitude': longitude,
        'ArrestId': incidentJSON['ArrestId'],
        'ChargeNumber': incidentJSON['ChargeNumber'],
        'Agency': incidentJSON['Agency'],
        'Charge': incidentJSON['Charge'],
        'Occupation': incidentJSON['Occupation']
    })

def get_string(jsonObj):
    pyObj = json.loads(jsonObj)
    return str(pyObj[0])
