from airbnb_priceforecaster.features.host_since import host_since
from ml_tooling.transformers import DFFeatureUnion, Select, FillNA
from airbnb_priceforecaster.features.amenities import amenities
from sklearn.pipeline import Pipeline

host_response_time = Pipeline([
    ("select", Select("host_response_time")),
    ("fill_na", FillNA("unknown", indicate_nan=True))
])

security_deposit = Pipeline([
    ("select", Select("security_deposit")),
    ("fill_na", FillNA(0, indicate_nan=True))
])

house_rules_len = Pipeline([
    ("select", Select("house_rules_len")),
    ("fill_na", FillNA(0))
])

host_acceptance_rate = Pipeline([
    ("select", Select("host_acceptance_rate")),
    ("fill_na", FillNA(9999, indicate_nan=True))
])

cleaning_fee = Pipeline([
    ("select", Select("cleaning_fee")),
    ("fill_na", FillNA(0, indicate_nan=True))
])

features = DFFeatureUnion([
    ("amenities", amenities),
    ("host_since", host_since),
    ("host_response_time", host_response_time),
    ("house_rules_len", house_rules_len),
    ("host_acceptance_rate", host_acceptance_rate),


])
