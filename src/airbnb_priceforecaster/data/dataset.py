import tempfile
from typing import Tuple
import pandas as pd
from ml_tooling.data import FileDataset
from ml_tooling.utils import DataType
from urllib.request import urlretrieve
from airbnb_priceforecaster import RAW_DATA_PATH, PROCESSED_DATA_PATH
from airbnb_priceforecaster.data.preprocess import preprocess_data, MAPPINGS
import gzip


class AirBnBDataset(FileDataset):
    def __init__(self, year: int, month: int, day: int):
        self.raw_data_path = RAW_DATA_PATH / f"listings_{year}_{month:02}_{day:02}.csv"

        super().__init__(PROCESSED_DATA_PATH / "listings.parquet")

        self.year = year
        self.month = month
        self.day = day

    def download_data(self):
        if self.raw_data_path.exists():
            print("Output data already exists - skipping...")
            return
        url = f"http://data.insideairbnb.com/denmark/hovedstaden/copenhagen/" \
              f"{self.year}-{self.month:02}-{self.day:02}/data/listings.csv.gz"
        self.raw_data_path.parent.mkdir(exist_ok=True, parents=True)
        print(f"Getting data from {url}...")
        with tempfile.NamedTemporaryFile(mode="wb") as temp:
            urlretrieve(url, temp.name)
            print("Data downloaded, unzipping...")
            with gzip.open(temp.name, "rt") as f:
                self.raw_data_path.write_text(f.read())
        print("Done fetching data!")

    def preprocess_data(self, force=False):
        if self.file_path.exists() and not force:
            print("Data is already preprocessed - skipping...")

        print("Preprocessing data...")
        df = pd.read_csv(self.raw_data_path, dtype=MAPPINGS, usecols=MAPPINGS.keys())
        df = preprocess_data(df)
        self.file_path.parent.mkdir(exist_ok=True, parents=True)
        df.to_parquet(self.file_path)
        print(f"Prepocessed data saved - {self.file_path}")

    def load_training_data(self) -> Tuple[pd.DataFrame, DataType]:
        self.download_data()
        self.preprocess_data()
        df = pd.read_parquet(self.file_path)
        return df.drop(columns="price"), df.price

    def load_prediction_data(self, idx) -> pd.DataFrame:
        return pd.read_csv(self.file_path).iloc[idx].drop(columns="is_canceled")
