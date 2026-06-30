---
type: "Table"
title: "route_networks.txt"
description: "Rules to assign routes to networks. Conditionally Forbidden: - Forbidden if `network_id` exists in routes.txt. - Optional otherwise."
resource: "https://gtfs.org/documentation/schedule/reference/#route_networkstxt"
tags: [gtfs, schedule, table, route-networks, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`route_networks.txt` is a GTFS Schedule file with file-level presence `Conditionally Forbidden`. Assigns routes from routes.txt to networks. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `network_id` | Foreign ID referencing [networks.txt](/tables/networks.md).`network_id` | Required | Identifies a network to which one or multiple `route_id`s belong. A `route_id` can only be defined in one `network_id`. [1] |
| `route_id` | Foreign ID referencing [routes.txt](/tables/routes.md).`route_id` | Required | Identifies a route. [1] |

# Grain

One row per `route_id` key in `route_networks.txt`. [1]

Primary key noted by the reference: `route_id`. [1]

# Relationships

- `route_networks.network_id` references [networks.txt](/tables/networks.md).`network_id`. [1]
- `route_networks.route_id` references [routes.txt](/tables/routes.md).`route_id`. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- The file-level presence is `Conditionally Forbidden`; read the table summary and schema before assuming the file is always present.

# Citations

[1] [GTFS Schedule Reference: route_networks.txt](https://gtfs.org/documentation/schedule/reference/#route_networkstxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
