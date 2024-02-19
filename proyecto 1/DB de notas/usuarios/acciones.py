# Importar el modelo de usuario desde el paquete usuarios
import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    
    def registro(self):
        print("\nRegistrándote en el sistema")
        nombre = input("Cuál es tu nombre: ")
        apellido = input("Cuáles son tus apellidos: ")
        email = input("Cuál es tu email: ")
        password = input("Cuál es tu contraseña: ") 
        
        # Crear instancia de la clase Usuario
        usuario = modelo.Usuario(nombre, apellido, email, password)
        
        # Registrar al usuario en la base de datos
        registro = usuario.registrar()
        
        # Mostrar mensaje de éxito o error
        if registro[0] >= 1:
            print(f"\nCorrecto, {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")
        
    def login(self):
        print("\nIdentificándote en el sistema")
        try:        
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")
            
            # Crear instancia de la clase Usuario
            usuario = modelo.Usuario('', '', email, password)
            
            # Identificar al usuario
            login = usuario.identificar()
            
            # Mostrar mensaje de bienvenida y acciones disponibles
            if login and email == login[3]:
                print(f"\nBienvenido {login[1]}, te has identificado en el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print("")       

    def proximasAcciones(self, usuario):
        print("""\nAcciones disponibles\n
        - Crear nota  (crear)
        - Mostrar nota (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)
        
        accion = input("\nQué quieres hacer ?: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)            
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Hasta la próxima {usuario[1]}")
            exit()
