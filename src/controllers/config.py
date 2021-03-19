from flask import render_template, redirect, request, url_for
from src.config.db import createDB, instalarDB
from src import app
import json

@app.route('/setting', methods=['POST'])
def setting():
    name = request.form.get('Db')
    user = request.form.get('User')
    password = request.form.get('Password')
    server = request.form.get('Host')
    port = request.form.get('Port')

    dbData = {
        'host' : server,
        'port' : int(port),
        'user' : user,
        'password' : password,
        'database' : name,
    }

    file = open('src/config/conexion.json', 'w')
    file.write(json.dumps(dbData))
    file.close()

    createDB()
    instalarDB()

    return redirect(url_for('index'))