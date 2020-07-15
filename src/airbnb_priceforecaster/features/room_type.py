"""
room_type
=========
What kind of room - Private room / shared room / entire apt etc. Should definitely affect price

Categorical
dtype: category
"""

from ml_tooling.transformers import Select, ToCategorical
from sklearn.pipeline import Pipeline

room_type = Pipeline([
    ("select", Select("room_type")),
    ("categorical", ToCategorical())
])