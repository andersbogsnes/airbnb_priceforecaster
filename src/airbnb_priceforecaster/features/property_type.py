"""
property_type
=============
What kind of property it is. House/Apartment/Room etc. Should definitely affect price

Categorical with a number of rare categories
dtype: category
"""

from ml_tooling.transformers import Select, RareFeatureEncoder, ToCategorical
from sklearn.pipeline import Pipeline

property_type = Pipeline([
    ("select", Select("property_type")),
    ("rare_features", RareFeatureEncoder(threshold=50)),
    ("categorical", ToCategorical())
])