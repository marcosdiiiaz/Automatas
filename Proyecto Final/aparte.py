# interfaz.py
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
from ap_traffic import Trafico
import pandas as pd
from pandastable import Table

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

def importar_csv():
    trafico.importarCSV()
    mostrar_tabla(trafico.datos_csv)

def mostrar_tabla(datos):
    df = pd.DataFrame(datos, columns=trafico.encabezados)
    ventana_tabla = tk.Toplevel(ventana00)
    ventana_tabla.title('Contenido del archivo CSV')
    columnas_seleccionadas = [4, 6, 8, 11, 12]
    df_seleccionado = df.iloc[:, columnas_seleccionadas]
    tabla = Table(ventana_tabla, dataframe=df_seleccionado)
    tabla.show()

def calcular_trafico():
    fecha_inicio = ent_fi.get()
    fecha_fin = ent_ff.get()
    trafico.calcularTrafico(fecha_inicio, fecha_fin)
    mostrar_tabla(trafico.datos_filtrados_fecha)
    if trafico.datos_filtrados_fecha:
        messagebox.showinfo("Contenido a Exportar", "El contenido a exportar son los datos filtrados por fecha.")
    else:
        messagebox.showinfo("Contenido a Exportar", "No hay datos para exportar.")

boton_importar = tk.Button(ventana00, text='Importar CSV', command=importar_csv)
boton_importar.pack()

boton_exportar = tk.Button(ventana00, text='Exportar Excel', command=trafico.exportarXLSX)
boton_exportar.pack()

boton_calcular = tk.Button(ventana00, text='Calcular Tráfico', command=calcular_trafico)
boton_calcular.pack()

ventana00.mainloop()
