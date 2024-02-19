# Importar módulos necesarios
import datetime
import hashlib
import usuarios.conexion as conexion

# Obtener la conexión a la base de datos
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
        
    def registrar(self):  
        # Obtener la fecha actual
        fecha = datetime.datetime.now()
        
        # Cifrar la contraseña usando SHA-256
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        # Definir la consulta SQL para el registro de usuario
        sql = "INSERT INTO usuario VALUES(null, %s, %s, %s, %s, %s)"
        
        # Crear una tupla con los datos del usuario
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        
        try:
            # Ejecutar la consulta SQL
            cursor.execute(sql, usuario)
            
            # Confirmar los cambios en la base de datos
            database.commit()
            
            # Devolver el resultado del registro
            result = [cursor.rowcount, self]
        except:
            # En caso de error, devolver un resultado indicando el fallo
            result = [0, self]
            
        return result

    def identificar(self): 
        # Definir la consulta SQL para la identificación del usuario
        sql = "SELECT * FROM usuario WHERE email = %s AND password = %s"
        
        # Cifrar la contraseña para compararla con la almacenada en la base de datos
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        
        # Crear una tupla con los datos para la consulta
        usuario = (self.email, cifrado.hexdigest())
        
        # Ejecutar la consulta SQL
        cursor.execute(sql, usuario)
        
        # Obtener el resultado de la consulta
        result = cursor.fetchone()
        return result
