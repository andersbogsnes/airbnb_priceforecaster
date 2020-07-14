house_rules
===========
What rules the guest must follow. Would try to extract some simple rules such as smoking allowed or similar

House rules will be used to extract features from, such as `is_no_smoking` or something indicating a lot of rules
dtype: string

host_since
==========
When started hosting. Hypothesis that being a host for longer affects the price - they might be able to charge a different price.
For our solution, we can set it to 0 or ask.

Is a date - note that date is not a dtype, but we can set read_csv to parse it automatically as a date
dtype: datetime

host_location
=============
Where the host is located. Hypothesis that the host being somewhere else affects the price

Text of where the host is located. Could be used to extract features from
dtype: string


host_response_time
==================
How long does it take for the host to accept/decline an offer. Hypothesis that this could be an indicator of "seriousness" which could affect the price

Categorical with 4 levels
dtype: category

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


host_has_profile_pic
====================
Does the host have a profile picture? Hypothesis that this could increase confidence and thus price

Is a bool, but represented as 't'/'f'. Read as string and preprocess
dtype: string

host_identity_verified
======================
Is the host verified. Hypothesis that this increases confidence and thus price

Is a bool, but represented as 't'/'f'. Read as string and preprocess
dtype: string


neighbourhood
=============
The area which the host writes.

Is a categorical of each neighbourhood
dtype: category


zipcode
=======
Zipcode (postnr) of the location

It's a common pitfall to convert to a number, but there is a possibility of a leading zero. This is very rare and only applies to old zipcodes and some military installations. [reference](https://da.wikipedia.org/wiki/Postnumre_i_Danmark)

To be certain, this should either be a categorical or a string, but an int should be OK for this usecase.

In this case, we are getting errors, since some of the zipcodes are missing. In addition, some of the zipcodes are not numbers, such as '2400 Kbh NV' or '2100 ø'. These need to be cleaned up as well. We need to import it as str to begin with
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


property_type
=============
What kind of property it is. House/Apartment/Room etc. Should definitely affect price

Categorical with a number of rare categories
dtype: category


room_type
=========
What kind of room - Private room / shared room / entire apt etc. Should definitely affect price

Categorical
dtype: category


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


beds
====
How many beds. More should increase price

A count of beds. Max value is 25
dtype: Int8


bed_type
========
What type of bed is available. Better bed should increase price

Type of bed
dtype: category


amenities
=========
Different types of amenities available. Should affect price

A set of amenities. Read as string and preprocess
dtype: string

square_feet
===========
Size of rental. Should affect price

Area in whole feet. Potentially very large
dtype: Int64


price
=====
The target variable

Is a float, but is prepended with `$`. Read as string and preprocess
dtype: string


security_deposit
================
What's the security deposit. Might be related to the price

Is a float, but is prepended with `$`. Read as string and preprocess
dtype: string

cleaning_fee
============
What's the cleaning fee. Affects price directly

Is a float, but is prepended with `$`. Read as string and preprocess
dtype: string

guests_included
===============
How many guests are included in the price. Directly impacts price

A count of guests. Max value is 16
dtype: Int8


extra_people
============
How much more for extra people. Directly impacts price

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