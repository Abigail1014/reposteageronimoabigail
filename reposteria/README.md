# Repostería – Taller de Aplicaciones en Internet

Aplicación web de inventario para una repostería, hecha con **Flask AppBuilder**
(plantilla generada con `flask fab create-app`) y **MySQL** (XAMPP/WAMP).

Las pantallas de listar, agregar, editar, ver, eliminar y buscar se generan
automáticamente a partir de los modelos y las vistas.

## Módulos

| Módulo (menú *Inventario*) | Tabla | Campos |
|---|---|---|
| Módulo Categorías | `categorias` | id, nombre (único), descripcion, activo |
| Módulo Ingredientes | `ingredientes` | id, nombre (único), categoria_id (FK), cantidad, unidad_medida, costo_unitario, stock_minimo, fecha_vencimiento, activo |

Relación: **una categoría tiene muchos ingredientes** (`back_populates`).

## Estructura

```
reposteria/
├── app/
│   ├── __init__.py      # create_app(): inicializa FAB, modelos y vistas
│   ├── extensions.py    # db (Flask-SQLAlchemy) y appbuilder
│   ├── models.py        # Categoria e Ingrediente
│   ├── views.py         # CategoriaView, IngredienteView y registro en el menú
│   ├── templates/       # 404.html
│   └── translations/    # traducciones (español incluido)
├── config.py            # conexión a la base de datos y configuración
├── init_db.py           # crea las tablas a partir de los modelos
├── run.py               # levanta el servidor
├── requirements.txt
└── .gitignore
```

## Cómo ejecutarlo (Windows, Command Prompt)

1. **Iniciar Apache y MySQL** desde el panel de XAMPP.
2. **Crear la base de datos vacía** `reposteria_db` en <http://localhost/phpmyadmin>
   (pestaña *Nueva*, cotejamiento `utf8mb4_general_ci`) o con SQL:
   `CREATE DATABASE reposteria_db;`
3. **Entorno virtual e instalación de dependencias** (Python 3.12 – 3.14):
   ```bat
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. **Revisar `config.py`**. Por defecto usa `root` sin contraseña en el puerto 3306:
   ```python
   "mysql+pymysql://root:@localhost:3306/reposteria_db?charset=utf8mb4"
   ```
   Si tu MySQL usa otro puerto (ej. 3307) o tiene contraseña, cámbialo ahí.
   También puedes definir la variable de entorno `DATABASE_URL`.
5. **Crear las tablas**:
   ```bat
   python init_db.py
   ```
6. **Crear el usuario administrador**:
   ```bat
   flask --app app fab create-admin
   ```
   (en clase se usó `admin` para usuario, nombre, correo y contraseña).
7. **Levantar el servidor**:
   ```bat
   python run.py
   ```
   Abrir <http://localhost:8080> e iniciar sesión.

Para detener el servidor: `Ctrl + C`.

## Notas

- `config.py` incluye una `SECRET_KEY` de 20 caracteres de ejemplo. **Cámbiala**
  o define la variable de entorno `SECRET_KEY` antes de publicar un proyecto real.
- Si cambias los modelos (agregar columnas) con tablas ya creadas, `db.create_all()`
  **no** las modifica: hay que borrar la tabla/base de datos y volver a ejecutar
  `python init_db.py`, o usar migraciones (tema de la próxima clase).
- Los errores `Warning` en rojo al iniciar son avisos de versión, no errores.

## Subir a GitHub

```bash
git init
git add .
git commit -m "Taller: modulos Categorias e Ingredientes con Flask AppBuilder"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main
```
