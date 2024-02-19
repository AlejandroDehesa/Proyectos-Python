# Importar el módulo de acciones desde el paquete usuarios
from usuarios import acciones

# Imprimir acciones disponibles
print("""
Acciones disponibles :
- registro
- login
""")

# Obtener la acción del usuario
accion = input("\nQué opción desea realizar: ")

# Crear instancia de la clase Acciones
hazEl = acciones.Acciones()

# Realizar la acción seleccionada por el usuario
if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
