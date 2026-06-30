---
type: "Process"
title: "Decide Static vs Realtime Source"
description: "Decision workflow for choosing GTFS Schedule, GTFS Realtime, or a journey-planner API for a transit question."
tags: [gtfs, schedule, realtime, process, source-selection]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

Static GTFS Schedule answers planned service questions. GTFS Realtime or a local journey-planner API is needed when the user asks about current operations, delays, cancellations, disruptions, vehicle positions, or live arrival predictions. [1] [2]

# Decision table

| user asks for | use | reason |
|---|---|---|
| Published scheduled departures for a date | GTFS Schedule | `stop_times`, `trips`, and service calendars are sufficient. |
| Service span, route count, stop count | GTFS Schedule | These are static feed metrics. |
| Is the bus delayed now? | GTFS Realtime or journey-planner API | Delay is not represented in static Schedule. |
| Is a trip cancelled today? | GTFS Realtime Trip Updates or local API | Cancellation is a realtime/service-status condition. |
| Where is the vehicle? | GTFS Realtime Vehicle Positions or local API | Vehicle location is realtime. |
| Is a station closed or service disrupted? | GTFS Realtime Service Alerts or local API | Alerts are realtime/disruption information. |
| Future scheduled service coverage | GTFS Schedule, with feed freshness check | Static feed may contain current and upcoming service. |

# Steps

1. Classify the question as scheduled, current, disruption, vehicle-location, or mixed.
2. For scheduled questions, use [Find and Use a GTFS Feed](/processes/find-and-use-gtfs-feed.md), [Validate a GTFS Feed](/processes/validate-a-gtfs-feed.md), and the relevant Schedule playbook.
3. For realtime questions, locate a GTFS Realtime feed or local journey-planner API and cite it separately from Schedule.
4. For mixed answers, report the scheduled baseline and the realtime overlay separately.
5. If only static GTFS is available, state that realtime status cannot be confirmed from the feed.

# Citations

[1] [GTFS Realtime Reference](https://gtfs.org/documentation/realtime/reference/)
[2] [GTFS Realtime Best Practices](https://gtfs.org/documentation/realtime/realtime-best-practices/)
[3] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
