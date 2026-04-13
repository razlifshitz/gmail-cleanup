#!/usr/bin/env python3
"""
שלב 1: הרץ את הסקריפט הזה כדי לקבל קישור אימות.
פתח את הקישור בדפדפן, אשר גישה, והדבק את הקוד שתקבל.
"""
import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
CREDS_PATH = '/home/user/gmail-cleanup/credentials.json'
TOKEN_PATH = '/home/user/gmail-cleanup/token.json'

flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
flow.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'

auth_url, _ = flow.authorization_url(prompt='consent')

print("\n" + "="*60)
print("פתח את הקישור הבא בדפדפן:")
print("="*60)
print(auth_url)
print("="*60)
print("\nלאחר האישור, הדבק את הקוד כאן:")
code = input("קוד: ").strip()

flow.fetch_token(code=code)
creds = flow.credentials

with open(TOKEN_PATH, 'w') as f:
    f.write(creds.to_json())

print(f"\nטוקן נשמר ב-{TOKEN_PATH}")
print("עכשיו תוכל להריץ audit.py")
