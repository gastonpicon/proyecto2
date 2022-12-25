from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS']= 'Content-Type'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='sistema'
mysql=MySQL(app)

@app.route('/api/customer/<int:id>')
@cross_origin()
def getCustomer(id):
    cur=mysql.connection.cursor()
    cur.execute('SELECT id, nombre, apellido, email, telefono, direccion FROM customers WHERE id = '+str(id))
    data=cur.fetchall()
    contenido={}
    for fila in data:
        contenido= {
            'id':fila[0],
            'nombre':fila[1],
            'apellido':fila[2],
            'email':fila[3],
            'telefono':fila[4],
            'direccion':fila[5]
        }
    return jsonify(contenido)

@app.route('/api/customers')
@cross_origin()
def getCustomers():
    cur=mysql.connection.cursor()
    cur.execute('SELECT id, nombre, apellido, email, telefono, direccion FROM customers')
    data=cur.fetchall()
    resultado=[]
    for fila in data:
        contenido= {
            'id':fila[0],
            'nombre':fila[1],
            'apellido':fila[2],
            'email':fila[3],
            'telefono':fila[4],
            'direccion':fila[5]
        }
        resultado.append(contenido)
    return jsonify(resultado)

@app.route('/api/customer/<int:id>', methods=['DELETE'])
@cross_origin()
def removeCustomer(id):
    cur=mysql.connection.cursor()
    cur.execute("DELETE FROM customers WHERE `customers`.`id` = " + str(id) + ";")
    mysql.connection.commit()
    return "cliente eliminado"

@app.route('/api/customer', methods=['POST'])
@cross_origin()
def createCustomer():
    if 'id' in request.json:
        updateCustomer()
    else:
        createCustomer()
    return "ok"

def createCustomer():
    request.json['nombre' ]
    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO `customers` (`id`, `nombre`, `apellido`, `email`, `telefono`, `direccion`) VALUES (NULL, %s, %s, %s, %s, %s);", (request.json['nombre'], request.json['apellido'], request.json['email'], request.json['telefono'], request.json['direccion']))
    mysql.connection.commit()
    return "cliente guardado"

def updateCustomer():
    request.json['nombre' ]
    cur=mysql.connection.cursor()
    cur.execute("UPDATE `customers` SET `nombre` = %s, `apellido` = %s, `email` = %s, `telefono` = %s, `direccion` = %s WHERE `customers`.`id` = %s;", (request.json['nombre'], request.json['apellido'], request.json['email'], request.json['telefono'], request.json['direccion'], request.json['id']))
    mysql.connection.commit()
    return "cliente guardado"

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(None,3000,True)

