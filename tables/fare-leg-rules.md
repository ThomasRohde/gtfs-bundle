---
type: "Table"
title: "fare_leg_rules.txt"
description: "Fare rules for individual legs of travel. File fare_leg_rules.txt provides a more detailed method for modeling fare structures. As such, the use of fare_leg_rules.txt is."
resource: "https://gtfs.org/documentation/schedule/reference/#fare_leg_rulestxt"
tags: [gtfs, schedule, table, fare-leg-rules, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`fare_leg_rules.txt` is a GTFS Schedule file with file-level presence `Optional`. Fare rules for individual legs of travel. Fares in fare_leg_rules.txt must be queried by filtering all the records in the file to find rules that match the leg to be traveled by the rider. To process the cost of a leg: 1. The file fare_leg_rules.txt must be filtered by the fields that define the characteristics of travel, these fields are: 2. If the leg exactly matches a record in fare_leg_rules.txt based on the characteristics of travel, that record must be processed to determine the cost of the leg. This file handles empty entries in two ways: empty semantics OR rule_priority. 3. If no exact matches are found AND the `rule_priority` field does not exist, then empty entries in `fare_leg_rules.network_id`, `fare_leg_rules.from_area_id`, and `fare_leg_rules.to_area_id` must be checked to process the cost of the leg: 4. If the `rule_priority` field exists, then 5. If the leg does not. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `leg_group_id` | ID | Optional | Identifies a group of entries in fare_leg_rules.txt. Used to describe fare transfer rules between `fare_transfer_rules.from_leg_group_id` and `fare_transfer_rules.to_leg_group_id`. Multiple entries in fare_leg_rules.txt may belong to the same `fare_leg_rules.leg_group_id`. The same entry in fare_leg_rules.txt (not including `fare_leg_rules.leg_group_id`) must not belong to multiple `fare_leg_rules.leg_group_id`. [1] |
| `network_id` | Foreign ID referencing [routes.txt](/tables/routes.md).`network_id` or [networks.txt](/tables/networks.md).`network_id` | Optional | Identifies a route network that applies for the fare leg rule. If the `rule_priority` field does not exist AND there are no matching `fare_leg_rules.network_id` values to the `network_id` being filtered, empty `fare_leg_rules.network_id` will be matched by default. An empty entry in `fare_leg_rules.network_id` corresponds to all networks defined in routes.txt or networks.txt excluding the ones listed under `fare_leg_rules.network_id` If the `rule_priority` field exists in the file, an empty `fare_leg_rules.network_id` indicates that the route network of the leg does not affect the matching of this rule. When. [1] |
| `from_area_id` | Foreign ID referencing [areas.txt](/tables/areas.md).`area_id` | Optional | Identifies a departure area. If the `rule_priority` field does not exist AND there are no matching `fare_leg_rules.from_area_id` values to the `area_id` being filtered, empty `fare_leg_rules.from_area_id` will be matched by default. An empty entry in `fare_leg_rules.from_area_id` corresponds to all areas defined in `areas.area_id` excluding the ones listed under `fare_leg_rules.from_area_id` If the `rule_priority` field exists in the file, an empty `fare_leg_rules.from_area_id` indicates that the departure area of the leg does not affect the matching of this rule. When matching against an effective fare leg of. [1] |
| `to_area_id` | Foreign ID referencing [areas.txt](/tables/areas.md).`area_id` | Optional | Identifies an arrival area. If the `rule_priority` field does not exist AND there are no matching `fare_leg_rules.to_area_id` values to the `area_id` being filtered, empty `fare_leg_rules.to_area_id` will be matched by default. An empty entry in `fare_leg_rules.to_area_id` corresponds to all areas defined in `areas.area_id` excluding the ones listed under `fare_leg_rules.to_area_id` If the `rule_priority` field exists in the file, an empty `fare_leg_rules.to_area_id` indicates that the arrival area of the leg does not affect the matching of this rule. When matching against an effective fare leg of multiple legs. [1] |
| `from_timeframe_group_id` | Foreign ID referencing [timeframes.txt](/tables/timeframes.md).`timeframe_group_id` | Optional | Defines the timeframe for the fare validation event at the start of the fare leg. The “start time” of the fare leg is the time at which the event is scheduled to occur. For example, the time could be the scheduled departure time of a bus at the start of a fare leg where the rider boards and validates their fare. For the rule matching semantics below, the start time is computed in local time, as determined by Local Time Semantics of timeframes.txt. The stop or station of the fare leg’s departure event should be used for timezone resolution, where appropriate. For a fare leg rule that specifies a. [1] |
| `to_timeframe_group_id` | Foreign ID referencing [timeframes.txt](/tables/timeframes.md).`timeframe_group_id` | Optional | Defines the timeframe for the fare validation event at the end of the fare leg. The “end time” of the fare leg is the time at which the event is scheduled to occur. For example, the time could be the scheduled arrival time of a bus at the end of a fare leg where the rider gets off and validates their fare. For the rule matching semantics below, the end time is computed in local time, as determined by Local Time Semantics of timeframes.txt. The stop or station of the fare leg’s arrival event should be used for timezone resolution, where appropriate. For a fare leg rule that specifies a `to_timeframe_group_id`. [1] |
| `fare_product_id` | Foreign ID referencing [fare-products.txt](/tables/fare-products.md).`fare_product_id` | Required | The fare product required to travel the leg. [1] |
| `rule_priority` | Non-negative integer | Optional | Defines the order of priority in which matching rules are applied to legs, allowing certain rules to take precedence over others. When multiple entries in fare_leg_rules.txt match, the rule or set of rules with the highest value for `rule_priority` will be selected. An empty value for `rule_priority` is treated as zero. [1] |

# Grain

One row per `network_id, from_area_id, to_area_id, from_timeframe_group_id, to_timeframe_group_id, fare_product_id` key in `fare_leg_rules.txt`. [1]

Primary key noted by the reference: `network_id, from_area_id, to_area_id, from_timeframe_group_id, to_timeframe_group_id, fare_product_id`. [1]

# Relationships

- `fare_leg_rules.network_id` references [routes.txt](/tables/routes.md).`network_id`. [1]
- `fare_leg_rules.network_id` references [networks.txt](/tables/networks.md).`network_id`. [1]
- `fare_leg_rules.from_area_id` references [areas.txt](/tables/areas.md).`area_id`. [1]
- `fare_leg_rules.to_area_id` references [areas.txt](/tables/areas.md).`area_id`. [1]
- `fare_leg_rules.from_timeframe_group_id` references [timeframes.txt](/tables/timeframes.md).`timeframe_group_id`. [1]
- `fare_leg_rules.to_timeframe_group_id` references [timeframes.txt](/tables/timeframes.md).`timeframe_group_id`. [1]
- `fare_leg_rules.fare_product_id` references [fare_products.txt](/tables/fare-products.md).`fare_product_id`. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- Fare concepts evolve in GTFS; this bundle records the April 27, 2026 Schedule Reference and keeps deeper fare modeling as a recommended enrichment pass.

# Citations

[1] [GTFS Schedule Reference: fare_leg_rules.txt](https://gtfs.org/documentation/schedule/reference/#fare_leg_rulestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
