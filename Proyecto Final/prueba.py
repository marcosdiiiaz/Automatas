import csv
import re

def calcular_trafico_ap(ruta_archivo, fecha_inicio, fecha_fin):
    trafico_ap = {}

    with open(ruta_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        encabezados = next(lector_csv)  # Leer la primera fila de encabezados

        # Obtener los índices de las columnas relevantes
        indice_input_octets = encabezados.index('Input_Octects')
        indice_output_octets = encabezados.index('Output_Octects')
        indice_ip_nas_ap = encabezados.index('IP_NAS_AP')
        indice_inicio_conexion_dia = encabezados.index('Inicio_de_Conexión_Dia')

        for fila in lector_csv:
            try:
                # Obtener los valores relevantes de la fila
                input_octets = int(fila[indice_input_octets])
                output_octets = int(fila[indice_output_octets])
                ip_nas_ap = fila[indice_ip_nas_ap]
                inicio_conexion_dia = fila[indice_inicio_conexion_dia]

                # Verificar si la fecha de inicio de conexión está dentro del rango especificado
                if re.match(r'\d{4}-\d{2}-\d{2}', inicio_conexion_dia):
                    if fecha_inicio <= inicio_conexion_dia <= fecha_fin:
                        # Calcular el tráfico total del AP sumando los octetos de entrada y salida
                        trafico_total = input_octets + output_octets

                        # Actualizar el diccionario de tráfico del AP
                        if ip_nas_ap in trafico_ap:
                            trafico_ap[ip_nas_ap] += trafico_total
                        else:
                            trafico_ap[ip_nas_ap] = trafico_total
            except ValueError:
                # Ignorar filas con valores no numéricos en la columna "Input_Octects"
                continue

    # Obtener el AP con mayor tráfico
    ap_max_trafico = max(trafico_ap, key=trafico_ap.get)
    trafico_maximo = trafico_ap[ap_max_trafico]

    return ap_max_trafico, trafico_maximo

# Ejemplo de uso
ruta_archivo = '/home/marcos/Escritorio/export-2019-to-now-v4.csv'
fecha_inicio = input('Ingrese una fecha inicial, formato aaaa-mm-dd: ')
fecha_fin = input('Ingrese una fecha final, formato aaaa-mm-dd: ')

ap_max_trafico, trafico_maximo = calcular_trafico_ap(ruta_archivo, fecha_inicio, fecha_fin)

print(f"El AP con más tráfico en el período {fecha_inicio} - {fecha_fin} es: {ap_max_trafico}")
print(f"Tráfico máximo: {trafico_maximo} octetos")
