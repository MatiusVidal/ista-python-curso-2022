import pandas as pd
import matplotlib.pyplot as plt
import csv

informacion_estudiate = pd.read_csv('datos\estudiante.csv')
print('LISTA DE ESTUDIANTES')

print(informacion_estudiate)

informacion_asistencia = pd.read_csv('datos\datos_asistencia.csv')

print('LISTA DE ASISTENCIAS')

print(informacion_asistencia)

informacion_del_estudiante = pd.merge(informacion_estudiate,informacion_asistencia, how='right')

print(informacion_del_estudiante)

print('ESTUDIANTES POR CEDULA = 1103456034')

print(informacion_del_estudiante[informacion_del_estudiante.cedula == 1103456034])

informacion_del_estudiante[informacion_del_estudiante.cedula == 1103456034].to_csv('datos\datos_reporte_1103456034.csv', index=True)

informacion_del_estudiante[informacion_del_estudiante.cedula == 1103456034]['fecha_dia'].value_counts().plot(kind='bar')

plt.show()

