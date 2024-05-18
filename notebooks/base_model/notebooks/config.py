import os

def get_home_path():
    return os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))

def get_current_model_path():
    return os.path.dirname(os.getcwd())
