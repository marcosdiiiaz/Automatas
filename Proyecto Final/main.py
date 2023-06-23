import re
import pandas as pd
from datetime import date as dt

# Seguimiento del tráfico de AP, para determinar cuál es el AP que más tráfico
# (Input Octets + Output Octets) ha tenido en un período de tiempo (rango de fechas).
# Debe incluir la posibilidad de ingresar un rango de fechas.

path_archivo = ''
datos = pd.read_csv(path_archivo)
