import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
from ap_traffic import Trafico


# --- Ventana --------------------
ventana00 = tk.Tk()
ventana00.title('Seguimiento del tráfico de Access Point')
ventana00.geometry('1920x1080')

# --- Frames ---------------------
fra_herramientas = tk.Frame(ventana00, borderwidth=2, relief=tk.FLAT, bg='blue')
fra_herramientas.place(anchor='center', relx=0.5, rely=0.085)
fra_borde00 = tk.Frame(fra_herramientas, bg='blue')
fra_borde00.pack(padx=682, pady=60)



# --- Etiquetas ------------------
et_fi = tk.Label(fra_herramientas, text='Fecha Inicial:', bg='blue')
et_fi.place(anchor='center', relx=0.3, rely=0.37)
et_ff = tk.Label(fra_herramientas, text='Fecha Final:', bg='blue')
et_ff.place(anchor='center', relx=0.5, rely=0.37)

# --- Entradas -------------------
ent_fi = tk.Entry(fra_herramientas)
ent_fi.place(anchor='center', relx=0.4, rely=0.37, height=30)
ent_ff = tk.Entry(fra_herramientas)
ent_ff.place(anchor='center', relx=0.6, rely=0.37, height=30)

# --- Botones --------------------
trafico = Trafico()  # Instancia de Trafico

bot_importar = tk.Button(fra_herramientas, text='Importar CSV', command=trafico.importarCSV)
bot_importar.place(anchor='center', relx=0.1, rely=0.37, width=150, height=30)

bot_exportar = tk.Button(fra_herramientas, text='Exportar Excel', command=trafico.exportarXLSX)
bot_exportar.place(anchor='center', relx=0.9, rely=0.63, width=150, height=30)


bot_calcular = tk.Button(fra_herramientas, text='Calcular Tráfico', command=lambda: trafico.calcularTrafico(ent_fi.get(), ent_ff.get()))
bot_calcular.place(anchor='center', relx=0.5, rely=0.63, width=150, height=30)


ventana00.mainloop()