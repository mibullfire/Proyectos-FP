from ovnis import *

def test_leer_fichero(fichero):
    lista = leer_fichero(fichero)
    print('Número de avistamientos:', len(lista))
    print('Primer avistamiento:', lista[0])

def test_numero_avistamientos_fecha(fichero):
    lista = leer_fichero(fichero)
    print('Número de avistamientos en 2004-10-23:', numero_avistamientos_fecha(lista, date(2010, 12, 3)))

def main():
    fichero = './data/ovnis.csv'
    test_leer_fichero(fichero)
    test_numero_avistamientos_fecha(fichero)
    
if __name__ == '__main__':
    main()