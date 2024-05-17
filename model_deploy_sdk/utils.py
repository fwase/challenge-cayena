import pandas as pd
import os
import sys
from config import Config

def get_dataset(dataset_name):
    home_path = Config.get_home_path()
    dataset_path = os.path.join(home_path, f"datasets/{dataset_name}.csv")

    return pd.read_csv(dataset_path)
