import os
import json
from datetime import datetime
from pprint import pprint
from clevertap_connect import Clevertap

if __name__ == '__main__':
    # User and Events Counts Results
    print('-'*20+' Counts Results '+'-'*20)
    path = f'{os.getcwd()}/config.ini'
    s = Clevertap(config_path=path, app='phonepe', api='counts', object_type='profiles')
    print('Clevertap.host: ', Clevertap.host)
    print('s.base_url: ', s.base_url)
    ev = ['App Launched', 'Homepage primary action', 'User Location', 'Vaccine Slot Search', 'App Uninstalled']
    fr_date = 20250706
    to_date = 20250706
    rec = []
    for i in ev:
        qu = {"event_name": i, "from": fr_date, "to": to_date}
        x = s.fetch_records(query=qu)
        rec.extend(x)
    print('\nResonse:\n')
    pprint(rec)
    print()
    # Save to JSON
    with open('counts_results.json', 'w') as f:
        json.dump(rec, f, default=str, indent=2)

    # Custom Query Counts Results
    print('-'*20+' Custom Query Counts Results '+'-'*20)
    query = {
        "event_name": "App Launched",
        "from": 20250607,
        "to": 20250607,
        'session_properties': [{'name': 'time_of_day', 'value': ['13:00', '14:00']}],
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "UTM Visited",
                    "from": 20250607,
                    "to": 20250607,
                    "session_properties": [
                        {
                            'name': 'utm_campaign',
                            'value': 'facebook'
                        }
                    ]
                }
            ]
        }
    }
    s = Clevertap(config_path=path, app='web', api='counts', object_type='events')
    print('Clevertap.host: ', Clevertap.host)
    print('s.base_url: ', s.base_url)
    x = s.fetch_records(query=query)
    print('\nResonse:\n')
    pprint(x)
    print()
    # Save to JSON
    with open('custom_query_counts_results.json', 'w') as f:
        json.dump(x, f, default=str, indent=2)

    # Custom Query Events (Raw Data) Results
    print('-'*20+' Custom Query Events (Raw Data) Results '+'-'*20)
    query = {
        "event_name": "App Launched",
        "from": 20250607,
        "to": 20250607,
        'session_properties': [{'name': 'time_of_day', 'value': ['13:00', '14:00']}],
        "advanced_query": {
            "did_all": [
                {
                    "event_name": "UTM Visited",
                    "from": 20250607,
                    "to": 20250607,
                    "session_properties": [
                        {
                            'name': 'utm_campaign',
                            'value': 'facebook'
                        }
                    ]
                }
            ]
        }
    }
    s = Clevertap(config_path=path, app='mobile', api='events', object_type='profiles')
    print('Clevertap.host: ', Clevertap.host)
    print('s.base_url: ', s.base_url)
    x = s.fetch_records(query=query)
    print('\nResonse:\n')
    pprint(x)
    # Save to JSON
    with open('new_custom_query_events_raw_data_results.json', 'w') as f:
        json.dump(x, f, default=str, indent=2)