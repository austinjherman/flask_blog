
# Let python know where the folder is
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import manager, server, and app
from flask.ext.script import Manager, Server
from flask.ext.migrate import MigrateCommand
from flask_blog import app

# Instantiate manager
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Set up the server, using manager and options
manager.add_command('runserver', Server(
    use_debugger = True,
    use_reloader = True,
    )
)

# Run the server
if __name__ == '__main__':
    manager.run()


