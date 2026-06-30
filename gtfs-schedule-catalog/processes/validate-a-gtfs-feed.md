---
type: "Process"
title: "Validate a GTFS Feed"
description: "Workflow for checking a downloaded GTFS Schedule feed before using it as evidence."
tags: [gtfs, schedule, process, validation, feed-quality]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

Validate a GTFS feed after discovery and before operational query workflows. The goal is not only parser success; the agent must decide whether the feed can support the requested question, whether service dates cover the request, and whether validation notices affect the answer. [1] [2]

# Steps

1. Record feed URL, source catalog or producer page, download timestamp, and checksum.
2. Run [Canonical GTFS Schedule Validator](/systems/canonical-gtfs-schedule-validator.md) using the web validator, CLI, or a preserved validation report. [1] [2]
3. Inspect hard problems first: missing required files, malformed CSV, missing required fields, invalid dates/times, and broken foreign keys.
4. Inspect question-specific [Validator Notice](/concepts/validator-notice.md) groups before deciding the feed is fit for use.
5. Confirm service coverage for the requested date using [Build Active Service Calendar](/processes/build-active-service-calendar.md).
6. If the feed has serious issues, report the feed-quality limitation and avoid presenting missing rows as proof of no service.
7. Preserve validation report URL or validator version when the result is part of a durable analysis.

# Acceptance criteria

- The feed zip can be opened and required files for the intended query are present.
- The requested service date is inside the feed's effective service coverage.
- Broken references do not affect the stops, trips, routes, or services needed for the query.
- Remaining warnings are either irrelevant to the question or explicitly disclosed.

# Citations

[1] [Canonical GTFS Schedule Validator](https://gtfs-validator.mobilitydata.org/)
[2] [MobilityData/gtfs-validator](https://github.com/MobilityData/gtfs-validator)
[3] [Canonical GTFS Schedule Validator: Validation Rules and Metadata](https://gtfs-validator.mobilitydata.org/rules.html)
