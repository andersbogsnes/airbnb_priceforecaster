"""
beds
====
How many beds. More should increase price

A count of beds. Max value is 25
dtype: Int8
"""

from ml_tooling.transformers import Select, FillNA
from sklearn.pipeline import Pipeline

beds = Pipeline([
    ("select", Select("beds")),
    ("fill_na", FillNA(127, indicate_nan=True))
])