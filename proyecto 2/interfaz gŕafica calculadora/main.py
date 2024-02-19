"""     CALCULADORA       """

from tkinter import *
from tkinter import messagebox


class Calculadora:  
    
    def __init__(self, alertas):
        # Defino las variablas para luego
        self.numero1=StringVar()
        self.numero2=StringVar()
        self.resultado=StringVar() 
        self.alertas= alertas
        
    
    def sumar(self):
        try:
            self.resultado.set(float(self.numero1.get()) + float(self.numero2.get()))
            self.mostrarResultado()
        except:
            messagebox.showerror("Error al introducir los valores", "Introduce valores numéricos")

    def restar(self):
        try:
            self.resultado.set(float(self.numero1.get()) - float(self.numero2.get()))
            self.mostrarResultado()
        except:
            messagebox.showerror("Error al introducir los valores", "Introduce valores numéricos")

    def multiplicar(self):
        try:
            self.resultado.set(float(self.numero1.get()) * float(self.numero2.get()))
            self.mostrarResultado()
        except:
            messagebox.showerror("Error al introducir los valores", "Introduce valores numéricos")


    def dividir(self):
        try:
            self.resultado.set(float(self.numero1.get()) / float(self.numero2.get()))
            self.mostrarResultado()
        except:
                    messagebox.showerror("Error al introducir los valores", "Introduce valores numéricos")


    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El Resultado de dicha operación es: {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")


ventana = Tk()
ventana.title("EJERCICIO CALCULADORA")
ventana.geometry("400x400")
ventana.config(bd=25)

calculadora= Calculadora(messagebox)




#Creo el marco donde irá todo el codigo
marco= Frame(ventana, width=400, height=250)
marco.config(
    bd=5,
    relief= SOLID,
    padx=15,
    pady=15
    )
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)


#Entrada de texto para primer número
Label(marco, text="Primer número ").pack()
Entry(marco, textvariable=calculadora.numero1, justify=CENTER).pack()

#Entrada de texto para segundo número
Label(marco, text="Segundo número ").pack()
Entry(marco, textvariable=calculadora.numero2, justify=CENTER).pack()

Label(marco, text="").pack()      #Este texto vacio es para hacer salto de linea, equivalente a ("\n")

#Seccion de los botones
Button(marco, text="Sumar", command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)



ventana.mainloop()