---
type: "Table"
title: "stops.txt"
description: "Stops where vehicles pick up or drop off riders. Also defines stations and station entrances. Conditionally Required: - Optional if demand-responsive zones are defined."
resource: "https://gtfs.org/documentation/schedule/reference/#stopstxt"
tags: [gtfs, schedule, table, stops, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`stops.txt` is a GTFS Schedule file with file-level presence `Conditionally Required`. Stops where vehicles pick up or drop off riders. Also defines stations and station entrances. Conditionally Required: - Optional if demand-responsive zones are defined in locations.geojson. - Required otherwise. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `stop_id` | Unique ID | Required | Identifies a location: stop/platform, station, entrance/exit, generic node or boarding area (see `location_type`). ID must be unique across all `stops.stop_id`, locations.geojson `id`, and `location_groups.location_group_id` values. Multiple routes may use the same `stop_id`. [1] |
| `stop_code` | Text | Optional | Short text or a number that identifies the location for riders. These codes are often used in phone-based transit information systems or printed on signage to make it easier for riders to get information for a particular location. The `stop_code` may be the same as `stop_id` if it is public facing. This field should be left empty for locations without a code presented to riders. [1] |
| `stop_name` | Text | Conditionally Required | Name of the location. The `stop_name` should match the agency's rider-facing name for the location as printed on a timetable, published online, or represented on signage. For translations into other languages, use translations.txt. When the location is a boarding area (`location_type=4`), the `stop_name` should contains the name of the boarding area as displayed by the agency. It could be just one letter (like on some European intercity railway stations), or text like “Wheelchair boarding area” (NYC’s Subway) or “Head of short trains” (Paris’ RER). Conditionally Required: - Required for locations which are stops. [1] |
| `tts_stop_name` | Text | Optional | Readable version of the `stop_name`. See "Text-to-speech field" in the Term Definitions for more. [1] |
| `stop_desc` | Text | Optional | Description of the location that provides useful, quality information. Should not be a duplicate of `stop_name`. [1] |
| `stop_lat` | Latitude | Conditionally Required | Latitude of the location. For stops/platforms (`location_type=0`) and boarding area (`location_type=4`), the coordinates must be the ones of the bus pole — if exists — and otherwise of where the travelers are boarding the vehicle (on the sidewalk or the platform, and not on the roadway or the track where the vehicle stops). Conditionally Required: - Required for locations which are stops (`location_type=0`), stations (`location_type=1`) or entrances/exits (`location_type=2`). - Optional for locations which are generic nodes (`location_type=3`) or boarding areas (`location_type=4`). [1] |
| `stop_lon` | Longitude | Conditionally Required | Longitude of the location. For stops/platforms (`location_type=0`) and boarding area (`location_type=4`), the coordinates must be the ones of the bus pole — if exists — and otherwise of where the travelers are boarding the vehicle (on the sidewalk or the platform, and not on the roadway or the track where the vehicle stops). Conditionally Required: - Required for locations which are stops (`location_type=0`), stations (`location_type=1`) or entrances/exits (`location_type=2`). - Optional for locations which are generic nodes (`location_type=3`) or boarding areas (`location_type=4`). [1] |
| `zone_id` | ID | Optional | Identifies the fare zone for a stop. If this record represents a station or station entrance, the `zone_id` is ignored. [1] |
| `stop_url` | URL | Optional | URL of a web page about the location. This should be different from the `agency.agency_url` and the `routes.route_url` field values. [1] |
| `location_type` | Enum | Optional | Location type. Valid options are: `0` (or empty) - Stop (or Platform). A location where passengers board or disembark from a transit vehicle. Is called a platform when defined within a `parent_station`. `1` - Station. A physical structure or area that contains one or more platform. `2` - Entrance/Exit. A location where passengers can enter or exit a station from the street. If an entrance/exit belongs to multiple stations, it may be linked by pathways to both, but the data provider must pick one of them as parent. `3` - Generic Node. A location within a station, not matching any other `location_type`, that may. [1] |
| `parent_station` | Foreign ID referencing [stops.txt](/tables/stops.md).`stop_id` | Conditionally Required | Defines hierarchy between the different locations defined in stops.txt. It contains the ID of the parent location, as followed: - Stop/platform (`location_type=0`): the `parent_station` field contains the ID of a station. - Station (`location_type=1`): this field must be empty. - Entrance/exit (`location_type=2`) or generic node (`location_type=3`): the `parent_station` field contains the ID of a station (`location_type=1`) - Boarding Area (`location_type=4`): the `parent_station` field contains ID of a platform. Conditionally Required: - Required for locations which are entrances (`location_type=2`), generic. [1] |
| `stop_timezone` | Timezone | Optional | Timezone of the location. If the location has a parent station, it inherits the parent station’s timezone instead of applying its own. Stations and parentless stops with empty `stop_timezone` inherit the timezone specified by `agency.agency_timezone`. The times provided in stop_times.txt are in the timezone specified by `agency.agency_timezone`, not `stop_timezone`. This ensures that the time values in a trip always increase over the course of a trip, regardless of which timezones the trip crosses. [1] |
| `wheelchair_boarding` | Enum | Optional | Indicates whether wheelchair boardings are possible from the location. Valid options are: For parentless stops: `0` or empty - No accessibility information for the stop. `1` - Some vehicles at this stop can be boarded by a rider in a wheelchair. `2` - Wheelchair boarding is not possible at this stop. For child stops: `0` or empty - Stop will inherit its `wheelchair_boarding` behavior from the parent station, if specified in the parent. `1` - There exists some accessible path from outside the station to the specific stop/platform. `2` - There exists no accessible path from outside the station to the specific. [1] |
| `level_id` | Foreign ID referencing [levels.txt](/tables/levels.md).`level_id` | Optional | Level of the location. The same level may be used by multiple unlinked stations. [1] |
| `platform_code` | Text | Optional | Platform identifier for a platform stop (a stop belonging to a station). This should be just the platform identifier (eg. "G" or "3"). Words like “platform” or "track" (or the feed’s language-specific equivalent) should not be included. This allows feed consumers to more easily internationalize and localize the platform identifier into other languages. [1] |
| `stop_access` | Enum | Conditionally Forbidden | Indicates how the stop is accessed for a particular station. Valid options are: `0` - The stop/platform cannot be directly accessed from the street network. It must be accessed from a station entrance if there is one defined for the station, otherwise the station itself. If there are pathways defined for the station, they must be used to access the stop/platform. `1` - Consuming applications should generate directions for access directly to the stop, independent of any entrances or pathways of the parent station. When `stop_access` is empty, the access for the specified stop or platform is considered undefined. [1] |

# Grain

One row per `stop_id` key in `stops.txt`. [1]

Primary key noted by the reference: `stop_id`. [1]

# Relationships

- `stops.parent_station` references [stops.txt](/tables/stops.md).`stop_id`. [1]
- `stops.level_id` references [levels.txt](/tables/levels.md).`level_id`. [1]
- `stops.location_type` controls whether a row is a stop, station, entrance/exit, generic node, or boarding area; see [location_type](/concepts/location-type.md). [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.
- The file-level presence is `Conditionally Required`; read the table summary and schema before assuming the file is always present.

# Citations

[1] [GTFS Schedule Reference: stops.txt](https://gtfs.org/documentation/schedule/reference/#stopstxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
