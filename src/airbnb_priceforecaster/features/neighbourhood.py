"""
neighbourhood
=============
The area which the host writes.

Is a categorical of each neighbourhood
dtype: category
"""
from ml_tooling.transformers import Select, ToCategorical
from sklearn.pipeline import Pipeline

neighbourhood = Pipeline([
    ("select", Select("neighbourhood")),
    ("categorical", ToCategorical())
])
