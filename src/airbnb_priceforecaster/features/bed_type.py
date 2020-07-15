"""
bed_type
========
What type of bed is available. Better bed should increase price

Type of bed
dtype: category
"""

from ml_tooling.transformers import Select, ToCategorical
from sklearn.pipeline import Pipeline

bed_type = Pipeline([
    ("select", Select("bed_type")),
    ("categorical", ToCategorical())
])