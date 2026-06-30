---
type: "Reference"
title: "GTFS Schedule Source Policy"
description: "Authoritative source boundary, feed-catalog policy, and citation rules for this public GTFS Schedule OKF bundle."
tags: [gtfs, schedule, source-policy, citations]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

Normative claims in this bundle use the canonical GTFS Schedule Reference and the Google Transit repository source for cross-checking. Best practices are treated as producer guidance, not as specification requirements. Feed catalogs are treated as discovery and implementation sources, not as GTFS specification authority. Vendor blogs are excluded unless a future implementation-caveat concept explicitly labels them as non-normative.

# Citation rules

- Table concepts cite the table-specific GTFS Schedule Reference anchor as their `resource` and citation `[1]`.
- Required/optional/conditionally required claims come from the Schedule Reference, not from best-practice guidance.
- Metrics that derive from fields cite the table concepts they depend on and the GTFS reference fields behind those tables.
- Implementation advice that is not in the reference should be marked as guidance and cite the best-practices page.
- Feed-catalog claims must cite catalog or provider pages, include an access date when the claim is current-state sensitive, and avoid presenting catalog metadata as normative GTFS requirements.
- Place-based timetable answers must identify the concrete feed or API used. If no feed is supplied, use [Find and Use a GTFS Feed](/processes/find-and-use-gtfs-feed.md) before querying tables.
- Validation findings must identify the validator source/version or report context when they materially affect an answer.
- GTFS Realtime claims must cite Realtime sources and stay out of the Schedule table catalog unless they describe the boundary.
- Extension and tool claims must identify whether they are adopted specification content, extension guidance, best practices, implementation guidance, or proposals.

# Feed catalog source boundary

| source class | examples | authority |
|---|---|---|
| Specification | GTFS Schedule Reference, google/transit source | Defines file format, field presence, types, and relationships. |
| Feed catalog | [Mobility Database](/systems/mobility-database.md), [Transitland](/systems/transitland.md) | Helps discover feeds, metadata, archives, and access URLs. |
| Validator | [Canonical GTFS Schedule Validator](/systems/canonical-gtfs-schedule-validator.md) | Diagnoses feed conformance and quality before query use. |
| Realtime companion | [GTFS Realtime](/concepts/gtfs-realtime.md) | Handles current updates, alerts, vehicle positions, and predictions outside static Schedule. |
| Community tool | [OpenTripPlanner](/systems/open-trip-planner.md), [GTFS Community Resources](/systems/gtfs-community-resources.md) | Implementation guidance for routing, producing, consuming, and validating data. |
| Producer feed page | [Rejseplanen GTFS Schedule Feed](/datasets/rejseplanen-gtfs-feed.md) source page | Preferred evidence for current producer endpoint and access terms. |
| Journey-planner API | Rejseplanen departure board or similar local APIs | Useful for realtime/current answers but not GTFS Schedule evidence unless explicitly documented as GTFS-derived.

# Citations

[1] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
[3] [GTFS Schedule Best Practices](https://gtfs.org/documentation/schedule/schedule-best-practices/)
[4] [GTFS.org: Sharing Data](https://gtfs.org/resources/sharing-data/)
[5] [Mobility Database](https://mobilitydatabase.org/)
[6] [Transitland Source Feeds](https://www.transit.land/feeds)
[7] [GTFS Realtime Reference](https://gtfs.org/documentation/realtime/reference/)
[8] [Canonical GTFS Schedule Validator](https://gtfs-validator.mobilitydata.org/)
[9] [GTFS.org Resources Overview](https://gtfs.org/resources/overview/)
