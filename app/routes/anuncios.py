from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import Anuncio, Categoria, Usuario
from app import db

anuncio_bp = Blueprint('anuncios', __name__, url_prefix='/anuncios')

@anuncio_bp.route('/')
def listar_anuncios():
    anuncios = Anuncio.query.all()
    categorias = Categoria.query.all()
    usuarios = Usuario.query.all()
    return render_template('anuncios.html', anuncios=anuncios, categorias=categorias, usuarios=usuarios)

@anuncio_bp.route('/crear', methods=['POST'])
def crear_anuncio():
    titulo = request.form['titulo']
    descripcion = request.form['descripcion']
    usuario_id = request.form['usuario_id']
    categoria_id = request.form['categoria_id']
    
    nuevo = Anuncio(titulo=titulo, descripcion=descripcion, usuario_id=usuario_id, categoria_id=categoria_id)
    db.session.add(nuevo)
    db.session.commit()
    flash('Anuncio publicado con éxito.', 'success')
    return redirect(url_for('anuncios.listar_anuncios'))

@anuncio_bp.route('/eliminar/<int:id>')
def eliminar_anuncio(id):
    anuncio = Anuncio.query.get_or_404(id)
    db.session.delete(anuncio)
    db.session.commit()
    flash('Anuncio eliminado.', 'info')
    return redirect(url_for('anuncios.listar_anuncios'))