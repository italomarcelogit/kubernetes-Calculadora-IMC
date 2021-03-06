from flask import render_template, request, redirect, json
from app import app
from app.mongo import MongoAPI
import socket

# data = {
#         "url": "mongodb://localhost:50027/admin",
#         "database": "flaskDB",
#         "collection": "IMC",
#     }
data = {
    "url": "mongodb://mongodb-service:27017/admin",
    "database": "flaskDB",
    "collection": "IMC",
}
meuhost = socket.gethostname()

@app.route('/')
@app.route('/index')
def index():

    entries = MongoAPI(data).read()
    return render_template('index.html',
                           entries=entries, 
                           meuhost=meuhost)


@app.route('/add', methods=['POST'])
def add():
    form = request.form
    fn = form.get('Nome')
    fp = float(form.get('Peso'))
    fa = float(form.get('Altura'))
    imc = round(fp/(fa*fa), 2)
    if imc < 18.6:
        cl = 'MAGREZA'
    elif imc < 25:
        cl = 'NORMAL'
    elif imc < 30:
        cl = 'SOBREPESO'
    elif imc < 40:
        cl = 'OBESIDADE'
    else:
        cl = 'OBESIDADE GRAVE'

    if fn and fp and fa:
        person = {'Nome': fn,
                  'Peso': fp,
                  'Altura': fa,
                  'Imc': imc,
                  'Classificacao': cl}
        MongoAPI(data).insertOne(person)

    entries = MongoAPI(data).read()

    return render_template('index.html', entries=entries, 
                           meuhost=meuhost)


@app.route('/action/<updel>/<person>', methods=['GET'])
def get_person(updel=None, person=None):
    entries = MongoAPI(data).readOne(str(person))
    if str(updel) == 'update':
        return render_template('update.html', entries=entries, 
                           meuhost=meuhost)
    elif str(updel) == 'delete':
        return render_template('delete.html', entries=entries, 
                           meuhost=meuhost)
    else:
        entries = MongoAPI(data).read()
        return render_template('index.html', entries=entries, 
                           meuhost=meuhost)


@app.route('/save', methods=['POST'])
def save():
    form = request.form
    oid = form.get('oid')
    fn = form.get('Nome')
    fp = float(form.get('Peso'))
    fa = float(form.get('Altura'))
    imc = round(fp / (fa * fa), 2)
    if imc < 18.6:
        cl = 'MAGREZA'
    elif imc < 25:
        cl = 'NORMAL'
    elif imc < 30:
        cl = 'SOBREPESO'
    elif imc < 40:
        cl = 'OBESIDADE'
    else:
        cl = 'OBESIDADE GRAVE'

    if fn and fp and fa:
        person = {'Nome': fn,
                  'Peso': fp,
                  'Altura': fa,
                  'Imc': imc,
                  'Classificacao': cl}
        MongoAPI(data).updateOne(oid, person)
    entries = MongoAPI(data).read()
    return render_template('index.html', entries=entries, 
                           meuhost=meuhost)


@app.route('/delete', methods=['POST'])
def delete():
    form = request.form
    oid = form.get('oid')
    if oid:
        MongoAPI(data).deleteOne(oid)
    entries = MongoAPI(data).read()
    return render_template('index.html', entries=entries, 
                           meuhost=meuhost)