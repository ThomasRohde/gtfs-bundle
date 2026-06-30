---
type: "Dataset"
title: "Rejseplanen GTFS Schedule Feed"
description: "Danish static GTFS Schedule feed used as a practical discovery example for Denmark timetable questions."
resource: "https://www.rejseplanen.info/labs/GTFS.zip"
tags: [gtfs, schedule, dataset, denmark, rejseplanen, feed-catalog]
timestamp: "2026-06-30T03:53:45+00:00"
---

# Summary

Rejseplanen Labs states that it offers a static GTFS dataset, updated approximately every 14 days, and that the static dataset does not contain realtime data. Rejseplanen also states that it offers a GTFS archive starting from 2025-12-15. [1]

As accessed on 2026-06-30, Transitland lists the Danish Rejseplanen GTFS feed with Onestop ID `f-rejseplanen~dk~gtfs`, format `GTFS`, current static URL `https://www.rejseplanen.info/labs/GTFS.zip`, license identifier `CC-BY-4.0`, and current feed-version service coverage from 2026-06-29 through 2026-09-23. Transitland also noted that the most recent imported feed had no `feed_info.txt` file. [2]

# Grain

One downloaded GTFS zip from the Rejseplanen Labs current static URL is one feed version. The stable URL may point to a newer feed over time, so record the download timestamp, archive URL, checksum, and service-date coverage when using it for reproducible analysis.

# Relationships

- This is an actual feed endpoint that can populate [GTFS Schedule Feed](/datasets/gtfs-schedule-feed.md).
- Use [Find and Use a GTFS Feed](/processes/find-and-use-gtfs-feed.md) before querying its [stops.txt](/tables/stops.md), [stop_times.txt](/tables/stop-times.md), [trips.txt](/tables/trips.md), [calendar.txt](/tables/calendar.md), and [calendar_dates.txt](/tables/calendar-dates.md).
- This feed was discovered through [Transitland](/systems/transitland.md) and corroborated against Rejseplanen Labs documentation. [1] [2]

# Practical notes

- Do not assume realtime departures from this feed; Rejseplanen explicitly describes the GTFS dataset as static. [1]
- For station-area questions, inspect `stops.txt` and nearby/transfer relationships rather than assuming one public station name maps to exactly one physical stop. Rejseplanen Labs notes that its GTFS data represents each physical stop with one stop number and includes connections between nearby stops, such as between train stations and bus stops. [1]
- If `feed_info.txt` is absent in a downloaded version, derive feed validity from `calendar.txt`, `calendar_dates.txt`, catalog metadata, and recorded download context rather than inventing feed metadata. [2]

# Citations

[1] [Rejseplanen Labs: Om GTFS Schedule/Static](https://labs.rejseplanen.dk/hc/da/articles/21639730766877-Om-GTFS-Schedule-Static)
[2] [Transitland: f-rejseplanen~dk~gtfs](https://www.transit.land/feeds/f-rejseplanen~dk~gtfs)
[3] [Rejseplanen Labs: Adgang til data fra Labs](https://labs.rejseplanen.dk/hc/da/articles/21553113674909-Adgang-til-data-fra-Labs)
