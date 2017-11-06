import os


class Config:
    '''
    General configurations
    '''

class ProdConfig(Config):
    '''
    production configuration child class

    args:
        config: the parent class
    '''
    pass
# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://chutha:chutha@localhost/watchlist_test'
#

class DevConfig(Config):
    '''
    Development configuration child class

    args:
        config: the parent class
    '''
    SQLALCHEMY_DATABASE_URI='sqlite:///database_sports.db'
    # SQLALCHEMY_DATABASE_URI='sqlite:////home/chutha/Documents/WORK/python/api-with-spiders/database_epl.db'



    DEBUG = True

config_options={
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}