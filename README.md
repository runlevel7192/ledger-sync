# ledger-sync

Nightly job that pulls the day's ledger entries from the internal API and
loads them into the analytics warehouse.

## Usage

```
pip install -r requirements.txt
python sync.py --date 2026-09-28
```

Config is read from `.env`. Runs from cron on the reporting box.

```
15 3 * * *  cd /srv/ledger-sync && /usr/bin/python3 sync.py >> /var/log/ledger-sync.log 2>&1
```
