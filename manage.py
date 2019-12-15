from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from api import app, db

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_pyfile('config.py')


# Migrate
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

