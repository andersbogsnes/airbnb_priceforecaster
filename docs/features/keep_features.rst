host_neighbourhood
==================
Where the host lives. Hypothesis that this could indicate "awayness", which could affect the price

Text of where the host is located. Could be used to extract features from
dtype: string


host_listings_count
===================
How many listings they have. Hypothesis that this could be an indicator of "seriousness" which could affect the price

Is a count, so an integer
dtype: Int64


host_total_listings_count
=========================
Unsure how this is different from above.

Is a count, so an integer
dtype: Int64


host_verifications
==================
What communication verifications does the host have. Hypothesis that more/specific types of validated communcations increases confidence

Is an array in string form. Need to read as string and preprocess
dtype: string




latitude
========
Approximate latitude

A float with max precision
dtype: float64


longitude
=========
Approximate longitude

A float with max precision
dtype: float64


is_location_exact
=================
Whether or not the location is exact or approximate

Is a bool, but represented as 't'/'f'. Read as string and preprocess
dtype: string


accommodates
============
How many people does it accomodate. Should definitely affect price

A count of people, so an int. Max value in the dataset is 16, so don't need much space
dtype: Int8


bathrooms
=========
How many bathrooms. More should increase price

A count of bathrooms, but sometimes they count "half bathrooms". Max value is 10
dtype: float32

bedrooms
========

How many bedrooms. More should increase price

A count of bedrooms. Max value is 101
dtype: Int8



price
=====
The target variable

Is a float, but is prepended with `$`. Read as string and preprocess
dtype: string



minimum_nights
==============
Minimum number of nights. Could impact price

A count of nights. max value is 1100
dtype: Int64


maximum_nights
==============
Maximum number of nights. Could impact price

A count of nights. Max value is 9999
dtype: Int64


instant_bookable
================
Whether or not the location is "instant bookable", an ease-of-use feature. Should make for a more popular rental and better price

Is a bool, but represented as 't'/'f'. Read as string and preprocess
dtype: string



cancellation_policy
===================
What's the cancellation policy? Should affect price

Categorical of policies
dtype: category


require_guest_profile_picture
=============================
If a guest profile picture is required to rent

Is a bool, but represented as 't'/'f'. Read as string and preprocess
dtype: string


require_guest_phone_verification
================================
If a verified phone number is required to rent

Is a bool, but represented as 't'/'f'. Read as string and preprocess
dtype: string