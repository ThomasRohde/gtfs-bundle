---
type: "Metric"
title: "Service Span"
description: "The first-to-last scheduled departure window for a service date, route, direction, or stop pattern."
tags: [gtfs, schedule, metric, service-span]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Definition

The first-to-last scheduled departure window for a service date, route, direction, or stop pattern. [1]

# Source tables

- [stop times](/tables/stop-times.md)
- [trips](/tables/trips.md)
- [calendar](/tables/calendar.md)
- [calendar dates](/tables/calendar-dates.md)

# Formula

```sql
WITH active_trips AS (
  SELECT t.trip_id, t.route_id, t.service_id
  FROM trips t
  JOIN active_service_dates d ON d.service_id = t.service_id
)
SELECT route_id,
       service_date,
       MIN(first_departure_seconds) AS first_departure_seconds,
       MAX(last_departure_seconds) AS last_departure_seconds
FROM active_trips
JOIN (
  SELECT trip_id,
         MIN(time_to_seconds(departure_time)) AS first_departure_seconds,
         MAX(time_to_seconds(departure_time)) AS last_departure_seconds
  FROM stop_times
  WHERE departure_time IS NOT NULL
  GROUP BY trip_id
) trip_bounds USING (trip_id)
GROUP BY route_id, service_date;
```

# Caveats

- Use service-day time parsing; GTFS times may exceed 24:00:00, so do not truncate at midnight.
- Treat times as service-day times and preserve values greater than 24:00:00 where applicable.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[2] [GTFS Schedule Reference: frequencies.txt](https://gtfs.org/documentation/schedule/reference/#frequenciestxt)
[3] [GTFS Schedule Reference: stop_times.txt](https://gtfs.org/documentation/schedule/reference/#stop_timestxt)
