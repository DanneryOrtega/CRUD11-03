import mariadb
from os import path
import json
import src.config.globals as globals

CONEXION_PATH = path.abspath('src/config/conexion.json')
SQL_PATH = path.abspath('db.sql')

def instalarDB():
    file_sql = open(SQL_PATH, 'r')
    sql = file_sql.read()

    sqlCommands = sql.split(';')
    
    cursor = globals.DB.cursor()
    
    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except:
            print ("Saltando comando")

    cursor.close()

def createDB():
    if path.exists(CONEXION_PATH):
        file_conexion = open(CONEXION_PATH, 'r')

        config = json.loads(file_conexion.read())

        globals.DB = mariadb.connect(**config)
        globals.DB.autocommit = True
    else:
        globals.DB = False

createDB()

#config = {
#    'host': 'localhost',
#    'port': 3306,
#    'user': 'root',
#    'password': '1234567890',
#    'database': 'flask_mvc'
#}

#try:
#   DB = mariadb.connect(**config)
#    DB.autocommit = True
#except:
#    DB = False
#    print("error al conectarse a la base de datos")