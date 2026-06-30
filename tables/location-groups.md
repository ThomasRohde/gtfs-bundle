---
type: "Table"
title: "location_groups.txt"
description: "A group of stops that together indicate locations where a rider may request pickup or drop off."
resource: "https://gtfs.org/documentation/schedule/reference/#location_groupstxt"
tags: [gtfs, schedule, table, location-groups, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`location_groups.txt` is a GTFS Schedule file with file-level presence `Optional`. Defines location groups, which are groups of stops where a rider may request pickup or drop off. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `location_group_id` | Unique ID | Required | Identifies a location group. ID must be unique across all `stops.stop_id`, locations.geojson `id`, and `location_groups.location_group_id` values. A location group is a group of stops that together indicate locations where a rider may request pickup or drop off. [1] |
| `location_group_name` | Text | Optional | The name of the location group as displayed to the rider. [1] |

# Grain

One row per `location_group_id` key in `location_groups.txt`. [1]

Primary key noted by the reference: `location_group_id`. [1]

# Relationships

- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- This file participates in GTFS-Flex or rider-requested service modeling and is intentionally summarized here rather than treated as the main schedule model.

# Citations

[1] [GTFS Schedule Reference: location_groups.txt](https://gtfs.org/documentation/schedule/reference/#location_groupstxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
