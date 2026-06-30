# Decisions

This index is a progressive-disclosure entry point for this part of the GTFS Schedule OKF bundle.

| concept | type | description |
|---|---|---|
| [model each gtfs file as table](model-each-gtfs-file-as-table.md) | Architectural Decision | Each official GTFS Schedule file is represented as one OKF Table concept. |
| [scope to static schedule](scope-to-static-schedule.md) | Architectural Decision | This bundle excludes GTFS Realtime and focuses on static Schedule feeds. |
| [calendar and calendar dates service model](calendar-and-calendar-dates-service-model.md) | Architectural Decision | Service-date modeling uses both calendar.txt and calendar_dates.txt, including the either/or rule. |
| [fares v1 and v2 boundary](fares-v1-and-v2-boundary.md) | Architectural Decision | The first pass gives Fares v1 full treatment and keeps Fares v2 tables compact but linked. |
