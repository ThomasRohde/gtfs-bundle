---
type: "Architectural Decision"
title: "Scope to Static GTFS Schedule"
description: "This bundle excludes GTFS Realtime and focuses on static Schedule feeds."
tags: [gtfs, schedule, decision, scope-to-static-schedule]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Context

GTFS Realtime has separate protocol buffer messages, freshness expectations, and operational patterns, so mixing it into this Schedule table catalog would blur modeling boundaries. Realtime remains a companion standard for current trip updates, vehicle positions, and service alerts. [1] [2]

# Decision

Accepted. Realtime is documented here only as a boundary and companion-standard concept through [GTFS Realtime](/concepts/gtfs-realtime.md) and [Decide Static vs Realtime Source](/processes/decide-static-vs-realtime-source.md). A full Realtime message catalog should be a separate OKF bundle.

# Consequences

- Agents can traverse the bundle using stable file paths and table links.
- Future enrichment can add depth without changing the concept IDs created here.
- Agents must switch to GTFS Realtime or journey-planner APIs for delays, cancellations, vehicle positions, alerts, and other current operational status.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[2] [GTFS Realtime Reference](https://gtfs.org/documentation/realtime/reference/)
