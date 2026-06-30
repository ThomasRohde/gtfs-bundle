---
type: "Table"
title: "rider_categories.txt"
description: "Defines categories of riders (e.g. elderly, student)."
resource: "https://gtfs.org/documentation/schedule/reference/#rider_categoriestxt"
tags: [gtfs, schedule, table, rider-categories, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`rider_categories.txt` is a GTFS Schedule file with file-level presence `Optional`. Defines categories of riders (e.g. elderly, student). [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `rider_category_id` | Unique ID | Required | Identifies a rider category. [1] |
| `rider_category_name` | Text | Required | Rider category name as displayed to the rider. [1] |
| `is_default_fare_category` | Enum | Required | Specifies if an entry in rider_categories.txt should be considered the default category (i.e. the main category that should be displayed to riders). For example: Adult fare, Regular fare, etc. Valid options are: `0` or empty - Category is not considered the default. `1` - Category is considered the default one. When multiple rider categories are eligible for a single fare product specified by a `fare_product_id`, there must be exactly one of these eligible rider categories indicated as the default rider category (`is_default_fare_category = 1`). [1] |
| `eligibility_url` | URL | Optional | URL of a web page, usually from the operating agency, that provides detailed information about a specific rider category and/or describes its eligibility criteria. [1] |

# Grain

One row per `rider_category_id` key in `rider_categories.txt`. [1]

Primary key noted by the reference: `rider_category_id`. [1]

# Relationships

- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- Fare concepts evolve in GTFS; this bundle records the April 27, 2026 Schedule Reference and keeps deeper fare modeling as a recommended enrichment pass.

# Citations

[1] [GTFS Schedule Reference: rider_categories.txt](https://gtfs.org/documentation/schedule/reference/#rider_categoriestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
