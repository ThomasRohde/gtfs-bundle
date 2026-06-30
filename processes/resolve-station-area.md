---
type: "Process"
title: "Resolve Station Area"
description: "Workflow for deciding whether a GTFS stop question refers to one stop, a parent station, platforms, or nearby stop points."
tags: [gtfs, schedule, process, stops, station-area]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

Place names in user questions rarely map cleanly to exactly one `stop_id`. Use [stops.txt](/tables/stops.md), station hierarchy fields, and transfer/pathway context to decide whether the answer should be exact-stop, parent-station, platform-set, or station-area scoped. [1]

# Steps

1. Search [stops.txt](/tables/stops.md) by exact `stop_name`, normalized name, and known local aliases.
2. Inspect `location_type`: stop/platform, station, entrance/exit, generic node, or boarding area. [1]
3. If a parent station is selected, include child stops/platforms whose `parent_station` points to it when the user asks about departures from the station.
4. If nearby bus stops share the same station name or are connected by [transfers.txt](/tables/transfers.md), document whether they are included as station-area stops.
5. Use [pathways.txt](/tables/pathways.md) and [levels.txt](/tables/levels.md) when the question concerns internal station navigation or accessibility.
6. If a spatial radius is used because hierarchy and transfers are insufficient, state the radius and treat it as an analysis choice, not a GTFS rule.
7. Return the final stop set with `stop_id`, `stop_name`, `location_type`, and inclusion rationale.

# Scope labels

| label | meaning |
|---|---|
| Exact stop | One specific `stop_id`. |
| Parent station | Child stops/platforms belonging to a station row. |
| Platform set | Multiple platform rows serving the same station or boarding location. |
| Station area | Stops near or named for the station, usually including bus bays or street stops when justified. |

# Citations

[1] [GTFS Schedule Reference: stops.txt](https://gtfs.org/documentation/schedule/reference/#stopstxt)
[2] [GTFS Schedule Reference: transfers.txt](https://gtfs.org/documentation/schedule/reference/#transferstxt)
[3] [GTFS Schedule Reference: pathways.txt](https://gtfs.org/documentation/schedule/reference/#pathwaystxt)
