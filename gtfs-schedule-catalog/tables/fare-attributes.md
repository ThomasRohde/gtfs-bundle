---
type: "Table"
title: "fare_attributes.txt"
description: "Fare information for a transit agency's routes."
resource: "https://gtfs.org/documentation/schedule/reference/#fare_attributestxt"
tags: [gtfs, schedule, table, fare-attributes, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`fare_attributes.txt` is a GTFS Schedule file with file-level presence `Optional`. Versions There are two modelling options for describing fares. GTFS-Fares V1 is the legacy option for describing minimal fare information. GTFS-Fares V2 is an updated method that allows for a more detailed account of an agency's fare structure. Both are allowed to be present in a dataset, but only one method should be used by a data consumer for a given dataset. It is recommended that GTFS-Fares V2 takes precedence over GTFS-Fares V1. The files associated with GTFS-Fares V1 are: - fare_attributes.txt - fare_rules.txt The files associated with GTFS-Fares V2 are: - fare_media.txt - fare_products.txt - rider_categories.txt - fare_leg_rules.txt - fare_leg_join_rules.txt - fare_transfer_rules.txt - timeframes.txt - networks.txt - route_networks.txt - areas.txt - stop_areas.txt [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `fare_id` | Unique ID | Required | Identifies a fare class. [1] |
| `price` | Non-negative float | Required | Fare price, in the unit specified by `currency_type`. [1] |
| `currency_type` | Currency code | Required | Currency used to pay the fare. [1] |
| `payment_method` | Enum | Required | Indicates when the fare must be paid. Valid options are: `0` - Fare is paid on board. `1` - Fare must be paid before boarding. [1] |
| `transfers` | Enum | Required | Indicates the number of transfers permitted on this fare. Valid options are: `0` - No transfers permitted on this fare. `1` - Riders may transfer once. `2` - Riders may transfer twice. empty - Unlimited transfers are permitted. [1] |
| `agency_id` | Foreign ID referencing [agency.txt](/tables/agency.md).`agency_id` | Conditionally Required | Identifies the relevant agency for a fare. Conditionally Required: - Required if multiple agencies are defined in agency.txt. - Recommended otherwise. [1] |
| `transfer_duration` | Non-negative integer | Optional | Length of time in seconds before a transfer expires. When `transfers`=`0` this field may be used to indicate how long a ticket is valid for or it may be left empty. [1] |

# Grain

One row per `fare_id` key in `fare_attributes.txt`. [1]

Primary key noted by the reference: `fare_id`. [1]

# Relationships

- `fare_attributes.agency_id` references [agency.txt](/tables/agency.md).`agency_id`. [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.
- Fare concepts evolve in GTFS; this bundle records the April 27, 2026 Schedule Reference and keeps deeper fare modeling as a recommended enrichment pass.

# Citations

[1] [GTFS Schedule Reference: fare_attributes.txt](https://gtfs.org/documentation/schedule/reference/#fare_attributestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
