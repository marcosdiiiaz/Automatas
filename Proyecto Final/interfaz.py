import tkinter as tk
from tkinter import filedialog, messagebox
from ap_traffic import Trafico

# --- Ventana --------------------
ventana00 = tk.Tk()
ventana00.title('Seguimiento del tráfico de Access Point')
ventana00.geometry('1920x1080')

# --- Etiquetas ------------------
etiqueta_inicio = tk.Label(ventana00, text='Fecha de Inicio:')
etiqueta_inicio.pack()
etiqueta_fin = tk.Label(ventana00, text='Fecha de Fin:')
etiqueta_fin.pack()

# --- Entradas -------------------
entrada_inicio = tk.Entry(ventana00)
entrada_inicio.pack()
entrada_fin = tk.Entry(ventana00)
entrada_fin.pack()

# --- Botones --------------------
boton_importar = tk.Button(ventana00, text='Importar CSV', command=Trafico().importarCSV)
boton_importar.pack()
boton_exportar = tk.Button(ventana00, text='Exportar Excel', command=Trafico().exportarXLSX)
boton_exportar.pack()
boton_calcular = tk.Button(ventana00, text='Calcular Tráfico', command=lambda: Trafico().calcularTrafico(entrada_inicio.get(), entrada_fin.get()))
boton_calcular.pack()


ventana00.mainloop()
