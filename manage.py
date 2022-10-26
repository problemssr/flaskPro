import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

env = os.environ.get("FLASK_ENV") or 'default'

# 2.在init模块中
app = create_app(env)

# 1.使用Manager启动  python manage.py runserver
manager = Manager(app=app)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
