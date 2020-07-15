from typing import List
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import requests

url = "https://dawa.aws.dk/postnumre/reverse"


def get_zipcode(series: pd.Series, client: requests.Session) -> str:
    resp = client.get(url, params={"x": series.longitude, "y": series.latitude})
    if resp.status_code == 200:
        return resp.json()["nr"]
    resp.raise_for_status()


def get_all_zipcodes(lats_longs: pd.DataFrame, n_workers: int = 10) -> List[str]:
    session = requests.Session()
    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        futures = [executor.submit(get_zipcode, lat_long, session) for _, lat_long in
                   lats_longs.iterrows()]
    return [future.result() for future in futures]


def get_missing_zip_codes(df: pd.DataFrame) -> pd.DataFrame:
    missing_lat_longs = df.loc[df.zipcode.isna(), ["latitude", "longitude"]]
    df.loc[df.zipcode.isna(), "zipcode"] = get_all_zipcodes(missing_lat_longs)
    return df
