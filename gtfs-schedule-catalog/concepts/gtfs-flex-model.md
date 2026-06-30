---
type: "Reference"
title: "GTFS Flex Model"
description: "Agent-oriented map of GTFS Flex demand-responsive service concepts and Schedule tables."
resource: "https://gtfs.org/community/extensions/flex/"
tags: [gtfs, schedule, flex, demand-responsive, model]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

GTFS Flex is a GTFS Schedule extension project for discoverability of demand-responsive transportation services. As accessed on 2026-06-30, the GTFS-Flex page says the major part of Flex was adopted into GTFS in March 2024 and describes use cases such as dial-a-ride, route deviation, point-to-zone, and checkpoint services. [1]

Flex extends the Schedule model with zones, pickup/drop-off windows, booking rules, and flexible location references. It remains Schedule data when represented in the adopted files and fields, but transactional booking and realtime components are outside this bundle's static Schedule scope. [1]

# Table map

| concept | tables / fields |
|---|---|
| Flexible zones | [locations.geojson](/tables/locations-geojson.md), `stop_times.location_id` |
| Location groups | [location_groups.txt](/tables/location-groups.md), [location_group_stops.txt](/tables/location-group-stops.md), `stop_times.location_group_id` |
| Pickup/drop-off windows | `start_pickup_drop_off_window`, `end_pickup_drop_off_window` in [stop_times.txt](/tables/stop-times.md) |
| Booking information | [booking_rules.txt](/tables/booking-rules.md), `pickup_booking_rule_id`, `drop_off_booking_rule_id` |
| Stop areas | [areas.txt](/tables/areas.md), [stop_areas.txt](/tables/stop-areas.md) |

# Agent boundary

Use [Query Demand Responsive Service](/processes/query-demand-responsive-service.md) for Flex-like questions. If the user asks to book a trip, check availability right now, or confirm request status, static GTFS Schedule is not sufficient; use a provider API or future GTFS-OnDemand-style source if available. [1]

# Citations

[1] [GTFS-Flex extension page](https://gtfs.org/community/extensions/flex/)
[2] [GTFS Schedule Reference: stop_times.txt](https://gtfs.org/documentation/schedule/reference/#stop_timestxt)
[3] [GTFS Schedule Reference: booking_rules.txt](https://gtfs.org/documentation/schedule/reference/#booking_rulestxt)
