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
        'IP_NAS_AP': r"^(\d{1,3}\.){3}\d{1,3}$",  # IP_NAS_AP index 4
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
        self.rango_abierto = []
        self.rango_cerrado = []
        self.dfa = None
        self.dfc = None
        self.ap_trafico_maximo = None
        self.trafico_maximo = 0

    def importarCSV(self):
        self.ruta_archivo = filedialog.askopenfilename(filetypes=[('Archivos CSV', '*.csv')])

        if self.ruta_archivo:
            try:
                with open(self.ruta_archivo, 'r') as archivo:
                    lector_csv = csv.reader(archivo)
                    self.encabezados = next(lector_csv)
                    self.datos_csv = list(lector_csv)
                    messagebox.showinfo("Información", "El archivo se ha importado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def exportarAbiertoXLSX(self):
        ruta_guardar = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[('Archivos de Excel', '*.xlsx')])
        if ruta_guardar:
            try:
                self.dfa.to_excel(ruta_guardar, index=False)
                messagebox.showinfo("Información", "El archivo se ha exportado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def exportarCerradoXLSX(self):
        ruta_guardar = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[('Archivos de Excel', '*.xlsx')])
        if ruta_guardar:
            try:
                self.dfc.to_excel(ruta_guardar, index=False)
                messagebox.showinfo("Información", "El archivo se ha exportado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def manejarErrores(self):
        self.errores = []
        self.datos_filtrados = []

        for fila in self.datos_csv:
            for indice in range(len(self.encabezados)):
                columna = self.encabezados[indice]
                valor = fila[indice]
                formato = self.formatos.get(columna)
                if not re.match(formato, valor):
                    self.errores.append(fila)
                    break
            else:
                self.datos_filtrados.append(fila)
        contador_errores = len(self.errores)
        if contador_errores != 0:
            messagebox.showinfo("Información", f"Se encontraron {contador_errores} errores en el archivo CSV.")

    def calcularRangoAbierto(self, fecha_inicio, fecha_fin):
        self.manejarErrores()
        self.rango_abierto = []
        self.dfa = None
        ap_trafico_maximo = None
        trafico_maximo = 0

        try:
            for fila in self.datos_filtrados:
                inicio_conexion_dia = fila[6]
                fin_conexion_dia = fila[8]
                if (fecha_inicio <= inicio_conexion_dia <= fecha_fin) or (fecha_inicio <= fin_conexion_dia <= fecha_fin) or (inicio_conexion_dia < fecha_inicio and fin_conexion_dia > fecha_fin):
                    self.rango_abierto.append(fila)

                input_octets = int(fila[11])
                output_octets = int(fila[12])
                trafico = input_octets + output_octets
                if trafico > trafico_maximo:
                    trafico_maximo = trafico
                    ap_trafico_maximo = fila[4]
        except Exception as e:
            messagebox.showerror('Error', str(e))
            return

        if not self.rango_abierto:
            messagebox.showerror('Error', 'No hay datos.')
            return

        try: # Guarda en DataFrame solo las columnas pedidas de cada fila.
            columnas_seleccionadas = [0, 4, 6, 8, 11, 12]
            datos_seleccionados = [[fila[i] for i in columnas_seleccionadas] for fila in self.rango_abierto]
            self.dfa = pd.DataFrame(datos_seleccionados, columns=[self.encabezados[i] for i in columnas_seleccionadas])
        except Exception as e:
            messagebox.showerror('Error', str(e))
            return

        if ap_trafico_maximo:
            messagebox.showinfo("Resultado", f"El AP con más tráfico en el rango de fechas proporcionado es: {ap_trafico_maximo}")
        else:
            messagebox.showinfo("Resultado", "No se encontraron datos dentro del rango de fechas proporcionado.")

            
    def calcularRangoCerrado(self, fecha_inicio, fecha_fin):
        self.manejarErrores()
        self.rango_cerrado = []
        self.dfc = None
        self.ap_trafico_maximo = None
        self.trafico_maximo = 0

        try:
            for row in self.datos_filtrados:
                inicio_conexion_dia = row[6]
                fin_conexion_dia = row[8]
                if fecha_inicio <= inicio_conexion_dia <= fecha_fin and fecha_inicio <= fin_conexion_dia <= fecha_fin:
                    self.rango_cerrado.append(row)

                input_octets = int(row[11])
                output_octets = int(row[12])
                trafico = input_octets + output_octets
                if trafico > self.trafico_maximo:
                    self.trafico_maximo = trafico
                    self.ap_trafico_maximo = row[4]
        except Exception as e:
            messagebox.showerror('Error', str(e))
            return

        if not self.rango_cerrado:
            messagebox.showerror('Error', 'No hay datos.')
            return

        try: # Guarda en DataFrame solo las columnas pedidas de cada fila.
            columnas_seleccionadas = [0, 4, 6, 8, 11, 12]
            datos_seleccionados = [[row[i] for i in columnas_seleccionadas] for row in self.rango_cerrado]
            self.dfc = pd.DataFrame(datos_seleccionados, columns=[self.encabezados[i] for i in columnas_seleccionadas])
        except Exception as e:
            messagebox.showerror('Error', str(e)) 
            return

        if self.ap_trafico_maximo:
            messagebox.showinfo("Resultado", f"El AP con más tráfico en el rango de fechas proporcionado es: {self.ap_trafico_maximo}")
        else:
            messagebox.showinfo("Resultado", "No se encontraron datos dentro del rango de fechas proporcionado.")

    def actualizarTabla(self, opcion):
        df = None
        if opcion == 'Rango Abierto':
            df = self.dfa
        elif opcion == 'Rango Cerrado':
            df = self.dfc
        return df