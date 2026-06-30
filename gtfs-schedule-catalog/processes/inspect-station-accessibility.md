---
type: "Process"
title: "Inspect Station Accessibility"
description: "Workflow for answering static GTFS questions about wheelchair access, pathways, levels, and station navigation."
tags: [gtfs, schedule, process, accessibility, pathways]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

Static GTFS can describe accessibility-related schedule and station information, including wheelchair boarding fields, station/pathway graph data, levels, and trip accessibility fields. It cannot confirm live elevator outages or current disruption status without realtime/API sources. [1] [2]

# Steps

1. Resolve the station, platform, or station area with [Resolve Station Area](/processes/resolve-station-area.md).
2. Inspect [stops.txt](/tables/stops.md) for `wheelchair_boarding`, `location_type`, `parent_station`, `stop_access`, and station hierarchy. [1]
3. Inspect [pathways.txt](/tables/pathways.md) for internal station links, pathway modes, directionality, slopes, width, and traversal time. [2]
4. Inspect [levels.txt](/tables/levels.md) where pathways use levels or elevators. [3]
5. Inspect [trips.txt](/tables/trips.md) for `wheelchair_accessible` when the question concerns a specific trip or departure. [4]
6. If the user asks about current elevator status, disruptions, or temporary closures, use [Decide Static vs Realtime Source](/processes/decide-static-vs-realtime-source.md).

# Output requirements

- State whether the answer is static feed accessibility data or current operational status.
- Distinguish stop/platform accessibility from vehicle/trip accessibility.
- If pathways are absent, say the feed does not model internal station navigation rather than assuming no accessible path.

# Citations

[1] [GTFS Schedule Reference: stops.txt](https://gtfs.org/documentation/schedule/reference/#stopstxt)
[2] [GTFS Schedule Reference: pathways.txt](https://gtfs.org/documentation/schedule/reference/#pathwaystxt)
[3] [GTFS Schedule Reference: levels.txt](https://gtfs.org/documentation/schedule/reference/#levelstxt)
[4] [GTFS Schedule Reference: trips.txt](https://gtfs.org/documentation/schedule/reference/#tripstxt)
