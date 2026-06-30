---
type: "Reference"
title: "Tools README"
description: "Maintainer notes for repository helper tools."
tags: [tools, maintenance, generator]
timestamp: "2026-06-30T06:22:18+02:00"
---

# Tools

`build_gtfs_schedule_catalog.py` regenerates the base GTFS Schedule table
catalog at the repository root from the official GTFS Schedule Reference.

`build_release.ps1` creates publication artifacts from a clean export of tracked
files. It avoids packaging local-only directories such as `.git`, `dist`, and
`.scratch`.

Important: the community enrichment layer is manually maintained. If this
generator is rerun, validate and reconcile the manual concepts and indexes
before publishing.

Recommended checks:

```powershell
codex plugin marketplace add ThomasRohde/okf-bundle-smith --ref master
codex plugin add okf-bundle-smith@okf-bundle-smith
python tools\build_gtfs_schedule_catalog.py
python <installed-okf-bundle-smith>\tools\okf_tool.py lint . --format markdown
.\tools\build_release.ps1 -OkfTool <installed-okf-bundle-smith>\tools\okf_tool.py
```
