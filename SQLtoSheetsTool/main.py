"""
SQLtoSheetsTool (Public Minimal Version)

Author: Gobind Malik
Version: 1.0

This script demonstrates a minimal, public version of a database-to-Google-Sheet automation tool. It allows you to:
- Fetch data from a MySQL database as a pandas DataFrame
- Read data from a Google Sheet
- Push (overwrite) data to a Google Sheet
- Save data previews to CSV files

This public version is intended for portfolio, demo, and educational use. It is simplified for clarity and ease of use. 

**Advanced features such as multi-database support, task-driven automation, connection pooling, dynamic query parameterization, and robust error handling are reserved for the full private version.**

For access to the full-featured private version, please contact the author.
"""

import pandas as pd
from utils import (
    fetch_mysql_data,
    read_gsheet,
    push_to_gsheet,
    save_preview
)
from configparser import ConfigParser

# Metadata
__version__ = "1.0"
__author__ = "Gobind Malik"

# Load config
config = ConfigParser()
config.read("config.ini")

if __name__ == "__main__":
    print(f"SQLtoSheetsTool v{__version__} (Author: {__author__})")
    print("Reading from MySQL...")
    query = """
        SELECT
            created_at AS date,
            platform,
            device,
            stay_type,
            SUM(users) AS total_users,
            SUM(events) AS total_events,
            ROUND(SUM(events) / NULLIF(SUM(users), 0), 2) AS avg_events_per_user,
            COUNT(*) AS rows_count
        FROM
            lobDeviceSplitEventsDaily
        WHERE
            metric_name = 'Make Payment/Book Now'
            AND created_at >= SUBDATE(CURRENT_DATE, 11)
        GROUP BY
            created_at,
            platform,
            device,
            stay_type
        ORDER BY
            created_at,
            platform,
            stay_type;
    """  # Change as needed
    db_name = 'research_growth'  # Change as needed
    df_mysql = fetch_mysql_data(query=query, db=db_name)
    print("MySQL Data (first 5 rows):")
    print(df_mysql.head())
    save_preview(df_mysql, "mysql_data_preview.csv")

    print("\nReading from Google Sheet...")
    spreadsheet_id = config["gsheet"]["spreadsheet_id"]
    sheet_name = config["gsheet"]["sheet_name"]
    df_gsheet = read_gsheet(spreadsheet_id, sheet_name)
    print("Google Sheet Data (first 5 rows):")
    print(df_gsheet.head())
    save_preview(df_gsheet, "gsheet_data_preview.csv")

    # Example: Push MySQL data to Google Sheet
    print("\nPushing MySQL data to Google Sheet...")
    push_to_gsheet(df_mysql, spreadsheet_id, sheet_name)
    print("Done.")
