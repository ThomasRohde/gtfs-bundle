---
type: "Reference"
title: "Fares v2 Model"
description: "Agent-oriented map of GTFS Fares v2 concepts, tables, and interpretation boundaries."
resource: "https://gtfs.org/resources/gtfs-schedule-feature-guides/fares/intro/"
tags: [gtfs, schedule, fares-v2, fares, model]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

Fares v2 is a GTFS Schedule feature and extension project for rider-facing fare information. GTFS.org describes Fares v2 as covering fare products, fare media, rider categories, route-based fares, zone-based fares, time-based fares, and fare transfers. [1]

The Schedule Reference describes Fares v1 as the legacy option and Fares v2 as the more detailed option; both can be present, but a consumer should use only one fare modeling method for a dataset, with Fares v2 recommended to take precedence. [2]

# Table map

| concept | tables |
|---|---|
| Fare products and media | [fare_products.txt](/tables/fare-products.md), [fare_media.txt](/tables/fare-media.md) |
| Rider categories | [rider_categories.txt](/tables/rider-categories.md) |
| Time-based fares | [timeframes.txt](/tables/timeframes.md), [fare_leg_rules.txt](/tables/fare-leg-rules.md) |
| Route/network-based fares | [networks.txt](/tables/networks.md), [route_networks.txt](/tables/route-networks.md), [fare_leg_rules.txt](/tables/fare-leg-rules.md) |
| Transfer fares | [fare_transfer_rules.txt](/tables/fare-transfer-rules.md), [fare_leg_join_rules.txt](/tables/fare-leg-join-rules.md) |
| Legacy fallback | [fare_attributes.txt](/tables/fare-attributes.md), [fare_rules.txt](/tables/fare-rules.md) |

# Agent boundary

Use this concept to identify whether Fares v2 data exists and how the main tables join. Do not promise complete fare calculation unless the feed has the required Fares v2 tables and the fare question's required feature is officially modeled in the reference fields. Check [GTFS Extension Maturity](/concepts/gtfs-extension-maturity.md) for evolving features. [1] [3]

# Citations

[1] [GTFS Fares: Introduction](https://gtfs.org/resources/gtfs-schedule-feature-guides/fares/intro/)
[2] [GTFS Schedule Reference: Fare versions](https://gtfs.org/documentation/schedule/reference/)
[3] [GTFS-Fares v2 extension page](https://gtfs.org/community/extensions/fares-v2/)
