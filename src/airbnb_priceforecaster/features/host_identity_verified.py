"""
host_identity_verified
======================
Is the host verified. Hypothesis that this increases confidence and thus price

Is a bool, but represented as 't'/'f'. Read as string and preprocess
dtype: string
"""

from ml_tooling.transformers import Select
from sklearn.pipeline import Pipeline

host_identity_verified = Pipeline([
    ("select", Select("host_identity_verified"))
])
