"""
guests_included
===============
How many guests are included in the price. Directly impacts price

A count of guests. Max value is 16
dtype: Int8

"""
from ml_tooling.transformers import Select
from sklearn.pipeline import Pipeline

guests_included = Pipeline([
    ("select", Select("guests_included")),
])