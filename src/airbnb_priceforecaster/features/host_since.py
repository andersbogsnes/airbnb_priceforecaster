from ml_tooling.transformers import Select, DateEncoder
from sklearn.pipeline import Pipeline

host_since = Pipeline([
    ("select", Select("host_since")),
    ("date_encoder", DateEncoder())
])