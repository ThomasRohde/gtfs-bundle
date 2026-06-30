---
type: "Table"
title: "routes.txt"
description: "Transit routes. A route is a group of trips that are displayed to riders as a single service."
resource: "https://gtfs.org/documentation/schedule/reference/#routestxt"
tags: [gtfs, schedule, table, routes, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`routes.txt` is a GTFS Schedule file with file-level presence `Required`. Transit routes. A route is a group of trips that are displayed to riders as a single service. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `route_id` | Unique ID | Required | Identifies a route. [1] |
| `agency_id` | Foreign ID referencing [agency.txt](/tables/agency.md).`agency_id` | Conditionally Required | Agency for the specified route. Conditionally Required: - Required if multiple agencies are defined in agency.txt. - Recommended otherwise. [1] |
| `route_short_name` | Text | Conditionally Required | Short name of a route. Often a short, abstract identifier (e.g., "32", "100X", "Green") that riders use to identify a route. Both `route_short_name` and `route_long_name` may be defined. Conditionally Required: - Required if `routes.route_long_name` is empty. - Recommended if there is a brief service designation. This should be the commonly-known passenger name of the service, and should be no longer than 12 characters. [1] |
| `route_long_name` | Text | Conditionally Required | Full name of a route. This name is generally more descriptive than the `route_short_name` and often includes the route's destination or stop. Both `route_short_name` and `route_long_name` may be defined. Conditionally Required: - Required if `routes.route_short_name` is empty. - Optional otherwise. [1] |
| `route_desc` | Text | Optional | Description of a route that provides useful, quality information. Should not be a duplicate of `route_short_name` or `route_long_name`. [1] |
| `route_type` | Enum | Required | Indicates the type of transportation used on a route. Valid options are: `0` - Tram, Streetcar, Light rail. Any light rail or street level system within a metropolitan area. `1` - Subway, Metro. Any underground rail system within a metropolitan area. `2` - Rail. Used for intercity or long-distance travel. `3` - Bus. Used for short- and long-distance bus routes. `4` - Ferry. Used for short- and long-distance boat service. `5` - Cable tram. Used for street-level rail cars where the cable runs beneath the vehicle (e.g., cable car in San Francisco). `6` - Aerial lift, suspended cable car (e.g., gondola lift, aerial. [1] |
| `route_url` | URL | Optional | URL of a web page about the particular route. Should be different from the `agency.agency_url` value. [1] |
| `route_color` | Color | Optional | Route color designation that matches public facing material. Defaults to white (`FFFFFF`) when omitted or left empty. The color difference between `route_color` and `route_text_color` should provide sufficient contrast when viewed on a black and white screen. [1] |
| `route_text_color` | Color | Optional | Legible color to use for text drawn against a background of `route_color`. Defaults to black (`000000`) when omitted or left empty. The color difference between `route_color` and `route_text_color` should provide sufficient contrast when viewed on a black and white screen. [1] |
| `route_sort_order` | Non-negative integer | Optional | Orders the routes in a way which is ideal for presentation to customers. Routes with smaller `route_sort_order` values should be displayed first. [1] |
| `continuous_pickup` | Enum | Conditionally Forbidden | Indicates that the rider can board the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, on every trip of the route. Valid options are: `0` - Continuous stopping pickup. `1` or empty - No continuous stopping pickup. `2` - Must phone agency to arrange continuous stopping pickup. `3` - Must coordinate with driver to arrange continuous stopping pickup. Values for `routes.continuous_pickup` may be overridden by defining values in `stop_times.continuous_pickup` for specific `stop_time`s along the route. Conditionally Forbidden: - Any value other than `1` or empty is Forbidden if. [1] |
| `continuous_drop_off` | Enum | Conditionally Forbidden | Indicates that the rider can alight from the transit vehicle at any point along the vehicle’s travel path as described by shapes.txt, on every trip of the route. Valid options are: `0` - Continuous stopping drop off. `1` or empty - No continuous stopping drop off. `2` - Must phone agency to arrange continuous stopping drop off. `3` - Must coordinate with driver to arrange continuous stopping drop off. Values for `routes.continuous_drop_off` may be overridden by defining values in `stop_times.continuous_drop_off` for specific `stop_time`s along the route. Conditionally Forbidden: - Any value other than `1` or. [1] |
| `network_id` | ID | Conditionally Forbidden | Identifies a group of routes. Multiple rows in routes.txt may have the same `network_id`. Conditionally Forbidden: - Forbidden if the route_networks.txt or networks.txt file exists. - Optional otherwise. [1] |
| `cemv_support` | Enum | Optional | Indicates if riders can access a transit service (i.e., trip) associated with this route by using a contactless EMV (Europay, Mastercard, and Visa) card or mobile device as fare media at a fare validator (such as in pay-as-you-go or open-loop systems). This field does not indicate that cEMV can be used to purchase other fare products or to add value to another fare media. Support for cEMVs should only be indicated if all services under this route are accessible with the use of cEMV cards or mobile devices as fare media. Valid options are: `0` or empty - No cEMV information for trips associated with this route. [1] |

# Grain

One row per `route_id` key in `routes.txt`. [1]

Primary key noted by the reference: `route_id`. [1]

# Relationships

- `routes.agency_id` references [agency.txt](/tables/agency.md).`agency_id`. [1]
- `routes.route_type` classifies route technology and is exposed as the [route_type](/concepts/route-type.md) business term. [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.

# Citations

[1] [GTFS Schedule Reference: routes.txt](https://gtfs.org/documentation/schedule/reference/#routestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
