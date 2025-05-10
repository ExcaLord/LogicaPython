# ==========================
# Operadores en Python
# ==========================

# --- Operadores aritméticos ---
a = 22
b = 1

# Suma
print(a + b)  # Resultado: 23

# Resta
print(a - b)  # Resultado: 21

# Multiplicación
print(a * b)  # Resultado: 22

# División (retorna float)
print(a / b)  # Resultado: 22.0

# Módulo (resto de la división)
print(a % b)  # Resultado: 0

# División entera (descarta decimales)
print(a // b)  # Resultado: 22

# Potenciación (a elevado a la b)
print(a**b)  # Resultado: 22

# --- Operadores lógicos ---
# Devuelven True o False según la condición

print(a > 20 and b < 2)  # True si ambas condiciones se cumplen
print(a > 20 or b < 2)  # True si al menos una condición se cumple
print(not (a > 20 and b < 2))  # Invierte el resultado lógico

# --- Operadores de comparación ---
print(a > b)  # Mayor que
print(a < b)  # Menor que
print(a >= b)  # Mayor o igual que
print(a <= b)  # Menor o igual que
print(a == b)  # Igual que
print(a != b)  # Diferente de

# --- Operadores de asignación ---
# Modifican el valor de la variable

a += 1  # Incrementa a en 1
a -= 1  # Decrementa a en 1
a *= 2  # Multiplica a por 2
a /= 2  # Divide a entre 2 (float)
a //= 2  # Divide a entre 2 (entero)
a %= 2  # Asigna a el resto de dividir a entre 2

# ==========================
# Estructuras de Control
# ==========================

# --- Condicionales ---
c = 22
d = 23

# if-else simple
if c > d:
    print("c es mayor que d")
else:
    print("c es menor que d")

# if-elif-else con condiciones compuestas
if c > d and a < c:
    print("c es mayor que d y a es menor que c")
elif c < d and a < d:
    print("c es menor que d o a es menor que d")
else:
    print("c es igual a d o a es igual a d")

# --- Ciclo while ---
# Imprime valores de c hasta que sea igual a d
while c < d:
    print(c)
    c += 1

# --- Simulación de do-while ---
# Ejecuta al menos una vez y luego verifica la condición
while True:
    print(c)
    c += 1
    if c > d:
        break

# --- Ciclos for con range ---
# Básico: del 0 al 9
for i in range(10):
    print(i)

# Con inicio y fin: del 1 al 9
for i in range(1, 10):
    print(i)

# Con inicio, fin y paso: del 1 al 9, saltando de a 2
for i in range(1, 10, 2):
    print(i)

# Con paso negativo: del 10 al 2, descendiendo
for i in range(10, 1, -1):
    print(i)

# --- Ciclo for sobre lista ---
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)

# --- Ciclo for sobre diccionario (solo claves) ---
diccionario = {"a": 1, "b": 2, "c": 3}
for clave in diccionario:
    print(clave)

# ==========================
# Ejercicio de filtrado de números
# ==========================
# Números entre 10 y 55 (incluidos), que sean pares,
# que NO sean el 16 y que NO sean múltiplos de 3

numeros_filtrados = [n for n in range(10, 56) if n % 2 == 0 and n != 16 and n % 3 != 0]
print(numeros_filtrados)

# ==========================
# Tips adicionales
# ==========================
# - Cambia los valores de a, b, c, d para experimentar.
# - Usa print con mensajes personalizados para entender mejor cada paso.
# - En Python no existe do-while, pero puedes simularlo con while True y break.
# - Para ver claves y valores de un diccionario:
#   for clave, valor in diccionario.items():
#       print(clave, valor)
# - Cosas que no se pueden hacer en Python:
#   no puedes declarar variables sin asignarles un valor.
#   no existen variables globales y locales como en otros lenguajes.
#   no existen punteros como en C/C++.
#   no existen las variables estáticas como en Java.
#   las variables no son de tipo constante.
