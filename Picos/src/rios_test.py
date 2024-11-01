# -*- coding: utf-8 -*-

from rios import *



def test_recorridos(rios):
    print ('-'*10, 'RECORRIDOS')
    print ('-'*10, 'mostrar-rios1')
    mostrar_rios1(rios)
    print ('-'*10, 'mostrar-rios2')
    mostrar_rios2(rios)
    print ('-'*10, 'mostrar-rios3')
    mostrar_rios3(rios)
    print ('-'*10, 'mostrar-rios4')
    mostrar_rios4(rios)
    
    
def test_filtrado(rios):
    print ('-'*10, 'FILTRADO')
    print ('-'*10, 'filtra_rios_de_continente ', 'África')
    rios_africanos = filtra_rios_de_continente(rios, 'África')
    mostrar_rios1(rios_africanos)

def test_seleccion(rios):
    print ('-'*10, 'SELECCION/TRANSFORMACION')
    print ('-'*10, 'selecciona_nombre_longitud ')
    nombre_longitud_rios = selecciona_nombre_longitud(rios)
    print(nombre_longitud_rios)
    print ('-'*10, 'selecciona_nombre_longitud_miles_km ')
    nombre_longitud_rios_miles = selecciona_nombre_longitud_miles_km(rios)
    print(nombre_longitud_rios_miles)
    print ('-'*10, 'selecciona_nombre ')
    nombre_rios = selecciona_nombre(rios)
    print(nombre_rios)

def test_filtrado_seleccion(rios):
    print ('-'*10, 'FILTRADO Y SELECCION/TRANSFORMACION')
    print ('-'*10, 'selecciona_nombre_rios_de_continente ', 'Asia')
    rios_asiaticos = selecciona_nombre_rios_de_continente(rios, 'Asia')
    mostrar_rios1(rios_asiaticos)
    
def test_eliminacion_duplicados(rios):
    print ('-'*10, 'ELIMINACION DUPLICADOS')
    print ('-'*10, 'selecciona_continentes_con_duplicados')
    lista_continentes = selecciona_continentes_con_duplicados(rios)
    print(lista_continentes)
    print ('-'*10, 'selecciona_continentes_sin_duplicados')
    conj_continentes = selecciona_continentes_sin_duplicados(rios)
    print(conj_continentes)
    print ('-'*10, 'selecciona_continentes_sin_duplicados_ordenado_1')
    lista_ord1= selecciona_continentes_sin_duplicados_ordenado_1(rios)
    print(lista_ord1)
    print ('-'*10, 'selecciona_continentes_sin_duplicados_ordenado_2')
    lista_ord2 = selecciona_continentes_sin_duplicados_ordenado_2(rios)
    print(lista_ord2)
    
def test_ordenacion_max_min(rios):
    print ('-'*10, 'ORDENACION, MAXIMO Y MINIMO')
    print ('-'*10, 'selecciona_longitudes_ordenadas_1')
    print(selecciona_longitudes_ordenadas_1(rios))
    print ('-'*10, 'selecciona_longitudes_ordenadas_2')
    print(selecciona_longitudes_ordenadas_2(rios))
    print ('-'*10, 'selecciona_longitudes_ordenadas_inv_1')
    print(selecciona_longitudes_ordenadas_inv_1(rios))
    print ('-'*10, 'selecciona_longitudes_ordenadas_inv_2')
    print(selecciona_longitudes_ordenadas_inv_2(rios))
    print ('-'*10, 'longitud_max')
    print(longitud_max(rios))
    print ('-'*10, 'selecciona_n_longitudes_mayores', '3 mayores' )
    print(selecciona_n_longitudes_mayores(rios))
    print ('-'*10, 'selecciona_n_longitudes_mayores', '5 mayores' )
    print(selecciona_n_longitudes_mayores(rios,5))    
    print ('-'*10, 'selecciona_n_longitudes_mayores', '20 mayores' )
    print(selecciona_n_longitudes_mayores(rios,20))

def test_ordenacion_max_min_lista_tuplas(rios):
    print ('-'*10, 'ORDENACION, MAXIMO Y MINIMO CON UNA LISTA DE TUPLAS')
    print ('-'*10, 'ordenar_rios_1')
    print(ordenar_rios_1(rios))
    print ('-'*10, 'ordenar_rios_2')
    print(ordenar_rios_2(rios))
    print ('-'*10, 'ordenar_rios_inv_1')
    print(ordenar_rios_inv_1(rios))  
    print ('-'*10, 'ordenar_rios_inv_2')
    print(ordenar_rios_inv_2(rios))
    print ('-'*10, 'ordenar_rios_por_longitud_1')
    print(ordenar_rios_por_longitud_1(rios))
    print ('-'*10, 'ordenar_rios_por_longitud_2')
    print(ordenar_rios_por_longitud_2(rios))
    print ('-'*10, 'ordenar_rios_por_longitud_inv_1')
    print(ordenar_rios_por_longitud_inv_1(rios))
    print ('-'*10, 'ordenar_rios_por_longitud_inv_2')
    print(ordenar_rios_por_longitud_inv_2(rios))

def test_otras_operaciones(rios):
    print ('-'*10, 'OTRAS OPERACIONES')
    print ('-'*10, 'media_longitudes_rios_de_continente', ' Asia')
    print("Longitud media de los ríos de Asia: {}".format(media_longitudes_rios_de_continente(rios, 'Asia')))
    
    
if __name__=='__main__':
    RIOS = [Rio("Amazonas", 7062, "América del Sur"), 
            Rio("Nilo", 6853, "África"),
            Rio("Yangtsé", 6300, "Asia"), 
            Rio("Misisipi", 6275, "América del Norte"),
            Rio("Amarillo", 5464, "Asia"), 
            Rio("Mekong", 4880, "Asia"),
            Rio("Congo", 4700, "África"), 
            Rio("Danubio", 2850, "Europa")]
    
    test_recorridos(RIOS)
    test_filtrado(RIOS)
    test_seleccion(RIOS)
    test_filtrado_seleccion(RIOS)
    test_eliminacion_duplicados(RIOS)
    test_ordenacion_max_min(RIOS)
    test_ordenacion_max_min_lista_tuplas(RIOS)
    test_otras_operaciones(RIOS)
    
    