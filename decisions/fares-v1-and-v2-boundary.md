---
type: "Architectural Decision"
title: "Keep Fares v1 Full and Fares v2 Discoverable"
description: "The first pass gives Fares v1 full treatment and keeps Fares v2 tables compact but linked."
tags: [gtfs, schedule, decision, fares-v1-and-v2-boundary]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Context

Fares v1 remains common in feeds, while Fares v2 adds richer fare products, media, leg rules, join rules, and transfer rules that deserve deeper fare-specific enrichment later. [1]

# Decision

Accepted. This bundle supports discovery and basic joins for Fares v2 without pretending to be a fare-calculation manual.

# Consequences

- Agents can traverse the bundle using stable file paths and table links.
- Future enrichment can add depth without changing the concept IDs created here.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
