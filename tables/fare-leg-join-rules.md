---
type: "Table"
title: "fare_leg_join_rules.txt"
description: "Rules for defining two or more legs should be considered as a single effective fare leg for the purposes of matching against rules in fare_leg_rules.txt"
resource: "https://gtfs.org/documentation/schedule/reference/#fare_leg_join_rulestxt"
tags: [gtfs, schedule, table, fare-leg-join-rules, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`fare_leg_join_rules.txt` is a GTFS Schedule file with file-level presence `Optional`. Primary Key (`from_network_id, to_network_id, from_stop_id, to_stop_id`) For a sub-journey of two consecutive legs with a transfer, if the transfer matches all matching predicates specified by a particular record in the file, then those two legs should be considered as a single effective fare leg for the purposes of matching against rules in fare_leg_rules.txt. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `from_network_id` | Foreign ID referencing [routes.txt](/tables/routes.md).`network_id` or [networks.txt](/tables/networks.md).`network_id` | Required | Matches a pre-transfer leg that uses the specified route network. If specified, the same `to_network_id` must also be specified. [1] |
| `to_network_id` | Foreign ID referencing [routes.txt](/tables/routes.md).`network_id` or [networks.txt](/tables/networks.md).`network_id` | Required | Matches a post-transfer leg that uses the specified route network. If specified, the same `from_network_id` must also be specified. [1] |
| `from_stop_id` | Foreign ID referencing [stops.txt](/tables/stops.md).`stop_id` | Conditionally Required | Matches a pre-transfer leg that ends at the specified stop (`location_type=0` or empty) or station (`location_type=1`). Conditionally Required: - Required if `to_stop_id` is defined. - Optional otherwise. [1] |
| `to_stop_id` | Foreign ID referencing [stops.txt](/tables/stops.md).`stop_id` | Conditionally Required | Matches a post-transfer leg that starts at the specified stop (`location_type=0` or empty) or station (`location_type=1`). Conditionally Required: - Required if `from_stop_id` is defined. - Optional otherwise. [1] |

# Grain

One row per record in `fare_leg_join_rules.txt` as defined by the file schema. [1]

# Relationships

- `fare_leg_join_rules.from_network_id` references [routes.txt](/tables/routes.md).`network_id`. [1]
- `fare_leg_join_rules.from_network_id` references [networks.txt](/tables/networks.md).`network_id`. [1]
- `fare_leg_join_rules.to_network_id` references [routes.txt](/tables/routes.md).`network_id`. [1]
- `fare_leg_join_rules.to_network_id` references [networks.txt](/tables/networks.md).`network_id`. [1]
- `fare_leg_join_rules.from_stop_id` references [stops.txt](/tables/stops.md).`stop_id`. [1]
- `fare_leg_join_rules.to_stop_id` references [stops.txt](/tables/stops.md).`stop_id`. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- Fare concepts evolve in GTFS; this bundle records the April 27, 2026 Schedule Reference and keeps deeper fare modeling as a recommended enrichment pass.

# Citations

[1] [GTFS Schedule Reference: fare_leg_join_rules.txt](https://gtfs.org/documentation/schedule/reference/#fare_leg_join_rulestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
