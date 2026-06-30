---
type: "Reference"
title: "GTFS Schedule Reference Overview"
description: "Public OKF overview for the GTFS Schedule static specification as a data catalog."
resource: "https://gtfs.org/documentation/schedule/reference/"
tags: [gtfs, schedule, reference, data-catalog]
timestamp: "2026-06-30T03:53:45+00:00"
---

# Summary

GTFS Schedule, often called static GTFS, is modeled here as a data catalog: a feed zip is the dataset, each official file is a table, each row grain is explicit, and foreign keys are represented as Markdown links so agents can traverse joins. The normative source revision used for this bundle is **April 27, 2026**. [1]

This bundle is scoped to GTFS Schedule only. GTFS Realtime is intentionally out of scope and should be treated as a separate future bundle because it has different message formats, freshness semantics, and operational questions. [1]

# Source policy

| source_id | title | url | publisher | date | source_type | reliability | used_for |
|---|---|---|---|---|---|---|---|
| `gtfs-reference` | GTFS Schedule Reference | https://gtfs.org/documentation/schedule/reference/ | MobilityData / GTFS documentation | April 27, 2026 | Primary specification | Authoritative | File presence, field schemas, foreign keys, field meanings, required vs optional rules |
| `google-transit-reference` | google/transit GTFS Schedule reference source | https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md | Google Transit GitHub repository | current default branch, accessed 2026-06-30 | Primary source repository | Authoritative source mirror | Cross-checking raw Markdown and anchors |
| `gtfs-best-practices` | GTFS Schedule Best Practices | https://gtfs.org/documentation/schedule/schedule-best-practices/ | MobilityData / GTFS documentation | accessed 2026-06-30 | Secondary guidance | Guidance, not normative spec | Producer/consumer caveats and future enrichment leads |
| `mobility-database` | Mobility Database | https://mobilitydatabase.org/ | MobilityData | accessed 2026-06-30 | Feed catalog | Discovery source | Finding candidate GTFS, GTFS Realtime, and GBFS feeds |
| `transitland` | Transitland Source Feeds | https://www.transit.land/feeds | Transitland | accessed 2026-06-30 | Feed catalog and archive | Discovery source | Finding feed URLs, Onestop IDs, imported versions, and catalog metadata |
| `producer-feed-pages` | Producer or national feed pages | varies | Feed producer or jurisdiction | accessed per task | Feed source | Preferred for current endpoint and access terms | Downloading a concrete GTFS feed for a real-world query |

# How to use this bundle

- Start with [GTFS Schedule Feed](/datasets/gtfs-schedule-feed.md) for dataset grain and feed-level assumptions.
- If the user asks about a real place or operator, first use [GTFS Feed Catalog](/concepts/gtfs-feed-catalog.md) and [Find and Use a GTFS Feed](/processes/find-and-use-gtfs-feed.md) to locate a concrete feed version.
- Use `/tables/` for file and field lookup, especially [trips.txt](/tables/trips.md), [stop_times.txt](/tables/stop-times.md), [calendar.txt](/tables/calendar.md), and [calendar_dates.txt](/tables/calendar-dates.md).
- Use `/systems/` for external feed catalog systems such as [Mobility Database](/systems/mobility-database.md) and [Transitland](/systems/transitland.md).
- Use `/concepts/` for vocabulary such as [service day](/concepts/service-day.md), [headway](/concepts/headway.md), and [route_type](/concepts/route-type.md).
- Use `/metrics/` for pseudo-SQL definitions over GTFS fields.
- Use `/decisions/` to understand the modeling boundaries of this OKF bundle.

# Freshness

GTFS evolves through the public revision process. This bundle records the Schedule Reference revision marked **April 27, 2026** and flags Fares v2, GTFS-Flex, and Realtime as likely future enrichment areas. [1]

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
[3] [GTFS Schedule Best Practices](https://gtfs.org/documentation/schedule/schedule-best-practices/)
[4] [Mobility Database](https://mobilitydatabase.org/)
[5] [Transitland Source Feeds](https://www.transit.land/feeds)
[6] [GTFS.org: Sharing Data](https://gtfs.org/resources/sharing-data/)
