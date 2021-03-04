from src.config.db import DB

class ProductosModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('select * from productos')

        productos = cursor.fetchall()
        
        cursor.close()

        return productos
    
    def crear(self, data):
        cursor = DB.cursor()
        #print(databproductos)
        cursor.execute('insert into productos(nombre, descripcion, precio_venta, precio_compra, estado) values(?,?,?,?,?)',(data['nombre'], data['descripcion'], data['precio_vta'], data['precio_compra'], data['estado'],))
        
        cursor.close()