---
type: "Reference"
title: "GTFS Realtime"
description: "Companion standard for realtime transit updates that should remain separate from the static Schedule table catalog."
resource: "https://gtfs.org/documentation/realtime/reference/"
tags: [gtfs, realtime, reference, boundary, companion-standard]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

GTFS Realtime is a companion feed specification for realtime transit information such as service disruptions, vehicle locations, and expected arrival times. It is distinct from GTFS Schedule and is represented with protocol buffer messages rather than Schedule `.txt` tables. [1]

The GTFS Realtime reference states that realtime entity IDs are resolved with respect to an existing GTFS feed, so Schedule remains the base identity and topology layer while Realtime supplies current updates. [1]

# Main realtime content types

| content type | use |
|---|---|
| Trip Updates | Predictions and updates for trips and stop times. |
| Vehicle Positions | Vehicle location and status. |
| Service Alerts | Disruptions, closures, effects, causes, and rider-facing alert text. |

# Boundary rule

Use this Schedule bundle for static trips, stops, calendars, routes, and scheduled departure times. Use GTFS Realtime or a local journey-planner API for current delays, cancellations, service alerts, platform changes, and vehicle positions. [1] [2]

# Relationships

- [Decide Static vs Realtime Source](/processes/decide-static-vs-realtime-source.md) chooses when to leave static Schedule.
- [Scope to Static GTFS Schedule](/decisions/scope-to-static-schedule.md) keeps Realtime outside the table catalog.
- [OpenTripPlanner](/systems/open-trip-planner.md) can use static GTFS and can receive GTFS Realtime data for routing applications. [3]

# Citations

[1] [GTFS Realtime Reference](https://gtfs.org/documentation/realtime/reference/)
[2] [GTFS Realtime Best Practices](https://gtfs.org/documentation/realtime/realtime-best-practices/)
[3] [OpenTripPlanner Interfaces and Data Sources](https://docs.opentripplanner.org/en/v2.0.0/Interfaces-Data-Sources/)
