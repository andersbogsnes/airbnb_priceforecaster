import pandas as pd
import numpy as np
from airbnb_priceforecaster.data.external_data import get_missing_zip_codes

MAPPINGS = {
    "house_rules": "string",
    "host_since": "string",
    "host_location": "string",
    "host_response_time": "category",
    "host_acceptance_rate": "string",
    "host_neighbourhood": "category",
    "host_listings_count": "Int64",
    "host_total_listings_count": "Int64",
    "host_has_profile_pic": "string",
    "host_identity_verified": "string",
    "neighbourhood": "category",
    "zipcode": "string",
    "latitude": "float64",
    "longitude": "float64",
    "property_type": "category",
    "room_type": "category",
    "accommodates": "Int8",
    "bathrooms": "float32",
    "bedrooms": "Int8",
    "beds": "Int8",
    "bed_type": "category",
    "amenities": "string",
    "square_feet": "Int64",
    "price": "string",
    "security_deposit": "string",
    "cleaning_fee": "string",
    "guests_included": "Int8",
    "extra_people": "string",
    "minimum_nights": "Int64",
    "maximum_nights": "Int64",
    "instant_bookable": "string",
    "cancellation_policy": "category",
    "require_guest_profile_picture": "string",
    "require_guest_phone_verification": "string"
}


def convert_price(series):
    return pd.to_numeric(series.str.replace("$", "").str.replace(",", ""),
                         errors="coerce").astype("float64")


def convert_percent(series):
    return pd.to_numeric(series.str.replace("%", ""), errors="coerce").astype("Int8")


def convert_bool(series):
    return series.map({"t": True, "f": False}).astype("bool")


def convert_datetime(series, format="%Y-%m-%d"):
    return pd.to_datetime(series, format=format)


def one_hot_encode_amenities(df: pd.DataFrame):
    return (
        df.amenities
            .str.slice(start=1, stop=-1)  # Remove the "{}" at the front and back
            .str.replace('"', '')  # Remove quoting of multi-word amenities
            .str.split(",")
            .apply(lambda x: pd.Series(index=set(x), data=1))  # For each row, make a Series of
            # 1s. `apply` will concatenate
            # the result
            .fillna(0)
            .astype("bool")
            .rename(columns=lambda x: "_".join(x.split(" ")).lower())  # Rename all columns to
        # lowercase snake_case
    )


def convert_amenities(df: pd.DataFrame) -> pd.DataFrame:
    one_hot_df = one_hot_encode_amenities(df)
    return df.join(one_hot_df).drop(columns="amenities")


def convert_zipcode(df: pd.DataFrame) -> pd.DataFrame:
    df.loc[df.zipcode.str.len() > 4, "zipcode"] = np.nan
    df = get_missing_zip_codes(df)
    df["zipcode"] = df["zipcode"].astype("int16")
    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df
            .assign(
            host_acceptance_rate=lambda x: convert_percent(x.host_acceptance_rate),
            host_has_profile_pic=lambda x: convert_bool(x.host_has_profile_pic),
            host_identity_verified=lambda x: convert_bool(x.host_identity_verified),
            price=lambda x: convert_price(x.price),
            security_deposit=lambda x: convert_price(x.security_deposit),
            cleaning_fee=lambda x: convert_price(x.cleaning_fee),
            extra_people=lambda x: convert_price(x.extra_people),
            instant_bookable=lambda x: convert_bool(x.instant_bookable),
            require_guest_profile_picture=lambda x: convert_bool(x.require_guest_profile_picture),
            require_guest_phone_verification=lambda x: convert_bool(
                x.require_guest_phone_verification),
            house_rules_len=lambda x: x["house_rules"].str.len(),
            host_since=lambda x: convert_datetime(x["host_since"])
        )
            .pipe(convert_amenities)
            .pipe(convert_zipcode)
    )
