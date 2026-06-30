# How to Use This OKF Bundle

This directory is an Open Knowledge Format (OKF) bundle for GTFS Schedule modeling questions. It is designed for direct Markdown consumption by humans and agents, including environments that do not have Codex, MCP, CLI, graph, or OKF-specific search tools.

## Start Here

- Read `index.md` first to understand the bundle scope, entry points, counts, and directory map.
- Read `log.md` to understand recent changes and freshness history.
- Treat the GTFS Schedule Reference revision marked April 27, 2026 as the bundle's recorded normative source baseline.
- Follow internal Markdown links to relevant concept files instead of loading every file at once.

## Scope

- Use this bundle for static GTFS Schedule questions: feed structure, table semantics, field relationships, static service calendars, fares, pathways, stops, routes, trips, stop times, frequencies, and schedule-derived metrics.
- Do not treat this bundle as a GTFS Realtime source. Start with `/decisions/scope-to-static-schedule.md` and `/concepts/gtfs-realtime.md` when deciding whether Realtime data is needed.
- Use GTFS Schedule Best Practices as secondary guidance only when the bundle explicitly cites or routes to it.

## Entry Points By Task

- Feed overview: `/datasets/gtfs-schedule-feed.md`
- Denmark/Rejseplanen feed endpoint: `/datasets/rejseplanen-gtfs-feed.md`
- GTFS table catalog: `/tables/index.md`
- Table joins and row grain: `/decisions/model-each-gtfs-file-as-table.md`, then the relevant table file under `/tables/`
- Stop departures: `/processes/query-stop-departures.md`
- Active service dates: `/processes/build-active-service-calendar.md`
- Feed discovery: `/processes/find-and-use-gtfs-feed.md`
- Feed validation: `/processes/validate-a-gtfs-feed.md`
- Static versus Realtime source choice: `/processes/decide-static-vs-realtime-source.md`
- Fares v2: `/concepts/fares-v2-model.md` and `/processes/interpret-fares-v2.md`
- Accessibility and station structure: `/processes/inspect-station-accessibility.md` and `/processes/resolve-station-area.md`
- Schedule KPIs: `/metrics/index.md`
- Modeling rationale: `/decisions/index.md`

## Real-World Timetable Questions

If the user asks for an actual journey, departure, next train, next bus, or stop timetable, do not stop at "this bundle has no GTFS rows." This bundle is a catalog and playbook: it tells you how to find and query the real feed.

Use this workflow:

1. Read `/processes/find-and-use-gtfs-feed.md`.
2. For Denmark timetable questions, start with `/datasets/rejseplanen-gtfs-feed.md`; it records the current static GTFS URL `https://www.rejseplanen.info/labs/GTFS.zip`.
3. If network/file access is available and the user wants a real answer, download or use the concrete GTFS feed version, record the source URL and access time, then query the feed.
4. Resolve public place names to GTFS stops using `/processes/resolve-station-area.md` and `stops.txt`. Do not assume a station name maps to one stop row.
5. Build active service IDs for the requested date with `/processes/build-active-service-calendar.md`, then query departures with `/processes/query-stop-departures.md`.
6. For origin-to-destination journey questions, search for direct trips first. If none exist, look for transfer paths using the feed's stops, trips, stop times, routes, calendars, transfers, and nearby station-area relationships.
7. If the requested answer depends on delays, cancellations, live platforms, or "right now" operational state, static GTFS Schedule is not enough. Say that the scheduled answer comes from static GTFS and that realtime accuracy requires GTFS Realtime or a journey-planner API.

When answering, separate these layers:

- OKF bundle facts, cited with concept paths.
- Feed facts observed in the downloaded GTFS files, with feed URL, download/access time, and service-date coverage.
- External realtime or journey-planner facts, clearly labeled as outside static GTFS.

## Reading Concepts

- Treat each concept file as one durable idea, GTFS table, process, metric, dataset, system, decision, or source.
- Use YAML frontmatter for identity, type, title, description, tags, timestamp, and canonical resource URI when present.
- Use bundle-relative paths as concept identifiers, for example `[tables/stop-times]` or `[processes/query-stop-departures]`.
- Follow absolute bundle-relative links such as `/tables/trips.md` as graph relationships.
- When interpreting GTFS files, prefer the table concept's grain, required fields, relationships, and citations over general model knowledge.

## Answering From This Bundle

- Prefer bundle content over general model knowledge for covered GTFS Schedule topics.
- Cite concept paths after bundle-grounded claims.
- Distinguish direct bundle facts from inference or external knowledge.
- Report when the bundle is stale, incomplete, contradictory, or missing concepts needed to answer.
- Use external knowledge only when requested or necessary, and label it clearly.
- For feed-specific questions, separate what this bundle says about the GTFS standard from facts observed in the actual feed being analyzed.

## Tooling

No OKF-specific tools are required. If search, graph, MCP, or CLI tools are available, they can speed up retrieval, but the source of truth is the Markdown bundle itself.
