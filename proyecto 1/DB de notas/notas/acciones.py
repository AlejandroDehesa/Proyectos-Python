# Archivo: notas/acciones.py

# Importar el modelo de nota desde el paquete notas
import notas.nota as modelo

class Acciones:
    
    def crear(self, usuario):
        print(f"Hola {usuario[1]}, \ncreando una nueva nota ...")
        
        # Obtener información de la nueva nota
        titulo = input("\nIntroduce el título de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")
        
        # Crear instancia de la clase Nota
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        
        # Guardar la nota en la base de datos
        guardar = nota.guardar()
        
        # Mostrar mensaje de éxito o error
        if guardar[0] >= 1:
            print(f"\nPerfecto, has guardado la nota: {nota.titulo}")
        else:
            print(f"No se ha podido guardar la nota, lo sentimos {usuario[1]}")
            
    def mostrar(self, usuario):
        print(f"\nDe acuerdo {usuario[1]}, aquí tienes tus notas:")
        
        # Crear instancia de la clase Nota
        nota = modelo.Nota(usuario[0])
        
        # Obtener y mostrar todas las notas del usuario
        notas = nota.listar()
        
        for nota in notas:
            print("################################")
            print(nota[2])
            print(nota[3])
            print("################################\n")

    def borrar(self, usuario):
        print(f"\nDe acuerdo, {usuario[1]}. Vamos a borrar notas")
        
        # Obtener el título de la nota a eliminar
        titulo = input("Introduce el título de la nota que deseas eliminar: ")
        
        # Crear instancia de la clase Nota
        nota = modelo.Nota(usuario[0], titulo)
        
        # Eliminar la nota de la base de datos
        eliminar = nota.eliminar(usuario[0], titulo)
        
        # Mostrar mensaje de éxito o error
        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No se ha podido borrar la nota, inténtelo más tarde")
