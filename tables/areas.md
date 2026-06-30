---
type: "Table"
title: "areas.txt"
description: "Area grouping of locations."
resource: "https://gtfs.org/documentation/schedule/reference/#areastxt"
tags: [gtfs, schedule, table, areas, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`areas.txt` is a GTFS Schedule file with file-level presence `Optional`. Defines area identifiers. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `area_id` | Unique ID | Required | Identifies an area. Must be unique in areas.txt. [1] |
| `area_name` | Text | Optional | The name of the area as displayed to the rider. [1] |

# Grain

One row per `area_id` key in `areas.txt`. [1]

Primary key noted by the reference: `area_id`. [1]

# Relationships

- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.

# Citations

[1] [GTFS Schedule Reference: areas.txt](https://gtfs.org/documentation/schedule/reference/#areastxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
