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
    
    def sum_two_numbers(a,b) :
        return a + b
    
    return sum_two_numbers

function_inside_function = main()
print(function_inside_function(2,3))

# Ejercicio 1.