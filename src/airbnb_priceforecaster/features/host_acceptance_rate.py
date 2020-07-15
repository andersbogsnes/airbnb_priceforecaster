from ml_tooling.transformers import Select, FillNA
from sklearn.pipeline import Pipeline

host_acceptance_rate = Pipeline([
    ("select", Select("host_acceptance_rate")),
    ("fill_na", FillNA(127, indicate_nan=True)),
])