---
type: "Reference"
title: "GTFS Optional Feature Map"
description: "Compact map of GTFS Schedule feature groups that are represented beyond the core required files."
tags: [gtfs, schedule, optional-files, fares-v2, flex]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

The first-pass catalog gives full table treatment to the core and common optional Schedule files, while keeping newer or specialized feature groups discoverable through compact table concepts and links. [1]

# Feature groups

| group | table concepts | modeling note |
|---|---|---|
| Fares v1 | [fare_attributes.txt](/tables/fare-attributes.md), [fare_rules.txt](/tables/fare-rules.md) | Legacy fare model commonly found in feeds. |
| Fares v2 | [timeframes.txt](/tables/timeframes.md), [rider_categories.txt](/tables/rider-categories.md), [fare_media.txt](/tables/fare-media.md), [fare_products.txt](/tables/fare-products.md), [fare_leg_rules.txt](/tables/fare-leg-rules.md), [fare_leg_join_rules.txt](/tables/fare-leg-join-rules.md), [fare_transfer_rules.txt](/tables/fare-transfer-rules.md) | More detailed fare modeling; use [Fares v2 Model](/concepts/fares-v2-model.md) and [Interpret Fares v2](/processes/interpret-fares-v2.md). |
| Pathways and levels | [pathways.txt](/tables/pathways.md), [levels.txt](/tables/levels.md) | Station internal navigation graph, with levels conditionally required for elevator pathways. |
| Translations and attribution | [translations.txt](/tables/translations.md), [attributions.txt](/tables/attributions.md) | Localized values and dataset attribution metadata. |
| GTFS-Flex and rider-requested service | [location_groups.txt](/tables/location-groups.md), [location_group_stops.txt](/tables/location-group-stops.md), [locations.geojson](/tables/locations-geojson.md), [booking_rules.txt](/tables/booking-rules.md) | Demand-responsive pickup/drop-off areas and booking rules; use [GTFS Flex Model](/concepts/gtfs-flex-model.md). |
| Static vs realtime boundary | [GTFS Realtime](/concepts/gtfs-realtime.md), [Decide Static vs Realtime Source](/processes/decide-static-vs-realtime-source.md) | Current disruptions, delays, vehicle positions, and alerts are companion-standard concerns, not Schedule table fields. |

# Maturity guidance

Use [GTFS Extension Maturity](/concepts/gtfs-extension-maturity.md) before treating an optional feature, extension page, proposal, or best practice as a normative Schedule requirement.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[2] [GTFS-Fares v2 extension page](https://gtfs.org/community/extensions/fares-v2/)
[3] [GTFS-Flex extension page](https://gtfs.org/community/extensions/flex/)
[4] [GTFS Realtime Reference](https://gtfs.org/documentation/realtime/reference/)
