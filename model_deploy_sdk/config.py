import os

class Config():
    @staticmethod
    def get_home_path():
        return os.path.dirname(os.getcwd())

    @staticmethod
    def get_path_model_store(prod_env=False):
        home_path = Config.get_home_path()
        if prod_env is True:
            return os.path.join(home_path, "model_store/production")
        
        return os.path.join(home_path, "model_store/staging")
