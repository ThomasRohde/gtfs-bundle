# Tools

`build_gtfs_schedule_catalog.py` regenerates the base GTFS Schedule table
catalog from the official GTFS Schedule Reference.

Important: the community enrichment layer under `gtfs-schedule-catalog/` is
manually maintained. If this generator is rerun, validate and reconcile the
manual concepts and indexes before publishing.

Recommended checks:

```powershell
python tools\build_gtfs_schedule_catalog.py
python <okf-bundle-smith-plugin-root>\tools\okf_tool.py lint gtfs-schedule-catalog --format markdown
```
