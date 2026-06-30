---
type: "Table"
title: "levels.txt"
description: "Levels within stations. Conditionally Required: - Required when describing pathways with elevators (`pathway_mode=5`). - Optional otherwise."
resource: "https://gtfs.org/documentation/schedule/reference/#levelstxt"
tags: [gtfs, schedule, table, levels, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`levels.txt` is a GTFS Schedule file with file-level presence `Conditionally Required`. Describes levels in a station. Useful in conjunction with pathways.txt. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `level_id` | Unique ID | Required | Identifies a level in a station. [1] |
| `level_index` | Float | Required | Numeric index of the level that indicates its relative position. Ground level should have index `0`, with levels above ground indicated by positive indices and levels below ground by negative indices. [1] |
| `level_name` | Text | Optional | Name of the level as seen by the rider inside the building or station. [1] |

# Grain

One row per `level_id` key in `levels.txt`. [1]

Primary key noted by the reference: `level_id`. [1]

# Relationships

- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- The file-level presence is `Conditionally Required`; read the table summary and schema before assuming the file is always present.

# Citations

[1] [GTFS Schedule Reference: levels.txt](https://gtfs.org/documentation/schedule/reference/#levelstxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
