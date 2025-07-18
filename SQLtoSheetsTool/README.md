# SQLtoSheetsTool (Public Minimal Version)

> **Note:** This is a public, minimal version of the project. It demonstrates basic MySQL-to-Google-Sheet automation. Many advanced features are available in the full private version—see below for details. If you are interested in the full version, please contact the author.

---

## 🚀 What This Version Does

- Connects to a MySQL database and fetches data as a pandas DataFrame.
- Reads data from a Google Sheet (read-only).
- Pushes (writes/overwrites) data to a Google Sheet.
- Prints both datasets to the console.

This is ideal for portfolio/demo purposes or as a starting point for your own automation scripts.

---

## ❌ Features Only in the Full Version

The full private version (not included here) supports:

- **Multi-database support:** ClickHouse, PostgreSQL, and more.
- **Task-driven automation:** Run parameterized jobs from YAML task files.
- **Advanced scheduling:** Easily automate recurring data syncs.
- **Connection pooling:** Efficient, scalable DB access.
- **Smart data type handling:** Automatic conversion for arrays, JSON, decimals, etc.
- **Centralized configuration:** Manage all settings in a single config file.
- **Secure secrets management:** Robust handling of credentials and tokens.
- **Dynamic query parameterization:** Flexible date ranges, substitutions, and more.
- **Extensible architecture:** Easily add new connectors, data sources, or destinations.

> **Contact the author for access to the full version or for custom solutions.**

---

## 🛠️ Setup

1. **Clone this repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure your settings:**
   - Copy `config.ini.sample` to `config.ini` and fill in your MySQL and Google Sheet details.
   - Download your Google API `credentials.json` from the [Google Cloud Console](https://console.cloud.google.com/) and place it in the `auth_secrets/` directory.

---

## ▶️ Usage

Run the script:
```bash
python main.py
```
- The script will print data from both MySQL and your Google Sheet, and push MySQL data to the sheet (overwriting its contents).
- On first run, you will be prompted to authenticate with Google (browser window will open).

---

## 📝 Example `config.ini`
```
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

---

## 🔐 Credentials
- Place your Google API `credentials.json` in the `auth_secrets/` folder.
- `token.json` will be auto-generated after first authentication.

---

## 📬 Contact
For access to the full-featured private version, or for custom solutions and support, please contact the author:

- **LinkedIn:** [Gobind Malik](https://www.linkedin.com/in/gobind-malik-9aa123a0/)

---

*For demo/portfolio use only. Do not share credentials or tokens.*