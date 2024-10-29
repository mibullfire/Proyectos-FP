from nombres import *
from config import *
from colorama import Fore

def test_leer_fichero(fichero):
    lista = leer_fichero(fichero)
    print(Fore.BLUE + '\ntest leer fichero')
    print(f'Se han leído {len(lista)} registros.')
    print('Los tres primeros')
    for i in range(0,3):
        print(lista[i])

def test_filtra_por_genero(lista, genero):
    filtrado = filtrar_por_genero(lista, genero)
    print(Fore.CYAN + '\ntest filtra por genero')
    print(f'Número de registros para "{genero}" {len(filtrado)}')

def test_calcula_nombres(lista, genero=None):
    nombres = calcular_nombres(lista, genero)
    print(Fore.GREEN + '\ntest calcula nombres')
    print(sorted(nombres)[:10])

def test_calcular_top_nombres_año(lista, año, limite=10, genero=None):
    res = calcular_top_nombres_de_año(lista, año, limite, genero)
    print(Fore.LIGHTBLACK_EX + '\ntest calcular top nombres año')
    print(res)

def test_calcular_nombres_ambos_generos(lista):
    res = calcular_nombres_ambos_generos(lista)
    print(Fore.LIGHTBLUE_EX + ('\ntest calcular nombres ambos generos'))
    print(res)

def test_calcular_nombres_compuestos(lista, genero=None):
    res = calcular_nombres_compuestos(lista, genero)
    print(Fore.LIGHTCYAN_EX + '\ntest calcular nombres compuestos')
    print(res)

def test_calcular_nombre_mas_frecuente_años(lista, nombre, año_inicial, año_final):
    res = calcular_nombre_mas_frecuente_años(lista, nombre, año_inicial, año_final)
    print(Fore.LIGHTMAGENTA_EX + '\ntest calcular nombre más frecuente años')
    print(f'El nombre {nombre} tiene una frecuencia media de {res} entre {año_inicial} y {año_final}')

def test_calcular_nombre_mas_frecuente_año_genero(lista, año, genero):
    res = calcular_nombre_mas_frecuente_año_genero(lista, año, genero)
    print(Fore.LIGHTYELLOW_EX + '\ntest calcular nombre más frecuente año genero')
    print(f'El nombre más frecuente en {año} para el género {genero} es {res}')

def test_calcular_año_mas_frecuencia_nombre(lista, nombre):
    res = calcular_año_mas_frecuencia_nombre(lista, nombre)
    print(Fore.LIGHTWHITE_EX + '\ntest calcular año más frecuencia nombre')
    print(f'El año con más frecuencia para el nombre {nombre} es {res}')

def test_calcular_nombres_mas_frecuentes(lista, genero, decada, n):
    res = calcular_nombres_mas_frecuentes(lista, genero, decada, n)
    print(Fore.LIGHTRED_EX + '\ntest calcular nombres más frecuentes')
    print(res)

def test_calcular_año_frecuencia_por_nombre(lista, genero):
    res = calcular_año_frecuencia_por_nombre(lista, genero)
    print(Fore.YELLOW + '\ntest calcular nombres compuestos')
    for nombre, valores in res.items():
        print(f'--> {nombre}: {valores}')

def test_calcular_nombre_mas_frecuente_por_año(lista, genero):
    res = calcular_nombre_mas_frecuente_por_año(lista, genero)
    print(Fore.MAGENTA + '\ntest calcular nombre más frecuente por año')
    print(res)

def test_calcular_frecuencia_por_año(lista, nombre):
    res = calcular_frecuencia_por_año(lista, nombre)
    print(Fore.LIGHTGREEN_EX + '\ntest calcular frecuencia por año')
    print(res)

def test_mostrar_evolucion_por_año(lista, nombre):
    mostrar_evolucion_por_año(lista, nombre)

def test_calcular_frecuencias_por_nombre(lista):
    res = calcular_frecuencias_por_nombre(lista)
    print(Fore.LIGHTGREEN_EX + '\ntest calcular frecuencias por nombre')
    print(res)

def test_mostras_frecuencias_nombres(lista, limite=10):
    res = mostrar_frecuencias_nombres(lista, limite)
    print(Fore.LIGHTGREEN_EX + '\ntest mostrar frecuencias nombres')

def main():
    test_leer_fichero(fichero)
    lista = leer_fichero(fichero)
    test_filtra_por_genero(lista, 'Hombre')
    test_filtra_por_genero(lista, 'Mujer')
    test_calcula_nombres(lista)
    test_calcula_nombres(lista, 'Hombre')
    test_calcula_nombres(lista, 'Mujer')
    test_calcular_top_nombres_año(lista, 2008)
    test_calcular_top_nombres_año(lista, 2008, genero='Hombre')
    test_calcular_top_nombres_año(lista, 2008, genero='Mujer')
    test_calcular_nombres_ambos_generos(lista)
    test_calcular_nombres_compuestos(lista)
    test_calcular_nombres_compuestos(lista, 'Hombre')
    test_calcular_nombres_compuestos(lista, 'Mujer')
    test_calcular_nombre_mas_frecuente_años(lista, 'NEREA', 2005, 2010)
    test_calcular_nombre_mas_frecuente_año_genero(lista, 2017, 'Mujer')
    test_calcular_año_mas_frecuencia_nombre(lista, 'VERA')
    test_calcular_nombres_mas_frecuentes(lista, 'Hombre', 2000, 3)
    test_calcular_año_frecuencia_por_nombre(lista, 'Mujer')
    test_calcular_nombre_mas_frecuente_por_año(lista, 'Hombre')
    test_calcular_nombre_mas_frecuente_por_año(lista, 'Mujer')
    test_calcular_frecuencia_por_año(lista, 'IKER')
    test_mostrar_evolucion_por_año(lista, 'IKER')
    test_calcular_frecuencias_por_nombre(lista)
    test_mostras_frecuencias_nombres(lista)

    print(Fore.RESET)

if __name__ == '__main__':
    main()