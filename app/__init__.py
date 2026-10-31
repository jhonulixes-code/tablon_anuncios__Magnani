from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración de seguridad y base de datos
    app.config['SECRET_KEY'] = 'clave_secreta_upea_2026'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_anuncios.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importar y registrar Blueprints (Modularización)
    from app.routes.auth import auth_bp
    from app.routes.usuarios import usuario_bp
    from app.routes.categorias import categoria_bp
    from app.routes.anuncios import anuncio_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(anuncio_bp)

    return app
