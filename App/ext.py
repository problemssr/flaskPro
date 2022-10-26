from flask_mail import Mail
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()


def init_ext(app):
    # 懒加载：调用时才加载
    db.init_app(app)
    migrate.init_app(app, db)
    Session(app)
    mail.init_app(app)
