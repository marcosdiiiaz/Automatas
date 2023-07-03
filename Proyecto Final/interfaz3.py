import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
from ap_traffic3 import Trafico

# --- Ventanas --------------------
class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Seguimiento del tráfico de Access Point')
        self.geometry('1920x1080')
        self.trafico = Trafico()
        

        # --- Frames ---------------------
        fra_herramientas = tk.Frame(self, borderwidth=2, relief=tk.FLAT, bg='blue')
        fra_herramientas.place(anchor='center', relx=0.5, rely=0.085)
        fra_borde00 = tk.Frame(fra_herramientas, bg='blue')
        fra_borde00.pack(padx=682, pady=60)

        # --- Etiquetas ------------------
        et_fi = tk.Label(fra_herramientas, text='Fecha Inicial:', bg='blue')
        et_fi.place(anchor='center', relx=0.3, rely=0.37)
        et_ff = tk.Label(fra_herramientas, text='Fecha Final:', bg='blue')
        et_ff.place(anchor='center', relx=0.5, rely=0.37)

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
        self.tabla00['columns'] = ('#', 'Columna1', 'Columna2', 'Columna3')  # Agregar columnas al Treeview
        self.tabla00.heading('#', text='#')
        self.tabla00.heading('Columna1', text='Columna1')
        self.tabla00.heading('Columna2', text='Columna2')
        self.tabla00.heading('Columna3', text='Columna3')
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
            columnas = ['#'] + list(df.columns)  # Agregar la columna de enumeración
            self.tabla00['columns'] = columnas
            for columna in columnas:
                self.tabla00.heading(columna, text=columna)

            # Agregar las filas del DataFrame al TreeView
            self.tabla00.delete(*self.tabla00.get_children())
            self.contador_filas = 0  # Reiniciar el contador de filas
            for _, fila in df.iterrows():
                self.contador_filas += 1  # Incrementar el contador de filas
                values = [self.contador_filas] + list(fila.values)  # Agregar el número de fila
                self.tabla00.insert('', tk.END, values=values)
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
