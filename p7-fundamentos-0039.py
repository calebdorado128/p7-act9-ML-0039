# Caleb Dorado NC = 0039

print("Variables 0039")
# Ejemplo 1: Variable con texto (String)
nombre = "Carlos"
print(nombre)
# Ejemplo 2: Variable con número entero (Integer)
edad = 25
print(edad)
# Ejemplo 3: Variable con número decimal (Float)
precio = 19.99
print(precio)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

print("Variables Multiples 0039")
# Ejemplo 1: Múltiples variables con diferentes valores
x, y, z = "Manzana", "Banana", "Cereza"
print(x)
print(y)
print(z)
# Ejemplo 2: Múltiples variables con un mismo valor
a = b = c = "Python"
print(a)
print(b)
print(c)
# Ejemplo 3: Desempacar una lista (Unpacking)
frutas = ["Naranja", "Mango", "Uva"]
p, q, r = frutas
print(p)
print(q)
print(r)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

print("Data Types 0039")
# Ejemplo 1: Lista (list) - Colección ordenada y modificable
colores = ["rojo", "verde", "azul"]
print(colores)
# Ejemplo 2: Diccionario (dict) - Estructura de clave-valor
usuario = {"nombre": "Ana", "edad": 30}
print(usuario)
# Ejemplo 3: Booleano (bool) - Valor de verdad (True o False)
es_mayor_de_edad = True
if es_mayor_de_edad:
    print("Acceso concedido: El usuario es mayor de edad.")
else:
    print("Acceso denegado: El usuario es menor de edad.")

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

print("Operadores Aritmeticos 0039")
# Ejemplo 1: Módulo (%) - Devuelve el residuo de una división
residuo = 10 % 3
print(residuo)
# Ejemplo 2: Exponenciación (**) - Eleva un número a una potencia
potencia = 2 ** 3
print(potencia)
# Ejemplo 3: División (/) - Divide un numero entre otro
division = 15 / 3
print(division)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

print("Operadores de Comparacion 0039")
# Ejemplo 1: Igualdad (==)
resultado_igual = (5 == 5)
print(resultado_igual)
# Ejemplo 2: Diferente de (!=)
resultado_diferente = (10 != 5)
print(resultado_diferente)
# Ejemplo 3: Mayor o igual que (>=)
resultado_mayor_igual = (7 >= 12)
print(resultado_mayor_igual)

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

print("Operadores Logicos 0039")
# Ejemplo 1: Operador AND (ambas condiciones deben ser True)
nota = 80
asistencia = 70
aprobado = (nota >= 60) and (asistencia >= 80)
print(aprobado)
# Ejemplo 2: Operador OR (al menos una condición debe ser True)
es_estudiante = True
es_tercera_edad = False
descuento = (es_estudiante) or (es_tercera_edad)
print(descuento)
# Ejemplo 3: Operador NOT (invierte el valor booleano)
terminado = False
hacer_tarea = not terminado  # Si terminado es False, resulta en True
print(hacer_tarea)

print("Hecho por Caleb Dorado NC = 0039")