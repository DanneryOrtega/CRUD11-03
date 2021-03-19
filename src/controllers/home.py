from flask import render_template
from src import app
import src.config.globals as globals
# from src.config.db import createDB
# from os import path

# CONEXION_PATH = path.abspath('src/config/conexion.json')

@app.route('/')
def index():
    # if path.exists(CONEXION_PATH):
    #     createDB()
    # elif globals.DB == False:
    if globals.DB == False:
        return render_template('instalacion.html')
    
    return render_template('index.html')



