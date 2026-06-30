---
type: "Architectural Decision"
title: "Model Each GTFS File as a Table"
description: "Each official GTFS Schedule file is represented as one OKF Table concept."
tags: [gtfs, schedule, decision, model-each-gtfs-file-as-table]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Context

This mirrors a data catalog: file paths are stable table IDs, schema rows are field definitions, and foreign-key references become graph links. [1]

# Decision

Accepted. This keeps retrieval predictable and lets agents answer field, requiredness, grain, and join questions without scanning the full specification.

# Consequences

- Agents can traverse the bundle using stable file paths and table links.
- Future enrichment can add depth without changing the concept IDs created here.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
