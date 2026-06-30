---
type: "Table"
title: "stop_times.txt"
description: "Times that a vehicle arrives at and departs from stops for each trip."
resource: "https://gtfs.org/documentation/schedule/reference/#stop_timestxt"
tags: [gtfs, schedule, table, stop-times, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`stop_times.txt` is a GTFS Schedule file with file-level presence `Required`. Times that a vehicle arrives at and departs from stops for each trip. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `trip_id` | Foreign ID referencing [trips.txt](/tables/trips.md).`trip_id` | Required | Identifies a trip. [1] |
| `arrival_time` | Time | Conditionally Required | Arrival time at the stop (defined by `stop_times.stop_id`) for a specific trip (defined by `stop_times.trip_id`) in the time zone specified by `agency.agency_timezone`, not `stops.stop_timezone`. If there are not separate times for arrival and departure at a stop, `arrival_time` and `departure_time` should be the same. For times occurring after midnight on the service day, enter the time as a value greater than 24:00:00 in HH:MM:SS. If exact arrival and departure times (`timepoint=1`) are not available, estimated or interpolated arrival and departure times (`timepoint=0`) should be provided. Conditionally. [1] |
| `departure_time` | Time | Conditionally Required | Departure time from the stop (defined by `stop_times.stop_id`) for a specific trip (defined by `stop_times.trip_id`) in the time zone specified by `agency.agency_timezone`, not `stops.stop_timezone`. If there are not separate times for arrival and departure at a stop, `arrival_time` and `departure_time` should be the same. For times occurring after midnight on the service day, enter the time as a value greater than 24:00:00 in HH:MM:SS. If exact arrival and departure times (`timepoint=1`) are not available, estimated or interpolated arrival and departure times (`timepoint=0`) should be provided. Conditionally. [1] |
| `stop_id` | Foreign ID referencing [stops.txt](/tables/stops.md).`stop_id` | Conditionally Required | Identifies the serviced stop. All stops serviced during a trip must have a record in stop_times.txt. Referenced locations must be stops/platforms, i.e. their `stops.location_type` value must be `0` or empty. A stop may be serviced multiple times in the same trip, and multiple trips and routes may service the same stop. On-demand service using stops should be referenced in the sequence in which service is available at those stops. A data consumer should assume that travel is possible from one stop or location to any stop or location later in the trip, provided that the `pickup/drop_off_type` of each stop_time and. [1] |
| `location_group_id` | Foreign ID referencing [location-groups.txt](/tables/location-groups.md).`location_group_id` | Conditionally Forbidden | Identifies the serviced location group that indicates groups of stops where riders may request pickup or drop off. All location groups serviced during a trip must have a record in stop_times.txt. Multiple trips and routes may service the same location group. On-demand service using location groups should be referenced in the sequence in which service is available at those location groups. A data consumer should assume that travel is possible from one stop or location to any stop or location later in the trip, provided that the `pickup/drop_off_type` of each stop_time and the time constraints of each. [1] |
| `location_id` | Foreign ID referencing [locations.geojson](/tables/locations-geojson.md).`id` | Conditionally Forbidden | Identifies the GeoJSON location that corresponds to serviced zone where riders may request pickup or drop off. All GeoJSON locations serviced during a trip must have a record in stop_times.txt. Multiple trips and routes may service the same GeoJSON location. On-demand service within locations should be referenced in the sequence in which service is available in those locations. A data consumer should assume that travel is possible from one stop or location to any stop or location later in the trip, provided that the `pickup/drop_off_type` of each stop_time and the time constraints of each. [1] |
| `stop_sequence` | Non-negative integer | Required | Order of stops, location groups, or GeoJSON locations for a particular trip. The values must increase along the trip but do not need to be consecutive. [1] |
| `stop_headsign` | Text | Optional | Text that appears on signage identifying the trip's destination to riders. This field overrides the default `trips.trip_headsign` when the headsign changes between stops. If the headsign is displayed for an entire trip, `trips.trip_headsign` should be used instead. A `stop_headsign` value specified for one `stop_time` does not apply to subsequent `stop_time`s in the same trip. If you want to override the `trip_headsign` for multiple `stop_time`s in the same trip, the `stop_headsign` value must be repeated in each `stop_time` row. [1] |
| `start_pickup_drop_off_window` | Time | Conditionally Required | Time that on-demand service becomes available in a GeoJSON location, location group, or stop. Conditionally Required: - Required if `stop_times.location_group_id` or `stop_times.location_id` is defined. - Required if `end_pickup_drop_off_window` is defined. - Forbidden if `arrival_time` or `departure_time` is defined. - Optional otherwise. [1] |
| `end_pickup_drop_off_window` | Time | Conditionally Required | Time that on-demand service ends in a GeoJSON location, location group, or stop. Conditionally Required: - Required if `stop_times.location_group_id` or `stop_times.location_id` is defined. - Required if `start_pickup_drop_off_window` is defined. - Forbidden if `arrival_time` or `departure_time` is defined. - Optional otherwise. [1] |
| `pickup_type` | Enum | Conditionally Forbidden | Indicates pickup method. Valid options are: `0` or empty - Regularly scheduled pickup. `1` - No pickup available. `2` - Must phone agency to arrange pickup. `3` - Must coordinate with driver to arrange pickup. Conditionally Forbidden: - `pickup_type=0` forbidden if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined. - `pickup_type=3` forbidden if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined. - Optional otherwise. [1] |
| `drop_off_type` | Enum | Conditionally Forbidden | Indicates drop off method. Valid options are: `0` or empty - Regularly scheduled drop off. `1` - No drop off available. `2` - Must phone agency to arrange drop off. `3` - Must coordinate with driver to arrange drop off. Conditionally Forbidden: - `drop_off_type=0` forbidden if `start_pickup_drop_off_window` or `end_pickup_drop_off_window` are defined. - Optional otherwise. [1] |
| `continuous_pickup` | Enum | Conditionally Forbidden | Indicates that the rider can board the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, from this `stop_time` to the next `stop_time` in the trip’s `stop_sequence`. Valid options are: `0` - Continuous stopping pickup. `1` or empty - No continuous stopping pickup. `2` - Must phone agency to arrange continuous stopping pickup. `3` - Must coordinate with driver to arrange continuous stopping pickup. If this field is populated, it overrides any continuous pickup behavior defined in routes.txt. If this field is empty, the `stop_time` inherits any continuous pickup behavior. [1] |
| `continuous_drop_off` | Enum | Conditionally Forbidden | Indicates that the rider can alight from the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, from this `stop_time` to the next `stop_time` in the trip’s `stop_sequence`. Valid options are: `0` - Continuous stopping drop off. `1` or empty - No continuous stopping drop off. `2` - Must phone agency to arrange continuous stopping drop off. `3` - Must coordinate with driver to arrange continuous stopping drop off. If this field is populated, it overrides any continuous drop-off behavior defined in routes.txt. If this field is empty, the `stop_time` inherits any continuous. [1] |
| `shape_dist_traveled` | Non-negative float | Optional | Actual distance traveled along the associated shape, from the first stop to the stop specified in this record. This field specifies how much of the shape to draw between any two stops during a trip. Must be in the same units used in shapes.txt. Values used for `shape_dist_traveled` must increase along with `stop_sequence`; they must not be used to show reverse travel along a route. Recommended for routes that have looping or inlining (the vehicle crosses or travels over the same portion of alignment in one trip). See `shapes.shape_dist_traveled`. [1] |
| `timepoint` | Enum | Optional | Indicates if arrival and departure times for a stop are strictly adhered to by the vehicle or if they are instead approximate and/or interpolated times. This field allows a GTFS producer to provide interpolated stop-times, while indicating that the times are approximate. Valid options are: `0` - Times are considered approximate. `1` - Times are considered exact. All records of stop_times.txt with defined arrival or departure times should have timepoint values populated. If no timepoint values are provided, all times are considered exact. [1] |
| `pickup_booking_rule_id` | Foreign ID referencing [booking-rules.txt](/tables/booking-rules.md).`booking_rule_id` | Optional | Identifies the boarding booking rule at this stop time. Recommended when `pickup_type=2`. [1] |
| `drop_off_booking_rule_id` | Foreign ID referencing [booking-rules.txt](/tables/booking-rules.md).`booking_rule_id` | Optional | Identifies the alighting booking rule at this stop time. Recommended when `drop_off_type=2`. [1] |

# Grain

One row per `trip_id, stop_sequence` key in `stop_times.txt`. [1]

Primary key noted by the reference: `trip_id, stop_sequence`. [1]

# Relationships

- `stop_times.trip_id` references [trips.txt](/tables/trips.md).`trip_id`. [1]
- `stop_times.stop_id` references [stops.txt](/tables/stops.md).`stop_id`. [1]
- `stop_times.location_group_id` references [location_groups.txt](/tables/location-groups.md).`location_group_id`. [1]
- `stop_times.location_id` references [locations.geojson.txt](/tables/locations-geojson.md).`id`. [1]
- `stop_times.pickup_booking_rule_id` references [booking_rules.txt](/tables/booking-rules.md).`booking_rule_id`. [1]
- `stop_times.drop_off_booking_rule_id` references [booking_rules.txt](/tables/booking-rules.md).`booking_rule_id`. [1]
- `stop_times.trip_id` plus `stop_sequence` orders each trip's stop visits and joins scheduled movement to [trips.txt](/tables/trips.md). [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.

# Citations

[1] [GTFS Schedule Reference: stop_times.txt](https://gtfs.org/documentation/schedule/reference/#stop_timestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
