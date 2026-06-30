---
type: "Metric"
title: "Peak Headway"
description: "The representative headway during a defined peak period."
tags: [gtfs, schedule, metric, peak-headway]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Definition

The representative headway during a defined peak period. [1]

# Source tables

- [frequencies](/tables/frequencies.md)
- [stop times](/tables/stop-times.md)
- [trips](/tables/trips.md)

# Formula

```sql
SELECT route_id,
       direction_id,
       percentile_cont(0.5) WITHIN GROUP (ORDER BY headway_secs) AS median_peak_headway_secs
FROM route_headways
WHERE departure_seconds BETWEEN peak_start_seconds AND peak_end_seconds
GROUP BY route_id, direction_id;
```

# Caveats

- Define peak windows explicitly for the analysis context; GTFS does not define a universal peak period.
- Treat times as service-day times and preserve values greater than 24:00:00 where applicable.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[2] [GTFS Schedule Reference: frequencies.txt](https://gtfs.org/documentation/schedule/reference/#frequenciestxt)
[3] [GTFS Schedule Reference: stop_times.txt](https://gtfs.org/documentation/schedule/reference/#stop_timestxt)
