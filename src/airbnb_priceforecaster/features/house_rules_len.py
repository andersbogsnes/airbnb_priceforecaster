"""
house_rules
===========
What rules the guest must follow. Would try to extract some simple rules such as smoking allowed
or similar

House rules will be used to extract features from, such as `is_no_smoking` or something
indicating a lot of rules
dtype: string
"""
from ml_tooling.transformers import Select, FillNA
from sklearn.pipeline import Pipeline

house_rules_len = Pipeline([
    ("select", Select("house_rules_len")),
    ("fill_na", FillNA(0))
])
