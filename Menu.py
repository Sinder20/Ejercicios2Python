import os
from EjerciciosImpares import Impares
from EjerciciosPares import Pares

class Menu():

    os.system('cls')

    while True:
        print("--> Selecciona una opción <--")

        print("\t1 - Ejercicios Pares")

        print("\t2 - Ejercicios Impares")

        print("\t3 - Salir del Programa")


        opcionMenu = input("Ingrese el número de la opción que desea: ")


        if opcionMenu == "1":

            print("")

            input("Has pulsado la opción 1...\nPresione 'Enter' para continuar...\n")
            Pares.ejercicio2()
            Pares.ejercicio4()
            Pares.ejercicio6()
            Pares.ejercicio8()
            Pares.ejercicio10()
            Pares.ejercicio12()
            Pares.ejercicio14()

        elif opcionMenu == "2":

            print("")

            input("Has pulsado la opción 2...\nPresione 'Enter' para continuar...\n")
            Impares.ejercicio1()
            Impares.ejercicio3()
            Impares.ejercicio5()
            Impares.ejercicio7()
            Impares.ejercicio9()
            Impares.ejercicio11()
            Impares.ejercicio13()
            Impares.ejercicio15()

        elif opcionMenu == "3":

            print("")

            input("Has pulsado la opción 3...\nPresione 'Enter' para continuar...\n")
            break

        elif opcionMenu == "3":
            break

        else:

            print("")

            input("No has pulsado ninguna opción correcta...\nPresione 'Enter' para continuar...\n")

Menu=Menu()
Menu.opcionMenu