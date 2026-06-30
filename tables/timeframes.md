---
type: "Table"
title: "timeframes.txt"
description: "Date and time periods to use in fare rules for fares that depend on date and time factors."
resource: "https://gtfs.org/documentation/schedule/reference/#timeframestxt"
tags: [gtfs, schedule, table, timeframes, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`timeframes.txt` is a GTFS Schedule file with file-level presence `Optional`. Used to describe fares that can vary based on the time of day, the day of the week, or a particular day in the year. Timeframes can be associated with fare products in fare_leg_rules.txt. There must not be overlapping time intervals for the same `timeframe_group_id` and `service_id` values. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `timeframe_group_id` | ID | Required | Identifies a timeframe or set of timeframes. [1] |
| `start_time` | Local time | Conditionally Required | Defines the beginning of a timeframe. The interval includes the start time. Values greater than `24:00:00` are forbidden. An empty value in `start_time` is considered `00:00:00`. Conditionally Required: - Required if `timeframes.end_time` is defined. - Forbidden otherwise [1] |
| `end_time` | Local time | Conditionally Required | Defines the end of a timeframe. The interval does not include the end time. Values greater than `24:00:00` are forbidden. An empty value in `end_time` is considered `24:00:00`. Conditionally Required: - Required if `timeframes.start_time` is defined. - Forbidden otherwise [1] |
| `service_id` | Foreign ID referencing [calendar.txt](/tables/calendar.md).`service_id` or [calendar-dates.txt](/tables/calendar-dates.md).`service_id` | Required | Identifies a set of dates that a timeframe is in effect. [1] |

# Grain

One row per unique combination of all provided identifying fields in `timeframes.txt`. [1]

Primary key noted by the reference: `*`. [1]

# Relationships

- `timeframes.service_id` references [calendar.txt](/tables/calendar.md).`service_id`. [1]
- `timeframes.service_id` references [calendar_dates.txt](/tables/calendar-dates.md).`service_id`. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- Fare concepts evolve in GTFS; this bundle records the April 27, 2026 Schedule Reference and keeps deeper fare modeling as a recommended enrichment pass.

# Citations

[1] [GTFS Schedule Reference: timeframes.txt](https://gtfs.org/documentation/schedule/reference/#timeframestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
