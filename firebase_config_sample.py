#!/usr/bin/env python3
# Sample firebase config file

import os

config_file_dir = os.path.dirname(__file__)
service_account_key = os.path.join(config_file_dir, 'serviceAccountKey.json')
firebase_database_url = 'https://your-google-cloud-project-db.firebaseio.com/'
