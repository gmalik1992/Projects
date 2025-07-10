"""
clevertap_connect.py

CleverTap API Connector – Public Version
----------------------------------------
A minimal Python client for fetching data from CleverTap's Events and Counts APIs.

- Supports cursor-based pagination
- Credentials loaded via config.ini
- Works with both 'events' and 'counts' endpoints for both advanced and hybrid CQL queries
- Safe for public repositories (no secrets embedded)

Note:
This public version omits production-grade features such as:
- Retry logic for errors (throttling, conflicts, delays)
- Detailed error handling and logging
- Metadata/context injection

These are present in the internal production version maintained in private repositories.

Example:
    ct = Clevertap('config.ini', app='web', api='counts', object_type='events')
    results = ct.fetch_records(query)
"""


import json
import requests
from configparser import ConfigParser
from datetime import datetime
from time import sleep
from pprint import pprint

class Clevertap:
    host = 'in1.api.clevertap.com'
    version = 1
    batch_size = 5000

    def __init__(self, config_path, app, api='events', object_type='events', region=None):
        conf = ConfigParser()
        conf.read(config_path)
        self.account_id = conf.get(app, 'id')
        self.account_pass = conf.get(app, 'password')
        self.api = api
        self.object_type = object_type
        self.cursor_key = 'cursor' if api == 'events' else 'req_id'
        self.records, self.cursor = [], None
        self.url = None

        if region: Clevertap.host = f"{region}.{Clevertap.host}"
        self.headers = {
            'X-CleverTap-Account-Id': self.account_id,
            'X-CleverTap-Passcode': self.account_pass,
            'Content-Type': 'application/json'
        }

    @property
    def base_url(self):
        api_string = 'counts/' + self.object_type if self.api == 'counts' else 'events'
        return f'https://{self.host}/{self.version}/{api_string}.json'

    def update_cursor(self, cursor):
        return f'{self.base_url}?{self.cursor_key}={cursor}'

    def fetch_records(self, query):
        # reset our records cache
        self.records = []
        self.cursor = None
        self.url = self.base_url

        response = self._call(body=query) or {}
        self.cursor = response.get(self.cursor_key, None)

        # keep making requests with the new cursor as long as we have a cursor
        while self.cursor:
            self.url = self.update_cursor(cursor=self.cursor)
            res = self._call()
            if res.get('status') != 'partial':
                self.records.append({'response': res})
            self.cursor = res.get('next_cursor' if self.api == 'events' else self.cursor_key)
        return self.records

    def _call(self, **kwargs):
        body = kwargs.get('body', None)
        if body:
            self.event_name = body.get('event_name')
            response = requests.post(url=self.url,
                                     headers=self.headers,
                                     params={'batch_size': Clevertap.batch_size},
                                     data=json.dumps(body))
            self.post_code = response.status_code
        elif self.cursor:
            response = requests.get(url=self.url,
                                    headers=self.headers)
            self.get_code = response.status_code
        return response.json()