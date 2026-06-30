---
type: "Reference"
title: "GTFS Schedule OKF Data Catalog README"
description: "Publication README for the GTFS Schedule OKF data catalog repository."
tags: [gtfs, schedule, okf, repository, readme]
timestamp: "2026-06-30T04:35:00+00:00"
---

# GTFS Schedule OKF Data Catalog

This repository contains a public Open Knowledge Format (OKF) bundle for the
GTFS Schedule specification. It models GTFS Schedule as a data catalog: one
dataset concept, one table concept per GTFS file, field schemas, row grains,
relationships, metrics, business terms, and practical workflows for using real
feeds.

The bundle is built for agents that need to answer questions such as:

- what each GTFS file or field means;
- how files join;
- how to determine active service on a date;
- how to query scheduled departures for a stop;
- when static GTFS is insufficient and GTFS Realtime or a journey-planner API is needed;
- where to find, validate, and interpret real GTFS feeds.

## Contents

- `index.md` - the OKF bundle entry point.
- `concepts/`, `datasets/`, `tables/`, `metrics/`, `processes/`, `systems/`, `decisions/` - the OKF bundle source.
- `tools/build_gtfs_schedule_catalog.py` - generator for the base Schedule table catalog.
- `dist/` - local generated artifacts, ignored by Git.
- `.scratch/` - local research/probe captures, ignored by Git.

The current bundle includes:

- 83 concepts
- 9 indexes
- 1 log
- 32 GTFS table concepts
- 10 process playbooks
- 5 system/tool/catalog concepts

## Entry Points

Start with [index.md](index.md).

High-value agent paths:

- Feed discovery: `concepts/gtfs-feed-catalog.md`
- Feed validation: `processes/validate-a-gtfs-feed.md`
- Stop departures: `processes/query-stop-departures.md`
- Active service dates: `processes/build-active-service-calendar.md`
- Static vs realtime: `processes/decide-static-vs-realtime-source.md`
- Fares v2: `concepts/fares-v2-model.md`
- Flex/on-demand service: `concepts/gtfs-flex-model.md`
- Accessibility/pathways: `processes/inspect-station-accessibility.md`

## Source Policy

Normative GTFS claims are cited to official GTFS/MobilityData sources:

- GTFS Schedule Reference
- GTFS Schedule Best Practices
- GTFS Realtime Reference
- GTFS Schedule governance
- MobilityData Canonical GTFS Schedule Validator

Feed catalogs, journey-planner APIs, validators, and community tools are labeled
as discovery or implementation guidance, not specification authority.

## Validate

Use the OKF Bundle Smith tooling:

```powershell
python <okf-bundle-smith-plugin-root>\tools\okf_tool.py lint . --format markdown
python <okf-bundle-smith-plugin-root>\tools\okf_tool.py stats .
.\tools\build_release.ps1 -OkfTool <okf-bundle-smith-plugin-root>\tools\okf_tool.py
```

The release script copies tracked files into `.scratch\release-bundle`, validates
that clean export, then writes the generated graph and zip into `dist\`. The
generated artifacts are intentionally not tracked in Git.

## Maintenance

`tools/build_gtfs_schedule_catalog.py` regenerates the base table catalog at the
repository root from the official GTFS Schedule Reference. The community
enrichment layer is manually maintained. If the generator is rerun, reconcile
manually maintained concepts, indexes, and log entries before publishing.

Do not package the Git working tree directly with `okf_tool.py package . ...`;
the packager includes local directories such as `.git` and `dist`. Use
`tools\build_release.ps1` for publication artifacts.

## License

Original OKF bundle content in this repository is released under CC BY 4.0. The
cited GTFS, MobilityData, Transitland, Rejseplanen, and OpenTripPlanner sources
remain governed by their own licenses and terms.
