"""Crea (si no existen) las tablas de la base de datos a partir de los modelos.

Uso:  python init_db.py
"""
from app import app
from app.extensions import db
from app.models import Categoria, Ingrediente  # noqa: F401  (registra los modelos)

with app.app_context():
    db.create_all()
    print("Tablas creadas correctamente:")
    for tabla in db.metadata.tables:
        print(f"  - {tabla}")
