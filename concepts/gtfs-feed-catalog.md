---
type: "Business Term"
title: "GTFS Feed Catalog"
description: "A registry or directory used to discover actual GTFS feed URLs before querying schedule data."
resource: "https://gtfs.org/resources/sharing-data/"
tags: [gtfs, schedule, business-term, feed-catalog, discovery]
timestamp: "2026-06-30T03:53:45+00:00"
---

# Summary

A GTFS feed catalog is a discovery layer for finding real feed endpoints, metadata, archives, licenses, and provider notes. It is different from the GTFS Schedule Reference: the reference defines file formats, while catalogs identify actual feeds that can be downloaded and queried. [1]

Use a feed catalog when a question names a real place, operator, country, or stop but no local GTFS zip has been supplied. After finding a candidate feed, use [Find and Use a GTFS Feed](/processes/find-and-use-gtfs-feed.md) and then query [stops.txt](/tables/stops.md), [stop_times.txt](/tables/stop-times.md), [trips.txt](/tables/trips.md), [calendar.txt](/tables/calendar.md), and [calendar_dates.txt](/tables/calendar-dates.md). [1]

# Common catalog types

| catalog type | examples | use |
|---|---|---|
| Global feed catalog | [Mobility Database](/systems/mobility-database.md), [Transitland](/systems/transitland.md) | Search across many countries and operators. |
| National or regional access point | Transport data portals, agency developer portals | Prefer when the jurisdiction publishes official endpoints or access terms. |
| Operator feed page | Transit agency data page | Prefer when it is the canonical producer source. |
| Archive | Transitland feed versions, producer archives | Reproduce historical analyses or inspect earlier feed validity windows. |

# Practical rule

For live or date-specific departure questions, first find the actual feed or API source. This bundle can explain the GTFS joins and fields, but it cannot answer a real timetable question without a concrete feed version. [1]

# Citations

[1] [GTFS.org: Sharing Data](https://gtfs.org/resources/sharing-data/)
[2] [Mobility Database](https://mobilitydatabase.org/)
[3] [Transitland Source Feeds](https://www.transit.land/feeds)
