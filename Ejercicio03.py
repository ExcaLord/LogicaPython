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

# Dictionaries #

my_dict = dict()
my_other_dict = {}

my_dict = {"nombre": "ExcaDev", "edad": 22, "ciudad": "Bogota"}
# en los dictionaries se pueden usar llaves y valores, y se pueden modificar
# Ejemplo:
print(my_dict)
my_dict["nombre"] = "ExcaLord"
print(my_dict.pop("edad"))
print(my_dict.clear())
my_dict = {"nombre": "ExcaDev", "edad": 22, "ciudad": "Bogota"}
print(my_dict.keys())


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

agenda = {}


def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        return agenda[nombre]
    else:
        return None


def insertar_contacto(agenda, nombre, telefono):
    if nombre not in agenda:
        agenda[nombre] = telefono
        print(f"Contacto {nombre} insertado con éxito.")
    else:
        print(f"El contacto {nombre} ya existe.")


def actualizar_contacto(agenda, nombre, telefono):
    if nombre in agenda:
        agenda[nombre] = telefono
        print(f"Contacto {nombre} actualizado con éxito.")
    else:
        print(f"El contacto {nombre} no existe.")


def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado con éxito.")
    else:
        print(f"El contacto {nombre} no existe.")


def mostrar_agenda(agenda):
    print(f"Agenda de contactos: {agenda}")


def _validar_telefono(telefono):
    if telefono.isdigit() and len(telefono) <= 11:
        return True
    else:
        return False


def _validar_nombre(nombre):
    if nombre.isalpha():
        return True
    else:
        return False


def __main__():
    print("Bienvenido a la agenda de contactos.")
    print("Seleccione una operación:")
    print("1. Buscar contacto")
    print("2. Insertar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar agenda")

    user_input = input("Ingrese el número de la operación que desea realizar: ")

    if user_input == "1":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        if _validar_nombre(nombre):
            contacto = buscar_contacto(agenda, nombre)
            if contacto:
                print(f"Contacto encontrado: {nombre} - {contacto}")
            else:
                print(f"Contacto {nombre} no encontrado.")
        else:
            print("Nombre inválido. Solo se permiten letras.")

    if user_input == "2":
        nombre = input("Ingrese el nombre del contacto a insertar: ")
        telefono = input("Ingrese el número de teléfono: ")
        if _validar_nombre(nombre) and _validar_telefono(telefono):
            insertar_contacto(agenda, nombre, telefono)
        else:
            print("Nombre o teléfono inválido.")
    if user_input == "3":
        nombre = input("Ingrese el nombre del contacto a actualizar: ")
        telefono = input("Ingrese el nuevo número de teléfono: ")
        if _validar_nombre(nombre) and _validar_telefono(telefono):
            actualizar_contacto(agenda, nombre, telefono)
        else:
            print("Nombre o teléfono inválido.")

    if user_input == "4":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        if _validar_nombre(nombre):
            eliminar_contacto(agenda, nombre)
        else:
            print("Nombre inválido. Solo se permiten letras.")

    if user_input == "5":
        mostrar_agenda(agenda)

    if user_input not in ["1", "2", "3", "4", "5"]:
        print("Operación no válida. Por favor, seleccione una operación válida.")


while True:
    if __name__ == "__main__":
        __main__()
    continuar = input("¿Desea realizar otra operación? (s/n): ").lower()
    if continuar == "s":
        __main__()
    elif continuar == "n":
        print("Gracias por usar la agenda de contactos. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese 's' o 'n'.")
