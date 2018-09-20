import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import create_app, db
from config import Config

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

# @manager.command
# def recreate_db():
#     """
#     Recreates a local database. You probably should not use this on
#     production.
#     """
#     db.drop_all()
#     db.create_all()
#     db.session.commit()

if __name__ == '__main__':
    manager.run()
