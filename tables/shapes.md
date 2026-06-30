---
type: "Table"
title: "shapes.txt"
description: "Rules for mapping vehicle travel paths, sometimes referred to as route alignments."
resource: "https://gtfs.org/documentation/schedule/reference/#shapestxt"
tags: [gtfs, schedule, table, shapes, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`shapes.txt` is a GTFS Schedule file with file-level presence `Optional`. Shapes describe the path that a vehicle travels along a route alignment, and are defined in the file shapes.txt. Shapes are associated with Trips, and consist of a sequence of points through which the vehicle passes in order. Shapes do not need to intercept the location of Stops exactly, but all Stops on a trip should lie within a small distance of the shape for that trip, i.e. close to straight line segments connecting the shape points. The shapes.txt file should be included for all route-based services (not for zone-based demand-responsive services). [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `shape_id` | ID | Required | Identifies a shape. [1] |
| `shape_pt_lat` | Latitude | Required | Latitude of a shape point. Each record in shapes.txt represents a shape point used to define the shape. [1] |
| `shape_pt_lon` | Longitude | Required | Longitude of a shape point. [1] |
| `shape_pt_sequence` | Non-negative integer | Required | Sequence in which the shape points connect to form the shape. Values must increase along the trip but do not need to be consecutive. [1] |
| `shape_dist_traveled` | Non-negative float | Optional | Actual distance traveled along the shape from the first shape point to the point specified in this record. Used by trip planners to show the correct portion of the shape on a map. Values must increase along with `shape_pt_sequence`; they must not be used to show reverse travel along a route. Distance units must be consistent with those used in stop_times.txt. Recommended for routes that have looping or inlining (the vehicle crosses or travels over the same portion of alignment in one trip). If a vehicle retraces or crosses the route alignment at points in the course of a trip, `shape_dist_traveled` is important. [1] |

# Grain

One row per `shape_id, shape_pt_sequence` key in `shapes.txt`. [1]

Primary key noted by the reference: `shape_id, shape_pt_sequence`. [1]

# Relationships

- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.

# Citations

[1] [GTFS Schedule Reference: shapes.txt](https://gtfs.org/documentation/schedule/reference/#shapestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
