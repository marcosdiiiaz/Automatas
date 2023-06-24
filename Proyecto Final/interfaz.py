import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

# ---------- Funciones -------------------
def menu_filtrado():
    et_menu.grid_forget()
    botonCargar.grid_forget()
    botonFiltrar.grid_forget()
    botonVer.grid_forget()
    botonVolver.grid(row=1, column=0, padx=10, pady=10)

def menu_principal():
    et_menu.grid(row=1, column=0, padx=10, pady=10)
    botonCargar.grid(row=2, column=0, padx=10, pady=10)
    botonFiltrar.grid(row=3, column=0, padx=10, pady=10)
    botonVer.grid(row=4, column=0, padx=10, pady=10)
    botonVolver.grid_forget()
# ----------------------------------------

# ---------- Ventana ---------------------
# Crear la ventana principal
ventana = tk.Tk()
# Establecer el título de la ventana
ventana.title('')
# Tamaño de la ventana
ventana.geometry('1920x1080')
# ----------------------------------------

# ----------- Texto ----------------------
# Fuentes para el texto
ft_normal = Font(family='Ubuntu')
ft_negrita = Font(family='Ubuntu', weight='bold')

# Crear etiqueta principal
et_main = tk.Label(ventana, text='Seguimiento del tráfico de Access Point', font=ft_negrita)
# Posición del label
et_main.grid(row=0, column=0, padx=10, pady=10)
# Crear etiqueta Menú Principal
et_menu = tk.Label(ventana, text='Menú Principal', font=ft_negrita)
# Posición del label
et_menu.grid(row=1, column=0, padx=10, pady=10)
# ----------------------------------------

# ---------- Botones ---------------------
# Estilos para los botones
style = ttk.Style()
style.configure('Custom.TButton', font=ft_normal)

# Crear botón Cargar CSV
botonCargar = ttk.Button(ventana, text='Cargar CSV', width=20, padding=(7, 7), style='Custom.TButton')
botonCargar.grid(row=2, column=0, padx=10, pady=10)

# Crear botón Filtrado por Fechas
botonFiltrar = ttk.Button(ventana, text='Filtrado por Fechas', width=20, padding=(7, 7), style='Custom.TButton', command=menu_filtrado)
botonFiltrar.grid(row=3, column=0, padx=10, pady=10)

# Crear botón Ver CSV
botonVer = ttk.Button(ventana, text='Ver CSV', width=20, padding=(7, 7), style='Custom.TButton')
botonVer.grid(row=4, column=0, padx=10, pady=10)

# Crear botón Volver al Menú Principal
botonVolver = ttk.Button(ventana, text='Volver al Menú Principal', width=20, padding=(7, 7), style='Custom.TButton', command=menu_principal)

# Mostrar inicialmente el menú principal
menu_principal()
# ----------------------------------------

# Ejecutar bucle de la ventana
ventana.mainloop()
