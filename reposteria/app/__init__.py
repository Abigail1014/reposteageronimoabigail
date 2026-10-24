from flask import Flask

from .extensions import appbuilder, db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config")
    db.init_app(app)
    with app.app_context():
        appbuilder.init_app(app, db.session)
        # Importar los modelos ANTES de create_all para que se creen las tablas
        from . import models  # noqa: F401
        db.create_all()
        # Registering the views and APIs
        from . import views  # noqa: F401
    return app


app = create_app()
