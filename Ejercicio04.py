# Cadenas de Caracteres #

# Existen dos formas de hacer cadenas de texto en Python
# Una es con comillas dobles u la otra con comillas simples.
# En caso de querer cadenas de texto muy largas puedes usar triple comillas dobles
my_str = "Exca Developer is Amazing"
my_other_str = "Exca Developer is Amazing"
parrafo = """Este es un parrafo largo
para demostracion sencillas """

# Primera opercaion que tenemos es la concatenacion

nombre = "Exca"
appelido = "Dev"
nombre_completo = nombre + " " + appelido
print(nombre_completo)


# Segunda cosa que podemos realizar con una cadena de texto es la multiplicacion

print("Matteo " * 3)

# Tercero podemos dividir una cadena de texto en partes
# Usando split

print("Exca Developer".split())

# Cuarto podemos tambien obetener la longitud de una cadena de texto

print(len("Exca Developer"))

# Quinto podemos tambien obtener la informacion de cierta posicion

print(nombre_completo[2:7])
