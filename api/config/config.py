#application configuration according to the enviroment the application is running on
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#production environment
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = '' #database configuration
    DEBUG = True

#development environment
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = '' #database configuration
    SQLALCHEMY_ECHO = False

#testing environment
class TestingConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = '' #database configuration
    SQLALCHEMY_ECHO = False