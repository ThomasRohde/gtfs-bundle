# Concepts

This index is a progressive-disclosure entry point for this part of the GTFS Schedule OKF bundle.

| concept | type | description |
|---|---|---|
| [gtfs schedule reference overview](gtfs-schedule-reference-overview.md) | Reference | Bundle overview, source table, scope, and freshness. |
| [source policy](source-policy.md) | Reference | Citation and source boundary policy. |
| [optional feature map](optional-feature-map.md) | Reference | Compact map of Fares v2, pathways, translations, attributions, and Flex files. |
| [validator notice](validator-notice.md) | Reference | A validation finding that should be interpreted before trusting or rejecting GTFS feed answers. |
| [gtfs realtime](gtfs-realtime.md) | Reference | Companion standard for realtime transit updates that should remain separate from the static Schedule table catalog. |
| [gtfs extension maturity](gtfs-extension-maturity.md) | Reference | How to distinguish adopted specification content, extensions, experimental fields, best practices, and proposals. |
| [fares v2 model](fares-v2-model.md) | Reference | Agent-oriented map of GTFS Fares v2 concepts, tables, and interpretation boundaries. |
| [gtfs flex model](gtfs-flex-model.md) | Reference | Agent-oriented map of GTFS Flex demand-responsive service concepts and Schedule tables. |
| [gtfs feed catalog](gtfs-feed-catalog.md) | Business Term | A registry or directory used to discover actual GTFS feed URLs before querying schedule data. |
| [service day](service-day.md) | Business Term | A GTFS scheduling day that may extend past 24:00:00 and does not always equal a calendar day. |
| [headway](headway.md) | Business Term | The time between departures from the same stop, represented directly in frequencies.txt or derived from stop_times.txt. |
| [route type](route-type.md) | Business Term | The GTFS field that classifies a route's transit mode. |
| [location type](location-type.md) | Business Term | The GTFS field that classifies stop rows as stops, stations, entrances, generic nodes, or boarding areas. |
| [timepoint](timepoint.md) | Business Term | A stop_time marker that distinguishes exact scheduled times from approximate or interpolated times. |
| [block interlining](block-interlining.md) | Business Term | A vehicle-work concept where sequential trips can be linked by block_id or explicit transfer rules. |
| [frequency vs schedule based service](frequency-vs-schedule-based-service.md) | Business Term | The distinction between headway-based trips and fixed scheduled trips represented in frequencies.txt. |
| [fare zone](fare-zone.md) | Business Term | A zone identifier used by Fares v1 rules to match origins, destinations, and contained zones. |
| [trip](trip.md) | Business Term | A sequence of two or more stops for a route during a specific time period. |
| [route](route.md) | Business Term | A group of trips displayed to riders as a single service. |
