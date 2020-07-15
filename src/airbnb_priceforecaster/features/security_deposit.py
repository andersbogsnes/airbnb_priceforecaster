"""
security_deposit
================
What's the security deposit. Might be related to the price

Is a float, but is prepended with `$`. Read as string and preprocess
dtype: string
"""
from ml_tooling.transformers import Select, FillNA
from sklearn.pipeline import Pipeline

security_deposit = Pipeline([
    ("select", Select("security_deposit")),
    ("fill_na", FillNA(0, indicate_nan=True))
])