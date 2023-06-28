import csv
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def calcular_trafico_ap(ruta_archivo, fecha_inicio, fecha_fin):
    trafico_ap = {}
    contador_errores = 0  # Contador de errores

    with open(ruta_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        encabezados = next(lector_csv)  # Leer la primera fila de encabezados

        # Obtener los índices de las columnas relevantes
        indice_id = encabezados.index('ID')
        indice_id_sesion = encabezados.index('ID_Sesion')
        indice_id_conexion_unico = encabezados.index('ID_Conexión_unico')
        indice_usuario = encabezados.index('Usuario')
        indice_ip_nas_ap = encabezados.index('IP_NAS_AP')
        indice_tipo_conexion = encabezados.index('Tipo__conexión')
        indice_inicio_conexion_dia = encabezados.index('Inicio_de_Conexión_Dia')
        indice_inicio_conexion_hora = encabezados.index('Inicio_de_Conexión_Hora')
        indice_fin_conexion_dia = encabezados.index('FIN_de_Conexión_Dia')
        indice_fin_conexion_hora = encabezados.index('FIN_de_Conexión_Hora')
        indice_sesion_time = encabezados.index('Session_Time')
        indice_input_octets = encabezados.index('Input_Octects')
        indice_output_octets = encabezados.index('Output_Octects')
        indice_mac_ap = encabezados.index('MAC_AP')
        indice_mac_cliente = encabezados.index('MAC_Cliente')
        indice_razon_terminacion = encabezados.index('Razon_de_Terminación_de_Sesión')


        for fila in lector_csv:
            try:
                # Obtener los valores relevantes de la fila
                id = int(fila[indice_id])
                id_sesion = fila[indice_id_sesion]
                id_conexion_unico = fila[indice_id_conexion_unico]
                usuario = fila[indice_usuario]
                ip_nas_ap = fila[indice_ip_nas_ap]
                tipo_conexion = fila[indice_tipo_conexion]
                inicio_conexion_dia = fila[indice_inicio_conexion_dia]
                inicio_conexion_hora = fila[indice_inicio_conexion_hora]
                fin_conexion_dia = fila[indice_fin_conexion_dia]
                fin_conexion_hora = fila[indice_fin_conexion_hora]
                sesion_time = fila[indice_sesion_time]
                input_octets = int(fila[indice_input_octets])
                output_octets = int(fila[indice_output_octets])
                mac_ap = fila[indice_mac_ap]
                mac_cliente = fila[indice_mac_cliente]
                razon_terminacion = fila[indice_razon_terminacion]

                #verificar todas las expresiones regulares
                # if re.match(r'^\d+$', id):
                #     if re.match(r'^[0-9A-Fa-f]{8}(-[0-9A-Fa-f]{8})?$', id_sesion):
                #         if re.match(r'^[0-9A-Fa-f]{8}(-[0-9A-Fa-f]{8})?$', id_conexion_unico):
                #             if re.match(r'^[a-zA-Z]+(?:[-_][a-zA-Z]+)?$', usuario):
                #                 if re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', ip_nas_ap):
                #                     if re.match(r'^Wireless-802\.11$', tipo_conexion):
                #                         if re.match(r'^\d{2}:\d{2}:\d{2}$', inicio_conexion_hora):
                #                             if re.match(r'^\d{4}-\d{2}-\d{2}$', fin_conexion_dia):
                #                                 if re.match(r'^\d{2}:\d{2}:\d{2}$', fin_conexion_hora):
                #                                     if re.match(r'^\d+$', sesion_time):
                #                                         if re.match(r'^[0-9A-Fa-f]{2}(?:-[0-9A-Fa-f]{2}){5}:[0-9A-Fa-f]{4}$', mac_ap):
                #                                             if re.match(r'^[0-9A-Fa-f]{2}(?:-[0-9A-Fa-f]{2}){5}$', mac_cliente):
                #                                                 if re.match(r'^[A-Z][a-z]{0,6}-[A-Z][a-z]{0,6}$', razon_terminacion):


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
                # Ignorar filas con valores no numéricos en la columna "Input_Octects" dentro del rango de fechas
                # Abre el archivo CSV en modo de lectura            
                    if id != r'^\d+$':
                        if id_sesion != r'^[0-9A-Fa-f]{8}(-[0-9A-Fa-f]{8})?$':
                            if id_conexion_unico != r'^[0-9A-Fa-f]{8}(-[0-9A-Fa-f]{8})?$':
                                if usuario != r'^[a-zA-Z]+(?:[-_][a-zA-Z]+)?$':
                                    if ip_nas_ap != r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$':
                                        if tipo_conexion != r'^Wireless-802\.11$':
                                            if inicio_conexion_hora != r'^\d{2}:\d{2}:\d{2}$':
                                                if fin_conexion_dia != r'^\d{4}-\d{2}-\d{2}$':
                                                    if fin_conexion_hora != r'^\d{2}:\d{2}:\d{2}$':
                                                        if sesion_time != r'^\d+$':
                                                            if mac_ap != r'^[0-9A-Fa-f]{2}(?:-[0-9A-Fa-f]{2}){5}:[0-9A-Fa-f]{4}$':
                                                                if mac_cliente != r'^[0-9A-Fa-f]{2}(?:-[0-9A-Fa-f]{2}){5}$':
                                                                    if razon_terminacion != r'^[A-Z][a-z]{0,6}-[A-Z][a-z]{0,6}$':
                                                                        if fecha_inicio <= inicio_conexion_dia <= fecha_fin:
                                                                            contador_errores += 1  # Incrementar el contador de errores
                                                                            continue
                

    # Obtener el AP con mayor tráfico
    ap_max_trafico = max(trafico_ap, key=trafico_ap.get)
    trafico_maximo = trafico_ap[ap_max_trafico]

    return ap_max_trafico, trafico_maximo, contador_errores

def obtener_archivo():
    ruta_archivo = filedialog.askopenfilename(filetypes=[('Archivos CSV', '*.csv')])
    ruta_archivo_entry.delete(0, tk.END)
    ruta_archivo_entry.insert(tk.END, ruta_archivo)

def calcular_trafico():
    ruta_archivo = ruta_archivo_entry.get()
    fecha_inicio = fecha_inicio_entry.get()
    fecha_fin = fecha_fin_entry.get()

    try:
        ap_max_trafico, trafico_maximo, contador_errores = calcular_trafico_ap(ruta_archivo, fecha_inicio, fecha_fin)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"El AP con más tráfico en el período {fecha_inicio} - {fecha_fin} es: {ap_max_trafico}\n")
        resultado_text.insert(tk.END, f"Tráfico máximo: {trafico_maximo} octetos\n")
        resultado_text.insert(tk.END, f"Errores encontrados: {contador_errores}")
    except Exception as e:
        messagebox.showerror('Error', str(e))




# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calcular Tráfico AP")
ventana.geometry("1920x1080")

# Etiquetas y campos de entrada
ruta_archivo_label = tk.Label(ventana, text="Ruta del archivo CSV:")
ruta_archivo_label.pack()
ruta_archivo_entry = tk.Entry(ventana, width=40)
ruta_archivo_entry.pack()

fecha_inicio_label = tk.Label(ventana, text="Fecha inicial (aaaa-mm-dd):")
fecha_inicio_label.pack()
fecha_inicio_entry = tk.Entry(ventana, width=20)
fecha_inicio_entry.pack()

fecha_fin_label = tk.Label(ventana, text="Fecha final (aaaa-mm-dd):")
fecha_fin_label.pack()
fecha_fin_entry = tk.Entry(ventana, width=20)
fecha_fin_entry.pack()

obtener_archivo_button = tk.Button(ventana, text="Seleccionar archivo", command=obtener_archivo)
obtener_archivo_button.pack()

calcular_button = tk.Button(ventana, text="Calcular tráfico", command=calcular_trafico)
calcular_button.pack()

resultado_text = tk.Text(ventana, height=5, width=40)
resultado_text.pack()

ventana.mainloop()