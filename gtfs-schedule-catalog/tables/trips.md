---
type: "Table"
title: "trips.txt"
description: "Trips for each route. A trip is a sequence of two or more stops that occur during a specific time period."
resource: "https://gtfs.org/documentation/schedule/reference/#tripstxt"
tags: [gtfs, schedule, table, trips, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`trips.txt` is a GTFS Schedule file with file-level presence `Required`. Trips for each route. A trip is a sequence of two or more stops that occur during a specific time period. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `route_id` | Foreign ID referencing [routes.txt](/tables/routes.md).`route_id` | Required | Identifies a route. [1] |
| `service_id` | Foreign ID referencing [calendar.txt](/tables/calendar.md).`service_id` or [calendar-dates.txt](/tables/calendar-dates.md).`service_id` | Required | Identifies a set of dates when service is available for one or more routes. [1] |
| `trip_id` | Unique ID | Required | Identifies a trip. [1] |
| `trip_headsign` | Text | Optional | Text that appears on signage identifying the trip's destination to riders. This field is recommended for all services with headsign text displayed on the vehicle which may be used to distinguish amongst trips in a route. If the headsign changes during a trip, values for `trip_headsign` may be overridden by defining values in `stop_times.stop_headsign` for specific `stop_time`s along the trip. [1] |
| `trip_short_name` | Text | Optional | Public facing text used to identify the trip to riders, for instance, to identify train numbers for commuter rail trips. If riders do not commonly rely on trip names, `trip_short_name` should be empty. A `trip_short_name` value, if provided, should uniquely identify a trip within a service day; it should not be used for destination names or limited/express designations. [1] |
| `direction_id` | Enum | Optional | Indicates the direction of travel for a trip. This field should not be used in routing; it provides a way to separate trips by direction when publishing time tables. Valid options are: `0` - Travel in one direction (e.g. outbound travel). `1` - Travel in the opposite direction (e.g. inbound travel). [1] |
| `block_id` | ID | Optional | Identifies the block to which the trip belongs. A block consists of a single trip or many sequential trips made using the same vehicle, defined by shared service days and `block_id`. A `block_id` may have trips with different service days, making distinct blocks. See the example below. To provide in-seat transfers information, transfers of `transfer_type` `4` should be provided instead. [1] |
| `shape_id` | Foreign ID referencing [shapes.txt](/tables/shapes.md).`shape_id` | Conditionally Required | Identifies a geospatial shape describing the vehicle travel path for a trip. Conditionally Required: - Required if the trip has a continuous pickup or drop-off behavior defined either in routes.txt or in stop_times.txt. - Optional otherwise. [1] |
| `wheelchair_accessible` | Enum | Optional | Indicates wheelchair accessibility. Valid options are: `0` or empty - No accessibility information for the trip. `1` - Vehicle being used on this particular trip can accommodate at least one rider in a wheelchair. `2` - No riders in wheelchairs can be accommodated on this trip. [1] |
| `bikes_allowed` | Enum | Optional | Indicates whether bikes are allowed. Valid options are: `0` or empty - No bike information for the trip. `1` - Vehicle being used on this particular trip can accommodate at least one bicycle. `2` - No bicycles are allowed on this trip. [1] |
| `cars_allowed` | Enum | Optional | Indicates whether cars are allowed. Valid options are: `0` or empty - No car information for the trip. `1` - Vehicle being used on this particular trip can accommodate at least one car. `2` - No cars are allowed on this trip. [1] |
| `safe_duration_factor` | Float | Optional | Multiplier applied to travel time estimates calculated for on-demand trips. See "Calculating on-demand trip time estimates with safe duration fields" section below for guidance on how to use this and the `safe_duration_offset` fields. [1] |
| `safe_duration_offset` | Float | Optional | Fixed offset value in seconds applied to travel time estimates calculated for on-demand trips. See "Calculating on-demand trip time estimates with safe duration fields" section below for guidance on how to use this and the `safe_duration_factor` fields. [1] |

# Grain

One row per `trip_id` key in `trips.txt`. [1]

Primary key noted by the reference: `trip_id`. [1]

# Relationships

- `trips.route_id` references [routes.txt](/tables/routes.md).`route_id`. [1]
- `trips.service_id` references [calendar.txt](/tables/calendar.md).`service_id`. [1]
- `trips.service_id` references [calendar_dates.txt](/tables/calendar-dates.md).`service_id`. [1]
- `trips.shape_id` references [shapes.txt](/tables/shapes.md).`shape_id`. [1]
- `trips.service_id` identifies a service pattern that can be declared in [calendar.txt](/tables/calendar.md), modified by [calendar_dates.txt](/tables/calendar-dates.md), or represented only in calendar_dates when calendar is omitted. [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.

# Citations

[1] [GTFS Schedule Reference: trips.txt](https://gtfs.org/documentation/schedule/reference/#tripstxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
