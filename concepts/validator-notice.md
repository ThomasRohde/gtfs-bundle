---
type: "Reference"
title: "Validator Notice"
description: "A validation finding that should be interpreted before trusting or rejecting GTFS feed answers."
resource: "https://gtfs-validator.mobilitydata.org/rules.html"
tags: [gtfs, schedule, validation, notice, data-quality]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

A validator notice is a finding emitted by the Canonical GTFS Schedule Validator. Notices help distinguish structural problems, specification compliance issues, and best-practice quality problems before an agent treats a GTFS feed as queryable evidence. [1]

Do not collapse all notices into "feed unusable" or "feed valid." For agent work, a notice should be mapped to the question being answered: a missing required file can block most schedule queries, while a naming best-practice warning may not block a departure lookup. [1] [2]

# Agent interpretation pattern

| question | inspect notices for |
|---|---|
| Departures for a stop/date | stop references, trip references, service-date coverage, required fields in [stop_times.txt](/tables/stop-times.md), [trips.txt](/tables/trips.md), [calendar.txt](/tables/calendar.md), and [calendar_dates.txt](/tables/calendar-dates.md). |
| Service coverage | stale or insufficient calendar coverage, missing feed metadata, and exception-date problems. |
| Fares | Fares v1/v2 table consistency and missing referenced products, zones, media, rider categories, or timeframes. |
| Station accessibility | [stops.txt](/tables/stops.md), [pathways.txt](/tables/pathways.md), [levels.txt](/tables/levels.md), and related accessibility fields. |

# Relationships

- Produced by [Canonical GTFS Schedule Validator](/systems/canonical-gtfs-schedule-validator.md).
- Reviewed during [Validate a GTFS Feed](/processes/validate-a-gtfs-feed.md).
- Should be cited or summarized when a feed-quality issue affects the final answer.

# Citations

[1] [Canonical GTFS Schedule Validator: Validation Rules and Metadata](https://gtfs-validator.mobilitydata.org/rules.html)
[2] [Canonical GTFS Schedule Validator](https://gtfs-validator.mobilitydata.org/)
