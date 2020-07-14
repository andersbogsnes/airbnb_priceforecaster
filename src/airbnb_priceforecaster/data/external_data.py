import json

import httpx
import asyncio
import pandas as pd
from airbnb_priceforecaster import EXTERNAL_DATA_PATH

url = r"https://dawa.aws.dk/postnumre/reverse"


async def get_zipcode(series, client):
    await asyncio.sleep(0.1)
    resp = await client.get(url, params={"x": series["longitude"], "y": series["latitude"]})
    if resp.status_code == 200:
        return resp.json()["nr"]
    if resp.is_error:
        raise ValueError(resp.text)


async def get_all_zipcodes(lats_longs):
    async with httpx.AsyncClient(timeout=httpx.Timeout(25)) as client:
        tasks = []
        for lat_lon in lats_longs:
            tasks.append(get_zipcode(lat_lon, client))
        return await asyncio.gather(*tasks)


def get_missing_zip_codes(df: pd.DataFrame):
    cache = EXTERNAL_DATA_PATH / "dawa" / "zipcodes.json"
    cache.parent.mkdir(exist_ok=True, parents=True)
    cached_data = {}
    if cache.exists():
        cached_data = json.loads(cache.read_text())

    missing_lat_longs = df.loc[df.zip_code.isna(),
                               ["latitude", "longitude"]].to_dict(orient="records")

    missing_lat_longs = [
        lat_long for lat_long in missing_lat_longs
        if (lat_long["latitude"], lat_long["longitude"]) not in cached_data
    ]

    if missing_lat_longs:
        results = asyncio.run(get_all_zipcodes(missing_lat_longs))

        for result, lat_long in zip(results, missing_lat_longs):
            cached_data[(lat_long["latitude"], lat_long["longitude"])] = result

        cache.write_text(json.dumps(cached_data))

    return cached_data
