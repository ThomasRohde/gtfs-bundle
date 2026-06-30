---
type: "Process"
title: "Check GTFS Spec Freshness"
description: "Workflow for refreshing claims about GTFS Schedule, Realtime, and extension maturity before answering."
tags: [gtfs, schedule, process, freshness, governance]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

GTFS evolves through community governance, extensions, and validator releases. Check source freshness before answering questions about current requirements, new files, extension adoption, or validator behavior. [1]

# Steps

1. Open the official English GTFS Schedule Reference and note its revision date. [2]
2. If the question involves Realtime, open the GTFS Realtime Reference and check for experimental fields or version notes. [3]
3. If the question involves Fares v2 or Flex, open the relevant extension page and feature guide, then verify which files/fields appear in the Schedule Reference. [4] [5]
4. If the question involves a proposed change, inspect GTFS Schedule Governance and the linked GitHub pull request or issue. [1]
5. If the question involves validation behavior, check the Canonical GTFS Schedule Validator docs or release notes. [6]
6. Update the bundle only when the source-backed change affects a durable concept, workflow, or citation.

# Output requirements

- Include source access date for current-state claims.
- Distinguish "reference requirement," "best practice," "extension page guidance," and "proposal."
- Do not update timestamps on unrelated concepts.

# Citations

[1] [Introduction to GTFS Governance](https://gtfs.org/community/governance/gtfs-schedule-governance/introduction/)
[2] [GTFS Schedule Reference](https://gtfs.org/documentation/schedule/reference/)
[3] [GTFS Realtime Reference](https://gtfs.org/documentation/realtime/reference/)
[4] [GTFS-Fares v2 extension page](https://gtfs.org/community/extensions/fares-v2/)
[5] [GTFS-Flex extension page](https://gtfs.org/community/extensions/flex/)
[6] [MobilityData/gtfs-validator releases](https://github.com/MobilityData/gtfs-validator/releases)
