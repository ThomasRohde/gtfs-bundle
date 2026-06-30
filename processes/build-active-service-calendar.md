---
type: "Process"
title: "Build Active Service Calendar"
description: "Workflow for deriving active service IDs for a requested GTFS service date."
tags: [gtfs, schedule, process, calendar, service-day]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

Most operational GTFS queries need an active service set. Build it from [calendar.txt](/tables/calendar.md) weekly patterns and [calendar_dates.txt](/tables/calendar-dates.md) additions/removals before joining to [trips.txt](/tables/trips.md). [1] [2]

# Steps

1. Normalize the requested date to GTFS `YYYYMMDD` service-date form.
2. If `calendar.txt` is present, select rows where the date is between `start_date` and `end_date` inclusive and the weekday flag for the requested date is `1`. [1]
3. If `calendar_dates.txt` is present, add rows with `exception_type=1` for the requested date and remove rows with `exception_type=2`. [2]
4. If `calendar.txt` is omitted, require `calendar_dates.txt` to contain all dates of service; do not assume weekly service patterns. [2]
5. Join resulting `service_id` values to [trips.txt](/tables/trips.md).
6. Preserve the distinction between calendar date and [service day](/concepts/service-day.md), because stop times may exceed 24:00:00 for service continuing after midnight. [3]

# Pseudo-SQL

```sql
WITH base AS (
  SELECT service_id
  FROM calendar
  WHERE :service_date BETWEEN start_date AND end_date
    AND weekday_flag(:service_date, monday, tuesday, wednesday,
                     thursday, friday, saturday, sunday) = 1
),
adds AS (
  SELECT service_id
  FROM calendar_dates
  WHERE date = :service_date AND exception_type = 1
),
removes AS (
  SELECT service_id
  FROM calendar_dates
  WHERE date = :service_date AND exception_type = 2
)
SELECT service_id FROM base
UNION
SELECT service_id FROM adds
EXCEPT
SELECT service_id FROM removes;
```

# Failure modes

- If neither calendar file can establish service for the date, report feed coverage uncertainty or no active service in the feed, depending on validation status.
- If the requested date is outside feed coverage, do not infer no service in the real world.
- If a feed has only `calendar_dates.txt`, the absence of a date means no service for that service ID in that feed.

# Citations

[1] [GTFS Schedule Reference: calendar.txt](https://gtfs.org/documentation/schedule/reference/#calendartxt)
[2] [GTFS Schedule Reference: calendar_dates.txt](https://gtfs.org/documentation/schedule/reference/#calendar_datestxt)
[3] [GTFS Schedule Reference: Term Definitions](https://gtfs.org/documentation/schedule/reference/#term-definitions)
