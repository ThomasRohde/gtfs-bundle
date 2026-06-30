---
type: "Table"
title: "translations.txt"
description: "Translations of customer-facing dataset values."
resource: "https://gtfs.org/documentation/schedule/reference/#translationstxt"
tags: [gtfs, schedule, table, translations, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`translations.txt` is a GTFS Schedule file with file-level presence `Optional`. In regions that have multiple official languages, transit agencies/operators typically have language-specific names and web pages. In order to best serve riders in those regions, it is useful for the dataset to include these language-dependent values. If both referencing methods (`record_id`, `record_sub_id`) and `field_value` are used to translate the same value in 2 different rows, the translation provided with (`record_id`, `record_sub_id`) takes precedence. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `table_name` | Enum | Required | Defines the table that contains the field to be translated. Allowed values are: - `agency` - `stops` - `routes` - `trips` - `stop_times` - `pathways` - `levels` - `feed_info` - `attributions` Any file added to GTFS will have a `table_name` value equivalent to the file name, as listed above (i.e., not including the `.txt` file extension). [1] |
| `field_name` | Text | Required | Name of the field to be translated. Fields with type `Text` may be translated, fields with type `URL`, `Email` and `Phone number` may also be “translated” to provide resources in the correct language. Fields with other types should not be translated. [1] |
| `language` | Language code | Required | Language of translation. If the language is the same as in `feed_info.feed_lang`, the original value of the field will be assumed to be the default value to use in languages without specific translations (if `default_lang` doesn't specify otherwise). [1] |
| `translation` | Text or URL or Email or Phone number | Required | Translated value. [1] |
| `record_id` | Foreign ID | Conditionally Required | Defines the record that corresponds to the field to be translated. The value in `record_id` must be the first or only field of a table's primary key, as defined in the primary key attribute for each table and below: - `agency_id` for agency.txt - `stop_id` for stops.txt; - `route_id` for routes.txt; - `trip_id` for trips.txt; - `trip_id` for stop_times.txt; - `pathway_id` for pathways.txt; - `level_id` for levels.txt; - `attribution_id` for attributions.txt. Fields in tables not defined above should not be translated. However producers sometimes add extra fields that are outside the official specification and. [1] |
| `record_sub_id` | Foreign ID | Conditionally Required | Helps the record that contains the field to be translated when the table doesn’t have a unique ID. Therefore, the value in `record_sub_id` is the secondary ID of the table, as defined by the table below: - None for agency.txt; - None for stops.txt; - None for routes.txt; - None for trips.txt; - `stop_sequence` for stop_times.txt; - None for pathways.txt; - None for levels.txt; - None for attributions.txt. Fields in tables not defined above should not be translated. However producers sometimes add extra fields that are outside the official specification and these unofficial fields may be translated. Below is the. [1] |
| `field_value` | Text or URL or Email or Phone number | Conditionally Required | Instead of defining which record should be translated by using `record_id` and `record_sub_id`, this field can be used to define the value which should be translated. When used, the translation will be applied when the fields identified by `table_name` and `field_name` contains the exact same value defined in field_value. The field must have exactly the value defined in `field_value`. If only a subset of the value matches `field_value`, the translation won’t be applied. If two translation rules match the same record (one with `field_value`, and the other one with `record_id`), the rule with `record_id` takes. [1] |

# Grain

One row per `table_name, field_name, language, record_id, record_sub_id, field_value` key in `translations.txt`. [1]

Primary key noted by the reference: `table_name, field_name, language, record_id, record_sub_id, field_value`. [1]

# Relationships

- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.

# Citations

[1] [GTFS Schedule Reference: translations.txt](https://gtfs.org/documentation/schedule/reference/#translationstxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
