---
type: "Process"
title: "Find and Use a GTFS Feed"
description: "Practical workflow for moving from a place-based timetable question to a concrete GTFS feed query."
tags: [gtfs, schedule, process, feed-discovery, querying]
timestamp: "2026-06-30T03:53:45+00:00"
---

# Summary

This process turns the GTFS specification catalog into an operational workflow. Use it whenever a user asks a real-world question, such as departures from a named stop, without providing a GTFS zip. A specification bundle explains fields and joins; a timetable answer requires a concrete feed version. [1]

# Steps

1. Identify the geography, operator, station, or stop name from the question.
2. Search a [GTFS Feed Catalog](/concepts/gtfs-feed-catalog.md), starting with [Mobility Database](/systems/mobility-database.md), [Transitland](/systems/transitland.md), and official national or operator portals. [1] [2] [3]
3. Prefer the producer's official feed URL when available; use catalog records to cross-check the URL, license, feed version, archive status, and service-date coverage. [1] [2]
4. Download the GTFS zip and record source URL, download timestamp, checksum, and catalog record identifier.
5. Inspect [feed_info.txt](/tables/feed-info.md) when present. If absent, do not invent feed metadata; derive analysis coverage from [calendar.txt](/tables/calendar.md), [calendar_dates.txt](/tables/calendar-dates.md), and catalog/version notes.
6. Find candidate stops in [stops.txt](/tables/stops.md). For station-area questions, check parent stations, platforms, nearby bus stops, pathways, transfers, and stop names before assuming one exact stop row.
7. Join [stop_times.txt](/tables/stop-times.md) to [trips.txt](/tables/trips.md) by `trip_id`.
8. Build active service dates from [calendar.txt](/tables/calendar.md) and [calendar_dates.txt](/tables/calendar-dates.md), then filter `trips.service_id` to the requested date.
9. Return departures using `stop_times.departure_time`, route context from [routes.txt](/tables/routes.md), and destination/headsign fields from [trips.txt](/tables/trips.md) or [stop_times.txt](/tables/stop-times.md).
10. If realtime accuracy is required, switch to a GTFS Realtime or local journey-planner API source; static GTFS Schedule alone cannot report delays, cancellations, or realtime platform changes.

# Pseudo-SQL

```sql
WITH active_service AS (
  -- Expand calendar.txt weekday ranges.
  -- Add calendar_dates.exception_type = 1.
  -- Remove calendar_dates.exception_type = 2.
  SELECT service_id
  FROM active_service_dates
  WHERE service_date = :requested_date
),
candidate_stops AS (
  SELECT stop_id, stop_name
  FROM stops
  WHERE stop_name ILIKE :stop_name_pattern
)
SELECT st.departure_time,
       r.route_short_name,
       r.route_long_name,
       t.trip_headsign,
       s.stop_name
FROM stop_times st
JOIN candidate_stops s ON s.stop_id = st.stop_id
JOIN trips t ON t.trip_id = st.trip_id
JOIN active_service a ON a.service_id = t.service_id
JOIN routes r ON r.route_id = t.route_id
ORDER BY st.departure_time;
```

# Quality checks

- Confirm the feed includes the requested date before reporting no service.
- Include access date and feed version when the answer depends on a current feed URL.
- State whether the answer is exact-stop, parent-station, or station-area scoped.
- Label non-GTFS sources, such as journey-planner APIs, as implementation sources rather than GTFS Schedule evidence.

# Citations

[1] [GTFS.org: Sharing Data](https://gtfs.org/resources/sharing-data/)
[2] [Mobility Database](https://mobilitydatabase.org/)
[3] [Transitland Source Feeds](https://www.transit.land/feeds)
[4] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
