---
type: "Table"
title: "networks.txt"
description: "Network grouping of routes. Conditionally Forbidden: - Forbidden if `network_id` exists in routes.txt. - Optional otherwise."
resource: "https://gtfs.org/documentation/schedule/reference/#networkstxt"
tags: [gtfs, schedule, table, networks, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`networks.txt` is a GTFS Schedule file with file-level presence `Conditionally Forbidden`. Defines network identifiers that apply for fare leg rules. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `network_id` | Unique ID | Required | Identifies a network. Must be unique in networks.txt. [1] |
| `network_name` | Text | Optional | The name of the network that apply for fare leg rules, as used by the local agency and its riders. [1] |

# Grain

One row per `network_id` key in `networks.txt`. [1]

Primary key noted by the reference: `network_id`. [1]

# Relationships

- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- The file-level presence is `Conditionally Forbidden`; read the table summary and schema before assuming the file is always present.

# Citations

[1] [GTFS Schedule Reference: networks.txt](https://gtfs.org/documentation/schedule/reference/#networkstxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
