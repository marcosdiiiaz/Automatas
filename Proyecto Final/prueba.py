import csv
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd

def importar_csv():
    ruta_archivo = filedialog.askopenfilename(filetypes=[('Archivos CSV', '*.csv')])
    ruta_archivo_entry.delete(0, tk.END)
    ruta_archivo_entry.insert(0, ruta_archivo)

def filtrar():
    ruta_archivo = ruta_archivo_entry.get()
    fecha_inicio = fecha_inicio_entry.get()
    fecha_fin = fecha_fin_entry.get()

    trafico_ap = {}

    with open(ruta_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        encabezados = next(lector_csv)  # Leer la primera fila de encabezados

        # Obtener los índices de las columnas relevantes
        indice_input_octets = encabezados.index('Input_Octects')
        indice_output_octets = encabezados.index('Output_Octects')
        indice_ip_nas_ap = encabezados.index('IP_NAS_AP')
        indice_inicio_conexion_dia = encabezados.index('Inicio_de_Conexión_Dia')

        for fila in lector_csv:
            try:
                # Obtener los valores relevantes de la fila
                input_octets = int(fila[indice_input_octets])
                output_octets = int(fila[indice_output_octets])
                ip_nas_ap = fila[indice_ip_nas_ap]
                inicio_conexion_dia = fila[indice_inicio_conexion_dia]

                # Verificar si la fecha de inicio de conexión está dentro del rango especificado
                if re.match(r'\d{4}-\d{2}-\d{2}', inicio_conexion_dia):
                    if fecha_inicio <= inicio_conexion_dia <= fecha_fin:
                        # Calcular el tráfico total del AP sumando los octetos de entrada y salida
                        trafico_total = input_octets + output_octets

                        # Actualizar el diccionario de tráfico del AP
                        if ip_nas_ap in trafico_ap:
                            trafico_ap[ip_nas_ap] += trafico_total
                        else:
                            trafico_ap[ip_nas_ap] = trafico_total
            except ValueError:
                # Ignorar filas con valores no numéricos en la columna "Input_Octects"
                continue

    # Obtener el AP con mayor tráfico
    ap_max_trafico = max(trafico_ap, key=trafico_ap.get)
    trafico_maximo = trafico_ap[ap_max_trafico]

    tabla.delete(*tabla.get_children())  # Borrar contenido anterior de la tabla

    for ap, trafico in trafico_ap.items():
        tabla.insert('', tk.END, values=(ap, trafico))

def exportar_excel():
    archivo_salida = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[('Archivos Excel', '*.xlsx')])
    if archivo_salida:
        filas_seleccionadas = tabla.selection()
        datos_exportar = []

        for fila in filas_seleccionadas:
            datos_exportar.append(tabla.item(fila)['values'])

        df = pd.DataFrame(datos_exportar, columns=['AP', 'Trafico'])
        df.to_excel(archivo_salida, index=False)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Análisis de Tráfico AP")
ventana.geometry("600x400")

# Crear los widgets
ruta_archivo_label = tk.Label(ventana, text="Ruta del archivo CSV:")
ruta_archivo_label.pack()

ruta_archivo_entry = tk.Entry(ventana, width=50)
ruta_archivo_entry.pack()

importar_csv_button = tk.Button(ventana, text="Importar CSV", command=importar_csv)
importar_csv_button.pack()

fechas_frame = tk.Frame(ventana)
fechas_frame.pack()

fecha_inicio_label = tk.Label(fechas_frame, text="Fecha inicio (formato aaaa-mm-dd):")
fecha_inicio_label.grid(row=0, column=0)

fecha_inicio_entry = tk.Entry(fechas_frame)
fecha_inicio_entry.grid(row=0, column=1)

fecha_fin_label = tk.Label(fechas_frame, text="Fecha fin (formato aaaa-mm-dd):")
fecha_fin_label.grid(row=1, column=0)

fecha_fin_entry = tk.Entry(fechas_frame)
fecha_fin_entry.grid(row=1, column=1)

filtrar_button = tk.Button(ventana, text="Filtrar", command=filtrar)
filtrar_button.pack()

tabla_frame = tk.Frame(ventana)
tabla_frame.pack()

tabla = ttk.Treeview(tabla_frame, columns=['AP', 'Trafico'])
tabla.heading('AP', text='AP')
tabla.heading('Trafico', text='Trafico')
tabla.pack()

exportar_excel_button = tk.Button(ventana, text="Exportar a Excel", command=exportar_excel)
exportar_excel_button.pack()

# Ejecutar la ventana
ventana.mainloop()
