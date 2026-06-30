from __future__ import annotations

"""Generate the base GTFS Schedule table catalog.

Maintenance note: this script predates the manually maintained community
enrichment layer in gtfs-schedule-catalog (feed catalogs, validation,
Realtime boundary, Fares v2/Flex playbooks, and tool maps). Do not rerun this
script against the enriched bundle unless you intend to reconcile those manual
concepts and indexes afterwards.
"""

import html
import re
import textwrap
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


BUNDLE = Path("gtfs-schedule-catalog")
REFERENCE_URL = "https://gtfs.org/documentation/schedule/reference/"
REFERENCE_RAW_URL = "https://raw.githubusercontent.com/google/transit/master/gtfs/spec/en/reference.md"
GITHUB_REFERENCE_URL = "https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md"
BEST_PRACTICES_URL = "https://gtfs.org/documentation/schedule/schedule-best-practices/"

FULL_TABLES = {
    "agency.txt",
    "stops.txt",
    "routes.txt",
    "trips.txt",
    "stop_times.txt",
    "calendar.txt",
    "calendar_dates.txt",
    "shapes.txt",
    "frequencies.txt",
    "transfers.txt",
    "feed_info.txt",
    "fare_attributes.txt",
    "fare_rules.txt",
}

CORE_ORDER = [
    "agency.txt",
    "stops.txt",
    "routes.txt",
    "trips.txt",
    "stop_times.txt",
    "calendar.txt",
    "calendar_dates.txt",
    "fare_attributes.txt",
    "fare_rules.txt",
    "timeframes.txt",
    "rider_categories.txt",
    "fare_media.txt",
    "fare_products.txt",
    "fare_leg_rules.txt",
    "fare_leg_join_rules.txt",
    "fare_transfer_rules.txt",
    "areas.txt",
    "stop_areas.txt",
    "networks.txt",
    "route_networks.txt",
    "shapes.txt",
    "frequencies.txt",
    "transfers.txt",
    "pathways.txt",
    "levels.txt",
    "location_groups.txt",
    "location_group_stops.txt",
    "locations.geojson",
    "booking_rules.txt",
    "translations.txt",
    "feed_info.txt",
    "attributions.txt",
]


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "gtfs-okf-catalog-builder/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def slug_for_file(file_name: str) -> str:
    return file_name.replace(".txt", "").replace(".geojson", "-geojson").replace("_", "-")


def base_for_file(file_name: str) -> str:
    if file_name.endswith(".txt"):
        return file_name[:-4]
    return file_name


def anchor_for_file(file_name: str) -> str:
    if file_name.endswith(".txt"):
        return "#" + file_name[:-4] + "txt"
    return "#" + file_name.replace(".", "")


def yaml_scalar(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def frontmatter(meta: dict[str, object]) -> str:
    lines = ["---"]
    for key, value in meta.items():
        if value is None:
            continue
        if isinstance(value, list):
            lines.append(f"{key}: [{', '.join(value)}]")
        else:
            lines.append(f"{key}: {yaml_scalar(str(value))}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def clean_inline(text: str, limit: int | None = None) -> str:
    text = html.unescape(text)
    text = text.replace("\r", " ").replace("\n", " ")
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"<hr\s*/?>.*", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("__", "")
    text = text.replace("&nbsp;", " ")
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        cut = text[:limit].rsplit(" ", 1)[0].rstrip(".,;")
        text = cut + "."
    return text


def md_table_cell(text: str) -> str:
    return clean_inline(text, limit=700).replace("|", "\\|")


def md_table_cell_preserve_links(text: str) -> str:
    text = html.unescape(text)
    text = text.replace("\r", " ").replace("\n", " ")
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"<hr\s*/?>.*", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("**", "").replace("__", "")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > 700:
        text = text[:700].rsplit(" ", 1)[0].rstrip(".,;") + "."
    return text.replace("|", "\\|")


def parse_markdown_table(block: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in block.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        if re.match(r"^\|\s*-+", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells:
            rows.append(cells)
    return rows


def parse_dataset_files(markdown: str) -> dict[str, dict[str, str]]:
    match = re.search(r"## Dataset Files(?P<body>.*?)(?:\n## File Requirements)", markdown, re.S)
    if not match:
        return {}
    rows = parse_markdown_table(match.group("body"))
    files: dict[str, dict[str, str]] = {}
    for row in rows[1:]:
        if len(row) < 3:
            continue
        file_match = re.search(r"\[([^\]]+)\]", row[0])
        if not file_match:
            continue
        file_name = file_match.group(1).replace("\\_", "_")
        files[file_name] = {
            "presence": clean_inline(row[1]),
            "description": clean_inline(row[2], limit=360),
        }
    return files


def parse_sections(markdown: str) -> dict[str, dict[str, object]]:
    headings = list(re.finditer(r"^### ([A-Za-z0-9_]+\.txt|locations\.geojson)\s*$", markdown, re.M))
    sections: dict[str, dict[str, object]] = {}
    for index, heading in enumerate(headings):
        file_name = heading.group(1)
        start = heading.end()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(markdown)
        body = markdown[start:end].strip()
        file_presence = re.search(r"File:\s+\*\*([^*]+)\*\*", body)
        primary_key = re.search(r"Primary key\s+\(([^)]+)\)", body)
        table_match = re.search(
            r"\|[^|\n]*Field Name[^|\n]*\|[^|\n]*Type[^|\n]*\|[^|\n]*Presence[^|\n]*\|[^|\n]*Description[^|\n]*\|(?P<table>.*?)(?:\n\n|\Z)",
            body,
            re.S,
        )
        fields: list[dict[str, str]] = []
        if table_match:
            rows = parse_markdown_table(table_match.group(0))
            for row in rows[1:]:
                if len(row) < 4:
                    continue
                field_name = clean_inline(row[0]).replace("`", "")
                fields.append(
                    {
                        "field": field_name,
                        "type": clean_inline(row[1]),
                        "presence": clean_inline(row[2]),
                        "description": clean_inline(row[3], limit=620),
                    }
                )
        before_table = body[: table_match.start()] if table_match else body
        summary_lines = []
        for line in before_table.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("File:") or stripped.startswith("Primary key"):
                continue
            if stripped.startswith("|") or stripped.startswith("- ") or stripped.startswith("* "):
                continue
            summary_lines.append(stripped)
        sections[file_name] = {
            "file_presence": clean_inline(file_presence.group(1)) if file_presence else "",
            "primary_key": clean_inline(primary_key.group(1)) if primary_key else "",
            "summary": clean_inline(" ".join(summary_lines), limit=900),
            "fields": fields,
        }
    return sections


def link_for_target(target: str, file_map: dict[str, str]) -> str | None:
    target = target.replace("\\_", "_")
    if target in file_map:
        return file_map[target]
    if f"{target}.txt" in file_map:
        return file_map[f"{target}.txt"]
    if target == "locations.geojson" and "locations.geojson" in file_map:
        return file_map["locations.geojson"]
    return None


def link_foreign_type(field_type: str, file_map: dict[str, str]) -> tuple[str, list[tuple[str, str]]]:
    relationships: list[tuple[str, str]] = []

    def replace_ref(match: re.Match[str]) -> str:
        ref = match.group(1).replace("\\_", "_")
        if "." not in ref:
            return match.group(0)
        table, column = ref.rsplit(".", 1)
        target = link_for_target(table, file_map)
        if not target:
            return match.group(0)
        relationships.append((table, column))
        label = table.replace("_", "-")
        return f"[{label}.txt]({target}).`{column}`"

    linked = re.sub(r"`([A-Za-z0-9_]+(?:\.geojson)?\.[A-Za-z0-9_]+)`", replace_ref, field_type)
    if "`id` from `locations.geojson`" in linked and "locations.geojson" in file_map:
        linked = linked.replace(
            "`id` from `locations.geojson`",
            "[locations.geojson](/tables/locations-geojson.md).`id`",
        )
        relationships.append(("locations.geojson", "id"))
    return linked, relationships


def table_path(file_name: str) -> str:
    return f"/tables/{slug_for_file(file_name)}.md"


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.replace("\r\n", "\n"), encoding="utf-8")


def table_title(file_name: str) -> str:
    return file_name


def table_description(file_name: str, dataset_meta: dict[str, str], section: dict[str, object]) -> str:
    desc = dataset_meta.get("description") or section.get("summary") or f"GTFS Schedule table {file_name}."
    return clean_inline(str(desc), limit=170)


def grain_from_primary_key(primary_key: str, file_name: str) -> str:
    primary_key = primary_key.replace("`", "")
    if not primary_key:
        return f"One row per record in `{file_name}` as defined by the file schema."
    if primary_key.lower() == "none":
        return f"`{file_name}` allows one dataset-level record."
    if primary_key == "*":
        return f"One row per unique combination of all provided identifying fields in `{file_name}`."
    return f"One row per `{primary_key}` key in `{file_name}`."


def extra_relationships(file_name: str) -> list[str]:
    extras: list[str] = []
    if file_name == "trips.txt":
        extras.append(
            "`trips.service_id` identifies a service pattern that can be declared in [calendar.txt](/tables/calendar.md), modified by [calendar_dates.txt](/tables/calendar-dates.md), or represented only in calendar_dates when calendar is omitted. [1]"
        )
    if file_name == "stop_times.txt":
        extras.append(
            "`stop_times.trip_id` plus `stop_sequence` orders each trip's stop visits and joins scheduled movement to [trips.txt](/tables/trips.md). [1]"
        )
    if file_name == "calendar_dates.txt":
        extras.append(
            "`calendar_dates.service_id` shares the service identifier namespace used by [trips.txt](/tables/trips.md) and [calendar.txt](/tables/calendar.md). [1]"
        )
    if file_name == "fare_rules.txt":
        extras.append(
            "`fare_rules.origin_id`, `destination_id`, and `contains_id` match fare zones encoded in `stops.zone_id` on [stops.txt](/tables/stops.md). [1]"
        )
    if file_name == "routes.txt":
        extras.append(
            "`routes.route_type` classifies route technology and is exposed as the [route_type](/concepts/route-type.md) business term. [1]"
        )
    if file_name == "stops.txt":
        extras.append(
            "`stops.location_type` controls whether a row is a stop, station, entrance/exit, generic node, or boarding area; see [location_type](/concepts/location-type.md). [1]"
        )
    if file_name == "frequencies.txt":
        extras.append(
            "`frequencies.trip_id` should point to a trip whose `stop_times.txt` record defines the stop pattern used for repeated departures. [1]"
        )
    if file_name == "transfers.txt":
        extras.append(
            "`from_trip_id`, `to_trip_id`, `from_route_id`, and `to_route_id` make transfer rules more specific than stop-pair-only rules. [1]"
        )
    return extras


def table_modeling_notes(file_name: str, presence: str) -> list[str]:
    notes = []
    if file_name in FULL_TABLES:
        notes.append("This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.")
    else:
        notes.append("This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.")
    if "Conditionally Required" in presence or "Conditionally Forbidden" in presence:
        notes.append(f"The file-level presence is `{presence}`; read the table summary and schema before assuming the file is always present.")
    if file_name.startswith("fare_") or file_name in {"timeframes.txt", "rider_categories.txt", "fare_media.txt", "fare_products.txt"}:
        notes.append("Fare concepts evolve in GTFS; this bundle records the April 27, 2026 Schedule Reference and keeps deeper fare modeling as a recommended enrichment pass.")
    if file_name in {"location_groups.txt", "location_group_stops.txt", "locations.geojson", "booking_rules.txt"}:
        notes.append("This file participates in GTFS-Flex or rider-requested service modeling and is intentionally summarized here rather than treated as the main schedule model.")
    return notes


def render_table_concept(
    file_name: str,
    section: dict[str, object],
    dataset_files: dict[str, dict[str, str]],
    file_map: dict[str, str],
    timestamp: str,
) -> tuple[str, int]:
    dataset_meta = dataset_files.get(file_name, {})
    presence = str(section.get("file_presence") or dataset_meta.get("presence") or "Optional")
    description = table_description(file_name, dataset_meta, section)
    anchor = anchor_for_file(file_name)
    resource = REFERENCE_URL + anchor
    summary = str(section.get("summary") or dataset_meta.get("description") or description)
    primary_key = str(section.get("primary_key") or "")
    fields = list(section.get("fields") or [])
    fk_edges = 0
    relationship_lines: list[str] = []

    schema_lines = ["| field | type | required | meaning |", "|---|---|---|---|"]
    for field in fields:
        linked_type, refs = link_foreign_type(field["type"], file_map)
        for table, column in refs:
            target = link_for_target(table, file_map)
            if target:
                relationship_lines.append(
                    f"- `{base_for_file(file_name)}.{field['field']}` references [{table}.txt]({target}).`{column}`. [1]"
                )
                fk_edges += 1
        schema_lines.append(
            f"| `{field['field']}` | {md_table_cell_preserve_links(linked_type)} | {md_table_cell(field['presence'])} | {md_table_cell(field['description'])} [1] |"
        )

    relationship_lines.extend(f"- {line}" for line in extra_relationships(file_name))
    relationship_lines = list(dict.fromkeys(relationship_lines))
    if not relationship_lines:
        relationship_lines = ["- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]"]

    notes = table_modeling_notes(file_name, presence)
    tags = ["gtfs", "schedule", "table", slug_for_file(file_name)]
    if file_name in FULL_TABLES:
        tags.append("full-catalog")
    else:
        tags.append("compact-catalog")

    body = frontmatter(
        {
            "type": "Table",
            "title": table_title(file_name),
            "description": description,
            "resource": resource,
            "tags": tags,
            "timestamp": timestamp,
        }
    )
    body += f"# Summary\n\n`{file_name}` is a GTFS Schedule file with file-level presence `{presence}`. {summary} [1]\n\n"
    body += "The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]\n\n"
    body += "# Schema\n\n" + "\n".join(schema_lines) + "\n\n"
    body += "# Grain\n\n" + grain_from_primary_key(primary_key, file_name) + " [1]\n\n"
    if primary_key:
        body += f"Primary key noted by the reference: `{primary_key.replace('`', '')}`. [1]\n\n"
    body += "# Relationships\n\n" + "\n".join(relationship_lines) + "\n\n"
    body += "# Modeling notes\n\n" + "\n".join(f"- {note}" for note in notes) + "\n\n"
    body += "# Citations\n\n"
    body += f"[1] [GTFS Schedule Reference: {file_name}]({resource})\n"
    body += f"[2] [google/transit GTFS Schedule reference source]({GITHUB_REFERENCE_URL})\n"
    return body, fk_edges


def concept_meta(kind: str, title: str, description: str, tags: list[str], timestamp: str, resource: str | None = None) -> str:
    return frontmatter(
        {
            "type": kind,
            "title": title,
            "description": description,
            "resource": resource,
            "tags": tags,
            "timestamp": timestamp,
        }
    )


def render_reference_overview(spec_revision: str, timestamp: str) -> str:
    return concept_meta(
        "Reference",
        "GTFS Schedule Reference Overview",
        "Public OKF overview for the GTFS Schedule static specification as a data catalog.",
        ["gtfs", "schedule", "reference", "data-catalog"],
        timestamp,
        REFERENCE_URL,
    ) + f"""# Summary

GTFS Schedule, often called static GTFS, is modeled here as a data catalog: a feed zip is the dataset, each official file is a table, each row grain is explicit, and foreign keys are represented as Markdown links so agents can traverse joins. The normative source revision used for this bundle is **{spec_revision}**. [1]

This bundle is scoped to GTFS Schedule only. GTFS Realtime is intentionally out of scope and should be treated as a separate future bundle because it has different message formats, freshness semantics, and operational questions. [1]

# Source policy

| source_id | title | url | publisher | date | source_type | reliability | used_for |
|---|---|---|---|---|---|---|---|
| `gtfs-reference` | GTFS Schedule Reference | {REFERENCE_URL} | MobilityData / GTFS documentation | {spec_revision} | Primary specification | Authoritative | File presence, field schemas, foreign keys, field meanings, required vs optional rules |
| `google-transit-reference` | google/transit GTFS Schedule reference source | {GITHUB_REFERENCE_URL} | Google Transit GitHub repository | current default branch, accessed 2026-06-30 | Primary source repository | Authoritative source mirror | Cross-checking raw Markdown and anchors |
| `gtfs-best-practices` | GTFS Schedule Best Practices | {BEST_PRACTICES_URL} | MobilityData / GTFS documentation | accessed 2026-06-30 | Secondary guidance | Guidance, not normative spec | Producer/consumer caveats and future enrichment leads |

# How to use this bundle

- Start with [GTFS Schedule Feed](/datasets/gtfs-schedule-feed.md) for dataset grain and feed-level assumptions.
- Use `/tables/` for file and field lookup, especially [trips.txt](/tables/trips.md), [stop_times.txt](/tables/stop-times.md), [calendar.txt](/tables/calendar.md), and [calendar_dates.txt](/tables/calendar-dates.md).
- Use `/concepts/` for vocabulary such as [service day](/concepts/service-day.md), [headway](/concepts/headway.md), and [route_type](/concepts/route-type.md).
- Use `/metrics/` for pseudo-SQL definitions over GTFS fields.
- Use `/decisions/` to understand the modeling boundaries of this OKF bundle.

# Freshness

GTFS evolves through the public revision process. This bundle records the Schedule Reference revision marked **{spec_revision}** and flags Fares v2, GTFS-Flex, and Realtime as likely future enrichment areas. [1]

# Citations

[1] [GTFS Schedule Reference]({REFERENCE_URL})
[2] [google/transit GTFS Schedule reference source]({GITHUB_REFERENCE_URL})
[3] [GTFS Schedule Best Practices]({BEST_PRACTICES_URL})
"""


def render_source_policy(timestamp: str) -> str:
    return concept_meta(
        "Reference",
        "GTFS Schedule Source Policy",
        "Authoritative source boundary and citation rules for this public GTFS Schedule OKF bundle.",
        ["gtfs", "schedule", "source-policy", "citations"],
        timestamp,
    ) + f"""# Summary

Normative claims in this bundle use the canonical GTFS Schedule Reference and the Google Transit repository source for cross-checking. Best practices are treated as producer guidance, not as specification requirements. Vendor blogs are excluded from this first pass unless a future implementation-caveat concept explicitly labels them as non-normative.

# Citation rules

- Table concepts cite the table-specific GTFS Schedule Reference anchor as their `resource` and citation `[1]`.
- Required/optional/conditionally required claims come from the Schedule Reference, not from best-practice guidance.
- Metrics that derive from fields cite the table concepts they depend on and the GTFS reference fields behind those tables.
- Implementation advice that is not in the reference should be marked as guidance and cite the best-practices page.

# Citations

[1] [GTFS Schedule Reference]({REFERENCE_URL})
[2] [google/transit GTFS Schedule reference source]({GITHUB_REFERENCE_URL})
[3] [GTFS Schedule Best Practices]({BEST_PRACTICES_URL})
"""


def render_optional_feature_map(timestamp: str) -> str:
    return concept_meta(
        "Reference",
        "GTFS Optional Feature Map",
        "Compact map of GTFS Schedule feature groups that are represented beyond the core required files.",
        ["gtfs", "schedule", "optional-files", "fares-v2", "flex"],
        timestamp,
    ) + """# Summary

The first-pass catalog gives full table treatment to the core and common optional Schedule files, while keeping newer or specialized feature groups discoverable through compact table concepts and links. [1]

# Feature groups

| group | table concepts | modeling note |
|---|---|---|
| Fares v1 | [fare_attributes.txt](/tables/fare-attributes.md), [fare_rules.txt](/tables/fare-rules.md) | Legacy fare model commonly found in feeds. |
| Fares v2 | [timeframes.txt](/tables/timeframes.md), [rider_categories.txt](/tables/rider-categories.md), [fare_media.txt](/tables/fare-media.md), [fare_products.txt](/tables/fare-products.md), [fare_leg_rules.txt](/tables/fare-leg-rules.md), [fare_leg_join_rules.txt](/tables/fare-leg-join-rules.md), [fare_transfer_rules.txt](/tables/fare-transfer-rules.md) | More detailed fare modeling; deeper fare-calculation rules are a recommended next pass. |
| Pathways and levels | [pathways.txt](/tables/pathways.md), [levels.txt](/tables/levels.md) | Station internal navigation graph, with levels conditionally required for elevator pathways. |
| Translations and attribution | [translations.txt](/tables/translations.md), [attributions.txt](/tables/attributions.md) | Localized values and dataset attribution metadata. |
| GTFS-Flex and rider-requested service | [location_groups.txt](/tables/location-groups.md), [location_group_stops.txt](/tables/location-group-stops.md), [locations.geojson](/tables/locations-geojson.md), [booking_rules.txt](/tables/booking-rules.md) | Demand-responsive pickup/drop-off areas and booking rules. |

# Citations

[1] [GTFS Schedule Reference](""" + REFERENCE_URL + """)
"""


def render_dataset(spec_revision: str, timestamp: str) -> str:
    return concept_meta(
        "Dataset",
        "GTFS Schedule Feed",
        "A static GTFS feed zip containing schedule files at the archive root.",
        ["gtfs", "schedule", "dataset", "feed"],
        timestamp,
        REFERENCE_URL + "#dataset-files",
    ) + f"""# Summary

A GTFS Schedule dataset is the complete set of files defined by the specification reference. The reference says dataset files are zipped together and reside at the root level of the archive, and changing the dataset creates a new version. This bundle uses the Schedule Reference revision marked **{spec_revision}**. [1]

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

# Relationships

- A feed contains many table files. See [Tables](/tables/index.md).
- A feed's active service dates are governed by [calendar.txt](/tables/calendar.md) and [calendar_dates.txt](/tables/calendar-dates.md).
- Dataset-level publisher, language, version, and coverage metadata can be provided by [feed_info.txt](/tables/feed-info.md).

# Citations

[1] [GTFS Schedule Reference: Dataset Files](""" + REFERENCE_URL + """#dataset-files)
"""


TERMS = [
    (
        "service-day",
        "Service Day",
        "Business Term",
        "A GTFS scheduling day that may extend past 24:00:00 and does not always equal a calendar day.",
        "A service day is the scheduling frame used by GTFS service calendars and stop times. GTFS times can exceed 24:00:00 to represent after-midnight service that still belongs to the same service day.",
        REFERENCE_URL + "#term-definitions",
        ["/tables/calendar.md", "/tables/calendar-dates.md", "/tables/stop-times.md"],
    ),
    (
        "headway",
        "Headway",
        "Business Term",
        "The time between departures from the same stop, represented directly in frequencies.txt or derived from stop_times.txt.",
        "For frequency-based service, `frequencies.headway_secs` records seconds between departures for a trip during a time window. For schedule-based service, headways can be derived from ordered stop_times departures.",
        REFERENCE_URL + "#frequenciestxt",
        ["/tables/frequencies.md", "/tables/stop-times.md"],
    ),
    (
        "route-type",
        "route_type",
        "Business Term",
        "The GTFS field that classifies a route's transit mode.",
        "`routes.route_type` is an enum used by GTFS consumers to distinguish modes such as tram, subway, rail, bus, ferry, cable tram, aerial lift, funicular, trolleybus, and monorail.",
        REFERENCE_URL + "#routestxt",
        ["/tables/routes.md"],
    ),
    (
        "location-type",
        "location_type",
        "Business Term",
        "The GTFS field that classifies stop rows as stops, stations, entrances, generic nodes, or boarding areas.",
        "`stops.location_type` changes the meaning of a stops.txt row and controls parent/child station modeling, pathway nodes, and boarding areas.",
        REFERENCE_URL + "#stopstxt",
        ["/tables/stops.md", "/tables/pathways.md"],
    ),
    (
        "timepoint",
        "timepoint",
        "Business Term",
        "A stop_time marker that distinguishes exact scheduled times from approximate or interpolated times.",
        "`stop_times.timepoint` indicates whether arrival and departure times are exact or approximate, which matters when deriving service spans and headways from stop_times.",
        REFERENCE_URL + "#stop_timestxt",
        ["/tables/stop-times.md"],
    ),
    (
        "block-interlining",
        "Block and Interlining",
        "Business Term",
        "A vehicle-work concept where sequential trips can be linked by block_id or explicit transfer rules.",
        "`trips.block_id` can identify trips performed by the same vehicle, while linked-trip transfer rules can express in-seat transfers or no in-seat transfers between sequential trips.",
        REFERENCE_URL + "#tripstxt",
        ["/tables/trips.md", "/tables/transfers.md"],
    ),
    (
        "frequency-vs-schedule-based-service",
        "Frequency- vs Schedule-Based Service",
        "Business Term",
        "The distinction between headway-based trips and fixed scheduled trips represented in frequencies.txt.",
        "`frequencies.exact_times=0` represents frequency-based service without fixed departures, while `exact_times=1` is a compressed representation of schedule-based service with exact repeated headways.",
        REFERENCE_URL + "#frequenciestxt",
        ["/tables/frequencies.md", "/tables/stop-times.md"],
    ),
    (
        "fare-zone",
        "Fare Zone",
        "Business Term",
        "A zone identifier used by Fares v1 rules to match origins, destinations, and contained zones.",
        "`stops.zone_id` can be referenced by `fare_rules.origin_id`, `destination_id`, and `contains_id` when modeling zone-based fares in Fares v1.",
        REFERENCE_URL + "#fare_rulestxt",
        ["/tables/stops.md", "/tables/fare-rules.md"],
    ),
    (
        "trip",
        "Trip",
        "Business Term",
        "A sequence of two or more stops for a route during a specific time period.",
        "In GTFS Schedule, trips are the scheduled units that join a route, service calendar, optional shape, and ordered stop_times.",
        REFERENCE_URL + "#tripstxt",
        ["/tables/trips.md", "/tables/stop-times.md"],
    ),
    (
        "route",
        "Route",
        "Business Term",
        "A group of trips displayed to riders as a single service.",
        "Routes group trips under rider-facing service names and mode classifications, then trips instantiate those routes on service days.",
        REFERENCE_URL + "#routestxt",
        ["/tables/routes.md", "/tables/trips.md"],
    ),
]


def render_terms(timestamp: str) -> list[tuple[str, str]]:
    files = []
    for slug, title, kind, description, summary, resource, related in TERMS:
        body = concept_meta(kind, title, description, ["gtfs", "schedule", "business-term", slug], timestamp, resource)
        body += f"# Summary\n\n{summary} [1]\n\n"
        body += "# Related concepts\n\n" + "\n".join(f"- [{Path(path).stem.replace('-', ' ')}]({path})" for path in related) + "\n\n"
        body += "# Citations\n\n" + f"[1] [GTFS Schedule Reference]({resource})\n"
        files.append((f"concepts/{slug}.md", body))
    return files


METRICS = [
    (
        "service-span",
        "Service Span",
        "The first-to-last scheduled departure window for a service date, route, direction, or stop pattern.",
        ["/tables/stop-times.md", "/tables/trips.md", "/tables/calendar.md", "/tables/calendar-dates.md"],
        """WITH active_trips AS (
  SELECT t.trip_id, t.route_id, t.service_id
  FROM trips t
  JOIN active_service_dates d ON d.service_id = t.service_id
)
SELECT route_id,
       service_date,
       MIN(first_departure_seconds) AS first_departure_seconds,
       MAX(last_departure_seconds) AS last_departure_seconds
FROM active_trips
JOIN (
  SELECT trip_id,
         MIN(time_to_seconds(departure_time)) AS first_departure_seconds,
         MAX(time_to_seconds(departure_time)) AS last_departure_seconds
  FROM stop_times
  WHERE departure_time IS NOT NULL
  GROUP BY trip_id
) trip_bounds USING (trip_id)
GROUP BY route_id, service_date;""",
        "Use service-day time parsing; GTFS times may exceed 24:00:00, so do not truncate at midnight.",
    ),
    (
        "trips-per-route-service-day",
        "Trips Per Route Per Service Day",
        "Count of scheduled trips by route and active service date.",
        ["/tables/trips.md", "/tables/calendar.md", "/tables/calendar-dates.md"],
        """SELECT t.route_id, d.service_date, COUNT(DISTINCT t.trip_id) AS trips
FROM trips t
JOIN active_service_dates d ON d.service_id = t.service_id
GROUP BY t.route_id, d.service_date;""",
        "Build `active_service_dates` from calendar weekly patterns plus calendar_dates additions/removals.",
    ),
    (
        "average-headway",
        "Average Headway",
        "Average departure spacing for a route, direction, stop, or frequency window.",
        ["/tables/frequencies.md", "/tables/stop-times.md", "/tables/trips.md"],
        """-- If frequencies.txt is present:
SELECT trip_id,
       SUM((time_to_seconds(end_time) - time_to_seconds(start_time))) /
       NULLIF(SUM((time_to_seconds(end_time) - time_to_seconds(start_time)) / headway_secs), 0) AS avg_headway_secs
FROM frequencies
GROUP BY trip_id;

-- If deriving from stop_times:
SELECT route_id, stop_id, AVG(next_departure_seconds - departure_seconds) AS avg_headway_secs
FROM ordered_departures
WHERE next_departure_seconds IS NOT NULL
GROUP BY route_id, stop_id;""",
        "Prefer frequencies.txt when trips are headway-based; otherwise derive from ordered scheduled departures at a consistent stop or pattern.",
    ),
    (
        "peak-headway",
        "Peak Headway",
        "The representative headway during a defined peak period.",
        ["/tables/frequencies.md", "/tables/stop-times.md", "/tables/trips.md"],
        """SELECT route_id,
       direction_id,
       percentile_cont(0.5) WITHIN GROUP (ORDER BY headway_secs) AS median_peak_headway_secs
FROM route_headways
WHERE departure_seconds BETWEEN peak_start_seconds AND peak_end_seconds
GROUP BY route_id, direction_id;""",
        "Define peak windows explicitly for the analysis context; GTFS does not define a universal peak period.",
    ),
    (
        "stop-count",
        "Stop Count",
        "Count of rider boarding/alighting stops in a feed or route subset.",
        ["/tables/stops.md", "/tables/stop-times.md"],
        """SELECT COUNT(DISTINCT stop_id) AS stop_count
FROM stops
WHERE COALESCE(location_type, 0) = 0;""",
        "Exclude stations, entrances/exits, generic nodes, and boarding areas unless the question explicitly asks for all locations.",
    ),
    (
        "route-count",
        "Route Count",
        "Count of distinct rider-facing routes in routes.txt.",
        ["/tables/routes.md"],
        """SELECT COUNT(DISTINCT route_id) AS route_count
FROM routes;""",
        "Filter by route_type or agency_id when comparing modal or agency-specific route counts.",
    ),
    (
        "calendar-service-date-coverage",
        "Calendar Service-Date Coverage",
        "The set and span of service dates represented by calendar.txt and calendar_dates.txt.",
        ["/tables/calendar.md", "/tables/calendar-dates.md", "/tables/feed-info.md"],
        """WITH active_service_dates AS (
  -- Expand calendar weekly patterns between start_date and end_date.
  -- Add calendar_dates where exception_type = 1.
  -- Remove calendar_dates where exception_type = 2.
)
SELECT MIN(service_date) AS first_service_date,
       MAX(service_date) AS last_service_date,
       COUNT(DISTINCT service_date) AS active_service_dates
FROM active_service_dates;""",
        "Compare active service dates to feed_info.feed_start_date and feed_info.feed_end_date when feed_info is present.",
    ),
]


def render_metrics(timestamp: str) -> list[tuple[str, str]]:
    files = []
    for slug, title, description, tables, formula, caveat in METRICS:
        body = concept_meta("Metric", title, description, ["gtfs", "schedule", "metric", slug], timestamp)
        body += f"# Definition\n\n{description} [1]\n\n"
        body += "# Source tables\n\n" + "\n".join(f"- [{Path(path).stem.replace('-', ' ')}]({path})" for path in tables) + "\n\n"
        body += "# Formula\n\n```sql\n" + formula.strip() + "\n```\n\n"
        body += "# Caveats\n\n" + f"- {caveat}\n"
        body += "- Treat times as service-day times and preserve values greater than 24:00:00 where applicable.\n\n"
        body += "# Citations\n\n"
        body += f"[1] [GTFS Schedule Reference]({REFERENCE_URL})\n"
        body += f"[2] [GTFS Schedule Reference: frequencies.txt]({REFERENCE_URL}#frequenciestxt)\n"
        body += f"[3] [GTFS Schedule Reference: stop_times.txt]({REFERENCE_URL}#stop_timestxt)\n"
        files.append((f"metrics/{slug}.md", body))
    return files


DECISIONS = [
    (
        "model-each-gtfs-file-as-table",
        "Model Each GTFS File as a Table",
        "Each official GTFS Schedule file is represented as one OKF Table concept.",
        "This mirrors a data catalog: file paths are stable table IDs, schema rows are field definitions, and foreign-key references become graph links.",
        "Accepted. This keeps retrieval predictable and lets agents answer field, requiredness, grain, and join questions without scanning the full specification.",
    ),
    (
        "scope-to-static-schedule",
        "Scope to Static GTFS Schedule",
        "This bundle excludes GTFS Realtime and focuses on static Schedule feeds.",
        "GTFS Realtime has separate protobuf messages, freshness expectations, and operational patterns, so mixing it into this Schedule catalog would blur modeling boundaries.",
        "Accepted. Realtime should be documented in a separate OKF bundle.",
    ),
    (
        "calendar-and-calendar-dates-service-model",
        "Handle Calendar and Calendar Dates Together",
        "Service-date modeling uses both calendar.txt and calendar_dates.txt, including the either/or rule.",
        "The Schedule Reference makes calendar.txt conditionally required unless all service dates are defined in calendar_dates.txt; calendar_dates.txt is required if calendar.txt is omitted.",
        "Accepted. Metrics should build an active service-date set before joining to trips.",
    ),
    (
        "fares-v1-and-v2-boundary",
        "Keep Fares v1 Full and Fares v2 Discoverable",
        "The first pass gives Fares v1 full treatment and keeps Fares v2 tables compact but linked.",
        "Fares v1 remains common in feeds, while Fares v2 adds richer fare products, media, leg rules, join rules, and transfer rules that deserve deeper fare-specific enrichment later.",
        "Accepted. This bundle supports discovery and basic joins for Fares v2 without pretending to be a fare-calculation manual.",
    ),
]


def render_decisions(timestamp: str) -> list[tuple[str, str]]:
    files = []
    for slug, title, description, context, decision in DECISIONS:
        body = concept_meta("Architectural Decision", title, description, ["gtfs", "schedule", "decision", slug], timestamp)
        body += f"# Context\n\n{context} [1]\n\n"
        body += f"# Decision\n\n{decision}\n\n"
        body += "# Consequences\n\n"
        body += "- Agents can traverse the bundle using stable file paths and table links.\n"
        body += "- Future enrichment can add depth without changing the concept IDs created here.\n\n"
        body += "# Citations\n\n" + f"[1] [GTFS Schedule Reference]({REFERENCE_URL})\n"
        files.append((f"decisions/{slug}.md", body))
    return files


def index_for_directory(title: str, entries: list[tuple[str, str, str]]) -> str:
    content = f"# {title}\n\n"
    content += "This index is a progressive-disclosure entry point for this part of the GTFS Schedule OKF bundle.\n\n"
    content += "| concept | type | description |\n|---|---|---|\n"
    for href, type_name, description in entries:
        label = Path(href).stem.replace("-", " ")
        content += f"| [{label}]({href}) | {type_name} | {description} |\n"
    return content


def render_root_index(table_count: int, metric_count: int, term_count: int, decision_count: int, spec_revision: str) -> str:
    return f"""# GTFS Schedule Data Catalog

Public OKF bundle for answering GTFS Schedule modeling questions with citations. It treats the static GTFS feed as a data catalog: dataset, tables, fields, row grain, relationships, business terms, metrics, and modeling decisions.

## Scope

- In scope: GTFS Schedule / static feed files from the Schedule Reference revision marked **{spec_revision}**.
- Out of scope: GTFS Realtime. See [Scope to Static GTFS Schedule](/decisions/scope-to-static-schedule.md).
- Normative source: [GTFS Schedule Reference]({REFERENCE_URL}).
- Secondary guidance only: [GTFS Schedule Best Practices]({BEST_PRACTICES_URL}).

## Entry Points

| question | start here |
|---|---|
| What is a GTFS feed? | [GTFS Schedule Feed](/datasets/gtfs-schedule-feed.md) |
| What files and fields exist? | [Tables](/tables/index.md) |
| How do files join? | [trips.txt](/tables/trips.md), [stop_times.txt](/tables/stop-times.md), [calendar.txt](/tables/calendar.md), [calendar_dates.txt](/tables/calendar-dates.md) |
| What does a term mean? | [Business terms](/concepts/index.md) |
| How do I compute schedule KPIs? | [Metrics](/metrics/index.md) |
| Why is the bundle modeled this way? | [Decisions](/decisions/index.md) |

## Counts

- Dataset concepts: 1
- Table concepts: {table_count}
- Metric concepts: {metric_count}
- Business-term concepts: {term_count}
- Architectural-decision concepts: {decision_count}

## Directories

- [Concepts](concepts/index.md) - overview, source policy, optional feature map, and vocabulary.
- [Datasets](datasets/index.md) - the feed zip as a dataset concept.
- [Tables](tables/index.md) - one concept per GTFS Schedule file.
- [Metrics](metrics/index.md) - common service KPIs derivable from schedule files.
- [Decisions](decisions/index.md) - modeling decisions and scope boundaries.

## Freshness

GTFS evolves. This bundle records the Schedule Reference revision marked **{spec_revision}** and should be refreshed when the reference changes, especially for Fares v2 and GTFS-Flex files.
"""


def main() -> None:
    timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    markdown = fetch_text(REFERENCE_RAW_URL)
    revision_match = re.search(r"\*\*Revised ([^.]+)\.", markdown)
    spec_revision = revision_match.group(1) if revision_match else "unknown revision"
    dataset_files = parse_dataset_files(markdown)
    sections = parse_sections(markdown)

    for directory in ["concepts", "datasets", "tables", "metrics", "decisions"]:
        (BUNDLE / directory).mkdir(parents=True, exist_ok=True)

    ordered_files = [file_name for file_name in CORE_ORDER if file_name in sections]
    file_map = {base_for_file(file_name): table_path(file_name) for file_name in ordered_files}
    file_map.update({file_name: table_path(file_name) for file_name in ordered_files})

    concept_entries: list[tuple[str, str, str]] = []
    dataset_entries: list[tuple[str, str, str]] = []
    table_entries: list[tuple[str, str, str]] = []
    metric_entries: list[tuple[str, str, str]] = []
    decision_entries: list[tuple[str, str, str]] = []
    join_edges = 0

    write_file(BUNDLE / "concepts" / "gtfs-schedule-reference-overview.md", render_reference_overview(spec_revision, timestamp))
    concept_entries.append(("gtfs-schedule-reference-overview.md", "Reference", "Bundle overview, source table, scope, and freshness."))
    write_file(BUNDLE / "concepts" / "source-policy.md", render_source_policy(timestamp))
    concept_entries.append(("source-policy.md", "Reference", "Citation and source boundary policy."))
    write_file(BUNDLE / "concepts" / "optional-feature-map.md", render_optional_feature_map(timestamp))
    concept_entries.append(("optional-feature-map.md", "Reference", "Compact map of Fares v2, pathways, translations, attributions, and Flex files."))

    for relative_path, body in render_terms(timestamp):
        write_file(BUNDLE / relative_path, body)
        description = next(term[3] for term in TERMS if relative_path.endswith(term[0] + ".md"))
        concept_entries.append((Path(relative_path).name, "Business Term", description))

    write_file(BUNDLE / "datasets" / "gtfs-schedule-feed.md", render_dataset(spec_revision, timestamp))
    dataset_entries.append(("gtfs-schedule-feed.md", "Dataset", "Static GTFS feed zip modeled as a dataset."))

    for file_name in ordered_files:
        body, edges = render_table_concept(file_name, sections[file_name], dataset_files, file_map, timestamp)
        join_edges += edges + len(extra_relationships(file_name))
        path = BUNDLE / "tables" / f"{slug_for_file(file_name)}.md"
        write_file(path, body)
        table_entries.append((path.name, "Table", table_description(file_name, dataset_files.get(file_name, {}), sections[file_name])))

    for relative_path, body in render_metrics(timestamp):
        write_file(BUNDLE / relative_path, body)
        description = next(metric[2] for metric in METRICS if relative_path.endswith(metric[0] + ".md"))
        metric_entries.append((Path(relative_path).name, "Metric", description))

    for relative_path, body in render_decisions(timestamp):
        write_file(BUNDLE / relative_path, body)
        description = next(decision[2] for decision in DECISIONS if relative_path.endswith(decision[0] + ".md"))
        decision_entries.append((Path(relative_path).name, "Architectural Decision", description))

    write_file(BUNDLE / "concepts" / "index.md", index_for_directory("Concepts", concept_entries))
    write_file(BUNDLE / "datasets" / "index.md", index_for_directory("Datasets", dataset_entries))
    write_file(BUNDLE / "tables" / "index.md", index_for_directory("Tables", table_entries))
    write_file(BUNDLE / "metrics" / "index.md", index_for_directory("Metrics", metric_entries))
    write_file(BUNDLE / "decisions" / "index.md", index_for_directory("Decisions", decision_entries))
    write_file(
        BUNDLE / "index.md",
        render_root_index(
            table_count=len(table_entries),
            metric_count=len(metric_entries),
            term_count=len(TERMS),
            decision_count=len(decision_entries),
            spec_revision=spec_revision,
        ),
    )
    write_file(
        BUNDLE / "log.md",
        f"""# Log

## 2026-06-30

- Created GTFS Schedule data catalog from the official Schedule Reference revision marked {spec_revision}.
- Generated {len(table_entries)} table concepts, {len(metric_entries)} metric concepts, {len(TERMS)} business-term concepts, one dataset concept, and {len(decision_entries)} architectural decisions.
- Modeled table relationships as bundle-relative Markdown links for OKF graph traversal.
""",
    )

    print(f"spec_revision={spec_revision}")
    print(f"tables={len(table_entries)}")
    print(f"metrics={len(metric_entries)}")
    print(f"terms={len(TERMS)}")
    print(f"decisions={len(decision_entries)}")
    print(f"join_edges={join_edges}")


if __name__ == "__main__":
    main()
