class Pares():

    def ejercicio2(self):
        lista = []
        print("* * * Programa que lee una secuencia de números y luego muestra la Suma y el Producto de ellos * * *")
        cantidad = int(input("¿Cuántos números deseas ingresar? "))

        i = 1
        j=1
        while (cantidad > 0):
            numero = int(input("Número #" + str(i) + ": "))
            lista.append(numero)
            i = i + 1
            j=j*numero
            cantidad = cantidad - 1

        print(lista)
        print("\n La suma de todos los número es:",sum(lista))
        print("\n La multiplicación de todos los números es:", j,"\n")



    def ejercicio4(self):
        print("* * * Programa que realice una multiplicación por medio de Sumas * * *")
        a=int(input("Ingrese el primer número: "))
        b=int(input("Ingrese el segundo número: "))
        multi=0

        for i in range(0, b):
            multi+=a

        print("El resultado es:", multi, "\n")



    def ejercicio6(self):
        n = 1
        limit=''
        print("* * * Programa que obtiene el Producto de una secuencia de Números que se detiene presionando 'F' * * *")

        while limit!='F':
            num= int(input("Ingrese un número: "))
            n *= num
            limit= str(input("Desea continuar? F=No / Presione una letra para continuar "))

        print("\n Fin del Programa!")

        print("\n La multiplicación de los números ingresados es:", n, "\n")



    def ejercicio8(self):
        print("* * * Programa que muestra el Binario de un número Decimal ingresado por el usuario * * *")
        num= int(input("Ingrese el número que desea convertir a binario: "))
        print("El número", num, "convertido a binario es:", bin(num)[2:], "\n")



    def ejercicio10(self):
        print("* * * Programa que calcula la Media de una serie de números * * *")
        n = 0
        limit = ''
        cont= 0
        media=0
        while limit != 'F':
            num = int(input("Ingrese un número: "))
            cont += 1
            n += num
            limit = str(input("Desea continuar? F=No / Presione una letra para continuar "))

        media= n/cont

        print("\nLa media de los números ingresados es:", media, "\n")



    def ejercicio12(self):
        print("* * * Programa que muestra el Mayor y Menor de una secuencia de números y se detiene al ingresar uno Impar * * *")
        num= int(input("Ingresa un número: "))

        while num%2==0:
            mayor= num
            menor= num

            while num%2==0:
                if num>mayor:
                    mayor=num
                else:
                    menor<num

                num= int(input("Ingresa un número: "))

        print("El número mayor es:", mayor)
        print("El número menor es:", menor, "\n")



    def ejercicio14(self):
        print("* * * Programa que de una secuencia de Números suma los 30 Números que ocupan posiciones de lectura Par * * *")
        suma= 0
        i=0
        for x in range(0,60):
            numero= int(input("Ingrese un Número: "))
            i=i+1
            if i%2 == 0:
                suma=suma+numero

        print("La suma de los pares es:", suma, "\n")


Pares=Pares()


#Pares.ejercicio2()
#Pares.ejercicio4()
#Pares.ejercicio6()
#Pares.ejercicio8()
#Pares.ejercicio10()
#Pares.ejercicio12()
#Pares.ejercicio14()