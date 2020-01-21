from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Comment,Blog
from  flask_migrate import Migrate, MigrateCommand

#manage.shell


# Creating app instance
app = create_app('production')

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(db=db,app= app, User = User ,Comment=Comment, Blog=Blog)
if __name__== '__main__':
    manager.run()
    db.create_all()