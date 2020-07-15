"""
host_since
==========
When started hosting. Hypothesis that being a host for longer affects the price - they might be able to charge a different price.
For our solution, we can set it to 0 or ask.

Is a date - note that date is not a dtype, but we can set read_csv to parse it automatically as a date
dtype: datetime
"""
from ml_tooling.transformers import Select, DateEncoder
from sklearn.pipeline import Pipeline

host_since = Pipeline([
    ("select", Select("host_since")),
    ("date_encoder", DateEncoder())
])