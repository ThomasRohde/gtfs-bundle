---
type: "Table"
title: "calendar_dates.txt"
description: "Exceptions for the services defined in the calendar.txt. Conditionally Required: - Required if calendar.txt is omitted. In which case calendar_dates.txt must contain all."
resource: "https://gtfs.org/documentation/schedule/reference/#calendar_datestxt"
tags: [gtfs, schedule, table, calendar-dates, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`calendar_dates.txt` is a GTFS Schedule file with file-level presence `Conditionally Required`. The calendar_dates.txt table explicitly activates or disables service by date. It may be used in two ways. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `service_id` | Foreign ID referencing [calendar.txt](/tables/calendar.md).`service_id` or ID | Required | Identifies a set of dates when a service exception occurs for one or more routes. Each (`service_id`, `date`) pair may only appear once in calendar_dates.txt if using calendar.txt and calendar_dates.txt in conjunction. If a `service_id` value appears in both calendar.txt and calendar_dates.txt, the information in calendar_dates.txt modifies the service information specified in calendar.txt. [1] |
| `date` | Date | Required | Date when service exception occurs. [1] |
| `exception_type` | Enum | Required | Indicates whether service is available on the date specified in the date field. Valid options are: `1` - Service has been added for the specified date. `2` - Service has been removed for the specified date. [1] |

# Grain

One row per `service_id, date` key in `calendar_dates.txt`. [1]

Primary key noted by the reference: `service_id, date`. [1]

# Relationships

- `calendar_dates.service_id` references [calendar.txt](/tables/calendar.md).`service_id`. [1]
- `calendar_dates.service_id` shares the service identifier namespace used by [trips.txt](/tables/trips.md) and [calendar.txt](/tables/calendar.md). [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.
- The file-level presence is `Conditionally Required`; read the table summary and schema before assuming the file is always present.

# Citations

[1] [GTFS Schedule Reference: calendar_dates.txt](https://gtfs.org/documentation/schedule/reference/#calendar_datestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
