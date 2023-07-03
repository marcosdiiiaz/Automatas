import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()

def mostrar_pregunta():
    respuesta = messagebox.askquestion("Pregunta", "¿Qué tipo de rango deseas calcular?")

    if respuesta == 'yes':
        calcular_rango_abierto()
    else:
        calcular_rango_cerrado()

def calcular_rango_abierto():
    # Lógica para calcular el rango abierto
    print("Calculando rango abierto")

def calcular_rango_cerrado():
    # Lógica para calcular el rango cerrado
    print("Calculando rango cerrado")

boton = tk.Button(ventana, text="Mostrar pregunta", command=mostrar_pregunta)
boton.pack()

ventana.mainloop()
