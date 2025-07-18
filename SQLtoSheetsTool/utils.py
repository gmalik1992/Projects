"""
utils.py - Utility functions for SQLtoSheetsTool (Public Minimal Version)
Author: Gobind Malik

Contains helper functions for MySQL and Google Sheets operations.
"""

import os
import pandas as pd
import pymysql
from configparser import ConfigParser
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from typing import Optional

# Load config
config = ConfigParser()
config.read("config.ini")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
CREDENTIALS_PATH = os.path.join("auth_secrets", "credentials.json")
TOKEN_PATH = os.path.join("auth_secrets", "token.json")


def get_mysql_connection(db: str) -> pymysql.connections.Connection:
    """Establish a connection to the MySQL database."""
    mysql_conf = config["mysql"]
    return pymysql.connect(
        host=mysql_conf["host"],
        user=mysql_conf["user"],
        password=mysql_conf["password"],
        database=db,
        port=int(mysql_conf.get("port", 3306)),
    )


def fetch_mysql_data(query: str, db: str) -> pd.DataFrame:
    """Fetch data from MySQL as a DataFrame."""
    conn = get_mysql_connection(db=db)
    try:
        df = pd.read_sql(query, conn)
    finally:
        conn.close()
    return df


def get_gsheet_service() -> object:
    """Authenticate and return the Google Sheets service."""
    creds: Optional[Credentials] = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())
    service = build("sheets", "v4", credentials=creds)
    return service.spreadsheets()


def read_gsheet(spreadsheet_id: str, sheet_name: str) -> pd.DataFrame:
    """Read data from a Google Sheet into a DataFrame."""
    sheets = get_gsheet_service()
    result = sheets.values().get(spreadsheetId=spreadsheet_id, range=f"{sheet_name}!A1:ZZ").execute()
    values = result.get("values", [])
    df = pd.DataFrame(values)
    if not df.empty:
        df.columns = df.iloc[0]
        df = df.iloc[1:]
    return df


def push_to_gsheet(df: pd.DataFrame, spreadsheet_id: str, sheet_name: str) -> None:
    """Push a DataFrame to a Google Sheet, overwriting its contents."""
    sheets = get_gsheet_service()
    values = [df.columns.tolist()] + df.astype(str).values.tolist()
    body = {"values": values}
    sheets.values().clear(spreadsheetId=spreadsheet_id, range=f"{sheet_name}!A:ZZ").execute()
    sheets.values().update(
        spreadsheetId=spreadsheet_id,
        range=f"{sheet_name}!A1",
        valueInputOption="USER_ENTERED",
        body=body
    ).execute()
    print(f"Pushed {len(df)} rows to Google Sheet '{sheet_name}'")


def save_preview(df: pd.DataFrame, filename: str) -> None:
    """Save the first 5 rows of a DataFrame to a CSV file."""
    df.head().to_csv(filename, index=False)
    print(f"Saved preview to {filename}") 