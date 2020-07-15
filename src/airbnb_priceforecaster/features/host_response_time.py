"""
host_response_time
==================
How long does it take for the host to accept/decline an offer. Hypothesis that this could be an indicator of "seriousness" which could affect the price

Categorical with 4 levels
dtype: category
"""
from ml_tooling.transformers import Select, FillNA, ToCategorical
from sklearn.pipeline import Pipeline

host_response_time = Pipeline([
    ("select", Select("host_response_time")),
    ("fill_na", FillNA("unknown", indicate_nan=True)),
    ("categorical", ToCategorical())
])