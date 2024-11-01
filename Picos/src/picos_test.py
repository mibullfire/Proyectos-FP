# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:43:48 2019

@author: reinaqu_2
"""
from picos import *
from colorama import Fore

if __name__=='__main__':
    PICOS = [Pico("Mulhacén", 3479, "Granada"), 
             Pico("Torreón", 1648, "Cádiz"),
             Pico("Peña Santa", 2596, "León"), 
             Pico("Naranjo", 2519, "Asturias"),
             Pico("Alcazaba", 3371, "Granada"), 
             Pico("Veleta", 3396, "Granada"),
             Pico("Torrecilla", 1919, "Málaga"), 
             Pico("Llambrión", 2647, "León"),
             Pico("Teide", 3718, "Santa Cruz de Tenerife")]
    
    print(Fore.BLACK)         
    mostrar_picos1(PICOS)

    print(Fore.BLUE)
    print(nombres(PICOS))

    print(Fore.CYAN)
    print(altitudNombres(PICOS))

    print(Fore.GREEN)
    print(granada(PICOS))

    print(Fore.LIGHTBLACK_EX)
    print(alturaMinima(PICOS))

    print(Fore.LIGHTBLUE_EX)
    print(sumaLeon(PICOS))

    print(Fore.LIGHTCYAN_EX)
    print(mayor(PICOS))

    print(Fore.LIGHTGREEN_EX)
    print(media(PICOS))

    print(Fore.LIGHTMAGENTA_EX)
    print(provincias(PICOS))

    print(Fore.RESET)