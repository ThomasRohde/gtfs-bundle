---
type: "Process"
title: "Query Demand Responsive Service"
description: "Workflow for interpreting GTFS Flex and on-demand service information in a static Schedule feed."
tags: [gtfs, schedule, process, flex, demand-responsive]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

Demand-responsive GTFS Schedule questions require more than fixed-stop departure lookup. Inspect Flex-related locations, groups, pickup/drop-off windows, booking rules, and route/trip pickup/drop-off behavior before answering. [1] [2]

# Steps

1. Detect Flex-related tables and fields with [GTFS Flex Model](/concepts/gtfs-flex-model.md).
2. Validate the feed, especially references from [stop_times.txt](/tables/stop-times.md) to [locations.geojson](/tables/locations-geojson.md), [location_groups.txt](/tables/location-groups.md), and [booking_rules.txt](/tables/booking-rules.md).
3. Resolve whether the rider boards/alights at a fixed stop, location group, stop area, or GeoJSON zone.
4. Inspect pickup/drop-off window fields in [stop_times.txt](/tables/stop-times.md).
5. Inspect pickup/drop-off type fields on [routes.txt](/tables/routes.md) and [stop_times.txt](/tables/stop-times.md) for whether service is regularly scheduled, unavailable, phone-arranged, driver-coordinated, or otherwise constrained.
6. Follow booking-rule references for prior notice, phone number, URL, booking window, and rider-facing messages. [3]
7. State that static GTFS can describe discoverability and booking information, but cannot complete a booking or verify live capacity.

# Output requirements

- Identify whether the answer concerns fixed stops, zones, location groups, or booking rules.
- Include booking contact or URL only if present in the feed.
- Do not infer door-to-door availability from a zone unless the feed explicitly models it.
- Use [Decide Static vs Realtime Source](/processes/decide-static-vs-realtime-source.md) if the user asks about current availability.

# Citations

[1] [GTFS-Flex extension page](https://gtfs.org/community/extensions/flex/)
[2] [GTFS Schedule Reference: stop_times.txt](https://gtfs.org/documentation/schedule/reference/#stop_timestxt)
[3] [GTFS Schedule Reference: booking_rules.txt](https://gtfs.org/documentation/schedule/reference/#booking_rulestxt)
