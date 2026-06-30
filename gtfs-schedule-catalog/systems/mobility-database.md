---
type: "System"
title: "Mobility Database"
description: "MobilityData's global catalog for discovering GTFS, GTFS Realtime, and GBFS feeds."
resource: "https://mobilitydatabase.org/"
tags: [gtfs, schedule, system, feed-catalog, mobility-database]
timestamp: "2026-06-30T03:53:45+00:00"
---

# Summary

Mobility Database is a MobilityData-maintained global catalog for transit and mobility feeds. As accessed on 2026-06-30, its public site says it serves more than 6000 feeds from more than 99 countries and includes GTFS, GTFS Realtime, and GBFS feeds. [1]

Use it as a first discovery source when a user asks for schedule data in a geography but has not supplied a feed URL. It is a catalog source, not a replacement for validating a specific downloaded GTFS zip against the [GTFS Schedule Reference](/concepts/gtfs-schedule-reference-overview.md). [1]

# Retrieval role

| need | use Mobility Database for |
|---|---|
| Find candidate feed URLs | Search or browse feed records for a region, provider, or format. |
| Assess feed data quality | Check catalog-integrated validator reports where available. |
| Cross-reference catalogs | Use Mobility Database IDs and exported catalogs to map feeds to other registries. |
| Add or repair feed metadata | Follow MobilityData contribution paths for catalog updates. |

# Relationships

- Mobility Database is a [GTFS Feed Catalog](/concepts/gtfs-feed-catalog.md).
- Candidate Schedule feeds discovered here should be queried with [Find and Use a GTFS Feed](/processes/find-and-use-gtfs-feed.md).
- A discovered feed should be represented as a [Dataset](/datasets/gtfs-schedule-feed.md) concept when it becomes a durable example or dependency.

# Caveats

- Catalog records and feed URLs can drift; refresh before answering current timetable questions.
- Some feeds have access restrictions or license terms even when listed in a catalog.
- Catalog-level metadata does not prove that a specific feed version contains a given stop or service date.

# Citations

[1] [Mobility Database](https://mobilitydatabase.org/)
[2] [MobilityData mobility-database-catalogs repository](https://github.com/MobilityData/mobility-database-catalogs)
[3] [GTFS.org: Sharing Data](https://gtfs.org/resources/sharing-data/)
