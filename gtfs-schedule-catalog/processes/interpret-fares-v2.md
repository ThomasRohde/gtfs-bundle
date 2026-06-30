---
type: "Process"
title: "Interpret Fares v2"
description: "Workflow for determining whether and how a GTFS feed can answer rider-facing fare questions."
tags: [gtfs, schedule, process, fares-v2, fares]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

Interpret Fares v2 by first deciding whether the feed uses Fares v2, Fares v1, or both. Then follow the Fares v2 tables from products and media through leg rules, timeframes, networks, and transfer rules. [1] [2]

# Steps

1. Validate the feed and inspect fare-related notices with [Validate a GTFS Feed](/processes/validate-a-gtfs-feed.md).
2. Detect Fares v2 tables: [fare_products.txt](/tables/fare-products.md), [fare_media.txt](/tables/fare-media.md), [fare_leg_rules.txt](/tables/fare-leg-rules.md), [fare_transfer_rules.txt](/tables/fare-transfer-rules.md), [timeframes.txt](/tables/timeframes.md), and [rider_categories.txt](/tables/rider-categories.md).
3. If both Fares v1 and Fares v2 are present, prefer one method consistently for the answer; do not merge the two unless a feed-specific source documents that behavior. [2]
4. Identify the fare product, media, rider category, route/network, zone, time period, and transfer rule needed by the user's question.
5. If a required Fares v2 feature is absent or still only discussed as an extension/proposal, report the gap instead of inventing fare logic.
6. Cite the feed version, fare tables used, and whether the answer is base fare, rider category, time-based, zone/network-based, or transfer-related.

# Failure modes

- A feed may have fare products but no leg rules that apply to a trip.
- A feed may use legacy Fares v1 only.
- A feed may include evolving or partially adopted Fares v2 features that are not supported by the consumer being modeled.

# Citations

[1] [GTFS Fares: Introduction](https://gtfs.org/resources/gtfs-schedule-feature-guides/fares/intro/)
[2] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[3] [GTFS-Fares v2 extension page](https://gtfs.org/community/extensions/fares-v2/)
