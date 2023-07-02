# interfaz.py
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
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
ent_fi = tk.Entry(ventana00)
ent_fi.pack()
ent_ff = tk.Entry(ventana00)
ent_ff.pack()

# --- Botones --------------------
trafico = Trafico()  # Crea una instancia de la clase Trafico

boton_importar = tk.Button(ventana00, text='Importar CSV', command=trafico.importarCSV)
boton_importar.pack()

boton_exportar = tk.Button(ventana00, text='Exportar Excel', command=trafico.exportarXLSX)
boton_exportar.pack()

boton_calcular = tk.Button(ventana00, text='Calcular Tráfico', command=lambda: trafico.calcularTrafico(ent_fi.get(), ent_ff.get()))
boton_calcular.pack()

ventana00.mainloop()
