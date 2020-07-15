"""
cleaning_fee
============
What's the cleaning fee. Affects price directly

Is a float, but is prepended with `$`. Read as string and preprocess
dtype: string
"""

from ml_tooling.transformers import Select, FillNA
from sklearn.pipeline import Pipeline

cleaning_fee = Pipeline([
    ("select", Select("cleaning_fee")),
    ("fill_na", FillNA(0, indicate_nan=True))
])