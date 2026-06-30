---
type: "Table"
title: "transfers.txt"
description: "Rules for making connections at transfer points between routes."
resource: "https://gtfs.org/documentation/schedule/reference/#transferstxt"
tags: [gtfs, schedule, table, transfers, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`transfers.txt` is a GTFS Schedule file with file-level presence `Optional`. When calculating an itinerary, GTFS-consuming applications interpolate transfers based on allowable time and stop proximity. Transfers.txt specifies additional rules and overrides for selected transfers. Fields `from_trip_id`, `to_trip_id`, `from_route_id` and `to_route_id` allow higher orders of specificity for transfer rules. Along with `from_stop_id` and `to_stop_id`, the ranking of specificity is as follows: 1. Both `trip_id`s defined: `from_trip_id` and `to_trip_id`. 2. One `trip_id` and `route_id` set defined: (`from_trip_id` and `to_route_id`) or (`from_route_id` and `to_trip_id`). 3. One `trip_id` defined: `from_trip_id` or `to_trip_id`. 4. Both `route_id`s defined: `from_route_id` and `to_route_id`. 5. One `route_id` defined: `from_route_id` or `to_route_id`. 6. Only `from_stop_id` and `to_stop_id` defined: no route or trip related fields set. For a given ordered pair of. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `from_stop_id` | Foreign ID referencing [stops.txt](/tables/stops.md).`stop_id` | Conditionally Required | Identifies a stop (`location_type=0`) or a station (`location_type=1`) where a connection between routes begins. If this field refers to a station, the transfer rule applies to all its child stops. It must refer to a stop (`location_type=0`) if `transfer_type` is `4` or `5`. Conditionally Required: - Required if `transfer_type` is empty, `0`, `1`, `2`, or `3`. - Optional if `transfer_type` is `4` or `5`. [1] |
| `to_stop_id` | Foreign ID referencing [stops.txt](/tables/stops.md).`stop_id` | Conditionally Required | Identifies a stop (`location_type=0`) or a station (`location_type=1`) where a connection between routes ends. If this field refers to a station, the transfer rule applies to all child stops. It must refer to a stop (`location_type=0`) if `transfer_type` is 4 or 5. Conditionally Required: - Required if `transfer_type` is empty, `0`, `1`, `2`, or `3`. - Optional if `transfer_type` is `4` or `5`. [1] |
| `from_route_id` | Foreign ID referencing [routes.txt](/tables/routes.md).`route_id` | Optional | Identifies a route where a connection begins. If `from_route_id` is defined, the transfer will apply to the arriving trip on the route for the given `from_stop_id`. If both `from_trip_id` and `from_route_id` are defined, the `trip_id` must belong to the `route_id`, and `from_trip_id` will take precedence. [1] |
| `to_route_id` | Foreign ID referencing [routes.txt](/tables/routes.md).`route_id` | Optional | Identifies a route where a connection ends. If `to_route_id` is defined, the transfer will apply to the departing trip on the route for the given `to_stop_id`. If both `to_trip_id` and `to_route_id` are defined, the `trip_id` must belong to the `route_id`, and `to_trip_id` will take precedence. [1] |
| `from_trip_id` | Foreign ID referencing [trips.txt](/tables/trips.md).`trip_id` | Conditionally Required | Identifies a trip where a connection between routes begins. If `from_trip_id` is defined, the transfer will apply to the arriving trip for the given `from_stop_id`. If both `from_trip_id` and `from_route_id` are defined, the `trip_id` must belong to the `route_id`, and `from_trip_id` will take precedence. Conditionally Required: - Required if `transfer_type` is `4` or `5`. - Optional otherwise. [1] |
| `to_trip_id` | Foreign ID referencing [trips.txt](/tables/trips.md).`trip_id` | Conditionally Required | Identifies a trip where a connection between routes ends. If `to_trip_id` is defined, the transfer will apply to the departing trip for the given `to_stop_id`. If both `to_trip_id` and `to_route_id` are defined, the `trip_id` must belong to the `route_id`, and `to_trip_id` will take precedence. Conditionally Required: - Required if `transfer_type` is `4` or `5`. - Optional otherwise. [1] |
| `transfer_type` | Enum | Required | Indicates the type of connection for the specified (`from_stop_id`, `to_stop_id`) pair. Valid options are: `0` or empty - Recommended transfer point between routes. `1` - Timed transfer point between two routes. The departing vehicle is expected to wait for the arriving one and leave sufficient time for a rider to transfer between routes. `2` - Transfer requires a minimum amount of time between arrival and departure to ensure a connection. The time required to transfer is specified by `min_transfer_time`. `3` - Transfers are not possible between routes at the location. `4` - Passengers can transfer from one trip. [1] |
| `min_transfer_time` | Non-negative integer | Optional | Amount of time, in seconds, that must be available to permit a transfer between routes at the specified stops. The `min_transfer_time` should be sufficient to permit a typical rider to move between the two stops, including buffer time to allow for schedule variance on each route. [1] |

# Grain

One row per `from_stop_id, to_stop_id, from_trip_id, to_trip_id, from_route_id, to_route_id` key in `transfers.txt`. [1]

Primary key noted by the reference: `from_stop_id, to_stop_id, from_trip_id, to_trip_id, from_route_id, to_route_id`. [1]

# Relationships

- `transfers.from_stop_id` references [stops.txt](/tables/stops.md).`stop_id`. [1]
- `transfers.to_stop_id` references [stops.txt](/tables/stops.md).`stop_id`. [1]
- `transfers.from_route_id` references [routes.txt](/tables/routes.md).`route_id`. [1]
- `transfers.to_route_id` references [routes.txt](/tables/routes.md).`route_id`. [1]
- `transfers.from_trip_id` references [trips.txt](/tables/trips.md).`trip_id`. [1]
- `transfers.to_trip_id` references [trips.txt](/tables/trips.md).`trip_id`. [1]
- `from_trip_id`, `to_trip_id`, `from_route_id`, and `to_route_id` make transfer rules more specific than stop-pair-only rules. [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.

# Citations

[1] [GTFS Schedule Reference: transfers.txt](https://gtfs.org/documentation/schedule/reference/#transferstxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
