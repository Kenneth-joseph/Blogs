import os

class Config:

  pass  



class DevConfig(Config):

    DEBUG= True
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:kent123kk@localhost/blog'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")


config_options={
    'development':DevConfig,
    'production':ProdConfig
}