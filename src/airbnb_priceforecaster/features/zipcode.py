"""
zipcode
=======
Zipcode (postnr) of the location

It's a common pitfall to convert to a number, but there is a possibility of a leading zero. This is very rare and only applies to old zipcodes and some military installations. [reference](https://da.wikipedia.org/wiki/Postnumre_i_Danmark)

To be certain, this should either be a categorical or a string, but an int should be OK for this usecase.

In this case, we are getting errors, since some of the zipcodes are missing. In addition, some of the zipcodes are not numbers, such as '2400 Kbh NV' or '2100 ø'. These need to be cleaned up as well. We need to import it as str to begin with
dtype: string
"""

from ml_tooling.transformers import Select
from sklearn.pipeline import Pipeline

zipcode = Pipeline([
    ("select", Select("zipcode"))
])

