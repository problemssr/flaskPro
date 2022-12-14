def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    TESTING = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "ROCK"
    SESSION_TYPE = "redis"
    SESSION_COOKIE_SECURE = True


class DevelopConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": 'mysql',
        "DRIVER": 'pymysql',
        "USER": 'root',
        "PASSWORD": '123456',
        "HOST": '127.0.0.1',
        "PORT": 3306,
        "NAME": "flask_use"
    }


class TestingConfig(Config):
    TESTING = True
    dbinfo = {
        "ENGINE": 'mysql',
        "DRIVER": 'pymysql',
        "USER": 'root',
        "PASSWORD": '123456',
        "HOST": '127.0.0.1',
        "PORT": 3306,
        "NAME": "flask_use"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):
    dbinfo = {
        "ENGINE": 'mysql',
        "DRIVER": 'pymysql',
        "USER": 'root',
        "PASSWORD": '123456',
        "HOST": '127.0.0.1',
        "PORT": 3306,
        "NAME": "flask_use"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": 'mysql',
        "DRIVER": 'pymysql',
        "USER": 'root',
        "PASSWORD": '123456',
        "HOST": '127.0.0.1',
        "PORT": 3306,
        "NAME": "flask_use"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "dafault": DevelopConfig
}
