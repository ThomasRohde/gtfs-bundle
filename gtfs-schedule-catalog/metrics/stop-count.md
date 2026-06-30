---
type: "Metric"
title: "Stop Count"
description: "Count of rider boarding/alighting stops in a feed or route subset."
tags: [gtfs, schedule, metric, stop-count]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Definition

Count of rider boarding/alighting stops in a feed or route subset. [1]

# Source tables

- [stops](/tables/stops.md)
- [stop times](/tables/stop-times.md)

# Formula

```sql
SELECT COUNT(DISTINCT stop_id) AS stop_count
FROM stops
WHERE COALESCE(location_type, 0) = 0;
```

# Caveats

- Exclude stations, entrances/exits, generic nodes, and boarding areas unless the question explicitly asks for all locations.
- Treat times as service-day times and preserve values greater than 24:00:00 where applicable.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[2] [GTFS Schedule Reference: frequencies.txt](https://gtfs.org/documentation/schedule/reference/#frequenciestxt)
[3] [GTFS Schedule Reference: stop_times.txt](https://gtfs.org/documentation/schedule/reference/#stop_timestxt)
