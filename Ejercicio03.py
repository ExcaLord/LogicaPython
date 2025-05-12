# Estructuras de Datos #

# Listas

# Formas de crear listas.
my_list = list()
my_other_list = []

my_list = ["Exca", "Developer", "ExcaLord"]
print(my_list)

# Append se usa para agregar elementos al final de la lista.
my_list.append("ExcaDev")
print(my_list)

# Pop para eliminar elementos al final de la lista.
my_list.pop()
print(my_list)

# Sort se usa para ordenar de forma generica una lista.
my_list.sort()
print(my_list)

# Para actulizar/cambiar un elemento de la lista podemos hacer lo siguiente.
my_list[2] = "ExcaLord Developer"
print(my_list)

# Para dividir listas y obtener los datos de cierto rango hacemos:
print(my_list[0:2])

# Insert para hacer la insercion de un elemento en una posicion deseada.

my_list.insert(2, "ExcaDev")
print(my_list)

# Tuples #

# Estas son las dos formas en las que puedes escribir una tuple
my_tuple = tuple()
my_other_tuple = ()
# Las tuplas son inmutables, no se le pueden modificar datos (como un contrato)

my_tuple = (4.120294, -2.34124)  # Como las cordenadas de un sitio fijo
latitud, longitud = my_tuple
print(latitud, longitud)
# en las tuplas no hay forma de anadir elementos o modificar los existente.
# pero se puede acceder a ellos o asignarlos a variables, o usarlos como key
# en dictionary.

my_tuple[1]
my_tuple[-2]

# Sets #

my_set = set()
my_other_set = {}

# utilizamos llaves para el set pero tambien se us en los diccionarios,
# la idea es saber la sintaxis con la que escribimos dentro de estos.

my_set = {23, 45, 13, "ExcaDev"}
print(my_set)
my_set.add(32)
print(my_set)

# Ejercicio 1.
# Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización
#   y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#   y a continuación los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no numéricos y con más
#   de 11 dígitos (o el número de dígitos que quieras).
# - También se debe proponer una operación de finalización del programa.
