from flask import Flask, request
import csv
import json

app = Flask(__name__)

@app.route('/get_all_estudiantes')
def get_all_estudiantes():
    with open('datos\estudiante.csv') as files:
        read_estudiante = csv.reader(files)
        next(read_estudiante)
        estudiante_lista = []
        for fila in read_estudiante:
            estudiante_lista.append(
                {'cedula': fila[0],
                'primer_apellido': fila[1],
                'segundo_apellido': fila[2],
                'primer_nombre': fila[3],
                'segundo_nombre': fila[4]
                })
    return json.dumps(sorted(estudiante_lista, key=lambda x: x['primer_nombre'] + x['primer_apellido']))

@app.route('/registro_asis_estudiante', methods=['POST'])
def registro_asis_estudiante():
    with open('datos\datos_asistencia.csv', 'a' , newline='') as files:
        escritor_csv = csv.writer(files,delimiter=',')
        escritor_csv.writerow([
            request.json['cedula'],
            request.json['materia'],
            request.json['fecha_anio'],
            request.json['fecha_mes'],
            request.json['fecha_dia']])
    return '<h1">REGISTRO EXITOSO DE LA ASISTENCIAS</h1>'

@app.route('/buscar_por_materia/<materia>')
def buscar_por_materia(materia):
    with open('datos\datos_asistencia.csv') as archivo:
        lectura = csv.reader(archivo)
        next(lectura)
        asistencia_lista = []
        for fila in lectura:
            if fila[1] == materia:
                informacion = "si existe"
            else:
                informacion = "no existe"
    return 'la materia ' + materia + ' ' + informacion

if __name__ == '__main__':
    app.run(debug=True)