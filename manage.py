from app import create_app,db
from flask_script import Manager,Server
from flask_sqlalchemy import SQLAlchemy
from app.models import Team
from flask_migrate import Migrate,MigrateCommand


# creating app is=nstances
app=create_app('production')
migrate=Migrate(app,db)
manager=Manager(app)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,Team=Team)


if __name__=='__main__':
    manager.run()
