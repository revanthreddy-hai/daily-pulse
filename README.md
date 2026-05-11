# Daily Pulse

Static public view for Revanth's Daily Pulse.

The local Pulse can contain private work context. Public pages in this repository
must be sanitized before publishing.

## Routes

- `/daily-pulse/` shows the latest public Pulse.
- `/daily-pulse/YYYY-MM-DD/` shows a specific dated Pulse.
- `/daily-pulse/archive/` lists past public Pulses.

Demo backfills can be regenerated with:

```bash
python3 scripts/backfill-demo-pulses.py
```
