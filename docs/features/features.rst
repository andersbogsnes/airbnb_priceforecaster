Features
--------

ID
==
Id is the unique ID of the column - don't need that
- drop

listing_url
===========
The url that was scraped
- drop

scrape_id
=========
ID of the scrape
- drop

last_scraped
============
When that record was last scraped
- drop

name
====
The name of the listing - a short message designed to attract the potential renter
- drop

summary
=======
A summary of the property - a paragraph with some information about the listing. Another project could be to predict whether the info page could be improved.
- drop

space
=====
A description of the living space
- drop

description
===========
Long form description
- drop

experiences_offered
===================
Whether or not the host offers any experiences - is all none in this dataset
- drop

neighborhood_overview
=====================
Describing the local neighborhood. Could be relevant for extracting some features about the neighborhood that are not present in the other data e.g. if bars + cafes are often mentioned, this could be used to tag all other listings in that neighborhood. Would be more advanced feature.
- drop

notes
=====
Any special mentions that the host wants to point out
- drop

transit
=======
A host-provided text describing about what kind of transit is available. Probably better to get that information from geo-coding
- drop

access
======
A host-provided text describing how much of the property is available
- drop

interaction
===========
A host-provided text describing how much they will be around
- drop

house_rules
===========
What rules the guest must follow. Would try to extract some simple rules such as smoking allowed or similar
- keep

thumbnail_url
=============
URL to the picture. Later could do some image feature extraction.
- drop

medium_url
==========
URL to the picture. Later could do some image feature extraction.
- drop

picture_url
===========
URL to the picture. Later could do some image feature extraction.
- drop

xl_picture_url
==============
URL to the picture. Later could do some image feature extraction.
- drop


host_id
=======
ID of the host
- drop

host_url
========
URL to the host page
- drop

host_name
=========
Name of the host
- drop

host_since
==========
When started hosting. Hypothesis that being a host for longer affects the price - they might be able to charge a different price.
For our solution, we can set it to 0 or ask.
- keep

host_location
=============
Where the host is located. Hypothesis that the host being somewhere else affects the price
- keep

host_about
==========
Text giving a description of who the host is.
- drop

host_response_time
==================
How long does it take for the host to accept/decline an offer. Hypothesis that this could be an indicator of "seriousness" which could affect the price
- keep

host_response_rate
==================
How many requests does the host respond to. Hypothesis that this could be an indicator of "seriousness" which could affect the price
- drop

host_acceptance_rate
====================
Out of all requests, how many are accepted. Hypothesis that this could be an indicator of "seriousness" which could affect the price
- drop

host_is_superhost
=================
Whether or not the host is a "superhost". Hypothesis that this could be an indicator of "seriousness" which could affect the price
- drop

host_thumbnail_url
==================
URL to thumbnail picture of host
- drop

host_picture_url
================
URL to picture of host
- drop

host_neighbourhood
==================
Where the host lives. Hypothesis that this could indicate "awayness", which could affect the price
- keep

host_listings_count
===================
How many listings they have. Hypothesis that this could be an indicator of "seriousness" which could affect the price
- keep

host_total_listings_count
=========================
Unsure how this is different from above.
- keep


host_verifications
==================
What communication verifications does the host have. Hypothesis that more/specific types of validated communcations increases confidence
- keep

host_has_profile_pic
====================
Does the host have a profile picture? Hypothesis that this could increase confidence and thus price
- keep


host_identity_verified
======================
Is the host verified. Hypothesis that this increases confidence and thus price
- keep

street
======
Anonymised and useless
- drop

neighbourhood
=============
The area which the host writes.
- keep

neighbourhood_cleansed
======================
Data cleansing from source - doesn't work
- drop

neighbourhood_group_cleansed
============================
Data cleansing from source - doesn't work
- drop

city
====
Should all be Copenhagen
- drop

state
=====
Should all be Hovedstaden
- drop

zipcode
=======
Zipcode (postnr) of the location
- keep

market
======
What Airbnb market. Should all be Copenhagen
- drop


smart_location
==============
All Copenhagen
- drop

country_code
============
All DK
- drop

country
=======
All Denmark
- drop


latitude
========
Approximate latitude
- keep

longitude
=========
Approximate longitude


is_location_exact
=================
Whether or not the location is exact or approximate

property_type
=============
What kind of property it is. House/Apartment/Room etc. Should definitely affect price

room_type
=========
What kind of room - Private room / shared room / entire apt etc. Should definitely affect price

accommodates
============
How many people does it accomodate. Should definitely affect price


bathrooms
=========
How many bathrooms. More should increase price

bedrooms
========
How many bedrooms. More should increase price

beds
====
How many beds. More should increase price


bed_type
========
What type of bed is available. Better bed should increase price

amenities
=========
Different types of amenities available. Should affect price

square_feet
===========
Size of rental. Should affect price

price
=====
The target variable

weekly_price
============
Some have a special weekly price. Not relevant
- drop

monthly_price
=============
Some have a special monthly price. Not relevant
- drop

security_deposit
================
What's the security deposit. Might be related to the price

cleaning_fee
============
What's the cleaning fee. Affects price directly

guests_included
===============
How many guests are included in the price. Directly impacts price

extra_people
============
How much more for extra people. Directly impacts price

minimum_nights
==============
Minimum number of nights. Could impact price

maximum_nights
==============
Maximum number of nights. Could impact price

minimum_minimum_nights
======================
Historically minimum

 'maximum_minimum_nights',
 'minimum_maximum_nights',
 'maximum_maximum_nights',
 'minimum_nights_avg_ntm',
 'maximum_nights_avg_ntm',
 'calendar_updated',
 'has_availability',
 'availability_30',
 'availability_60',
 'availability_90',
 'availability_365',
 'calendar_last_scraped',
 'number_of_reviews',
 'number_of_reviews_ltm',
 'first_review',
 'last_review',
 'review_scores_rating',
 'review_scores_accuracy',
 'review_scores_cleanliness',
 'review_scores_checkin',
 'review_scores_communication',
 'review_scores_location',
 'review_scores_value',
 'requires_license',
 'license',
 'jurisdiction_names',
 'instant_bookable',
 'is_business_travel_ready',
 'cancellation_policy',
 'require_guest_profile_picture',
 'require_guest_phone_verification',
 'calculated_host_listings_count',
 'calculated_host_listings_count_entire_homes',
 'calculated_host_listings_count_private_rooms',
 'calculated_host_listings_count_shared_rooms',
 'reviews_per_month']
