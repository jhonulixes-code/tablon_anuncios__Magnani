from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Categoria
from app import db

categoria_bp = Blueprint('categorias', __name__, url_prefix='/categorias')

@categoria_bp.route('/')
def listar_categorias():
    categorias = Categoria.query.all()
    return render_template('categorias.html', categorias=categorias)

@categoria_bp.route('/crear', methods=['POST'])
def crear_categoria():
    nombre = request.form['nombre']
    nueva = Categoria(nombre=nombre)
    db.session.add(nueva)
    db.session.commit()
    flash('Categoría agregada con éxito.', 'success')
    return redirect(url_for('categorias.listar_categorias'))

@categoria_bp.route('/eliminar/<int:id>')
def eliminar_categoria(id):
    cat = Categoria.query.get_or_404(id)
    db.session.delete(cat)
    db.session.commit()
    flash('Categoría eliminada.', 'info')
    return redirect(url_for('categorias.listar_categorias'))