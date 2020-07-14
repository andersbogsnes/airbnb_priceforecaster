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

host_about
==========
Text giving a description of who the host is.
- drop

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

street
======
Anonymised and useless
- drop

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

weekly_price
============
Some have a special weekly price. Not relevant
- drop

monthly_price
=============
Some have a special monthly price. Not relevant
- drop

maximum_minimum_nights
======================
Historically maximum minimum number of nights
- drop


minimum_maximum_nights
======================
Historically, minum max-nights
- drop

maximum_maximum_nights
======================
Historically, maximum max-nights
- drop

minimum_nights_avg_ntm
======================
?
- drop

maximum_nights_avg_ntm
======================
?
- drop

calendar_updated
================
The last time the calendar was updated. A text field.
- drop

has_availability
================
Whether or not the rental has availability

- drop

availability_30
===============
Number of availabilites over the next 30 days. Could be relevant to see if someone is overpricing. Maybe some adjusted target?

- drop


availability_60
===============
Number of availabilites over the next 60 days. Could be relevant to see if someone is under/overpriced. Maybe some adjusted target?
- drop

availability_90
===============
Number of availabilites over the next 90 days.
- drop
availability_365
================
Number of availabilities over the next 365 days.
- drop
calendar_last_scraped
=====================
When the calendar was last scraped
- drop
number_of_reviews
=================
Number of reviews of the rental
- drop
number_of_reviews_ltm
=====================
?
- drop
first_review
============
When was the first review
- drop

last_review
===========
When was the last review
- drop
review_scores_rating
====================
Total review
- drop
review_scores_accuracy
======================
Review of how accurate the information was
- drop
review_scores_cleanliness
=========================
Review of how clean it was
- drop

review_scores_checkin
=====================
Review of the checkin process
- drop

review_scores_communication
===========================
Review of host communication

- drop

review_scores_location
======================
Review of location. Could be relevant as a location scoring index -> high/low quality location
 - drop

review_scores_value
===================
Review of the overall value of the rental. Could be used to backtest validity of a given price
 - drop

requires_license
=================
If a license is required. In this dataset, always no.

 - drop

license
=======
Type of license? only 3 different values in the datasat and 11 non-NaN observations
 - drop

jurisdiction_names
==================
Not relevant in Copenhagen
- drop

calculated_host_listings_count
==============================
How many listings does the host have. Derived feature
- drop

calculated_host_listings_count_entire_homes
===========================================
How many homes is the host renting.
- drop

calculated_host_listings_count_private_rooms
============================================
How many private rooms is the host renting
- drop

calculated_host_listings_count_shared_rooms
===========================================
How many shared rooms is the host renting
- drop

reviews_per_month
=================
How many reviews per month does this property get
- drop

is_business_travel_ready
========================
Whether the rental is appropriate for business travel

Only false values in the dataset