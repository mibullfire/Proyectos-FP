from consumo_electrico import *
from colorama import Fore

def test_lee_facturas(ruta_fichero: str) -> None:
    res = lee_facturas(ruta_fichero)
    print(Fore.BLUE + '\nTest lee_fecturas')
    print(f'Total facturas: {len(res)}')
    print('Mostrando las dos primeras')
    print(res[:2])
    print('Mostrando las dos últimas')
    print(res[-2:])

def test_extrae_precio_por_mes(facturas: List[Factura], tipo_tarifa: str) -> None:
    res = extrae_precio_por_mes(facturas, tipo_tarifa)
    print(Fore.CYAN + '\nTest extrae_precio_por_mes')
    print(f'Precio por mes para tarifa {tipo_tarifa}')
    for i,j in res.items():
        print(f'-> {i}: {j}')

def test_busca_vivienda_mayor_consumo_acumulado(facturas: List[Factura]) -> None:
    res = busca_vivienda_mayor_consumo_acumulado(facturas)
    print(Fore.GREEN + '\nTest busca_vivienda_mayor_consumo_acumulado')
    print(f'La vivienda con mayor consumo acumulado es la {res[0]} con un consumo total de {res[1]} kWh.')

def test_barrios_mayor_consumo_valle_medio(facturas: List[Factura], top_n: int) -> None:
    res = barrios_mayor_consumo_valle_medio(facturas, top_n)
    print(Fore.LIGHTMAGENTA_EX +'\nTest barrios_mayor_consumo_valle_medio')
    for i in res:
        print(f'- {i}')

def test_compara_importe_tipos_factura(facturas: List[Factura], id_vivienda: str) -> None:
    res = compara_importe_tipos_factura(facturas, id_vivienda)
    print(Fore.LIGHTYELLOW_EX + 'Test compara_importe_tipos_factura')
    print(f'La vivienda {id_vivienda}, haciendo un cambio de tarifa {res[0]}, habría pagado un total de {res[2]} euros en lugar de {res[1]} si hubiera cambiado de tipo de tarifa.')

def main():
    ruta_fichero = './data/consumos_sevilla_2023.csv'
    test_lee_facturas(ruta_fichero)
    facturas = lee_facturas(ruta_fichero)
    test_extrae_precio_por_mes(facturas, 'tramos')
    test_busca_vivienda_mayor_consumo_acumulado(facturas)
    test_barrios_mayor_consumo_valle_medio(facturas, 3)
    test_compara_importe_tipos_factura(facturas, '005')

if __name__ == '__main__':
    main()