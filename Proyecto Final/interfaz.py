import tkinter as tk
from tkinter import ttk, filedialog, messagebox, font
from datetime import datetime
from ap_traffic3 import Trafico

# --- Ventanas --------------------
class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Seguimiento del tráfico de Access Point')
        self.configure(bg='#343434')
        self.geometry('1920x1080')
        self.trafico = Trafico()

        # --- Frames ---------------------
        fra_herramientas = tk.Frame(self, borderwidth=2, relief=tk.FLAT, bg='#2c2c2c')
        fra_herramientas.place(anchor='center', relx=0.5, rely=0.085)
        fra_borde00 = tk.Frame(fra_herramientas, bg='#2c2c2c')
        fra_borde00.pack(padx=682, pady=60)

        # --- Etiquetas ------------------
        et_fi = tk.Label(fra_herramientas, text='Fecha Inicial', fg='#dde8ed', bg='#2c2c2c')
        et_fi.place(anchor='center', relx=0.4, rely=0.15)

        et_ff = tk.Label(fra_herramientas, text='Fecha Final', fg='#dde8ed', bg='#2c2c2c')
        et_ff.place(anchor='center', relx=0.6, rely=0.15)

        font_size = 12  # Tamaño de fuente deseado
        font_style = font.Font(size=font_size, weight="bold")  # Establecer weight como "bold"
        et_fi['font'] = font_style
        et_ff['font'] = font_style

        # --- Entradas -------------------
        self.ent_fi = tk.Entry(fra_herramientas)
        self.ent_fi.place(anchor='center', relx=0.4, rely=0.37, height=30)
        self.ent_ff = tk.Entry(fra_herramientas)
        self.ent_ff.place(anchor='center', relx=0.6, rely=0.37, height=30)

        # --- Botones --------------------
        btn_ayuda = tk.Button(fra_herramientas, text='Ayuda')
        btn_ayuda.place(anchor='center', relx=0.1, rely=0.37, width=150, height=30)

        btn_importar = tk.Button(fra_herramientas, text='Importar CSV', command=self.trafico.importarCSV)
        btn_importar.place(anchor='center', relx=0.1, rely=0.63, width=150, height=30)

        self.btn_calcular = tk.Button(fra_herramientas, text='Calcular Tráfico', command=self.calcularTrafico)
        self.btn_calcular.place(anchor='center', relx=0.5, rely=0.63, width=150, height=30)

        btn_tabla = tk.Button(fra_herramientas, text='Ver Tabla', command=self.verTabla)
        btn_tabla.place(anchor='center', relx=0.9, rely=0.37, width=150, height=30)

        btn_exportar = tk.Button(fra_herramientas, text='Exportar Excel', command=self.exportarXLSX)
        btn_exportar.place(anchor='center', relx=0.9, rely=0.63, width=150, height=30)

        # --- Tablas ---------------------
        self.tabla00 = ttk.Treeview(self)
        self.tabla00.place(anchor='center', relx=0.5, rely=0.5)
        self.tabla00['columns'] = ('ColumnaAP', 'ColumnaInicio', 'ColumnaFin', 'ColumnaInput', 'ColumnaOutput')
        self.tabla00.heading('#0', text='#')
        self.tabla00.heading('ColumnaAP', text='IP NAS AP')
        self.tabla00.heading('ColumnaInicio', text='Inicio de Conexión Día')
        self.tabla00.heading('ColumnaFin', text='Fin de Conexión Día')
        self.tabla00.heading('ColumnaInput', text='Input Octects')
        self.tabla00.heading('ColumnaOutput', text='Output Octects')
        self.contador_filas = 0  # Variable de contador de filas

        self.mainloop()

    # --- Funciones ----------------------
    def calcularTrafico(self):
        subventana_calcular = SubventanaCalcular(self, 'Calcular Tráfico', '¿En qué rango quiere calcular el tráfico?')
        opcion = subventana_calcular.mostrar()
        if opcion == 'Rango Abierto':
            fecha_inicio = self.ent_fi.get()
            fecha_fin = self.ent_ff.get()
            self.trafico.calcularRangoAbierto(fecha_inicio, fecha_fin)
        elif opcion == 'Rango Cerrado':
            fecha_inicio = self.ent_fi.get()
            fecha_fin = self.ent_ff.get()
            self.trafico.calcularRangoCerrado(fecha_inicio, fecha_fin)

    def verTabla(self):
        subventana_ver_tabla = SubventanaVerTabla(self, 'Ver Tabla', '¿Qué tabla quiere ver?')
        opcion = subventana_ver_tabla.mostrar()
        df = self.trafico.actualizarTabla(opcion)  # Obtener el DataFrame df
        if df is not None:
            # Configurar las columnas del TreeView
            columnas = ['IP NAS AP', 'Inicio de Conexión Día', 'Fin de Conexión Día', 'Input Octects', 'Output Octects']
            self.tabla00['columns'] = columnas
            for columna in columnas:
                self.tabla00.heading(columna, text=columna)

            # Agregar las filas del DataFrame al TreeView
            self.tabla00.delete(*self.tabla00.get_children())
            self.contador_filas = 0  # Reiniciar el contador de filas
            for _, fila in df.iterrows():
                self.contador_filas += 1
                values = list(fila.values)  # Obtener los valores de la fila
                self.tabla00.insert('', tk.END, text=(str(self.contador_filas)), values=values)
        else:
            messagebox.showerror('Error', 'No hay datos.')

    def exportarXLSX(self):
        subventana_exportar = SubventanaExportar(self, 'Exportar XLSX', '¿Qué rango quiere exportar?')
        opcion = subventana_exportar.mostrar()
        if opcion == 'Rango Abierto':
            self.trafico.exportarAbiertoXLSX()
        elif opcion == 'Rango Cerrado':
            self.trafico.exportarCerradoXLSX()


# --- Complementos -----------------------
class Subventana(tk.Toplevel):
    def __init__(self, parent, title, question):
        super().__init__(parent)
        self.geometry('300x100')
        self.title(title)
        self.question = question
        self.opcion = None

        self.et_opcion = tk.Label(self, text=self.question)
        self.et_opcion.pack(pady=10)

    def opcion_abierto(self):
        self.opcion = 'Rango Abierto'
        self.destroy()

    def opcion_cerrado(self):
        self.opcion = 'Rango Cerrado'
        self.destroy()

    def mostrar(self):
        self.wait_window()
        return self.opcion


class SubventanaCalcular(Subventana):
    def __init__(self, parent, title, question):
        super().__init__(parent, title, question)

        btn_abierto = tk.Button(self, text='Rango Abierto', command=self.opcion_abierto)
        btn_abierto.pack(side=tk.LEFT, padx=10)

        btn_cerrado = tk.Button(self, text='Rango Cerrado', command=self.opcion_cerrado)
        btn_cerrado.pack(side=tk.LEFT, padx=10)

class SubventanaVerTabla(Subventana):
    def __init__(self, parent, title, question):
        super().__init__(parent, title, question)

        btn_abierto = tk.Button(self, text='Rango Abierto', command=self.opcion_abierto)
        btn_abierto.pack(side=tk.LEFT, padx=10)

        btn_cerrado = tk.Button(self, text='Rango Cerrado', command=self.opcion_cerrado)
        btn_cerrado.pack(side=tk.LEFT, padx=10)

class SubventanaExportar(Subventana):
    def __init__(self, parent, title, question):
        super().__init__(parent, title, question)

        btn_abierto = tk.Button(self, text='Rango Abierto', command=self.opcion_abierto)
        btn_abierto.pack(side=tk.LEFT, padx=10)

        btn_cerrado = tk.Button(self, text='Rango Cerrado', command=self.opcion_cerrado)
        btn_cerrado.pack(side=tk.LEFT, padx=10)


ventana = Ventana()
ventana.mainloop()