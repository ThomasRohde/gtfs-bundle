---
type: "Table"
title: "fare_rules.txt"
description: "Rules to apply fares for itineraries."
resource: "https://gtfs.org/documentation/schedule/reference/#fare_rulestxt"
tags: [gtfs, schedule, table, fare-rules, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`fare_rules.txt` is a GTFS Schedule file with file-level presence `Optional`. The fare_rules.txt table specifies how fares in fare_attributes.txt apply to an itinerary. Most fare structures use some combination of the following rules: For examples that demonstrate how to specify a fare structure with fare_rules.txt and fare_attributes.txt, see FareExamples in the GoogleTransitDataFeed open source project wiki. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `fare_id` | Foreign ID referencing [fare-attributes.txt](/tables/fare-attributes.md).`fare_id` | Required | Identifies a fare class. [1] |
| `route_id` | Foreign ID referencing [routes.txt](/tables/routes.md).`route_id` | Optional | Identifies a route associated with the fare class. If several routes with the same fare attributes exist, create a record in fare_rules.txt for each route. [1] |
| `origin_id` | Foreign ID referencing [stops.txt](/tables/stops.md).`zone_id` | Optional | Identifies an origin zone. If a fare class has multiple origin zones, create a record in fare_rules.txt for each `origin_id`. [1] |
| `destination_id` | Foreign ID referencing [stops.txt](/tables/stops.md).`zone_id` | Optional | Identifies a destination zone. If a fare class has multiple destination zones, create a record in fare_rules.txt for each `destination_id`. [1] |
| `contains_id` | Foreign ID referencing [stops.txt](/tables/stops.md).`zone_id` | Optional | Identifies the zones that a rider will enter while using a given fare class. Used in some systems to calculate correct fare class. [1] |

# Grain

One row per unique combination of all provided identifying fields in `fare_rules.txt`. [1]

Primary key noted by the reference: `*`. [1]

# Relationships

- `fare_rules.fare_id` references [fare_attributes.txt](/tables/fare-attributes.md).`fare_id`. [1]
- `fare_rules.route_id` references [routes.txt](/tables/routes.md).`route_id`. [1]
- `fare_rules.origin_id` references [stops.txt](/tables/stops.md).`zone_id`. [1]
- `fare_rules.destination_id` references [stops.txt](/tables/stops.md).`zone_id`. [1]
- `fare_rules.contains_id` references [stops.txt](/tables/stops.md).`zone_id`. [1]
- `fare_rules.origin_id`, `destination_id`, and `contains_id` match fare zones encoded in `stops.zone_id` on [stops.txt](/tables/stops.md). [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.
- Fare concepts evolve in GTFS; this bundle records the April 27, 2026 Schedule Reference and keeps deeper fare modeling as a recommended enrichment pass.

# Citations

[1] [GTFS Schedule Reference: fare_rules.txt](https://gtfs.org/documentation/schedule/reference/#fare_rulestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
