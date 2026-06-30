---
type: "Reference"
title: "GTFS Extension Maturity"
description: "How to distinguish adopted specification content, extensions, experimental fields, best practices, and proposals."
resource: "https://gtfs.org/community/governance/gtfs-schedule-governance/introduction/"
tags: [gtfs, schedule, governance, extensions, maturity]
timestamp: "2026-06-30T04:18:00+00:00"
---

# Summary

GTFS changes through community governance. As accessed on 2026-06-30, GTFS.org says new Schedule pull requests from July 7, 2025 onward are subject to the new Schedule Governance Framework, while older listed pull requests continue under the former governance until resolved. [1]

Agents should distinguish adopted specification content from extension project pages, feature guides, best practices, experimental realtime fields, and open proposals. This avoids treating community discussion or guidance as mandatory GTFS Schedule requirements. [1] [2]

# Maturity classes

| class | evidence | agent treatment |
|---|---|---|
| Adopted specification | GTFS Schedule Reference field/file definitions | Treat as normative for Schedule feeds. |
| Adopted feature guide | GTFS.org feature guide backed by reference fields | Use as modeling guidance and cite the underlying reference fields. |
| Extension project | GTFS.org extension page such as Fares v2 or Flex | Treat as evolving; verify which parts are officially adopted. |
| Best practice | GTFS Schedule Best Practices | Label as guidance, not a required spec rule. |
| Experimental realtime field | GTFS Realtime field marked experimental | Treat as subject to change until adopted. |
| Proposal or pull request | GitHub issue/PR or governance artifact | Do not treat as implemented unless the source says it has been adopted. |

# Agent rule

When a user asks whether a field or feature is "official," check the Schedule Reference first, then the relevant extension/feature page, then governance or GitHub history. If sources disagree, prefer the English official GTFS.org reference and state the freshness date. [1]

# Citations

[1] [Introduction to GTFS Governance](https://gtfs.org/community/governance/gtfs-schedule-governance/introduction/)
[2] [GTFS Realtime Reference: Experimental fields](https://gtfs.org/documentation/realtime/reference/#term-definitions)
[3] [GTFS Schedule Best Practices](https://gtfs.org/documentation/schedule/schedule-best-practices/)
