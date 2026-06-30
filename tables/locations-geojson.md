---
type: "Table"
title: "locations.geojson"
description: "Zones for rider pickup or drop-off requests by on-demand services, represented as GeoJSON polygons."
resource: "https://gtfs.org/documentation/schedule/reference/#locationsgeojson"
tags: [gtfs, schedule, table, locations-geojson, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`locations.geojson` is a GTFS Schedule file with file-level presence `Optional`. Defines zones where riders can request either pickup or drop off by on-demand services. These zones are represented as GeoJSON polygons. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `\- type` | String | Required | `"Feature"` [1] |
| `\- id` | String | Required | Identifies a location. ID must be unique across all `stops.stop_id`, locations.geojson `id`, and `location_groups.location_group_id` values. [1] |
| `\- properties` | Object | Required | Location property keys. [1] |
| `\- stop_name` | String | Optional | Indicates the name of the location as displayed to riders. [1] |
| `\- stop_desc` | String | Optional | Meaningful description of the location to help orient riders. [1] |
| `\- geometry` | Object | Required | Geometry of the location. [1] |
| `\- type` | String | Required | Must be of type: - `"Polygon"` - `"MultiPolygon"` [1] |
| `\- coordinates` | Array | Required | Geographic coordinates (latitude and longitude) defining the geometry of the location. [1] |

# Grain

One row per record in `locations.geojson` as defined by the file schema. [1]

# Relationships

- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- This file participates in GTFS-Flex or rider-requested service modeling and is intentionally summarized here rather than treated as the main schedule model.

# Citations

[1] [GTFS Schedule Reference: locations.geojson](https://gtfs.org/documentation/schedule/reference/#locationsgeojson)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
