# Funciones y Alcance #

global_variable = 10
# Se puede usar la variable global dentro de la funcion


def modify_global_variable():
    global global_variable
    # Se puede modificar la variable global dentro de la funcion
    global_variable = 20


print(f"Variable global fuera de la funcion: {global_variable}")


def nombre():
    nombre = input("Cual es tu nombre? ")
    return nombre


def edad():
    edad = int(input("Cual es tu edad? "))
    return edad


def nacimiento():
    day = int(input("En que dia naciste? "))
    month = int(input("En que mes naciste? "))
    year = int(input("En que year naciste? "))
    fecha = f"Naciste el {day:02d} {month:02d} {year}"
    return fecha


# Ejemplo de while True
# Se usa para crear un bucle infinito
# Se usa para pedir al usuario que ingrese datos
# Se usa para validar que el usuario ingrese todos los datos
# Se termina el bucle cuando el usuario ingresa todos los datos

while True:
    n = nombre()
    e = edad()
    b = nacimiento()

    if n and e and b:
        print(f"Ya veo te llamas {n} de edad {e} y {b}")
        break
    else:
        print("No Digitaste todos los valores que ocurrio?, intentalo nuevamente!")

# Funcion vacia
# No hace nada, solo se define
# Se puede usar para definir una funcion que no hace nada


def vacia():
    return None


# Ejemplo funcion varios argumentos
# Se pueden definir funciones con varios argumentos


def sum_three_numbers(a, b, c):
    return a + b + c


# Funcion dentro de otra funcion
# Se pueden definir funciones dentro de otras funciones
# La funcion interna solo es visible dentro de la funcion externa
# En este caso la funcion interna se llama sum_two_numbers
# La funcion interna puede ser devuelta como resultado de la funcion externa
# En este caso la funcion interna se devuelve como resultado de la funcion externa


def main():
    def sum_two_numbers(a, b):
        return a + b

    return sum_two_numbers


function_inside_function = main()
print(function_inside_function(2, 3))

# For Loop
# Se usa para iterar sobre una secuencia (lista, tupla, diccionario, conjunto o cadena)
# Se usa para iterar sobre un rango de numeros
# Se usa para iterar sobre una cadena de texto
# Se usa para iterar sobre un objeto iterable

for i in range(10):
    print(1)

# Ejercicio 1.
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
# - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
# - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
# - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
# - La función retorna el número de veces que se ha impreso el número en lugar de los textos.


def printNumber(str1, str2):
    contador_numero = 0

    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(str1 + "" + str2)
        elif number % 3 == 0:
            print(str1)
        elif number % 5 == 0:
            print(str2)
        else:
            print(number)
            contador_numero += 1
    return contador_numero


print(printNumber("Empanada", "Arepa Rellena"))
