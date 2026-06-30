---
type: "Metric"
title: "Calendar Service-Date Coverage"
description: "The set and span of service dates represented by calendar.txt and calendar_dates.txt."
tags: [gtfs, schedule, metric, calendar-service-date-coverage]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Definition

The set and span of service dates represented by calendar.txt and calendar_dates.txt. [1]

# Source tables

- [calendar](/tables/calendar.md)
- [calendar dates](/tables/calendar-dates.md)
- [feed info](/tables/feed-info.md)

# Formula

```sql
WITH active_service_dates AS (
  -- Expand calendar weekly patterns between start_date and end_date.
  -- Add calendar_dates where exception_type = 1.
  -- Remove calendar_dates where exception_type = 2.
)
SELECT MIN(service_date) AS first_service_date,
       MAX(service_date) AS last_service_date,
       COUNT(DISTINCT service_date) AS active_service_dates
FROM active_service_dates;
```

# Caveats

- Compare active service dates to feed_info.feed_start_date and feed_info.feed_end_date when feed_info is present.
- Treat times as service-day times and preserve values greater than 24:00:00 where applicable.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[2] [GTFS Schedule Reference: frequencies.txt](https://gtfs.org/documentation/schedule/reference/#frequenciestxt)
[3] [GTFS Schedule Reference: stop_times.txt](https://gtfs.org/documentation/schedule/reference/#stop_timestxt)
