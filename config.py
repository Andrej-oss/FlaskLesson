class Config:
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/owners_pets'


class ProdConfig(Config):
    pass
