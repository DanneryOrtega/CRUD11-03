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
        cursor.execute('insert into productos(nombre, descripcion, precio_venta, precio_compra, ganancia, estado) values(?,?,?,?,?,?)',(data['nombre'], data['descripcion'], data['precio_vta'], data['precio_compra'], data['ganancia'], data['estado'],))
        cursor.close()



    def editar(self, data):
        cursor = DB.cursor()
        #cursor.execute('UPDATE productos SET nombre=?, descripcion=?, precio_venta=?, precio_compra=?, ganancia=?, estado=? where id=?',(data['nombre'], data['descripcion'], data['precio_vta'], data['precio_compra'], data['ganancia'], data['estado'],))
        cursor.execute('select * from productos where id=?', (data['id'],))

        productos = cursor.fetchall()
        print(productos)
        
        cursor.close()