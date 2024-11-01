# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:43:37 2019

@author: reinaqu_2
"""

from collections import namedtuple

Pico = namedtuple("Pico", "nombre altitud provincia")



def mostrar_picos1(picos):
    for pico in picos:
        print(pico)

        # -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:43:37 2019

@author: reinaqu_2
"""

from collections import namedtuple

Pico = namedtuple("Pico", "nombre altitud provincia")



def mostrar_picos1(picos):
    for pico in picos:
        print(pico)



# 2.1 Obtener una lista con los nombres de los picos ordenada alfabéticamente
# Resultado esperado: [‘Alcazaba’, ‘Llambrión’, ‘Mulhacén’, ‘Naranjo’, ‘Peña Santa’, ‘Teide’, ‘Torrecilla’, ‘Torreón’, ‘Veleta’
def nombres(lista:list[Pico])->list:
    nombres = [r.nombre for r in lista]
    return sorted(nombres)

# 2.2 Obtener una lista con la altitud en kms y el nombre de los picos
# Resultado esperado: [(3.479, ‘Mulhacén’), (1.648, ‘Torreón’), (2.596, ‘Peña Santa’), (2.519, ‘Naranjo’), (3.371, ‘Alcazaba’), (3.396, ‘Veleta’), (1.919, ‘Torrecilla’), (2.647, ‘Llambrión’), (3.718,
# ‘Teide’)]
def altitudNombres(lista:list[Pico])->list[tuple[float, str]]:
    return [(r.altitud/1000, r.nombre) for r in lista]


# 2.3 Obtener una lista con los picos que están en la provincia de Granada
# Resultado esperado: [(‘Mulhacén’, 3479, ‘Granada’), (‘Alcazaba’, 3371, ‘Granada’), (‘Veleta’, 3396,
# ‘Granada’)]
def granada(lista:list[Pico])->list[Pico]:
    return [r for r in lista if r.provincia == 'Granada']


# 2.4 Obtener una lista con la altitud y el nombre de los picos que tienen más de 2000
# metros de altitud, ordenada de mayor a menor altitud
# Resultado esperado: [(3718, ‘Teide’), (3479, ‘Mulhacén’), (3396, ‘Veleta’), (3371, ‘Alcazaba’), (2647,
# ‘Llambrión’), (2596, ‘Peña Santa’), (2519, ‘Naranjo’)]
def alturaMinima(lista:list[Pico])->list[tuple[int, str]]:
    res = [(r.altitud, r.nombre) for r in lista if r.altitud > 2000]
    return sorted(res, key=lambda x: x[0], reverse=True)


# 2.5 Obtener la suma de las altitudes de los picos que están en la provincia de León
# Resultado esperado: 5243
def sumaLeon(lista:list[Pico])->int:
    res = [r.altitud for r in lista if r.provincia == 'León']
    return sum(res)


# 2.6 Obtener el nombre y la altitud del pico más alto de la lista
# Resultado esperado: (3718, ‘Teide’)
def mayor(lista:list[Pico])->tuple[int, str]:
    return max([(r.altitud, r.nombre) for r in lista], key = lambda x:x[0])


# 2.7 Obtener la altitud media de los picos
# Resultado esperado: 2810.3333333333335
def media(lista:list[Pico])->float:
    res = [r.altitud for r in lista]
    return sum(res)/len(res)


# 2.8 Obtener una lista ordenada con las provincias donde hay picos, sin repetir ninguna
# Resultado esperado: [‘Asturias’, ‘Cádiz’, ‘Granada’, ‘León’, ‘Málaga’, ‘Santa Cruz de Tenerife’]
def provincias(lista:list[Pico])->list[str]:
    res = {r.provincia for r in lista}
    return sorted(list(res))