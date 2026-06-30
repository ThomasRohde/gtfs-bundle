---
type: "Process"
title: "Query Stop Departures"
description: "Repeatable GTFS Schedule workflow for departure lists at an exact stop or station area."
tags: [gtfs, schedule, process, departures, stop-times]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

Stop departures come from [stop_times.txt](/tables/stop-times.md), joined to [trips.txt](/tables/trips.md), [routes.txt](/tables/routes.md), and an active service set from [calendar.txt](/tables/calendar.md) and [calendar_dates.txt](/tables/calendar-dates.md). Use this playbook after discovering and validating a concrete feed. [1]

# Steps

1. Run [Find and Use a GTFS Feed](/processes/find-and-use-gtfs-feed.md) and [Validate a GTFS Feed](/processes/validate-a-gtfs-feed.md).
2. Resolve the stop scope with [Resolve Station Area](/processes/resolve-station-area.md): exact stop, parent station, platform set, or station-area stop set.
3. Build active service IDs for the requested service date with [Build Active Service Calendar](/processes/build-active-service-calendar.md).
4. Filter `stop_times.stop_id` to the selected stops.
5. Join `stop_times.trip_id` to `trips.trip_id`; filter `trips.service_id` to active service IDs.
6. Join `trips.route_id` to `routes.route_id` for route names, route type, and agency context.
7. Use `stop_times.departure_time` as the scheduled departure. If departure is empty but arrival is available, report the limitation rather than silently substituting unless the feed explicitly uses equal arrival/departure times for the stop.
8. Use `trips.trip_headsign` and `stop_times.stop_headsign` for rider-facing direction, with `stop_times.stop_headsign` taking stop-specific precedence where present.
9. Preserve times greater than 24:00:00 as service-day times and explain their next-calendar-day display if needed.

# Pseudo-SQL

```sql
WITH active_service AS (
  SELECT service_id
  FROM active_service_dates
  WHERE service_date = :service_date
),
selected_stops AS (
  SELECT stop_id
  FROM resolved_station_area_stops
)
SELECT st.departure_time,
       r.route_short_name,
       r.route_long_name,
       COALESCE(st.stop_headsign, t.trip_headsign) AS direction,
       st.stop_id,
       t.trip_id
FROM stop_times st
JOIN selected_stops s ON s.stop_id = st.stop_id
JOIN trips t ON t.trip_id = st.trip_id
JOIN active_service a ON a.service_id = t.service_id
JOIN routes r ON r.route_id = t.route_id
ORDER BY st.departure_time, r.route_short_name;
```

# Output requirements

- State feed URL/version or catalog record used.
- State whether the answer is exact-stop, parent-station, or station-area scoped.
- State whether the result is scheduled-only or includes realtime/API data.
- If the requested date is not covered by the feed, answer "not covered by this feed" rather than "no departures."

# Citations

[1] [GTFS Schedule Reference: stop_times.txt](https://gtfs.org/documentation/schedule/reference/#stop_timestxt)
[2] [GTFS Schedule Reference: trips.txt](https://gtfs.org/documentation/schedule/reference/#tripstxt)
[3] [GTFS Schedule Reference: calendar.txt](https://gtfs.org/documentation/schedule/reference/#calendartxt)
[4] [GTFS Schedule Reference: calendar_dates.txt](https://gtfs.org/documentation/schedule/reference/#calendar_datestxt)
