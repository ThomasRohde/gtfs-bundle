---
type: "Table"
title: "pathways.txt"
description: "Pathways linking together locations within stations."
resource: "https://gtfs.org/documentation/schedule/reference/#pathwaystxt"
tags: [gtfs, schedule, table, pathways, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`pathways.txt` is a GTFS Schedule file with file-level presence `Optional`. Files pathways.txt and levels.txt use a graph representation to describe subway or train stations, with nodes representing locations and edges representing pathways. To navigate from the station entrance/exit (a node represented as a location with `location_type=2`) to a platform (a node represented as a location with `location_type=0` or empty), the rider will move through walkways, fare gates, stairs, and other edges represented as pathways. Generic nodes (nodes represented with `location_type=3`) can be used to connect pathways throughout a station. Pathways are intended to exhaustively define the internal access graph of a station. If any pathways are defined within a station, data consumers should assume that all relevant connections within that station are described. However, the optional `stop_access` field in `stops.txt` may be used to explicitly define whether a stop is. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `pathway_id` | Unique ID | Required | Identifies a pathway. Used by systems as an internal identifier for the record. Must be unique in the dataset. Different pathways may have the same values for `from_stop_id` and `to_stop_id`. [1] |
| `from_stop_id` | Foreign ID referencing [stops.txt](/tables/stops.md).`stop_id` | Required | Location at which the pathway begins. Must contain a `stop_id` that identifies a platform (`location_type=0` or empty), entrance/exit (`location_type=2`), generic node (`location_type=3`) or boarding area (`location_type=4`). Values for `stop_id` that identify stations (`location_type=1`), or stops (`location_type=0` or empty) with `stop_access=1`, are forbidden. [1] |
| `to_stop_id` | Foreign ID referencing [stops.txt](/tables/stops.md).`stop_id` | Required | Location at which the pathway ends. Must contain a `stop_id` that identifies a platform (`location_type=0` or empty), entrance/exit (`location_type=2`), generic node (`location_type=3`) or boarding area (`location_type=4`). Values for `stop_id` that identify stations (`location_type=1`), or stops (`location_type=0` or empty) with `stop_access=1`, are forbidden. [1] |
| `pathway_mode` | Enum | Required | Type of pathway between the specified (`from_stop_id`, `to_stop_id`) pair. Valid options are: `1` - Walkway. `2` - Stairs. `3` - Moving sidewalk/travelator. `4` - Escalator. `5` - Elevator. `6` - Fare gate (or payment gate): A pathway that crosses into an area of the station where proof of payment is required to cross. Fare gates may separate paid areas of the station from unpaid ones, or separate different payment areas within the same station from each other. This information can be used to avoid routing passengers through stations using shortcuts that would require passengers to make unnecessary payments. [1] |
| `is_bidirectional` | Enum | Required | Indicates the direction that the pathway can be taken: `0` - Unidirectional pathway that can only be used from `from_stop_id` to `to_stop_id`. `1` - Bidirectional pathway that can be used in both directions. Exit gates (`pathway_mode=7`) must not be bidirectional. [1] |
| `length` | Non-negative float | Optional | Horizontal length in meters of the pathway from the origin location (defined in `from_stop_id`) to the destination location (defined in `to_stop_id`). This field is recommended for walkways (`pathway_mode=1`), fare gates (`pathway_mode=6`) and exit gates (`pathway_mode=7`). [1] |
| `traversal_time` | Positive integer | Optional | Average time in seconds needed to walk through the pathway from the origin location (defined in `from_stop_id`) to the destination location (defined in `to_stop_id`). This field is recommended for moving sidewalks (`pathway_mode=3`), escalators (`pathway_mode=4`) and elevator (`pathway_mode=5`). [1] |
| `stair_count` | Non-null integer | Optional | Number of stairs of the pathway. A positive `stair_count` implies that the rider walk up from `from_stop_id` to `to_stop_id`. And a negative `stair_count` implies that the rider walk down from `from_stop_id` to `to_stop_id`. This field is recommended for stairs (`pathway_mode=2`). If only an estimated stair count can be provided, it is recommended to approximate 15 stairs for 1 floor. [1] |
| `max_slope` | Float | Optional | Maximum slope ratio of the pathway. Valid options are: `0` or empty - No slope. `Float` - Slope ratio of the pathway, positive for upwards, negative for downwards. This field should only be used with walkways (`pathway_mode=1`) and moving sidewalks (`pathway_mode=3`). [1] |
| `min_width` | Positive float | Optional | Minimum width of the pathway in meters. This field is recommended if the minimum width is less than 1 meter. [1] |
| `signposted_as` | Text | Optional | Public facing text from physical signage that is visible to riders. May be used to provide text directions to riders, such as 'follow signs to '. The text in `singposted_as` should appear exactly how it is printed on the signs. When the physical signage is multilingual, this field may be populated and translated following the example of `stops.stop_name` in the field definition of `feed_info.feed_lang`. [1] |
| `reversed_signposted_as` | Text | Optional | Same as `signposted_as`, but when the pathway is used from the `to_stop_id` to the `from_stop_id`. [1] |

# Grain

One row per `pathway_id` key in `pathways.txt`. [1]

Primary key noted by the reference: `pathway_id`. [1]

# Relationships

- `pathways.from_stop_id` references [stops.txt](/tables/stops.md).`stop_id`. [1]
- `pathways.to_stop_id` references [stops.txt](/tables/stops.md).`stop_id`. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.

# Citations

[1] [GTFS Schedule Reference: pathways.txt](https://gtfs.org/documentation/schedule/reference/#pathwaystxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
