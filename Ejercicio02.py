# Funciones y Alcance #


def nombre():
    nombre = input("Cual es tu nombre?")
    return nombre


def edad():
    edad = int(input("Cual es tu edad?"))
    return edad


def nacimiento():
    day = int(input("En que dia naciste?"))
    month = int(input("En que mes naciste?"))
    year = int(input("En que year naciste?"))
    fecha = f"Naciste el {day:02d} {month:02d} {year}"
    return fecha


while True:
    n = nombre()
    e = edad()
    b = nacimiento()

    if n and e and b:
        print(f"Ya veo te llamas {n} de edad {e} y {b}")
        break
    else:
        print("No Digitaste todos los valores que ocurrio?, intentalo nuevamente!")
