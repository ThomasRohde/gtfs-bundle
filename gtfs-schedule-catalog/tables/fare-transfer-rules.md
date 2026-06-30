---
type: "Table"
title: "fare_transfer_rules.txt"
description: "Fare rules for transfers between legs of travel. Along with fare_leg_rules.txt, file fare_transfer_rules.txt provides a more detailed method for modeling fare."
resource: "https://gtfs.org/documentation/schedule/reference/#fare_transfer_rulestxt"
tags: [gtfs, schedule, table, fare-transfer-rules, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`fare_transfer_rules.txt` is a GTFS Schedule file with file-level presence `Optional`. Fare rules for transfers between legs of travel defined in `fare_leg_rules.txt`. A fare transfer rule defined from `from_leg_group_id` to `to_leg_group_id` does not apply in the reverse direction. To process the cost of a multi-leg journey: 1. The applicable fare leg groups defined in fare_leg_rules.txt should be determined for all individual legs or effective fare legs of travel based on the rider’s journey. 2. The file fare_transfer_rules.txt must be filtered by the fields that define the characteristics of the transfer, these fields are: 3. If the transfer exactly matches a record in fare_transfer_rules.txt based on the characteristics of the transfer, then that record must be processed to determine the transfer cost. 4. If no exact matches are found, then empty entries in `from_leg_group_id` or in `to_leg_group_id` must be checked to process the transfer cost: 5. If the transfer. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `from_leg_group_id` | Foreign ID referencing [fare-leg-rules.txt](/tables/fare-leg-rules.md).`leg_group_id` | Optional | Identifies a group of pre-transfer fare leg rules. If there are no matching `fare_transfer_rules.from_leg_group_id` values to the `leg_group_id` being filtered, empty `fare_transfer_rules.from_leg_group_id` will be matched by default. An empty entry in `fare_transfer_rules.from_leg_group_id` corresponds to all leg groups defined under `fare_leg_rules.leg_group_id` excluding the ones listed under `fare_transfer_rules.from_leg_group_id` [1] |
| `to_leg_group_id` | Foreign ID referencing [fare-leg-rules.txt](/tables/fare-leg-rules.md).`leg_group_id` | Optional | Identifies a group of post-transfer fare leg rules. If there are no matching `fare_transfer_rules.to_leg_group_id` values to the `leg_group_id` being filtered, empty `fare_transfer_rules.to_leg_group_id` will be matched by default. An empty entry in `fare_transfer_rules.to_leg_group_id` corresponds to all leg groups defined under `fare_leg_rules.leg_group_id` excluding the ones listed under `fare_transfer_rules.to_leg_group_id` [1] |
| `transfer_count` | Non-zero integer | Conditionally Forbidden | Defines how many consecutive transfers the transfer rule may be applied to. Valid options are: `-1` - No limit. `1` or more - Defines how many transfers the transfer rule may span. If a sub-journey matches multiple records with different `transfer_count`s, then the rule with the minimum `transfer_count` that is greater than or equal to the current transfer count of the sub-journey is to be selected. Conditionally Forbidden: - Forbidden if `fare_transfer_rules.from_leg_group_id` does not equal `fare_transfer_rules.to_leg_group_id`. - Required if `fare_transfer_rules.from_leg_group_id` equals. [1] |
| `duration_limit` | Positive integer | Optional | Defines the duration limit of the transfer. Must be expressed in integer increments of seconds. If there is no duration limit, `fare_transfer_rules.duration_limit` must be empty. [1] |
| `duration_limit_type` | Enum | Conditionally Required | Defines the relative start and end of `fare_transfer_rules.duration_limit`. Valid options are: `0` - Between the departure fare validation of the first leg in transfer sub-journey and the arrival fare validation of the last leg in transfer sub-journey. `1` - Between the departure fare validation of the first leg in transfer sub-journey and the departure fare validation of the last leg in transfer sub-journey. `2` - Between the arrival fare validation of the first leg in transfer sub-journey and the departure fare validation of the last leg in transfer sub-journey. `3` - Between the arrival fare validation of the. [1] |
| `fare_transfer_type` | Enum | Required | Indicates the cost processing method of transferring between legs in a journey: ![](examples/2-leg.svg) Valid options are: `0` - From-leg `fare_leg_rules.fare_product_id` plus `fare_transfer_rules.fare_product_id`; A + AB. `1` - From-leg `fare_leg_rules.fare_product_id` plus `fare_transfer_rules.fare_product_id` plus to-leg `fare_leg_rules.fare_product_id`; A + AB + B. `2` - `fare_transfer_rules.fare_product_id`; AB. Cost processing interactions between multiple transfers in a journey: ![](examples/3-leg.svg) `fare_transfer_type` Processing A > B Processing B > C `0` A + AB S + BC `1` A + AB +B S + BC + C `2` AB. [1] |
| `fare_product_id` | Foreign ID referencing [fare-products.txt](/tables/fare-products.md).`fare_product_id` | Optional | The fare product required to transfer between two fare legs. If empty, the cost of the transfer rule is 0. [1] |

# Grain

One row per `from_leg_group_id, to_leg_group_id, fare_product_id, transfer_count, duration_limit` key in `fare_transfer_rules.txt`. [1]

Primary key noted by the reference: `from_leg_group_id, to_leg_group_id, fare_product_id, transfer_count, duration_limit`. [1]

# Relationships

- `fare_transfer_rules.from_leg_group_id` references [fare_leg_rules.txt](/tables/fare-leg-rules.md).`leg_group_id`. [1]
- `fare_transfer_rules.to_leg_group_id` references [fare_leg_rules.txt](/tables/fare-leg-rules.md).`leg_group_id`. [1]
- `fare_transfer_rules.fare_product_id` references [fare_products.txt](/tables/fare-products.md).`fare_product_id`. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- Fare concepts evolve in GTFS; this bundle records the April 27, 2026 Schedule Reference and keeps deeper fare modeling as a recommended enrichment pass.

# Citations

[1] [GTFS Schedule Reference: fare_transfer_rules.txt](https://gtfs.org/documentation/schedule/reference/#fare_transfer_rulestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
