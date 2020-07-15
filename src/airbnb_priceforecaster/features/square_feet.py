"""
square_feet
===========
Size of rental. Should affect price

Area in whole feet. Potentially very large
dtype: Int64
"""
from ml_tooling.transformers import Select, FillNA
from sklearn.pipeline import Pipeline

square_feet = Pipeline([
    ("select", Select("square_feet")),
    ("fill_na", FillNA(0))
])