import csv
from datetime import datetime, timedelta
from typing import *
from isodate import parse_duration

# Definición de NamedTuple Participante
Participante = NamedTuple('Participante', [
    ('carrera_id', str),
    ('nombre', str),
    ('apellidos', str),
    ('edad', int),
    ('sexo', str),
    ('duracion', timedelta)
])

# Definición de NamedTuple Carrera
Carrera = NamedTuple('Carrera', [
    ('carrera_id', str),
    ('localidad', str),
    ('fecha_hora', datetime),
    ('tipo', str),
    ('distancia', int),
    ('desnivel', int),
    ('participantes', List[Participante])
])

def parseFecha(cadena:str)->datetime:
    return datetime.strptime(cadena, '%Y-%m-%d %H:%M')

def parseaDuracion(cadena:str)->timedelta:
    return parse_duration(cadena)

def leeCarreras(nomfichCarreras: str, nomfichParticipantes: str) -> List[Carrera]:
    participantes = []
    res = []

    with open(nomfichParticipantes, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)
        for CarreraID,Nombre,Apellidos,Edad,Sexo,Duracion in lector:
            participantes.append(Participante(CarreraID,Nombre,Apellidos,int(Edad),Sexo,parseaDuracion(Duracion)))
    
    with open(nomfichCarreras, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)
        for CarreraID,Localidad,FechaHora,Tipo,Distancia,Desnivel in lector:
            participantesCarrera = list(filter(lambda i: i.carrera_id == CarreraID, participantes))
            res.append(Carrera(CarreraID,Localidad,parseFecha(FechaHora),Tipo,int(Distancia),int(Desnivel),participantesCarrera))

    return res

# Ejercicio 4.1

# Función que recibe el nombre y apellidos de un participante y devuelve la carrera con mayor desnivel
# en la que haya participado. En caso de empate en el desnivel, devuelve la carrera de menor distancia.

def carreraMayorDesnivelParticipante(carreras: List[Carrera], nombre: str, apellidos: str) -> Optional[Carrera]:
    filtradoParticipante = list(filter(lambda i: nombre in [ii.nombre for ii in i.participantes] and apellidos in [ii.apellidos for ii in i.participantes], carreras))
    desnivelMinimo = min([i.desnivel for i in filtradoParticipante])
    res = list(filter(lambda i: i.desnivel == desnivelMinimo, filtradoParticipante))
    ## Devolver un resultado distinto en funcion de la respuesta:
    if len(res) == 0: return None
    if len(res) == 1: return res[0].carrera_id
    else: return min(res, key = lambda x: x.distancia)[0].carrera_id
    

# Ejercicio 4.2

# Función que recibe el identificador de una carrera y calcula el tiempo medio por kilómetro (minutos por km)
# de todos los participantes de esa carrera. Si no se puede calcular, devuelve 0
def tiempoMedioCarrera(carreras: List[Carrera], carrera_id: str) -> float:
    filtrado = list(filter(lambda x: x.carrera_id == carrera_id, carreras))[0]
    distancia = filtrado.distancia / 1000
    tiempos = [(i.duracion.total_seconds()/60)/distancia for i in filtrado.participantes]
    return sum(tiempos)/len(tiempos)


from collections import defaultdict

# Ejercicio 4.3

# Función que recibe el identificador de una carrera y devuelve un diccionario con los ganadores por categoría
# La clave es la categoría, y el valor es el nombre y apellido del ganador de esa categoría.
# La categoría se calcula por grupos de edad y sexo (por ejemplo, 46-55-HOMBRE)

Categoria = NamedTuple('Categoria', [
    ('edadMin', int),
    ('edadMax', int),
    ('sexo',str)
])

categorias: List[Categoria] = [
    Categoria(0, 15, 'HOMBRE'),
    Categoria(0, 15, 'MUJER'),
    Categoria(16, 25, 'HOMBRE'),
    Categoria(16, 25, 'MUJER'),
    Categoria(26, 35, 'HOMBRE'),
    Categoria(26, 35, 'MUJER'),
    Categoria(36, 45, 'HOMBRE'),
    Categoria(36, 45, 'MUJER'),
    Categoria(46, 55, 'HOMBRE'),
    Categoria(46, 55, 'MUJER'),
    Categoria(56, 65, 'HOMBRE'),
    Categoria(56, 65, 'MUJER'),
    Categoria(66, 150, 'HOMBRE'), # Se asume 150 como edad máxima razonable.
    Categoria(66, 150, 'MUJER'), # Se asume 150 como edad máxima razonable.
]

def participanteCategoria(cadena:Participante):
    for i in categorias:
        if i.edadMin <= cadena.edad <= i.edadMax:
            return True 
        else: False

def ganadoresPorCategoria(carreras: List[Carrera], carrera_id: str) -> Dict[str, str]:
    dicc = defaultdict(list)
    filtrado = list(filter(lambda x: x.carrera_id == carrera_id, carreras))[0].participantes
    res = {}
    for i in categorias:
        for j in filtrado:
            if participanteCategoria(j):
                dicc[i].append((j.nombre, j.apellidos, j.duracion.total_seconds()/60))
    for i in list(dicc.items()):
        participantes = i[1]
        ganador = min(participantes, key = lambda x: x[2])
        res[i[0]] = f'{ganador[0]} {ganador[1]}'
    return res

carreras = leeCarreras('./data/carreras.csv', './data/participantes.csv')
print(ganadoresPorCategoria(carreras, 'tr_cobre_23'))
