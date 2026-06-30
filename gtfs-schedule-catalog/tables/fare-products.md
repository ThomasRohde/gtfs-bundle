---
type: "Table"
title: "fare_products.txt"
description: "To describe the different types of tickets or fares that can be purchased by riders. File fare_products.txt describes fare products that are not represented in."
resource: "https://gtfs.org/documentation/schedule/reference/#fare_productstxt"
tags: [gtfs, schedule, table, fare-products, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`fare_products.txt` is a GTFS Schedule file with file-level presence `Optional`. Used to describe the range of fares available for purchase by riders or taken into account when computing the total fare for journeys with multiple legs, such as transfer costs. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `fare_product_id` | ID | Required | Identifies a fare product or set of fare products. Multiple records sharing the same `fare_product_id` are permitted as long as they contain different `fare_media_id`s or `rider_category_id`s. Differing `fare_media_id`s would indicate various methods are available for employing the fare product, potentially at different prices. Differing `rider_category_id`s would indicate multiple rider categories are eligible for the fare product, potentially at different prices. [1] |
| `fare_product_name` | Text | Optional | The name of the fare product as displayed to riders. [1] |
| `rider_category_id` | Foreign ID referencing [rider-categories.txt](/tables/rider-categories.md).`rider_category_id` | Optional | Identifies a rider category eligible for the fare product. If `fare_products.rider_category_id` is empty, the fare product is eligible for any `rider_category_id`. When multiple rider categories are eligible for a single fare product specified by a `fare_product_id`, there must be only one of these rider categories indicated as the default rider category (`is_default_fare_category = 1`). [1] |
| `fare_media_id` | Foreign ID referencing [fare-media.txt](/tables/fare-media.md).`fare_media_id` | Optional | Identifies a fare media that can be employed to use the fare product during the trip. When `fare_media_id` is empty, it is considered that the fare media is unknown. [1] |
| `amount` | Currency amount | Required | The cost of the fare product. May be negative to represent transfer discounts. May be zero to represent a fare product that is free. The currency amount must contain the number of decimal places specified by the norm ISO 4217 for the accompanying Currency code. [1] |
| `currency` | Currency code | Required | The currency of the cost of the fare product. [1] |

# Grain

One row per `fare_product_id, rider_category_id, fare_media_id` key in `fare_products.txt`. [1]

Primary key noted by the reference: `fare_product_id, rider_category_id, fare_media_id`. [1]

# Relationships

- `fare_products.rider_category_id` references [rider_categories.txt](/tables/rider-categories.md).`rider_category_id`. [1]
- `fare_products.fare_media_id` references [fare_media.txt](/tables/fare-media.md).`fare_media_id`. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- Fare concepts evolve in GTFS; this bundle records the April 27, 2026 Schedule Reference and keeps deeper fare modeling as a recommended enrichment pass.

# Citations

[1] [GTFS Schedule Reference: fare_products.txt](https://gtfs.org/documentation/schedule/reference/#fare_productstxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
