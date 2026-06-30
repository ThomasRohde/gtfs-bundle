---
type: "Table"
title: "frequencies.txt"
description: "Headway (time between trips) for headway-based service or a compressed representation of fixed-schedule service."
resource: "https://gtfs.org/documentation/schedule/reference/#frequenciestxt"
tags: [gtfs, schedule, table, frequencies, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`frequencies.txt` is a GTFS Schedule file with file-level presence `Optional`. Frequencies.txt represents trips that operate on regular headways (time between trips). This file may be used to represent two different types of service. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `trip_id` | Foreign ID referencing [trips.txt](/tables/trips.md).`trip_id` | Required | Identifies a trip to which the specified headway of service applies. [1] |
| `start_time` | Time | Required | Time at which the first vehicle departs from the first stop of the trip with the specified headway. [1] |
| `end_time` | Time | Required | Time at which service changes to a different headway (or ceases) at the first stop in the trip. [1] |
| `headway_secs` | Positive integer | Required | Time, in seconds, between departures from the same stop (headway) for the trip, during the time interval specified by `start_time` and `end_time`. Multiple headways may be defined for the same trip, but must not overlap. New headways may start at the exact time the previous headway ends. [1] |
| `exact_times` | Enum | Optional | Indicates the type of service for a trip. See the file description for more information. Valid options are: `0` or empty - Frequency-based trips. `1` - Schedule-based trips with the exact same headway throughout the day. In this case the `end_time` value must be greater than the last desired trip `start_time` but less than the last desired trip start_time + `headway_secs`. [1] |

# Grain

One row per `trip_id, start_time` key in `frequencies.txt`. [1]

Primary key noted by the reference: `trip_id, start_time`. [1]

# Relationships

- `frequencies.trip_id` references [trips.txt](/tables/trips.md).`trip_id`. [1]
- `frequencies.trip_id` should point to a trip whose `stop_times.txt` record defines the stop pattern used for repeated departures. [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.

# Citations

[1] [GTFS Schedule Reference: frequencies.txt](https://gtfs.org/documentation/schedule/reference/#frequenciestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
