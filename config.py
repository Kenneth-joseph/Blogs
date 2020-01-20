import os

class Config:

    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:kent123kk@localhost/blog'
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevConfig(Config):

    DEBUG= True
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:kent123kk@localhost/blog'
    SECRET_KEY='ec8931e771065c37db55e08205aba565'
    ENV='development'


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")


config_options={
    'development':DevConfig,
    'production':ProdConfig
}