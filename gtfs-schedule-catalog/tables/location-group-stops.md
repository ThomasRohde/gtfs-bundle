---
type: "Table"
title: "location_group_stops.txt"
description: "Rules to assign stops to location groups."
resource: "https://gtfs.org/documentation/schedule/reference/#location_group_stopstxt"
tags: [gtfs, schedule, table, location-group-stops, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`location_group_stops.txt` is a GTFS Schedule file with file-level presence `Optional`. Assigns stops from stops.txt to location groups. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `location_group_id` | Foreign ID referencing [location-groups.txt](/tables/location-groups.md).`location_group_id` | Required | Identifies a location group to which one or multiple `stop_id`s belong. The same `stop_id` may be defined in many `location_group_id`s. [1] |
| `stop_id` | Foreign ID referencing [stops.txt](/tables/stops.md).`stop_id` | Required | Identifies a stop belonging to the location group. [1] |

# Grain

One row per unique combination of all provided identifying fields in `location_group_stops.txt`. [1]

Primary key noted by the reference: `*`. [1]

# Relationships

- `location_group_stops.location_group_id` references [location_groups.txt](/tables/location-groups.md).`location_group_id`. [1]
- `location_group_stops.stop_id` references [stops.txt](/tables/stops.md).`stop_id`. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- This file participates in GTFS-Flex or rider-requested service modeling and is intentionally summarized here rather than treated as the main schedule model.

# Citations

[1] [GTFS Schedule Reference: location_group_stops.txt](https://gtfs.org/documentation/schedule/reference/#location_group_stopstxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
