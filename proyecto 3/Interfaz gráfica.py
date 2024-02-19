from tkinter import *
from tkinter import ttk

ventana= Tk()
#ventana.geometry("450x500")
ventana.minsize(500,500)
ventana.title("PROYECTO TKINTER")
ventana.resizable(0,0)

#Pantallas
def home():
    #Montar pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=180,
        pady=20   
    )
    home_label.grid(row=0, column=0)
    # Mostrar el Treeview nuevamente
    products_box.grid(row=1)
    products_table.grid(row=1, column=0, columnspan=2)
    
    
    # Listar productos
    """
    for product in products: 
        if len(product) == 3:
            product.append("Añadido")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="------------").grid()
    """
    for product in products: 
        if len(product) == 3:
            product.append("Añadido")
            products_table.insert('', 0, text=product[0], values = product[1])


        
    
    #Ocultar pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    


def add():
    #Encabezado
    add_label.config(
        fg="white",
        bg="black",
        
        font=("Arial", 30),
        padx=100,
        pady=20   
    )
    add_label.grid(row=0, column=0, columnspan=4,)
    
    #Campos de formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5,pady=5)
    add_name_entry.grid(row=1, column=1, padx=5,pady=5)
    
    #Campos de formulario
    add_price_label.grid(row=2, column=0, padx=5,pady=5)
    add_price_entry.grid(row=2, column=1, padx=5,pady=5)
    
    #Campos de formulario
    add_description_label.grid(row=3, column=0, padx=5,pady=5)
    add_description_entry.grid(row=3, column=1, padx=5,pady=5)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=10,
        pady=15
    )
    
    
    add_separator.grid(row=4,)
    
    boton = Button(add_frame, text="Guardar", command=add_products)
    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        padx=15,
        bg="Black",
        fg="White"
    )

    
    
    #Ocultar pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_table.grid_remove()


def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=120,
        pady=20    
    )
    info_label.grid(row=0, column=0)
    
    data_label.grid(row=1, column=0)
    
    #Ocultar pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    add_frame.grid_remove()
    add_label.grid_remove()
    products_table.grid_remove()




def add_products():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    home()

#Variables inportantes
products= []
name_data=StringVar()
price_data=StringVar()


#Definir campos de pantalla         INICIO
home_label= Label(ventana, text="Inicio")
products_box=Frame(ventana, width=250)

Label(products_box).grid(row=0)
products_table=ttk.Treeview(height=12,columns=2)
products_table.grid(row=1, column=0, columnspan=2)
products_table.heading("#0", text="Producto", anchor=W)
products_table.heading("#1", text="Precio", anchor=W)


#Definir campos de pantalla         AÑADIR PRODUCTO
add_label= Label(ventana, text="Añadir producto")
#Definir campos de pantalla         INFORMACIÓN
info_label= Label(ventana, text="Información")
#Definir campos de pantalla         INFORMACIÓN
data_label= Label(ventana, text="Creado por Alex Dehesa")


#Campos del formulario
add_frame=Frame(ventana)
add_name_label=Label(add_frame, text="Nombre del producto: ")
add_name_entry=Entry(add_frame, text=name_data)

add_price_label=Label(add_frame, text="Precio del producto: ")
add_price_entry=Entry(add_frame, text=price_data)

add_description_label=Label(add_frame, text="Descripción: ")
add_description_entry=Text(add_frame)


add_separator=Label(ventana)

boton = Button(ventana, text="Guardar", command=add_products)




#Cargar pantalla de inicio
home()


#Menu superior
menu_superior= Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)


#Cargar el menú venta
ventana.config(menu=menu_superior)





ventana.mainloop()