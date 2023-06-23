import re
import pandas as pd
import tkinter as tk
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

path_archivo = '/home/juan-4u41/Escritorio/2023/Autómatas y gramática/Otros/export-2019-to-now-v4.csv'
d = pd.read_csv(path_archivo)
