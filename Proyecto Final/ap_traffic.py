import re
import csv
import pandas as pd
from tkinter import filedialog, messagebox

# Seguimiento del tráfico de AP, para determinar cuál es el AP que más tráfico
# (Input Octets + Output Octets) ha tenido en un período de tiempo (rango de fechas).
# Debe incluir la posibilidad de ingresar un rango de fechas.

class Trafico:

    def __init__(self):
        self.formatos = {
        'ID': r"^\d+$",  # ID index 0
        'ID_Sesion': r"^(([0-9]|[A-F]){8}|([0-9]|[A-F]){16})(-([0-9]|[A-F]){8})?$",  # ID_Sesion index 1
        'ID_Conexión_unico': r"^([0-9]|[a-f]){16}$",  # ID_Conexión_unico index 2
        'Usuario': r"^.*$",  # Usuario index 3
        'IP_NAS_AP': r"^(?:\d{1,3}\.){3}\d{1,3}$",  # IP_NAS_AP index 4
        'Tipo__conexión': r"^Wireless-802.11$",  # Tipo__conexión index 5
        'Inicio_de_Conexión_Dia': r"^\d{4}-\d{2}-\d{2}$",  # Inicio_de_Conexión_Dia index 6
        'Inicio_de_Conexión_Hora': r"^\d{2}:\d{2}:\d{2}$",  # Inicio_de_Conexión_Hora index 7
        'FIN_de_Conexión_Dia': r"^\d{4}-\d{2}-\d{2}$",  # FIN_de_Conexión_Dia index 8
        'FIN_de_Conexión_Hora': r"^\d{2}:\d{2}:\d{2}$",  # FIN_de_Conexión_Hora index 9
        'Session_Time': r"^\d+$",  # Session_Time index 10
        'Input_Octects': r"^\d+$",  # Input_Octects index 11
        'Output_Octects': r"^\d+$",  # Output_Octects index 12
        'MAC_AP': r"^(([A-F]|[0-9]){2}-){5}([A-F]|[0-9]){2}:[A-Z]{4}$",  # MAC_AP index 13
        'MAC_Cliente': r"^(([A-F]|[0-9]){2}-){5}([A-F]|[0-9]){2}$",  # MAC_Cliente index 14
        'Razon_de_Terminación_de_Sesión': r"^.*$",  # Razon_de_Terminación_de_Sesión index 15
        '': r"^.*$"
        }
        self.encabezados = []
        self.datos_filtrados = []

    def importarCSV(self):
        ruta_archivo = filedialog.askopenfilename(filetypes=[('Archivos CSV', '*.csv')])

        if ruta_archivo:
            try:
                with open(ruta_archivo, 'r') as archivo:
                    lector_csv = csv.reader(archivo)
                    self.encabezados = next(lector_csv)
                    self.datos_csv = list(lector_csv)
            except FileNotFoundError:
                messagebox.showerror("Error", "Archivo no encontrado.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        self.manejarErrores()

    def manejarErrores(self):
        self.errores = []
        self.datos_filtrados = []

        for row in self.datos_csv:
            for index in range(len(self.encabezados)):
                columna = self.encabezados[index]
                value = row[index]
                formato = self.formatos.get(columna)
                if not re.match(formato, value):
                    self.errores.append(row)
                    break
            else:
                self.datos_filtrados.append(row)
        contador_errores = len(self.errores)
        if contador_errores != 0:
            messagebox.showinfo("Información", f"Se encontraron {contador_errores} errores en el archivo CSV.")

    def calcularTrafico(self, fecha_inicio, fecha_fin):
        trafico_ap = {}
        self.fila_utilizada = []
        
        for fila in self.datos_filtrados:
            ip_nas_ap = fila[4]
            inicio_conexion_dia = fila[6]
            fin_conexion_dia = fila[8]
            input_octets = int(fila[11])
            output_octets = int(fila[12])

            if fecha_inicio <= inicio_conexion_dia <= fecha_fin or fecha_inicio <= fin_conexion_dia <= fecha_fin or (inicio_conexion_dia < fecha_inicio and fin_conexion_dia > fecha_fin):
                self.fila_utilizada.append(fila)

                if ip_nas_ap in trafico_ap:
                    trafico_ap[ip_nas_ap] += input_octets + output_octets
                else:
                    trafico_ap[ip_nas_ap] = input_octets + output_octets

        if trafico_ap:
            ap_max_trafico = max(trafico_ap, key=trafico_ap.get)
            trafico_maximo = trafico_ap[ap_max_trafico]
            messagebox.showinfo("Información", f"El AP con mayor tráfico es: {ap_max_trafico}\n"
                                                f"El tráfico máximo es: {trafico_maximo}")

    def exportarXLSX(self):
        ruta_guardar = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Archivos XLSX', '*.xlsx')])

        if ruta_guardar:
            try:
                df = pd.DataFrame(self.fila_utilizada)
                df.to_excel(ruta_guardar, index=False)
                messagebox.showinfo("Información", "Archivo XLSX exportado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", e)