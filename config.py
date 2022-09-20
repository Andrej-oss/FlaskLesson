class Config:
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/admin_db'
    SECRET_KEY = 'my super secret  keyyy:)'


class ProdConfig(Config):
    pass
