---
type: "System"
title: "Canonical GTFS Schedule Validator"
description: "MobilityData's validator for checking GTFS Schedule feeds against the official reference and best practices."
resource: "https://github.com/MobilityData/gtfs-validator"
tags: [gtfs, schedule, system, validation, validator]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

The Canonical GTFS Schedule Validator is a MobilityData-maintained tool for evaluating GTFS Schedule datasets against the official GTFS Schedule Reference and GTFS Schedule Best Practices. As accessed on 2026-06-30, MobilityData provides a web validator that accepts a locally saved GTFS zip or a dataset URL. [1] [2]

Use the validator before trusting a newly discovered feed for agent answers. A valid-looking zip can still have broken references, missing required fields, stale service dates, invalid shapes, or quality notices that change whether a question can be answered safely. [1] [3]

# Agent use

| agent question | validator role |
|---|---|
| Can I query this feed? | Check hard validity and required-file problems before building joins. |
| Why are departures missing? | Look for missing service dates, broken trip references, or stop/service coverage notices. |
| Is this an authoritative no-service answer? | Confirm the feed covers the requested date and does not only fail due to stale or incomplete data. |
| Is this feed production-ready? | Review warnings and best-practice notices, not only parser success. |

# Relationships

- Use [Validate a GTFS Feed](/processes/validate-a-gtfs-feed.md) before running operational playbooks.
- Interpret validator output through [Validator Notice](/concepts/validator-notice.md).
- Feed discovery still starts with [GTFS Feed Catalog](/concepts/gtfs-feed-catalog.md), [Mobility Database](/systems/mobility-database.md), or [Transitland](/systems/transitland.md).

# Caveats

- Validator output is diagnostic evidence, not the GTFS specification itself.
- Notices may be version-sensitive; record validator version or report URL when preserving analysis.
- Passing validation does not imply realtime accuracy. Use [Decide Static vs Realtime Source](/processes/decide-static-vs-realtime-source.md) for current-delay or disruption questions.

# Citations

[1] [Canonical GTFS Schedule Validator](https://gtfs-validator.mobilitydata.org/)
[2] [MobilityData/gtfs-validator](https://github.com/MobilityData/gtfs-validator)
[3] [Canonical GTFS Schedule Validator: Validation Rules and Metadata](https://gtfs-validator.mobilitydata.org/rules.html)
