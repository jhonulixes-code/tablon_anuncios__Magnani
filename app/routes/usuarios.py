from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Usuario
from app import db

usuario_bp = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@usuario_bp.route('/')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@usuario_bp.route('/crear', methods=['POST'])
def crear_usuario():
    nombre = request.form['nombre']
    email = request.form['email']
    password = request.form['password']
    
    nuevo = Usuario(nombre=nombre, email=email, password=password)
    db.session.add(nuevo)
    db.session.commit()
    flash('Usuario registrado con éxito.', 'success')
    return redirect(url_for('usuarios.listar_usuarios'))

@usuario_bp.route('/eliminar/<int:id>')
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado.', 'info')
    return redirect(url_for('usuarios.listar_usuarios'))