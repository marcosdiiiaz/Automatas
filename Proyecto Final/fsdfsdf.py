import tkinter as tk
from tkinter import font

def main():
    ventana = tk.Tk()
    ventana.title("Fuentes disponibles")

    # Obtener la lista de nombres de fuentes
    nombres_fuentes = font.families()

    # Crear una etiqueta para mostrar los nombres de las fuentes
    etiqueta = tk.Label(ventana, text="\n".join(nombres_fuentes))
    etiqueta.pack()

    ventana.mainloop()

if __name__ == '__main__':
    main()
