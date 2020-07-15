"""
host_has_profile_pic
====================
Does the host have a profile picture? Hypothesis that this could increase confidence and thus price

Is a bool, but represented as 't'/'f'. Read as string and preprocess
dtype: string
"""
from ml_tooling.transformers import Select
from sklearn.pipeline import Pipeline

host_has_profile_pic = Pipeline([
    ("select", Select("host_has_profile_pic"))
])
