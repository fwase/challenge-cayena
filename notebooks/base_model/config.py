import os

def get_home_path():
    return os.path.dirname(os.path.dirname(os.getcwd()))

def get_abc():
    return os.path.join(get_home_path(), 'model_deploy_sdk')