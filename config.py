import os

class Config:

  pass  



class DevConfig(Config):

    DEBUG= True
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:kent123kk@localhost/blog'
    SECRET_KEY = 'kent1234567'


class ProdConfig(Config):

    DEBUG=False


config_options={
    'development':DevConfig,
    'production':ProdConfig
}