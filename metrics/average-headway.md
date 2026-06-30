---
type: "Metric"
title: "Average Headway"
description: "Average departure spacing for a route, direction, stop, or frequency window."
tags: [gtfs, schedule, metric, average-headway]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Definition

Average departure spacing for a route, direction, stop, or frequency window. [1]

# Source tables

- [frequencies](/tables/frequencies.md)
- [stop times](/tables/stop-times.md)
- [trips](/tables/trips.md)

# Formula

```sql
-- If frequencies.txt is present:
SELECT trip_id,
       SUM((time_to_seconds(end_time) - time_to_seconds(start_time))) /
       NULLIF(SUM((time_to_seconds(end_time) - time_to_seconds(start_time)) / headway_secs), 0) AS avg_headway_secs
FROM frequencies
GROUP BY trip_id;

-- If deriving from stop_times:
SELECT route_id, stop_id, AVG(next_departure_seconds - departure_seconds) AS avg_headway_secs
FROM ordered_departures
WHERE next_departure_seconds IS NOT NULL
GROUP BY route_id, stop_id;
```

# Caveats

- Prefer frequencies.txt when trips are headway-based; otherwise derive from ordered scheduled departures at a consistent stop or pattern.
- Treat times as service-day times and preserve values greater than 24:00:00 where applicable.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[2] [GTFS Schedule Reference: frequencies.txt](https://gtfs.org/documentation/schedule/reference/#frequenciestxt)
[3] [GTFS Schedule Reference: stop_times.txt](https://gtfs.org/documentation/schedule/reference/#stop_timestxt)
