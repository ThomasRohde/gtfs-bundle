---
type: "Metric"
title: "Route Count"
description: "Count of distinct rider-facing routes in routes.txt."
tags: [gtfs, schedule, metric, route-count]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Definition

Count of distinct rider-facing routes in routes.txt. [1]

# Source tables

- [routes](/tables/routes.md)

# Formula

```sql
SELECT COUNT(DISTINCT route_id) AS route_count
FROM routes;
```

# Caveats

- Filter by route_type or agency_id when comparing modal or agency-specific route counts.
- Treat times as service-day times and preserve values greater than 24:00:00 where applicable.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[2] [GTFS Schedule Reference: frequencies.txt](https://gtfs.org/documentation/schedule/reference/#frequenciestxt)
[3] [GTFS Schedule Reference: stop_times.txt](https://gtfs.org/documentation/schedule/reference/#stop_timestxt)
