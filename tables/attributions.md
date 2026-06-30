---
type: "Table"
title: "attributions.txt"
description: "Dataset attributions."
resource: "https://gtfs.org/documentation/schedule/reference/#attributionstxt"
tags: [gtfs, schedule, table, attributions, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`attributions.txt` is a GTFS Schedule file with file-level presence `Optional`. The file defines the attributions applied to the dataset. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `attribution_id` | Unique ID | Optional | Identifies an attribution for the dataset or a subset of it. This is mostly useful for translations. [1] |
| `agency_id` | Foreign ID referencing [agency.txt](/tables/agency.md).`agency_id` | Optional | Agency to which the attribution applies. If one `agency_id`, `route_id`, or `trip_id` attribution is defined, the other ones must be empty. If none of them is specified, the attribution will apply to the whole dataset. [1] |
| `route_id` | Foreign ID referencing [routes.txt](/tables/routes.md).`route_id` | Optional | Functions in the same way as `agency_id` except the attribution applies to a route. Multiple attributions may apply to the same route. [1] |
| `trip_id` | Foreign ID referencing [trips.txt](/tables/trips.md).`trip_id` | Optional | Functions in the same way as `agency_id` except the attribution applies to a trip. Multiple attributions may apply to the same trip. [1] |
| `organization_name` | Text | Required | Name of the organization that the dataset is attributed to. [1] |
| `is_producer` | Enum | Optional | The role of the organization is producer. Valid options are: `0` or empty - Organization doesn’t have this role. `1` - Organization does have this role. At least one of the fields `is_producer`, `is_operator`, or `is_authority` should be set at `1`. [1] |
| `is_operator` | Enum | Optional | Functions in the same way as `is_producer` except the role of the organization is operator. [1] |
| `is_authority` | Enum | Optional | Functions in the same way as `is_producer` except the role of the organization is authority. [1] |
| `attribution_url` | URL | Optional | URL of the organization. [1] |
| `attribution_email` | Email | Optional | Email of the organization. [1] |
| `attribution_phone` | Phone number | Optional | Phone number of the organization. [1] |

# Grain

One row per `attribution_id` key in `attributions.txt`. [1]

Primary key noted by the reference: `attribution_id`. [1]

# Relationships

- `attributions.agency_id` references [agency.txt](/tables/agency.md).`agency_id`. [1]
- `attributions.route_id` references [routes.txt](/tables/routes.md).`route_id`. [1]
- `attributions.trip_id` references [trips.txt](/tables/trips.md).`trip_id`. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.

# Citations

[1] [GTFS Schedule Reference: attributions.txt](https://gtfs.org/documentation/schedule/reference/#attributionstxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
