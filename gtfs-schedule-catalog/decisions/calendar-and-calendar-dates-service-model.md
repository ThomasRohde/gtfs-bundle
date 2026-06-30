---
type: "Architectural Decision"
title: "Handle Calendar and Calendar Dates Together"
description: "Service-date modeling uses both calendar.txt and calendar_dates.txt, including the either/or rule."
tags: [gtfs, schedule, decision, calendar-and-calendar-dates-service-model]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Context

The Schedule Reference makes calendar.txt conditionally required unless all service dates are defined in calendar_dates.txt; calendar_dates.txt is required if calendar.txt is omitted. [1]

# Decision

Accepted. Metrics should build an active service-date set before joining to trips.

# Consequences

- Agents can traverse the bundle using stable file paths and table links.
- Future enrichment can add depth without changing the concept IDs created here.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
