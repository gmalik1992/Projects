# CleverTap API Connector (Public Version)

A lightweight Python 3.8+ library for querying aggregated counts and raw event/user data from the [CleverTap API](https://developer.clevertap.com/), via a simplified class interface.

This public-facing version is ideal for understanding the core logic and quickly getting started with CleverTap data extraction using Python.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Class Parameters](#class-parameters)
- [Example Query](#example-query)
- [Output](#output)
- [What’s NOT Included](#whats-not-included)
- [Advanced Google Sheets Automation (Private Version)](#advanced-google-sheets-automation-private-version)
- [Python Version](#python-version)
- [References](#references)
- [Contact](#contact)

---

## ✨ Features

- 🔌 Supports both `'counts'` and `'events'` APIs for advanced & hybrid CQL queries
- 🔄 Handles cursor-based pagination for large responses
- 📦 Returns data in clean JSON format
- 🔐 Externalizes all credentials via a config file (safe for GitHub)
- 📁 Includes example JSON response files for reference

---

## ⚙️ Installation

Ensure Python 3.8 or higher is installed. Then install required dependencies:

```bash
pip install requests
```

---

## 🧠 Usage

```python
from clevertap_connect import Clevertap

ct = Clevertap('config.ini', app='web', api='counts', object_type='events')
results = ct.fetch_records(query)
```

---

## 🧾 Class Parameters

| Parameter    | Type   | Description                                                                 |
|--------------|--------|-----------------------------------------------------------------------------|
| config_path  | str    | Path to your CleverTap config file (e.g., `config.ini`)                     |
| app          | str    | Section name in the config file (e.g., `'web'`, `'train'`)                  |
| api          | str    | Either `'counts'` for aggregated data or `'events'` for raw data            |
| object_type  | str    | `'events'` or `'profiles'` (applies to both counts and events APIs)          |
| region       | str    | Optional. Example: `'in1'` (India), `'eu1'` (Europe)                        |

---

## 📌 Example Query

```python
query = {
    "event_name": "Flight Search",
    "from": 20250607,
    "to": 20250607,
    "session_properties": [{"name": "time_of_day", "value": ["00:00", "14:00"]}],
    "advanced_query": {
        "did_all": [{
            "event_name": "UTM Visited",
            "from": 20250607,
            "to": 20250607,
            "session_properties": [{"name": "utm_campaign", "value": "dsa_generic_flight"}]
        }]
    }
}
```

---

## ✅ Output

All responses are returned as a list of dictionaries, each containing a response key and optional context.

See the included `sample_response.json` files for reference.

---

## 🔒 What’s NOT Included (Compared to Full Version)

This public version has been stripped down to keep it clean and safe for sharing. It does **not** include:

- Retry logic for throttled or failed requests (e.g., HTTP 429, 409)
- Handling of error codes like cursor not ready or request throttled
- Advanced exception traceback handling
- Dynamic context injection (e.g., tagging with timestamp, batch ID)
- Google Sheet automation integration

---

## 🧠 Advanced Google Sheets Automation (Only in Private Version)

The private version includes an advanced utility script `clevertap_gsheet_automation.py` that:

- 📖 Reads query parameters from a Google Sheet
- 🔄 Dynamically constructs CleverTap-compatible queries
- 📬 Fetches data from CleverTap APIs
- 📝 Writes results back into another sheet

This makes it possible for non-technical teams to run complex queries by simply filling in rows in a shared sheet.

**Supported features include:**

- Advanced & hybrid CQL queries
- Automatic detection of date/time column types
- Full control of parameters like `utm_campaign`, date ranges, etc.

> **Note:** For the Google Sheets integration and robust retry-safe API logic, please contact the author for access to the private repository.

---

## 🐍 Python Version

Compatible with Python 3.8 and above.

---

## 📎 References

- [CleverTap CQL Docs](https://developer.clevertap.com/docs/clevertap-query-language)
- Sample Hybrid CQL Payloads

---

## 👤 Contact

If you’re interested in the advanced, production-ready version (including Google Sheet automation, retries, and error handling), feel free to reach out to the author.