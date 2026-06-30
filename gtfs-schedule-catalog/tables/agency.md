---
type: "Table"
title: "agency.txt"
description: "Transit agencies with service represented in this dataset."
resource: "https://gtfs.org/documentation/schedule/reference/#agencytxt"
tags: [gtfs, schedule, table, agency, full-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`agency.txt` is a GTFS Schedule file with file-level presence `Required`. Transit agencies with service represented in this dataset. [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `agency_id` | Unique ID | Conditionally Required | Identifies a transit brand which is often synonymous with a transit agency. Note that in some cases, such as when a single agency operates multiple separate services, agencies and brands are distinct. This document uses the term "agency" in place of "brand". A dataset may contain data from multiple agencies. Conditionally Required: - Required when the dataset contains data for multiple transit agencies. - Recommended otherwise. [1] |
| `agency_name` | Text | Required | Full name of the transit agency. [1] |
| `agency_url` | URL | Required | URL of the transit agency. [1] |
| `agency_timezone` | Timezone | Required | Timezone where the transit agency is located. If multiple agencies are specified in the dataset, each must have the same `agency_timezone`. [1] |
| `agency_lang` | Language code | Optional | Primary language used by this transit agency. Should be provided to help GTFS consumers choose capitalization rules and other language-specific settings for the dataset. [1] |
| `agency_phone` | Phone number | Optional | A voice telephone number for the specified agency. This field is a string value that presents the telephone number as typical for the agency's service area. It may contain punctuation marks to group the digits of the number. Dialable text (for example, TriMet's "503-238-RIDE") is permitted, but the field must not contain any other descriptive text. [1] |
| `agency_fare_url` | URL | Optional | URL of a web page where a rider can purchase tickets or other fare instruments for that agency, or a web page containing information about that agency's fares. [1] |
| `agency_email` | Email | Optional | Email address actively monitored by the agency’s customer service department. This email address should be a direct contact point where transit riders can reach a customer service representative at the agency. [1] |
| `cemv_support` | Enum | Optional | Indicates if riders can access a transit service (i.e., trip) associated with this agency by using a contactless EMV (Europay, Mastercard, and Visa) card or mobile device as fare media at a fare validator (such as in pay-as-you-go or open-loop systems). This field does not indicate that cEMV can be used to purchase other fare products or to add value to another fare media. Support for cEMVs should only be indicated if all services under this agency are accessible with the use of cEMV cards or mobile devices as fare media. Valid options are: `0` or empty - No cEMV information for trips associated with this. [1] |

# Grain

One row per `agency_id` key in `agency.txt`. [1]

Primary key noted by the reference: `agency_id`. [1]

# Relationships

- No direct foreign-key relationship is defined for this file in the GTFS Schedule Reference. [1]

# Modeling notes

- This is modeled as a full catalog table in the first-pass bundle because it is core, conditionally required, or commonly used in schedule analysis.

# Citations

[1] [GTFS Schedule Reference: agency.txt](https://gtfs.org/documentation/schedule/reference/#agencytxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
