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
