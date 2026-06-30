---
type: "Reference"
title: "Tools README"
description: "Maintainer notes for repository helper tools."
tags: [tools, maintenance, generator]
timestamp: "2026-06-30T04:35:00+00:00"
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
python tools\build_gtfs_schedule_catalog.py
python <okf-bundle-smith-plugin-root>\tools\okf_tool.py lint . --format markdown
.\tools\build_release.ps1 -OkfTool <okf-bundle-smith-plugin-root>\tools\okf_tool.py
```
