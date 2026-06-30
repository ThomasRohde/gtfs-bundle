---
type: "Table"
title: "fare_media.txt"
description: "To describe the fare media that can be employed to use fare products. File fare_media.txt describes concepts that are not represented in fare_attributes.txt and."
resource: "https://gtfs.org/documentation/schedule/reference/#fare_mediatxt"
tags: [gtfs, schedule, table, fare-media, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`fare_media.txt` is a GTFS Schedule file with file-level presence `Optional`. To describe the different fare media that can be employed to use fare products. Fare media are physical or virtual holders used for the representation and/or validation of a fare product. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `fare_media_id` | Unique ID | Required | Identifies a fare media. [1] |
| `fare_media_name` | Text | Optional | Name of the fare media. For fare media which are transit cards (`fare_media_type =2`) or mobile apps (`fare_media_type =4`), the `fare_media_name` should be included and should match the rider-facing name used by the organizations delivering them. [1] |
| `fare_media_type` | Enum | Required | The type of fare media. Valid options are: `0` - None. Used when there is no fare media involved in purchasing or validating a fare product, such as paying cash to a driver or conductor with no physical ticket provided. `1` - Physical paper ticket that allows a passenger to take either a certain number of pre-purchased trips or unlimited trips within a fixed period of time. `2` - Physical transit card that has stored tickets, passes or monetary value. `3` - cEMV (contactless Europay, Mastercard and Visa) as an open-loop token container for account-based ticketing. `4` - Mobile app that have stored virtual. [1] |

# Grain

One row per `fare_media_id` key in `fare_media.txt`. [1]

Primary key noted by the reference: `fare_media_id`. [1]

# Relationships

- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- Fare concepts evolve in GTFS; this bundle records the April 27, 2026 Schedule Reference and keeps deeper fare modeling as a recommended enrichment pass.

# Citations

[1] [GTFS Schedule Reference: fare_media.txt](https://gtfs.org/documentation/schedule/reference/#fare_mediatxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
