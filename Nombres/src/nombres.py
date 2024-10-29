from collections import namedtuple
import csv
from datetime import *
import matplotlib.pyplot as plt
from typing import *

FrecuenciaNombre = namedtuple('FrecuenciaNombre', 'año,nombre,frecuencia,genero')

# Ejercicio 1
def leer_fichero(fichero:str)->list[FrecuenciaNombre]:
    with open (fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        return [FrecuenciaNombre(int(año),nombre,int(frecuencia),genero) for año,nombre,frecuencia,genero in lector]

# Ejercicio 2
def filtrar_por_genero(lista:list[FrecuenciaNombre], genero:str)->list[FrecuenciaNombre]:
    return [i for i in lista if i.genero == genero]

# Ejercicio 3
def calcular_nombres(lista:list[FrecuenciaNombre], genero:str=None)->set:
    return set(i.nombre for i in lista if (genero == None or i.genero == genero))

# Ejercicio 4
def calcular_top_nombres_de_año(lista:list[FrecuenciaNombre], año:int, limite:int=10, genero:str=None)->list:
    res = [(i.nombre, i.frecuencia) for i in lista if i.año == año and (genero == None or i.genero == genero)]
    return sorted(res, key = lambda x: x[1], reverse=True)[:limite]

# Ejercicio 5
def calcular_nombres_ambos_generos(lista:list[FrecuenciaNombre])->set:
    hombres = calcular_nombres(lista, 'Hombre')
    mujeres = calcular_nombres(lista, 'Mujer')
    return set(i for i in hombres if i in mujeres)

# Ejercicio 6
def calcular_nombres_compuestos(lista:list[FrecuenciaNombre], genero:str=None)->set:
    nombres = calcular_nombres(lista, genero)
    return sorted(set(i for i in nombres if ' ' in i))

# Ejercicio 7
def calcular_nombre_mas_frecuente_años(lista:list[FrecuenciaNombre], nombre:str, año_inicial:int, año_final:int)->float:
    res = [i.frecuencia for i in lista if (i.nombre == nombre and año_inicial <= i.año <= año_final)]
    return sum(res)/len(res) if len(res) > 0 else 0

# Ejercicioo 8
def calcular_nombre_mas_frecuente_año_genero(lista:list[FrecuenciaNombre], año:int, genero:str):
    return max([i for i in lista if i.año == año and i.genero == genero], key = lambda x: x.frecuencia).nombre

# Ejercicio 9
def calcular_año_mas_frecuencia_nombre(lista:list[FrecuenciaNombre], nombre:str)->int:
    return max([i for i in lista if i.nombre == nombre], key = lambda x: x.frecuencia).año

################################################################################################################
###################################       EJERCICIOS DE DICCIONARIOS         ###################################
################################################################################################################
# Ejercicio 10
def calcular_nombres_mas_frecuentes(lista:list[FrecuenciaNombre], genero:str, decada:int, n:int)->list:
    diccionario = {}
    for i in lista:
        if (i.genero == genero and str(i.año)[2] == str(decada)[2]):
            diccionario[i.nombre] = diccionario.get(i.nombre, 0) + i.frecuencia
    return sorted(diccionario.items(), key = lambda x: x[1], reverse=True)[:n]

# Ejercicio 11
def calcular_año_frecuencia_por_nombre(lista:list[FrecuenciaNombre], genero:str)->dict:
    diccionario = {}
    for i in lista:
        if i.genero == genero:
            diccionario[i.nombre] = diccionario.get(i.nombre, []) + [(i.año, i.frecuencia)]
    return diccionario

# Ejercicio 12
def calcular_nombre_mas_frecuente_por_año(lista:list[FrecuenciaNombre], genero:str)->list[tuple]:
    diccionario = {}
    for i in lista:
        if i.genero == genero:
            diccionario[i.año] = diccionario.get(i.año, []) + [(i.nombre, i.frecuencia)]
    return [(año, max(valores, key=lambda x: x[1])[0], max(valores, key=lambda x: x[1])[1]) for año, valores in diccionario.items()]

# Ejercicio 13
def calcular_frecuencia_por_año(lista:list[FrecuenciaNombre], nombre:str)->list[(int, int)]:
    return sorted([(i.año, i.frecuencia) for i in lista if i.nombre == nombre], key = lambda x:x[0])

# Ejercicio 14
def mostrar_evolucion_por_año(lista:list[FrecuenciaNombre], nombre:str)->None:
    diccionario = {}
    for i in lista:
        if i.nombre == nombre:
            diccionario[i.año] = diccionario.get(i.año, 0) + i.frecuencia

    años = list(diccionario.keys())
    frecuencias = list(diccionario.values())

    plt.plot(años, frecuencias)
    plt.title("Evolución del nombre '{}'".format(nombre))
    plt.show()
    
# Ejercicio 15
def calcular_frecuencias_por_nombre(lista:list[FrecuenciaNombre]) -> Dict[str, int]:
    diccionario = {}
    for i in lista:
        diccionario[i.nombre] = diccionario.get(i.nombre, 0) + i.frecuencia
    return diccionario
# Ejercicio 16
def mostrar_frecuencias_nombres(lista:list[FrecuenciaNombre], limite:int=10)->None:
    diccionario = calcular_frecuencias_por_nombre(lista)
    nombres = sorted(diccionario.items(), key = lambda x: x[1], reverse=True)[:limite]
    nombres, frecuencias = zip(*nombres)    
    plt.bar(nombres, frecuencias)
    plt.xticks(rotation=80)
    plt.title("Frecuencia de los {} nombres más comunes".format(limite))
    plt.show()