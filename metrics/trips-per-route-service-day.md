---
type: "Metric"
title: "Trips Per Route Per Service Day"
description: "Count of scheduled trips by route and active service date."
tags: [gtfs, schedule, metric, trips-per-route-service-day]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Definition

Count of scheduled trips by route and active service date. [1]

# Source tables

- [trips](/tables/trips.md)
- [calendar](/tables/calendar.md)
- [calendar dates](/tables/calendar-dates.md)

# Formula

```sql
SELECT t.route_id, d.service_date, COUNT(DISTINCT t.trip_id) AS trips
FROM trips t
JOIN active_service_dates d ON d.service_id = t.service_id
GROUP BY t.route_id, d.service_date;
```

# Caveats

- Build `active_service_dates` from calendar weekly patterns plus calendar_dates additions/removals.
- Treat times as service-day times and preserve values greater than 24:00:00 where applicable.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[2] [GTFS Schedule Reference: frequencies.txt](https://gtfs.org/documentation/schedule/reference/#frequenciestxt)
[3] [GTFS Schedule Reference: stop_times.txt](https://gtfs.org/documentation/schedule/reference/#stop_timestxt)
