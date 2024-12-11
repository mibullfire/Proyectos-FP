from reservas import *
from colorama import Fore

def test_lee_reservas(fichero:str)->None:
    print(Fore.RED+"\nTesteando lee_reservas")
    res = lee_reservas(fichero)
    print(f"Reservas: {len(res)}")
    print(res[:3])

def test_total_fecturado(lista_reservas:List[Reserva], fecha_ini:Optional[date]=None, fecha_fin:Optional[date]=None)->None:
    print(Fore.GREEN+"\nTesteando total_facturado")
    print(f"Total facturado: {total_facturado(lista_reservas, fecha_ini, fecha_fin)}")

def main():
    fichero = './data/reservas.csv'
    lista = lee_reservas(fichero)
    test_lee_reservas(fichero)
    test_total_fecturado(lista, fecha_ini=parse_fecha('2022-02-01'))
    Fore.RESET

if __name__ == "__main__":
    main()