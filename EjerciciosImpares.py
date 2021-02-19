class Impares():

    def ejercicio1(self):
        print("* * * Programa que lee un número y muestra su tabla de multiplicar * * *")
        num= int(input("Ingrese el número que desea mostrar su tabla de multiplicar: "))
        for i in range(0,11):
            resultado=i*num
            print(("%d X %d = %d")%(num, i, resultado))
        print(" ")


    def ejercicio3(self):

        n=0
        print("* * * Programa que lee una secuencia de números y se detiene hasta ingresar un Número NEGATIVO * * *")
        num= int(input("Ingrese un número: "))

        while num >=0:
            n+=num
            num= int(input("Ingrese un número: "))

        print("La suma de los números positivos es:", n, "\n")



    def ejercicio5(self):
        print("* * * División por medio de Restas * * *")
        dividendo=int(input("Ingrese el dividendo: "))
        divisor= int(input("Ingrese el divisor: "))

        if divisor==0:
            print("ERROR EL DIVISOR NO TIENE QUE SER 'CERO'")
        else:
            cociente=0
            resto=dividendo
            while resto>=divisor:
                resto-=divisor
                cociente+=1
            print("El cociente es:", cociente)
            print("El residuo es:", resto)
        print(" ")


    def ejercicio7(self):
        lista = []
        print("* * * Programa que lee una secuencia de números y muestra el Mayor * * *")
        cantidad = int(input("¿Cuántos números deseas ingresar? "))
        mayor = 0
        i = 1

        while (cantidad > 0):
            numero = int(input("Número #" + str(i) + ": "))
            lista.append(numero)
            i = i + 1
            cantidad = cantidad - 1

        mayor = max(lista)

        print("\n Los números que ingresó son: ", lista)
        print("\n El número mayor es: ", mayor, "\n")



    def ejercicio9(self):
        suma = 0
        print("* * * Programa que suma los números divisibles entre 5, comenzando desde el 2 y va de 3 en 3 * * *")
        limit = int(input("Ingrese el rango hasta dónde quiere llegar: "))
        for x in range(2, limit, 3):

            print(x, end=", ")
            if x % 5 == 0:
                suma += x

        print("\nLa suma de los números generados que son divisibles entre 5 es:", suma, "\n")



    def ejercicio11(self):
        print("* * * Sucesión de Fibonacci * * *")
        limit= int(input("Ingrese la cantidad de términos que desea imprimir: "))
        num1=1
        num2=0
        num3=1

        for x in range(0, limit):
            num3+=1
            print(num2, end="  ")
            sum= num2 + num1
            num2=num1
            num1=sum
        print(" ")


    def ejercicio13(self):
        sum=0
        stop=''
        print("* * * Programa que lee una secuencia de números y luego muestra la suma de los Números Pares * * *")
        while stop!='N':
            num = int(input("Ingrese un número entero: "))
            stop= str(input("Desea Continar? N=No / Presione otra letra para continuar: "))
            if num % 2 == 0:
                sum += num
                print(sum)

            elif num % 2 !=0:
                continue

        print("La suma de los números pares es:", sum, "\n")



    def ejercicio15(self):
        from math import factorial
        print("* * * Programa para calcular el factorial de un número * * *")

        num= int(input("Ingrese el número: "))

        print("El factorial de", num, "es", factorial(num), "\n")



Impares=Impares()

#Impares.ejercicio1()
#Impares.ejercicio3()
#Impares.ejercicio5()
#Impares.ejercicio7()
#Impares.ejercicio9()
#Impares.ejercicio11()
#Impares.ejercicio13()
#Impares.ejercicio15()
