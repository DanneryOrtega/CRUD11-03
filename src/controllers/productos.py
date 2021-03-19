from flask import render_template, request, redirect, url_for
from src import app
from src.models.productos import ProductosModel

@app.route('/productos') 
def productos():
    #if request.method == 'GET':
        #if id != 'null': return render_template('productos/editar.html')#id = request.form.get('id')
    #print(id)
    productosModel = ProductosModel()

    productos = productosModel.productos()

    return render_template('productos/index.html', productos = productos)#

@app.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    # Esta funcion me sirve para mostrar el formulario de creacion
    # Y tambien me sirve para crear un nuevo producto
    # Estos pasos se identifican con los metodos
    if request.method == 'GET':
        # Mostramos el formulario de creación
        return render_template('productos/crear.html')
   
    #Aca es la creación del producto
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio_vta = request.form.get('precio_vta')
    precio_compra = request.form.get('precio_compra')
    ganancia = request.form.get('ganancia')
    estado = True if request.form.get('estado') == 'a' else False

    databproductos = {
        'nombre' : nombre,
        'descripcion' : descripcion,
        'precio_vta' : float(precio_vta),
        'precio_compra' : float(precio_compra),
        'ganancia' : float(ganancia),
        'estado' : estado
    }
    productosModel = ProductosModel()
    productosModel.crear(databproductos)
    return redirect(url_for('productos'))

@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):

    productosModel = ProductosModel()
    print(id)

    if request.method == 'GET':
        print('cualquiercosa')
    else:
        print('otracualquiercosa')
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio_vta = request.form.get('precio_vta')
    precio_compra = request.form.get('precio_compra')
    ganancia = request.form.get('ganancia')
    estado = True if request.form.get('estado') == 'a' else False

    databproductos = {
        'id' : id,
        'nombre' : nombre,
        'descripcion' : descripcion,
        'precio_vta' : float(precio_vta),
        'precio_compra' : float(precio_compra),
        'ganancia' : float(ganancia),
        'estado' : estado
    }
    productosModel.editar(databproductos)

    return redirect(url_for('productos'))
    #productosModel.crear(databproductos)
    #productosModel.editar(databproductos)

@app.route('/productos/editar_registro/<int:id>', methods=['GET', 'POST'])
def editar_registro(id):
    if request.method == 'GET':
        
        productosModel = ProductosModel()
        producto = productosModel.sacar_producto(id)
        #print(producto)
        return render_template('productos/editar.html', producto=producto)
    
    