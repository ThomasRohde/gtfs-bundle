---
type: "Table"
title: "feed_info.txt"
description: "Dataset metadata, including publisher, version, and expiration information. Conditionally Required: - Required if translations.txt is provided. - Recommended otherwise."
resource: "https://gtfs.org/documentation/schedule/reference/#feed_infotxt"
tags: [gtfs, schedule, table, feed-info, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`feed_info.txt` is a GTFS Schedule file with file-level presence `Conditionally Required`. The file contains information about the dataset itself, rather than the services that the dataset describes. In some cases, the publisher of the dataset is a different entity than any of the agencies. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `feed_publisher_name` | Text | Required | Full name of the organization that publishes the dataset. This may be the same as one of the `agency.agency_name` values. [1] |
| `feed_publisher_url` | URL | Required | URL of the dataset publishing organization's website. This may be the same as one of the `agency.agency_url` values. [1] |
| `feed_lang` | Language code | Required | Default language used for the text in this dataset. This setting helps GTFS consumers choose capitalization rules and other language-specific settings for the dataset. The file `translations.txt` can be used if the text needs to be translated into languages other than the default one. The default language may be multilingual for datasets with the original text in multiple languages. In such cases, the `feed_lang` field should contain the language code `mul` defined by the norm ISO 639-2, and a translation for each language used in the dataset should be provided in `translations.txt`. If all the original text in. [1] |
| `default_lang` | Language code | Optional | Defines the language that should be used when the data consumer doesn’t know the language of the rider. It will often be `en` (English). [1] |
| `feed_start_date` | Date | Recommended | The dataset provides complete and reliable schedule information for service in the period from the beginning of the `feed_start_date` day to the end of the `feed_end_date` day. Both days may be left empty if unavailable. The `feed_end_date` date must not precede the `feed_start_date` date if both are given. It is recommended that dataset providers give schedule data outside this period to advise of likely future service, but dataset consumers should treat it mindful of its non-authoritative status. If `feed_start_date` or `feed_end_date` extend beyond the active calendar dates defined in calendar.txt and. [1] |
| `feed_end_date` | Date | Recommended | (see above) [1] |
| `feed_version` | Text | Recommended | String that indicates the current version of their GTFS dataset. GTFS-consuming applications can display this value to help dataset publishers determine whether the latest dataset has been incorporated. [1] |
| `feed_contact_email` | Email | Optional | Email address for communication regarding the GTFS dataset and data publishing practices. `feed_contact_email` is a technical contact for GTFS-consuming applications. Provide customer service contact information through agency.txt. It's recommended that at least one of `feed_contact_email` or `feed_contact_url` are provided. [1] |
| `feed_contact_url` | URL | Optional | URL for contact information, a web-form, support desk, or other tools for communication regarding the GTFS dataset and data publishing practices. `feed_contact_url` is a technical contact for GTFS-consuming applications. Provide customer service contact information through agency.txt. It's recommended that at least one of `feed_contact_url` or `feed_contact_email` are provided. [1] |

# Grain

`feed_info.txt` allows one dataset-level record. [1]

Primary key noted by the reference: `none`. [1]

# Relationships

- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.
- The file-level presence is `Conditionally Required`; read the table summary and schema before assuming the file is always present.

# Citations

[1] [GTFS Schedule Reference: feed_info.txt](https://gtfs.org/documentation/schedule/reference/#feed_infotxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
