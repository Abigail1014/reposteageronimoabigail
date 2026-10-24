from flask_appbuilder import AppBuilder, Model
from flask_sqlalchemy import SQLAlchemy

# FAB 5.x usa Flask-SQLAlchemy directamente; compartimos el metadata de Model
db = SQLAlchemy(metadata=Model.metadata)
appbuilder = AppBuilder()
