import pandas as pd
import os
from .config import Config

def get_dataset(dataset_name):
    home_path = Config.get_home_path()
    dataset_path = os.path.join(home_path, f"datasets/{dataset_name}.csv")

    return pd.read_csv(dataset_path)

def load_test_dataset():
    path_file =  os.path.join(Config.get_current_data_model(), 'data/test_dataset.csv')
    return pd.read_csv(path_file)

def load_train_dataset():
    path_file =  os.path.join(Config.get_current_data_model(), 'data/train_dataset.csv')
    return pd.read_csv(path_file)

def load_validation_dataset():
    path_file =  os.path.join(Config.get_current_data_model(), 'data/validation_dataset.csv')
    return pd.read_csv(path_file)

def create_new_model(model_name):
    return None