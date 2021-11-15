from app.instance.config import GOOGLE_MAPS_API_KEY


class Config:
    '''
    General configuration parent class
    '''
    GOOGLE_MAPS_API_KEY=""
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True