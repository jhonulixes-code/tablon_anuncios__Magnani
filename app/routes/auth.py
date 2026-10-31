from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        usuario = Usuario.query.filter_by(email=email, password=password).first()
        if usuario:
            session['usuario_id'] = usuario.id
            session['nombre'] = usuario.nombre
            flash('¡Inicio de sesión exitoso!', 'success')
            return redirect(url_for('anuncios.listar_anuncios'))
        else:
            flash('Correo o contraseña incorrectos.', 'danger')
            
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('auth.login'))