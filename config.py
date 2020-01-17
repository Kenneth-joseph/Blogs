class Config:

    pass



class DevConfig(Config):

    DEBUG= True


class ProdConfig(Config):

    DEBUG=False


app_config={
    'development':DevConfig,
    'production':ProdConfig
}