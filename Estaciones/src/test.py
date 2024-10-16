from cosas import *

def test_leer_fichero(fichero):
    lista = leer_fichero(fichero)
    print(f'El numero de estaciones es {len(lista)}')
    print(lista[0])

def test_filtra_estaciones_libres(fichero, k):
    lista = leer_fichero(fichero)
    print(estaciones_libres(lista, k))

def test_estaciones_cercanas_a_ubicacion(fichero, punto, k):
    lista = leer_fichero(fichero)
    print(estaciones_cercanas_a_ubicacion(lista, punto, k))

def test_media_coordenadas(fichero):
    lista = leer_fichero(fichero)
    print(media_coordenadas(lista))

def main():
    fichero = './data/estaciones.csv'
    #test_leer_fichero(fichero)
    #test_filtra_estaciones_libres(fichero, 10)
    #test_estaciones_cercanas_a_ubicacion(fichero, punto(37.391,-5.98), 2)
    test_media_coordenadas(fichero)

if __name__ == '__main__':
    main()