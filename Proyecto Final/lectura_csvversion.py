import re
import csv
from datetime import date as dt

# Seguimiento del tráfico de AP, para determinar cuál es el AP que más tráfico
# (Input Octets + Output Octets) ha tenido en un período de tiempo (rango de fechas).
# Debe incluir la posibilidad de ingresar un rango de fechas.

# Tenemos 16 columnas:
# ID,
# ID_Sesion,
# ID_Conexión_unico,
# Usuario,
# IP_NAS_AP,
# Tipo__conexión,
# Inicio_de_Conexión_Dia,
# Inicio_de_Conexión_Hora,
# FIN_de_Conexión_Dia,
# FIN_de_Conexión_Hora,
# Session_Time,
# Input_Octects,
# Output_Octects,
# MAC_AP,
# MAC_Cliente,
# Razon_de_Terminación_de_Sesión

path_archivo = '/home/marcos/Escritorio/export-2019-to-now-v4.csv'

with open(path_archivo, 'r') as archivo_csv:
    reader = csv.reader(archivo_csv)
    for i, fila in enumerate(reader):
        if i < 5:  # Imprime solo las primeras 5 filas
            print(fila)
