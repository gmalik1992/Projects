# 👨‍💻 Gobind Malik — Project Portfolio

Welcome to my project portfolio repository! I'm a data & backend engineer with a passion for building practical tools — from API connectors and automation pipelines to AI-powered apps and full-stack web applications.

This repository is a curated collection of projects that demonstrate my skills across **Python**, **data engineering**, **AI/LLM integration**, **Flask web development**, and **cloud automation**.

---

## 📁 Projects Overview

| Project | Domain | Tech Stack | Highlights |
|---|---|---|---|
| [Analytics / Finance Data Extractor](#-analytics--finance-data-extractor) | AI · FinTech | Python, OpenAI GPT-4o, Streamlit, Pandas | Extracts structured financial data from raw news using LLMs |
| [CleverTap Connector](#-clevertap-connector) | Data Engineering · MarTech | Python, REST APIs, CleverTap CQL | Pagination-safe API connector with Google Sheets automation |
| [Flask Blog](#-flask-blog) | Full-Stack Web | Python, Flask, SQLAlchemy, JWT | Full-featured blog with auth, email resets, and CRUD |
| [SQLtoSheetsTool](#-sqltoSheetstool) | Data Automation | Python, MySQL, Google Sheets API, Pandas | Syncs SQL query results directly into Google Sheets |

---

## 🧾 Analytics / Finance Data Extractor

**Folder:** [`Analytics/`](./Analytics)

A **Streamlit-based UI** that uses OpenAI's `gpt-4o` model to extract structured financial metrics from unstructured news articles — no manual parsing required.

### What it does
- Accepts raw, unstructured finance news as input
- Uses GPT-4o to intelligently extract: Company Name, Stock Symbol, Revenue, Net Income, and EPS
- Displays results in a clean, readable table via Streamlit

### Tech Stack
`Python` · `OpenAI API (GPT-4o)` · `Streamlit` · `Pandas`

### Key Files
```
Analytics/
├── main.py                    # Streamlit UI entry point
├── finance_data_extractor.py  # Core GPT-4o extraction logic
├── requirements.txt
└── README.md
```

### Highlights
- Demonstrates practical LLM integration for real-world finance data workflows
- Clean separation of UI and business logic
- Ready to extend with additional metrics or data sources

---

## 🔌 CleverTap Connector

**Folder:** [`Clevertap_Connector/`](./Clevertap_Connector)

A lightweight **Python library** for querying aggregated counts and raw event/user data from the [CleverTap API](https://developer.clevertap.com/) via a clean, simplified class interface.

### What it does
- Supports both `counts` and `events` API modes
- Handles cursor-based pagination for large datasets automatically
- Returns clean JSON output, ready for downstream processing
- Externalises credentials securely via a config file

### Tech Stack
`Python 3.8+` · `CleverTap REST API` · `CQL (CleverTap Query Language)` · `requests`

### Usage
```python
from clevertap_connect import Clevertap

ct = Clevertap('config.ini', app='web', api='counts', object_type='events')
results = ct.fetch_records(query)
```

### Key Parameters

| Parameter | Description |
|---|---|
| `config_path` | Path to your CleverTap credentials config file |
| `app` | Config section name (e.g., `'web'`, `'train'`) |
| `api` | `'counts'` for aggregated data or `'events'` for raw data |
| `object_type` | `'events'` or `'profiles'` |
| `region` | Optional. e.g., `'in1'` (India), `'eu1'` (Europe) |

### Highlights
- Supports advanced & hybrid CQL queries
- Public version is GitHub-safe (no credentials, no internal logic exposed)
- **Private version** includes: retry logic for HTTP 429/409, Google Sheets automation, dynamic query construction, and batch tagging

> 💡 Contact the author for access to the full production-ready private version with Google Sheets integration.

---

## 📝 Flask Blog

**Folder:** [`Flask_Blog/`](./Flask_Blog)

A **full-stack blog application** built with Flask, featuring user authentication, profile management, and secure password reset via email — inspired by Corey Schafer's Flask tutorial series, extended with clean architecture and modern Flask practices.

### What it does
- User registration, login, and logout
- Create, edit, and delete blog posts
- Profile picture upload
- Secure password reset via email using Flask-Mail and App Passwords
- JWT-based token links for email verification

### Tech Stack
`Python` · `Flask` · `SQLAlchemy` · `Flask-Login` · `Flask-Mail` · `PyJWT` · `SQLite` · `python-dotenv`

### Running Locally
```bash
cd Flask_Blog
python run.py
```

Set up a `.env` file with:
```env
FLASK_APP_EMAIL_USER=your-email@mail.com
FLASK_APP_EMAIL_PASS=your-app-password
SECRET_KEY="generated-secret-key"
SQLALCHEMY_DATABASE_URI="sqlite:///site.db"
```

### Highlights
- Modular Flask app structure with Blueprints
- Session management with Flask-Login
- Token-based secure email flows using PyJWT
- SQLite database with SQLAlchemy ORM

### Future Plans
- Deploy to Render / Heroku
- Add pagination and search
- Dockerise the application

---

## 🗄️ SQLtoSheetsTool

**Folder:** [`SQLtoSheetsTool/`](./SQLtoSheetsTool)

A **data automation tool** that connects a MySQL database to Google Sheets — fetching query results and writing them directly into a target sheet, enabling non-technical teams to access live data without touching SQL.

### What it does
- Connects to a MySQL database and fetches data as a Pandas DataFrame
- Reads from and writes/overwrites data to a Google Sheet
- First-run Google OAuth flow for seamless authentication

### Tech Stack
`Python 3.10+` · `MySQL` · `Google Sheets API` · `Pandas` · `google-auth`

### Setup
```bash
pip install -r requirements.txt
# Configure config.ini with your MySQL and Google Sheet details
# Place credentials.json in auth_secrets/
python main.py
```

### Example `config.ini`
```ini
[mysql]
host = your-db-host
user = your-db-user
password = your-db-pass
database = your-db-name
port = 3306

[gsheet]
spreadsheet_id = your-google-spreadsheet-id
sheet_name = your-sheet-name
```

### Highlights
- Clean, minimal public version ideal for learning and portfolio review
- **Private version** supports: ClickHouse, PostgreSQL, YAML task files, scheduling, connection pooling, dynamic query parameterisation, and more

> 💡 Contact the author for the full production-ready private version.

---

## 🛠️ Skills & Technologies

```
Languages      Python, SQL, Bash
Frameworks     Flask, Streamlit
AI/LLM         OpenAI GPT-4o, Prompt Engineering
Data           Pandas, SQLAlchemy, MySQL, ClickHouse
APIs           CleverTap, Google Sheets API, OpenAI API
Auth & Security Flask-Login, PyJWT, OAuth2, python-dotenv
Tools          Git, Conda, pip, REST APIs
```

---

## 📬 Contact

- **GitHub:** [@gmalik1992](https://github.com/gmalik1992/Projects)
- **LinkedIn:** [Gobind Malik](https://www.linkedin.com/in/gobind-malik-9aa123a0/)

---

> ⚠️ **Note:** Some projects in this repository are public, minimal versions. Private/full versions with advanced features (retry logic, multi-DB support, scheduling, etc.) are available on request. Please reach out via LinkedIn or GitHub.
