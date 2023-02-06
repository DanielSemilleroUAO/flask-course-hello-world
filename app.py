from flask import Flask, request, render_template

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
