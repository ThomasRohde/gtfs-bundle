---
type: "Dataset"
title: "GTFS Schedule Feed"
description: "A static GTFS feed zip containing schedule files at the archive root."
resource: "https://gtfs.org/documentation/schedule/reference/#dataset-files"
tags: [gtfs, schedule, dataset, feed]
timestamp: "2026-06-30T03:53:45+00:00"
---

# Summary

A GTFS Schedule dataset is the complete set of files defined by the specification reference. The reference says dataset files are zipped together and reside at the root level of the archive, and changing the dataset creates a new version. This bundle uses the Schedule Reference revision marked **April 27, 2026**. [1]

# Catalog model

| asset | OKF concept |
|---|---|
| Feed zip | This Dataset concept |
| GTFS `.txt` or `.geojson` file | One [Table](/tables/index.md) concept per file |
| Field | Row in a table concept's `# Schema` section |
| Foreign key | Markdown link from the field to the referenced table |
| Derived KPI | One [Metric](/metrics/index.md) concept with formula and source tables |

# Required core

Core schedule analysis usually starts from [agency.txt](/tables/agency.md), [stops.txt](/tables/stops.md), [routes.txt](/tables/routes.md), [trips.txt](/tables/trips.md), [stop_times.txt](/tables/stop-times.md), and the service calendar represented by [calendar.txt](/tables/calendar.md) and/or [calendar_dates.txt](/tables/calendar-dates.md). [1]

# Grain

One dataset version is one published GTFS feed archive. Individual files are modeled at their own row grains in `/tables/`.

# Finding actual feeds

The GTFS Schedule Reference defines the feed structure, but it does not provide a universal registry of current feed URLs. For real geography-specific questions, use a [GTFS Feed Catalog](/concepts/gtfs-feed-catalog.md), [Mobility Database](/systems/mobility-database.md), [Transitland](/systems/transitland.md), or an official producer page to identify a concrete feed zip before querying this data model. [2] [3]

The [Rejseplanen GTFS Schedule Feed](/datasets/rejseplanen-gtfs-feed.md) is included as a practical Denmark example.

# Relationships

- A feed contains many table files. See [Tables](/tables/index.md).
- A feed's active service dates are governed by [calendar.txt](/tables/calendar.md) and [calendar_dates.txt](/tables/calendar-dates.md).
- Dataset-level publisher, language, version, and coverage metadata can be provided by [feed_info.txt](/tables/feed-info.md).
- Feed discovery can start from [Mobility Database](/systems/mobility-database.md), [Transitland](/systems/transitland.md), or producer pages, then follow [Find and Use a GTFS Feed](/processes/find-and-use-gtfs-feed.md).

# Citations

[1] [GTFS Schedule Reference: Dataset Files](https://gtfs.org/documentation/schedule/reference/#dataset-files)
[2] [GTFS.org: Sharing Data](https://gtfs.org/resources/sharing-data/)
[3] [Transitland Source Feeds](https://www.transit.land/feeds)
