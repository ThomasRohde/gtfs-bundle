---
type: "System"
title: "Transitland"
description: "Catalog, archive, and API platform for discovering and inspecting public transit feeds."
resource: "https://www.transit.land/feeds"
tags: [gtfs, schedule, system, feed-catalog, transitland, atlas]
timestamp: "2026-06-30T03:53:45+00:00"
---

# Summary

Transitland aggregates and indexes public GTFS, GTFS Realtime, GBFS, and MDS source feeds. Its Source Feeds page can be used to search feed records, while Transitland Atlas is an open GitHub-backed feed registry in Distributed Mobility Feed Registry format. [1] [2]

Use Transitland when a task needs a feed URL, a stable feed identifier, an operator relationship, feed archive versions, or a quick way to inspect whether a feed has been imported recently. [1]

# Key identifiers

| item | meaning |
|---|---|
| Feed Onestop ID | Globally unique feed identifier beginning with `f-`. |
| Operator Onestop ID | Operator identifier beginning with `o-`. |
| `static_current` | Current static GTFS URL in Transitland Atlas. |
| Feed version | Imported GTFS version with earliest and latest service dates where available. |

# Relationships

- Transitland is a [GTFS Feed Catalog](/concepts/gtfs-feed-catalog.md).
- Transitland Atlas can point to a current feed URL that is then downloaded and queried with [Find and Use a GTFS Feed](/processes/find-and-use-gtfs-feed.md).
- The [Rejseplanen GTFS Schedule Feed](/datasets/rejseplanen-gtfs-feed.md) is a practical example of a Transitland-discoverable feed.

# Caveats

- A Transitland feed record can lag the producer's current state or reflect fetch/import errors.
- Transitland may expose derived metadata, archive versions, and API affordances that are useful but are not part of the GTFS Schedule specification.
- Always inspect the downloaded feed itself before relying on specific stop, trip, or service-date coverage.

# Citations

[1] [Transitland Source Feeds](https://www.transit.land/feeds)
[2] [Transitland Atlas feed registry documentation](https://www.transit.land/documentation/atlas)
[3] [GTFS.org: Sharing Data](https://gtfs.org/resources/sharing-data/)
