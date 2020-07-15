"""
extra_people
============
How much more for extra people. Directly impacts price

Is a float, but is prepended with `$`. Read as string and preprocess
dtype: string
"""

from ml_tooling.transformers import Select
from sklearn.pipeline import Pipeline

extra_people = Pipeline([
    ("select", Select("extra_people")),
])