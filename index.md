# GTFS Schedule Data Catalog

Public OKF bundle for answering GTFS Schedule modeling questions with citations. It treats the static GTFS feed as a data catalog: dataset, tables, fields, row grain, relationships, business terms, metrics, and modeling decisions.

## Scope

- In scope: GTFS Schedule / static feed files from the Schedule Reference revision marked **April 27, 2026**.
- Out of scope: GTFS Realtime. See [Scope to Static GTFS Schedule](/decisions/scope-to-static-schedule.md).
- Normative source: [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/).
- Secondary guidance only: [GTFS Schedule Best Practices](https://gtfs.org/documentation/schedule/schedule-best-practices/).

## Entry Points

| question | start here |
|---|---|
| What is a GTFS feed? | [GTFS Schedule Feed](/datasets/gtfs-schedule-feed.md) |
| Where do I find an actual GTFS feed? | [GTFS Feed Catalog](/concepts/gtfs-feed-catalog.md), [Mobility Database](/systems/mobility-database.md), [Transitland](/systems/transitland.md) |
| How do I go from a place name to a feed query? | [Find and Use a GTFS Feed](/processes/find-and-use-gtfs-feed.md) |
| How do I validate a feed before using it? | [Validate a GTFS Feed](/processes/validate-a-gtfs-feed.md), [Canonical GTFS Schedule Validator](/systems/canonical-gtfs-schedule-validator.md) |
| How do I query stop departures? | [Query Stop Departures](/processes/query-stop-departures.md), [Build Active Service Calendar](/processes/build-active-service-calendar.md), [Resolve Station Area](/processes/resolve-station-area.md) |
| When do I need GTFS Realtime? | [Decide Static vs Realtime Source](/processes/decide-static-vs-realtime-source.md), [GTFS Realtime](/concepts/gtfs-realtime.md) |
| What files and fields exist? | [Tables](/tables/index.md) |
| How do files join? | [trips.txt](/tables/trips.md), [stop_times.txt](/tables/stop-times.md), [calendar.txt](/tables/calendar.md), [calendar_dates.txt](/tables/calendar-dates.md) |
| What does a term mean? | [Business terms](/concepts/index.md) |
| How do I compute schedule KPIs? | [Metrics](/metrics/index.md) |
| How do I handle Fares v2, Flex, or accessibility? | [Fares v2 Model](/concepts/fares-v2-model.md), [GTFS Flex Model](/concepts/gtfs-flex-model.md), [Inspect Station Accessibility](/processes/inspect-station-accessibility.md) |
| Which tools and ecosystem resources are useful? | [GTFS Community Resources](/systems/gtfs-community-resources.md), [OpenTripPlanner](/systems/open-trip-planner.md) |
| Why is the bundle modeled this way? | [Decisions](/decisions/index.md) |

## Counts

- Dataset concepts: 2
- System concepts: 5
- Process concepts: 10
- Table concepts: 32
- Metric concepts: 7
- Business-term concepts: 11
- Architectural-decision concepts: 4
- Reference concepts: 10
- License/notice concepts: 2

## Directories

- [Concepts](concepts/index.md) - overview, source policy, optional feature map, and vocabulary.
- [Datasets](datasets/index.md) - the feed zip model and practical feed examples.
- [Systems](systems/index.md) - external feed catalogs and discovery platforms.
- [Processes](processes/index.md) - practical workflows for using the catalog against real feeds.
- [Tables](tables/index.md) - one concept per GTFS Schedule file.
- [Metrics](metrics/index.md) - common service KPIs derivable from schedule files.
- [Decisions](decisions/index.md) - modeling decisions and scope boundaries.
- [Tools](tools/index.md) - maintainer helper scripts and tool notes.

## Publication Resources

- [README](README.md) - repository overview and validation commands.
- [License](LICENSE.md) - license statement for original OKF bundle content.
- [Notice](NOTICE.md) - third-party source and generated artifact notice.

## Freshness

GTFS evolves. This bundle records the Schedule Reference revision marked **April 27, 2026** and should be refreshed when the reference changes, especially for Fares v2, GTFS-Flex, validator behavior, and Realtime boundary guidance.
