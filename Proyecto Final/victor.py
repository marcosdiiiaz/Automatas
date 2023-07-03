import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import re
import os

# Crear la ventana principal
root = tk.Tk()
root.title("Registro de Conexiones")

# Función para importar el archivo CSV
def importar_csv():
    # Abrir el cuadro de diálogo para seleccionar el archivo
    archivo = filedialog.askopenfilename(filetypes=[("Archivo CSV", "*.csv")])

    # Leer el archivo CSV y crear un DataFrame
    global df
    df = pd.read_csv(archivo)

    # Eliminar las filas que no tienen 16 valores
    df = df.dropna(thresh=16)

    # Obtener solo el nombre del archivo
    nombre_archivo = os.path.basename(archivo)

    # Actualizar la etiqueta de la ruta del archivo con el nombre
    ruta_label.config(text=nombre_archivo)

# Crear el botón para importar el archivo CSV
importar_button = ttk.Button(root, text="Importar CSV", command=importar_csv)
importar_button.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

# Crear la etiqueta para mostrar la ruta del archivo
ruta_label = ttk.Label(root, text="")
ruta_label.grid(column=1, row=0, padx=5, pady=5, sticky=tk.W)

# Definir las variables para entrada de datos
busqueda_entry = ttk.Entry(root)
busqueda_entry.grid(column=1, row=1, padx=5, pady=5, sticky=tk.W)
fecha_inicio_entry = ttk.Entry(root)
fecha_inicio_entry.grid(column=2, row=1, padx=5, pady=5, sticky=tk.W)
fecha_fin_entry = ttk.Entry(root)
fecha_fin_entry.grid(column=3, row=1, padx=5, pady=5, sticky=tk.W)

# Definir la variable df_resultado
df_resultado = pd.DataFrame()

# Crear una función para buscar en el DataFrame
def buscar():
    # Obtener los valores de búsqueda y fecha
    busqueda = busqueda_entry.get()
    fecha_inicio = fecha_inicio_entry.get()
    fecha_fin = fecha_fin_entry.get()

    # Validar el formato de fecha
    fecha_regex = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(fecha_regex, fecha_inicio) or not re.match(fecha_regex, fecha_fin):
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, "Error: El formato de fecha es inválido. Por favor ingrese una fecha en el formato AAAA-MM-DD.")
    else:
        # Expresión regular para el usuario
        usuario_regex = r'^[a-zA-Z0-9_-]+$'

        # Expresión regular para la fecha
        fecha_regex = r'^[0-9-]+$'

        # Expresión regular para la dirección MAC
        mac_regex = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'

        # Filtrar las filas según las expresiones regulares
        df_filtrado = df[df['Usuario'].str.match(usuario_regex, na=False) &
                         df['Inicio_de_Conexión_Dia'].str.match(fecha_regex, na=False) &
                         df['FIN_de_Conexión_Dia'].str.match(fecha_regex, na=False) &
                         df['MAC_Cliente'].str.match(mac_regex, na=False)]

        # Filtrar las filas por búsqueda y fecha y asignarlas a un nuevo DataFrame
        df_filtrado = df_filtrado.loc[(df_filtrado['Usuario'].str.contains(busqueda, na=False)) &
                                      (df_filtrado['Inicio_de_Conexión_Dia'].between(fecha_inicio, fecha_fin))]

        # Seleccionar las columnas relevantes y mostrar el resultado
        global df_resultado
        df_resultado = df_filtrado.loc[:, ['Usuario', 'Inicio_de_Conexión_Dia', 'FIN_de_Conexión_Dia', 'MAC_Cliente']]
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, df_resultado.to_string(index=False))

buscar_button = ttk.Button(root, text="Buscar", command=buscar)
buscar_button.grid(column=4, row=1, padx=5, pady=5, sticky=tk.W)

# Crear el botón para exportar a Excel
def exportar_excel():
    # Abrir el cuadro de diálogo para seleccionar la ubicación del archivo
    archivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivo de Excel", "*.xlsx")])

    # Guardar el DataFrame en el archivo de Excel
    df_resultado.to_excel(archivo, index=False)

exportar_button = ttk.Button(root, text="Exportar a Excel", command=exportar_excel)
exportar_button.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)

# Crear el widget de texto para mostrar el resultado
resultado_frame = ttk.Frame(root)
resultado_frame.grid(column=0, row=2, columnspan=5, padx=5, pady=5, sticky=tk.NSEW)

resultado_text = tk.Text(resultado_frame, height=20, width=80)
resultado_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(resultado_frame, orient=tk.VERTICAL, command=resultado_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

resultado_text.config(yscrollcommand=scrollbar.set)

# Iniciar la ventana principal
root.mainloop()