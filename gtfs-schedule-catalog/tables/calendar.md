---
type: "Table"
title: "calendar.txt"
description: "Service dates specified using a weekly schedule with start and end dates. Conditionally Required: - Required unless all dates of service are defined in."
resource: "https://gtfs.org/documentation/schedule/reference/#calendartxt"
tags: [gtfs, schedule, table, calendar, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`calendar.txt` is a GTFS Schedule file with file-level presence `Conditionally Required`. Service dates specified using a weekly schedule with start and end dates. Conditionally Required: - Required unless all dates of service are defined in calendar_dates.txt. - Optional otherwise. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `service_id` | Unique ID | Required | Identifies a set of dates when service is available for one or more routes. [1] |
| `monday` | Enum | Required | Indicates whether the service operates on all Mondays in the date range specified by the `start_date` and `end_date` fields. Note that exceptions for particular dates may be listed in calendar_dates.txt. Valid options are: `1` - Service is available for all Mondays in the date range. `0` - Service is not available for Mondays in the date range. [1] |
| `tuesday` | Enum | Required | Functions in the same way as `monday` except applies to Tuesdays [1] |
| `wednesday` | Enum | Required | Functions in the same way as `monday` except applies to Wednesdays [1] |
| `thursday` | Enum | Required | Functions in the same way as `monday` except applies to Thursdays [1] |
| `friday` | Enum | Required | Functions in the same way as `monday` except applies to Fridays [1] |
| `saturday` | Enum | Required | Functions in the same way as `monday` except applies to Saturdays. [1] |
| `sunday` | Enum | Required | Functions in the same way as `monday` except applies to Sundays. [1] |
| `start_date` | Date | Required | Start service day for the service interval. [1] |
| `end_date` | Date | Required | End service day for the service interval. This service day is included in the interval. [1] |

# Grain

One row per `service_id` key in `calendar.txt`. [1]

Primary key noted by the reference: `service_id`. [1]

# Relationships

- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.
- The file-level presence is `Conditionally Required`; read the table summary and schema before assuming the file is always present.

# Citations

[1] [GTFS Schedule Reference: calendar.txt](https://gtfs.org/documentation/schedule/reference/#calendartxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
