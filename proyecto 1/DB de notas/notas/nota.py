# Importar módulos necesarios
import mysql.connector
import usuarios.conexion as conexion

# Obtener la conexión a la base de datos
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:
    def __init__(self, usuario_id, titulo="", descripcion=""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion 

    def guardar(self):
        # Definir la consulta SQL para guardar una nota
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)
        
        # Ejecutar la consulta SQL
        cursor.execute(sql, nota)
        database.commit()
        
        # Devolver el resultado del guardado
        return [cursor.rowcount, self]

    def listar(self):
        # Definir la consulta SQL para listar todas las notas de un usuario
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"
        
        # Ejecutar la consulta SQL
        cursor.execute(sql)
        result = cursor.fetchall()
        
        # Devolver el resultado de la consulta
        return result

    def eliminar(self, usuario_id, titulo):
        # Definir la consulta SQL para eliminar una nota
        sql = f"DELETE FROM notas WHERE usuario_id = {usuario_id} AND titulo LIKE '%{titulo}%'"
        
        # Ejecutar la consulta SQL
        cursor.execute(sql)
        database.commit()
        
        # Devolver el resultado de la eliminación
        return [cursor.rowcount, self]
