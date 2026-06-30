---
type: "System"
title: "OpenTripPlanner"
description: "Open-source multimodal trip planner that can build routing graphs from GTFS and OpenStreetMap inputs."
resource: "https://docs.opentripplanner.org/en/latest/Basic-Tutorial/"
tags: [gtfs, schedule, system, routing, trip-planning, opentripplanner]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

OpenTripPlanner is an open-source trip-planning system. Its documentation describes a graph-building phase that analyzes GTFS, OpenStreetMap, and other inputs to build a transportation network, followed by a server phase that provides trip planning and API services. [1]

Use OpenTripPlanner as implementation guidance when the task is route planning, transfer-aware itinerary search, multimodal graph construction, or consumer behavior testing. Use raw GTFS table workflows when the task is field lookup, feed validation, or simple departure lists. [1] [2]

# Agent use

| need | use OTP? |
|---|---|
| List scheduled departures at one stop | Usually no; raw GTFS query is simpler. |
| Find an itinerary between origin and destination | Yes; OTP models routing graph and transfers. |
| Test how a consumer might route through GTFS and OSM | Yes. |
| Validate GTFS spec compliance | No; use [Canonical GTFS Schedule Validator](/systems/canonical-gtfs-schedule-validator.md). |
| Add realtime overlays to routing | Possible; OTP documentation says it can receive GTFS Realtime data. [2] |

# Relationships

- Use after [Validate a GTFS Feed](/processes/validate-a-gtfs-feed.md) when routing behavior matters.
- Use [Decide Static vs Realtime Source](/processes/decide-static-vs-realtime-source.md) before mixing static and realtime inputs.
- Feed data still follows [GTFS Schedule Feed](/datasets/gtfs-schedule-feed.md).

# Citations

[1] [OpenTripPlanner Basic Tutorial](https://docs.opentripplanner.org/en/latest/Basic-Tutorial/)
[2] [OpenTripPlanner Interfaces and Data Sources](https://docs.opentripplanner.org/en/v2.0.0/Interfaces-Data-Sources/)
[3] [GTFS.org Resources Overview](https://gtfs.org/resources/overview/)
