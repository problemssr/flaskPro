from django.conf.global_settings import SECRET_KEY
from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_blue


def create_app(env):
    # 2.创建flask对象
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.config['SESSION_TYPE'] = "redis"
    app.config['SESSION_TYPE'] = "redis"
    app.config['MAIL_SERVER'] = "smtp.163.com"
    app.config['MAIL_PORT'] = 25
    app.config['MAIL_USERNAME'] = "excellentChina@163.com"
    app.config['MAIL_PASSWORD'] = "ATFXLEWWVSCNEJPM"
    app.config['MAIL_DEFAULT_SENDER'] = "excellentChina@163.com"

    # 3.初始化配置
    app.config.from_object(envs.get(env))
    # 3.加载扩展库
    init_ext(app)
    # 3.加载路由
    init_blue(app)
    return app
