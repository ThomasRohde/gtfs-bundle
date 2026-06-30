---
type: "Table"
title: "stop_areas.txt"
description: "Rules to assign stops to areas."
resource: "https://gtfs.org/documentation/schedule/reference/#stop_areastxt"
tags: [gtfs, schedule, table, stop-areas, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`stop_areas.txt` is a GTFS Schedule file with file-level presence `Optional`. Assigns stops from stops.txt to areas. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `area_id` | Foreign ID referencing [areas.txt](/tables/areas.md).`area_id` | Required | Identifies an area to which one or multiple `stop_id`s belong. The same `stop_id` may be defined in many `area_id`s. [1] |
| `stop_id` | Foreign ID referencing [stops.txt](/tables/stops.md).`stop_id` | Required | Identifies a stop. If a station (i.e. a stop with `stops.location_type=1`) is defined in this field, it is assumed that all of its platforms (i.e. all stops with `stops.location_type=0` that have this station defined as `stops.parent_station`) are part of the same area. This behavior can be overridden by assigning platforms to other areas. [1] |

# Grain

One row per unique combination of all provided identifying fields in `stop_areas.txt`. [1]

Primary key noted by the reference: `*`. [1]

# Relationships

- `stop_areas.area_id` references [areas.txt](/tables/areas.md).`area_id`. [1]
- `stop_areas.stop_id` references [stops.txt](/tables/stops.md).`stop_id`. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.

# Citations

[1] [GTFS Schedule Reference: stop_areas.txt](https://gtfs.org/documentation/schedule/reference/#stop_areastxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
