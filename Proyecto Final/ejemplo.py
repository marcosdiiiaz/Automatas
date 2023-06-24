# # Especifica el rango de fechas
# fecha_inicio = dt(2023, 1, 1)
# fecha_fin = dt(2023, 12, 31)

# # Filtra los datos por el rango de fechas
# datos_filtrados = df[(df['Fecha'] >= fecha_inicio) & (df['Fecha'] <= fecha_fin)]

# # Calcula el tráfico total para cada Access Point (AP)
# datos_agrupados = datos_filtrados.groupby('AP')['Input Octets', 'Output Octets'].sum()

# # Encuentra el AP con el mayor tráfico
# ap_mas_trafico = datos_agrupados['Input Octets'] + datos_agrupados['Output Octets']
# ap_mas_trafico = ap_mas_trafico.idxmax()

# # Imprime el resultado
# print(f"El AP con más tráfico en el período de {fecha_inicio} a {fecha_fin} es: {ap_mas_trafico}")
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Has presionado el botón!")

def main():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Elementos de Tkinter")

    # Cambiar el color de fondo de la ventana
    ventana.configure(bg='green')

    # Crear un Frame para agrupar los elementos
    frame = ttk.Frame(ventana, padding=20)
    frame.pack()

    # Crear un botón
    boton = ttk.Button(frame, text="Presionar", command=mostrar_mensaje)
    boton.pack(pady=10)

    # Crear una etiqueta
    etiqueta = ttk.Label(frame, text="Texto de ejemplo")
    etiqueta.pack(pady=10)

    # Crear un campo de entrada
    entrada = ttk.Entry(frame)
    entrada.pack(pady=10)

    # Crear una casilla de verificación
    casilla_verif = ttk.Checkbutton(frame, text="Opción 1")
    casilla_verif.pack()

    # Crear botones de opción
    opcion_1 = ttk.Radiobutton(frame, text="Opción 1")
    opcion_1.pack()
    opcion_2 = ttk.Radiobutton(frame, text="Opción 2")
    opcion_2.pack()

    # Crear una lista desplegable
    lista = tk.Listbox(frame)
    for i in range(5):
        lista.insert(tk.END, f"Elemento {i+1}")
    lista.pack(pady=10)

    # Crear un cuadro de lista desplegable
    combo = ttk.Combobox(frame)
    combo['values'] = ("Opción 1", "Opción 2", "Opción 3")
    combo.pack(pady=10)

    # Crear un lienzo
    lienzo = tk.Canvas(frame, width=200, height=200, bg="white")
    lienzo.pack(pady=10)

    # Dibujar un rectángulo en el lienzo
    lienzo.create_rectangle(50, 50, 150, 150, fill="blue")

    # Crear un contenedor Frame dentro del frame principal
    subframe = ttk.Frame(frame, padding=10)
    subframe.pack(pady=10)

    # Crear un menú
    menubar = tk.Menu(ventana)
    archivo_menu = tk.Menu(menubar, tearoff=0)
    archivo_menu.add_command(label="Abrir")
    archivo_menu.add_command(label="Guardar")
    archivo_menu.add_separator()
    archivo_menu.add_command(label="Salir", command=ventana.quit)
    menubar.add_cascade(label="Archivo", menu=archivo_menu)
    ventana.config(menu=menubar)

    # Crear una barra de desplazamiento
    scrollbar = ttk.Scrollbar(ventana)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Crear un área de texto
    texto = tk.Text(ventana, yscrollcommand=scrollbar.set)
    for i in range(20):
        texto.insert(tk.END, f"Línea {i+1}\n")
    texto.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar.config(command=texto.yview)

    # Ejecutar el bucle principal
    ventana.mainloop()

if __name__ == '__main__':
    main()
