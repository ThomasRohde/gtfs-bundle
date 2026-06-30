---
type: "Table"
title: "booking_rules.txt"
description: "Booking information for rider-requested services."
resource: "https://gtfs.org/documentation/schedule/reference/#booking_rulestxt"
tags: [gtfs, schedule, table, booking-rules, compact-catalog]
timestamp: "2026-06-30T03:31:40+00:00"
---

# Summary

`booking_rules.txt` is a GTFS Schedule file with file-level presence `Optional`. Defines the booking rules for rider-requested services [1]

The schema, field presence, field types, primary-key notes, and relationship hints below are sourced from the GTFS Schedule Reference revision used by this bundle. [1]

# Schema

| field | type | required | meaning |
|---|---|---|---|
| `booking_rule_id` | Unique ID | Required | Identifies a rule. [1] |
| `booking_type` | Enum | Required | Indicates how far in advance booking can be made. Valid options are: `0` - Real time booking. `1` - Up to same-day booking with advance notice. `2` - Up to prior day(s) booking. [1] |
| `prior_notice_duration_min` | Integer | Conditionally Required | Minimum number of minutes before travel to make the request. Conditionally Required: - Required for `booking_type=1`. - Forbidden otherwise. [1] |
| `prior_notice_duration_max` | Integer | Conditionally Forbidden | Maximum number of minutes before travel to make the booking request. Conditionally Forbidden: - Forbidden for `booking_type=0` and `booking_type=2`. - Optional for `booking_type=1`. [1] |
| `prior_notice_last_day` | Integer | Conditionally Required | Last day before travel to make the booking request. Example: “Ride must be booked 1 day in advance before 5PM” will be encoded as `prior_notice_last_day=1`. Conditionally Required: - Required for `booking_type=2`. - Forbidden otherwise. [1] |
| `prior_notice_last_time` | Time | Conditionally Required | Last time on the last day before travel to make the booking request. Example: “Ride must be booked 1 day in advance before 5PM” will be encoded as `prior_notice_last_time=17:00:00`. Conditionally Required: - Required if `prior_notice_last_day` is defined. - Forbidden otherwise. [1] |
| `prior_notice_start_day` | Integer | Conditionally Forbidden | Earliest day before travel to make the booking request. Example: “Ride can be booked at the earliest one week in advance at midnight” will be encoded as `prior_notice_start_day=7`. Conditionally Forbidden: - Forbidden for `booking_type=0`. - Forbidden for `booking_type=1` if `prior_notice_duration_max` is defined. - Optional otherwise. [1] |
| `prior_notice_start_time` | Time | Conditionally Required | Earliest time on the earliest day before travel to make the booking request. Example: “Ride can be booked at the earliest one week in advance at midnight” will be encoded as `prior_notice_start_time=00:00:00`. Conditionally Required: - Required if `prior_notice_start_day` is defined. - Forbidden otherwise. [1] |
| `prior_notice_service_id` | Foreign ID referencing [calendar.txt](/tables/calendar.md).`service_id` | Conditionally Forbidden | Indicates the service days on which `prior_notice_last_day` or `prior_notice_start_day` are counted. Example: If empty, `prior_notice_start_day=2` will be two calendar days in advance. If defined as a `service_id` containing only business days (weekdays without holidays), `prior_notice_start_day=2` will be two business days in advance. Conditionally Forbidden: - Optional if `booking_type=2`. - Forbidden otherwise. [1] |
| `message` | Text | Optional | Message to riders utilizing service at a `stop_time` when booking on-demand pickup and drop off. Meant to provide minimal information to be transmitted within a user interface about the action a rider must take in order to utilize the service. [1] |
| `pickup_message` | Text | Optional | Functions in the same way as `message` but used when riders have on-demand pickup only. [1] |
| `drop_off_message` | Text | Optional | Functions in the same way as `message` but used when riders have on-demand drop off only. [1] |
| `phone_number` | Phone number | Optional | Phone number to call to make the booking request. [1] |
| `info_url` | URL | Optional | URL providing information about the booking rule. [1] |
| `booking_url` | URL | Optional | URL to an online interface or app where the booking request can be made. [1] |

# Grain

One row per `booking_rule_id` key in `booking_rules.txt`. [1]

Primary key noted by the reference: `booking_rule_id`. [1]

# Relationships

- `booking_rules.prior_notice_service_id` references [calendar.txt](/tables/calendar.md).`service_id`. [1]

# Modeling notes

- This compact table concept keeps the file discoverable and captures its joins without expanding every implementation caveat in this first pass.
- This file participates in GTFS-Flex or rider-requested service modeling and is intentionally summarized here rather than treated as the main schedule model.

# Citations

[1] [GTFS Schedule Reference: booking_rules.txt](https://gtfs.org/documentation/schedule/reference/#booking_rulestxt)
[2] [google/transit GTFS Schedule reference source](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md)
