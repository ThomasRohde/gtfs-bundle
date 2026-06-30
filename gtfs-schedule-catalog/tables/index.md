# Tables

This index is a progressive-disclosure entry point for this part of the GTFS Schedule OKF bundle.

| concept | type | description |
|---|---|---|
| [agency](agency.md) | Table | Transit agencies with service represented in this dataset. |
| [stops](stops.md) | Table | Stops where vehicles pick up or drop off riders. Also defines stations and station entrances. Conditionally Required: - Optional if demand-responsive zones are defined. |
| [routes](routes.md) | Table | Transit routes. A route is a group of trips that are displayed to riders as a single service. |
| [trips](trips.md) | Table | Trips for each route. A trip is a sequence of two or more stops that occur during a specific time period. |
| [stop times](stop-times.md) | Table | Times that a vehicle arrives at and departs from stops for each trip. |
| [calendar](calendar.md) | Table | Service dates specified using a weekly schedule with start and end dates. Conditionally Required: - Required unless all dates of service are defined in. |
| [calendar dates](calendar-dates.md) | Table | Exceptions for the services defined in the calendar.txt. Conditionally Required: - Required if calendar.txt is omitted. In which case calendar_dates.txt must contain all. |
| [fare attributes](fare-attributes.md) | Table | Fare information for a transit agency's routes. |
| [fare rules](fare-rules.md) | Table | Rules to apply fares for itineraries. |
| [timeframes](timeframes.md) | Table | Date and time periods to use in fare rules for fares that depend on date and time factors. |
| [rider categories](rider-categories.md) | Table | Defines categories of riders (e.g. elderly, student). |
| [fare media](fare-media.md) | Table | To describe the fare media that can be employed to use fare products. File fare_media.txt describes concepts that are not represented in fare_attributes.txt and. |
| [fare products](fare-products.md) | Table | To describe the different types of tickets or fares that can be purchased by riders. File fare_products.txt describes fare products that are not represented in. |
| [fare leg rules](fare-leg-rules.md) | Table | Fare rules for individual legs of travel. File fare_leg_rules.txt provides a more detailed method for modeling fare structures. As such, the use of fare_leg_rules.txt is. |
| [fare leg join rules](fare-leg-join-rules.md) | Table | Rules for defining two or more legs should be considered as a single effective fare leg for the purposes of matching against rules in fare_leg_rules.txt |
| [fare transfer rules](fare-transfer-rules.md) | Table | Fare rules for transfers between legs of travel. Along with fare_leg_rules.txt, file fare_transfer_rules.txt provides a more detailed method for modeling fare. |
| [areas](areas.md) | Table | Area grouping of locations. |
| [stop areas](stop-areas.md) | Table | Rules to assign stops to areas. |
| [networks](networks.md) | Table | Network grouping of routes. Conditionally Forbidden: - Forbidden if `network_id` exists in routes.txt. - Optional otherwise. |
| [route networks](route-networks.md) | Table | Rules to assign routes to networks. Conditionally Forbidden: - Forbidden if `network_id` exists in routes.txt. - Optional otherwise. |
| [shapes](shapes.md) | Table | Rules for mapping vehicle travel paths, sometimes referred to as route alignments. |
| [frequencies](frequencies.md) | Table | Headway (time between trips) for headway-based service or a compressed representation of fixed-schedule service. |
| [transfers](transfers.md) | Table | Rules for making connections at transfer points between routes. |
| [pathways](pathways.md) | Table | Pathways linking together locations within stations. |
| [levels](levels.md) | Table | Levels within stations. Conditionally Required: - Required when describing pathways with elevators (`pathway_mode=5`). - Optional otherwise. |
| [location groups](location-groups.md) | Table | A group of stops that together indicate locations where a rider may request pickup or drop off. |
| [location group stops](location-group-stops.md) | Table | Rules to assign stops to location groups. |
| [locations geojson](locations-geojson.md) | Table | Zones for rider pickup or drop-off requests by on-demand services, represented as GeoJSON polygons. |
| [booking rules](booking-rules.md) | Table | Booking information for rider-requested services. |
| [translations](translations.md) | Table | Translations of customer-facing dataset values. |
| [feed info](feed-info.md) | Table | Dataset metadata, including publisher, version, and expiration information. Conditionally Required: - Required if translations.txt is provided. - Recommended otherwise. |
| [attributions](attributions.md) | Table | Dataset attributions. |
