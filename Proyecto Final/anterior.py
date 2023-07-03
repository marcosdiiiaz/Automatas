import re
import csv
import pandas as pd
from tkinter import filedialog, messagebox, Tk, Label, Entry, Button, ttk

class TraficoGUI(Tk):

    def __init__(self):
        super().__init__()

        self.title("Seguimiento de Tráfico de AP")
        self.geometry("800x400")

        self.fecha_inicio_label = Label(self, text="Fecha de Inicio (YYYY-MM-DD):")
        self.fecha_inicio_label.pack()
        self.fecha_inicio_entry = Entry(self)
        self.fecha_inicio_entry.pack()

        self.fecha_fin_label = Label(self, text="Fecha de Fin (YYYY-MM-DD):")
        self.fecha_fin_label.pack()
        self.fecha_fin_entry = Entry(self)
        self.fecha_fin_entry.pack()

        self.importar_csv_button = Button(self, text="Importar CSV", command=self.importarCSV)
        self.importar_csv_button.pack()

        self.tabla = ttk.Treeview(self)
        self.tabla["columns"] = ("ID", "ID_Sesion", "ID_Conexión_unico", "Usuario", "IP_NAS_AP", "Tipo__conexión",
                                 "Inicio_de_Conexión_Dia", "Inicio_de_Conexión_Hora", "FIN_de_Conexión_Dia",
                                 "FIN_de_Conexión_Hora", "Session_Time", "Input_Octects", "Output_Octects",
                                 "MAC_AP", "MAC_Cliente", "Razon_de_Terminación_de_Sesión", "")

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("ID_Sesion", text="ID Sesión")
        self.tabla.heading("ID_Conexión_unico", text="ID Conexión Único")
        self.tabla.heading("Usuario", text="Usuario")
        self.tabla.heading("IP_NAS_AP", text="IP NAS AP")
        self.tabla.heading("Tipo__conexión", text="Tipo de Conexión")
        self.tabla.heading("Inicio_de_Conexión_Dia", text="Inicio de Conexión (Día)")
        self.tabla.heading("Inicio_de_Conexión_Hora", text="Inicio de Conexión (Hora)")
        self.tabla.heading("FIN_de_Conexión_Dia", text="Fin de Conexión (Día)")
        self.tabla.heading("FIN_de_Conexión_Hora", text="Fin de Conexión (Hora)")
        self.tabla.heading("Session_Time", text="Tiempo de Sesión")
        self.tabla.heading("Input_Octects", text="Octetos de Entrada")
        self.tabla.heading("Output_Octects", text="Octetos de Salida")
        self.tabla.heading("MAC_AP", text="MAC AP")
        self.tabla.heading("MAC_Cliente", text="MAC Cliente")
        self.tabla.heading("Razon_de_Terminación_de_Sesión", text="Razón de Terminación de Sesión")
        self.tabla.heading("", text="")

        self.tabla.column("#0", width=0, stretch=False)
        self.tabla.column("ID", anchor="center", width=50)
        self.tabla.column("ID_Sesion", anchor="center", width=120)
        self.tabla.column("ID_Conexión_unico", anchor="center", width=150)
        self.tabla.column("Usuario", anchor="center", width=100)
        self.tabla.column("IP_NAS_AP", anchor="center", width=100)
        self.tabla.column("Tipo__conexión", anchor="center", width=120)
        self.tabla.column("Inicio_de_Conexión_Dia", anchor="center", width=120)
        self.tabla.column("Inicio_de_Conexión_Hora", anchor="center", width=120)
        self.tabla.column("FIN_de_Conexión_Dia", anchor="center", width=120)
        self.tabla.column("FIN_de_Conexión_Hora", anchor="center", width=120)
        self.tabla.column("Session_Time", anchor="center", width=100)
        self.tabla.column("Input_Octects", anchor="center", width=120)
        self.tabla.column("Output_Octects", anchor="center", width=120)
        self.tabla.column("MAC_AP", anchor="center", width=150)
        self.tabla.column("MAC_Cliente", anchor="center", width=120)
        self.tabla.column("Razon_de_Terminación_de_Sesión", anchor="center", width=150)
        self.tabla.column("", anchor="center", width=0, stretch=False)

        self.tabla.pack()

        self.calcular_trafico_button = Button(self, text="Calcular Tráfico", command=self.calcularTrafico)
        self.calcular_trafico_button.pack()

        self.exportar_excel_button = Button(self, text="Exportar a Excel", command=self.exportarXLSX)
        self.exportar_excel_button.pack()

        self.formatos = {
            'ID': r"^\d+$",
            'ID_Sesion': r"^(([0-9]|[A-F]){8}|([0-9]|[A-F]){16})(-([0-9]|[A-F]){8})?$",
            'ID_Conexión_unico': r"^([0-9]|[a-f]){16}$",
            'Usuario': r"^.*$",
            'IP_NAS_AP': r"^(?:\d{1,3}\.){3}\d{1,3}$",
            'Tipo__conexión': r"^Wireless-802.11$",
            'Inicio_de_Conexión_Dia': r"^\d{4}-\d{2}-\d{2}$",
            'Inicio_de_Conexión_Hora': r"^\d{2}:\d{2}:\d{2}$",
            'FIN_de_Conexión_Dia': r"^\d{4}-\d{2}-\d{2}$",
            'FIN_de_Conexión_Hora': r"^\d{2}:\d{2}:\d{2}$",
            'Session_Time': r"^\d+$",
            'Input_Octects': r"^\d+$",
            'Output_Octects': r"^\d+$",
            'MAC_AP': r"^(([A-F]|[0-9]){2}-){5}([A-F]|[0-9]){2}:[A-Z]{4}$",
            'MAC_Cliente': r"^(([A-F]|[0-9]){2}-){5}([A-F]|[0-9]){2}$",
            'Razon_de_Terminación_de_Sesión': r"^.*$",
            '': r"^.*$"
        }

        self.encabezados = []
        self.datos_csv = []
        self.datos_filtrados = []
        self.datos_filtrados_fecha = []

    def importarCSV(self):
        ruta_archivo = filedialog.askopenfilename(filetypes=[('Archivos CSV', '*.csv')])

        if ruta_archivo:
            try:
                with open(ruta_archivo, 'r') as archivo:
                    lector_csv = csv.reader(archivo)
                    self.encabezados = next(lector_csv)
                    self.datos_csv = list(lector_csv)

                    # Limpiar la tabla existente antes de cargar los nuevos datos
                    self.tabla.delete(*self.tabla.get_children())

                    for row in self.datos_csv:
                        self.tabla.insert("", "end", values=row)
            except FileNotFoundError:
                messagebox.showerror("Error", "Archivo no encontrado.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        self.manejarErrores()


    def exportarXLSX(self):
        ruta_guardar = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                    filetypes=[('Archivos de Excel', '*.xlsx')])
        if ruta_guardar:
            try:
                columnas_seleccionadas = [4, 6, 8, 11, 12]
                datos_seleccionados = [[row[i] for i in columnas_seleccionadas] for row in
                                       self.datos_filtrados_fecha]

                df = pd.DataFrame(datos_seleccionados,
                                  columns=[self.encabezados[i] for i in columnas_seleccionadas])

                df.to_excel(ruta_guardar, index=False)
                messagebox.showinfo("Información", "El archivo se ha exportado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

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

    def calcularTrafico(self):
        fecha_inicio = self.fecha_inicio_entry.get()
        fecha_fin = self.fecha_fin_entry.get()

        for row in self.datos_filtrados:
            inicio_conexion_dia = row[6]
            fin_conexion_dia = row[8]
            if (fecha_inicio <= inicio_conexion_dia <= fecha_fin) and (
                    fecha_inicio <= fin_conexion_dia <= fecha_fin):
                self.datos_filtrados_fecha.append(row)

        ap_trafico_maximo = None
        trafico_maximo = 0
        for row in self.datos_filtrados_fecha:
            input_octets = int(row[11])
            output_octets = int(row[12])
            trafico = input_octets + output_octets
            if trafico > trafico_maximo:
                trafico_maximo = trafico
                ap_trafico_maximo = row[4]

        if ap_trafico_maximo:
            messagebox.showinfo("Resultado",
                                f"El AP con más tráfico en el rango de fechas proporcionado es: {ap_trafico_maximo}")
        else:
            messagebox.showinfo("Resultado", "No se encontraron datos dentro del rango de fechas proporcionado.")

trafico_gui = TraficoGUI()
trafico_gui.mainloop()