#!/usr/bin/env python3
"""Pull ledger entries and load them into the warehouse."""
import argparse
import os
from datetime import date

import requests
from dotenv import load_dotenv

load_dotenv()
API_URL = os.environ['LEDGER_API_URL']
API_KEY = os.environ['LEDGER_API_KEY']


def fetch_entries(day):
    r = requests.get(f'{API_URL}/ledger/entries', params={'date': day},
                     headers={'Authorization': f'Bearer {API_KEY}'}, timeout=30)
    r.raise_for_status()
    return r.json().get('entries', [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--date', default=date.today().isoformat())
    args = ap.parse_args()
    entries = fetch_entries(args.date)
    print(f'{len(entries)} ledger entries for {args.date}')


if __name__ == '__main__':
    main()
