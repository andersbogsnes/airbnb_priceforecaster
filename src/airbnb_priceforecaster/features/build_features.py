from airbnb_priceforecaster.features.amenities import amenities
from airbnb_priceforecaster.features.bed_type import bed_type
from airbnb_priceforecaster.features.beds import beds
from airbnb_priceforecaster.features.cleaning_fee import cleaning_fee
from airbnb_priceforecaster.features.host_acceptance_rate import host_acceptance_rate
from airbnb_priceforecaster.features.host_response_time import host_response_time
from airbnb_priceforecaster.features.host_since import host_since
from airbnb_priceforecaster.features.house_rules_len import house_rules_len
from airbnb_priceforecaster.features.property_type import property_type
from airbnb_priceforecaster.features.room_type import room_type
from airbnb_priceforecaster.features.security_deposit import security_deposit
from airbnb_priceforecaster.features.square_feet import square_feet
from airbnb_priceforecaster.features.neighbourhood import neighbourhood
from airbnb_priceforecaster.features.host_has_profile_pic import host_has_profile_pic
from airbnb_priceforecaster.features.host_identity_verified import host_identity_verified
from airbnb_priceforecaster.features.zipcode import zipcode
from airbnb_priceforecaster.features.guests_included import guests_included
from airbnb_priceforecaster.features.extra_people import extra_people
from ml_tooling.transformers import DFFeatureUnion
from sklearn.pipeline import Pipeline

features = DFFeatureUnion([
    ("amenities", amenities),
    # ("host_since", host_since),
    ("host_response_time", host_response_time),
    ("house_rules_len", house_rules_len),
    ("host_acceptance_rate", host_acceptance_rate),
    ("cleaning_fee", cleaning_fee),
    ("square_feet", square_feet),
    ("security_deposit", security_deposit),
    ("neighbourhood", neighbourhood),
    ("host_has_profile_pic", host_has_profile_pic),
    ("host_identity_verified", host_identity_verified),
    ("zipcode", zipcode),
    ("guests_included", guests_included),
    ("extra_people", extra_people),
    ("bed_type", bed_type),
    ("beds", beds),
    ("property_type", property_type),
    ("room_type", room_type)
])


def get_pipeline(clf):
    return Pipeline([
        ("features", features),
        ("clf", clf)
    ])
