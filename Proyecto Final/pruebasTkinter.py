import tkinter as tk
from tkinter import ttk
import pandas as pd

# Crear un DataFrame de ejemplo
data = {'Nombre': ['Juan', 'María', 'Carlos', 'Ana'],
        'Edad': [25, 30, 35, 28],
        'Ciudad': ['México', 'Madrid', 'Buenos Aires', 'Lima']}
df = pd.DataFrame(data)

# Crear una ventana de Tkinter
window = tk.Tk()

# Crear el TreeView
tree = ttk.Treeview(window)

# Configurar las columnas del TreeView
tree['columns'] = list(df.columns)
for column in df.columns:
    tree.heading(column, text=column)

# Agregar las filas del DataFrame al TreeView
for _, row in df.iterrows():
    values = list(row.values)
    tree.insert('', tk.END, values=values)

# Empacar el TreeView en la ventana
tree.pack()

# Iniciar el bucle principal de la aplicación
window.mainloop()
