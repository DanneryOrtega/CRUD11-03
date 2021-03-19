#from src.config.globals as globals
import src.config.globals as globals
#from src.config.db import DB

class ProductosModel():

    def productos(self):
        cursor = globals.DB.cursor()

        cursor.execute('SELECT * FROM productos')

        productos = cursor.fetchall()

        cursor.close()

        return productos

    def sacar_producto(self, id):
        cursor = globals.DB.cursor()

        cursor.execute('SELECT * FROM productos WHERE id=?',(id,))

        producto = cursor.fetchone()

        cursor.close()

        return producto

    
    def crear(self, data):
        cursor = globals.DB.cursor()
        #print(databproductos)
        cursor.execute('insert into productos(nombre, descripcion, precio_venta, precio_compra, ganancia, estado) values(?,?,?,?,?,?)',(data['nombre'], data['descripcion'], data['precio_vta'], data['precio_compra'], data['ganancia'], data['estado'],))
        
        cursor.close()



    def editar(self, data):
        cursor = globals.DB.cursor()
        print(data)
        cursor.execute('UPDATE productos SET nombre=?, descripcion=?, precio_venta=?, precio_compra=?, ganancia=?, estado=? where id=?',(data['nombre'], data['descripcion'], data['precio_vta'], data['precio_compra'], data['ganancia'], data['estado'], data['id'],))
        
        cursor.close()