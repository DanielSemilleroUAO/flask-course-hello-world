from flask import Flask, request, render_template, url_for
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    app.logger.debug('Mensaje a nivel debug')
    app.logger.info(f'Mensaje a nivel info {request.path}')
    app.logger.warn('Mensaje a nivel warn')
    app.logger.error('Mensaje a nivel error')
    return 'Hola mundo'


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre}'


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es {edad}'


@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return f'Tu nombre es: {nombre}'


@app.route('/mostrar/html/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre_html(nombre):
    return render_template('mostrar.html', nombre=nombre)


@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='Daniel'))


@app.route('/salir')
def salir():
    return abort(404)


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error.html', error=error), 404


@app.route('/api/mostrar/<nombre>')
def mostrar_json(nombre):
    return {
        'nombre': nombre
    }
