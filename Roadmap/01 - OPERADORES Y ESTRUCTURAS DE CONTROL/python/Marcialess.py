
"""
Operadores Aritmeticos
"""

print(f'Este es un operador suma 12 + 3 = {12+3}')
print(f'Este es un operador resta 12 + 3 = {12-3}')
print(f'Este es un operador multiplicar 12 * 3 = {12*3}')
print(f'Este es un operador division 12 / 3 = {12/3}')
print(f'Este es un operador division entero 12 / 3 = {12 // 3}')
print(f'Este es un operador potencia 12 ** 3 = {12 ** 3}')
print(f'Este es un operador modulo 16 % 3 = {12 % 3}')

"""
Operador Relacionales
Un operador relacional se emplea para comparar y establecer la relación entre ellos. Devuelve un valor booleano (true o false) basado en la condición.
"""

print(f"Este es el operador mayor que > {1 > 3}")
print(f"Este es el operador menor que > {1 < 3}")
print(f"Este es el operador igual que ==  {1 == 3}")
print(f"Este es el operador diferente que != {1 != 3}")
print(f"Este es el operador mayor igual que >= {1 >= 3}")
print(f"Este es el operador menor igual que =< {1 <=3}")

"""
Operadores de Asignacion
Se utiliza un operador de asignación para asignar valores a una variable. Esto generalmente se combina con otros operadores.
"""

number = 21
print(number)
number += 3
print(number)
number -= 5
print(number)
number *= 3
print(number)
number /= 2
print(number)
number **= 5
print(number)
number %= 2
print(number)

"""
Operadores Lógicos
Se utiliza un operador lógico para tomar una decisión basada en múltiples condiciones. Los operadores lógicos utilizados en Python son  and, or y not.
"""
print(f'5 + 5 == 10 AND 10 + 3 != 10 es: {5 + 5 == 10 and 10 + 3 != 10}')
print(f'5 + 5 == 10 AND 10 + 3 >= 10 es: {5 + 5 == 10 or 10 + 3 >= 10}')
print(f'not 10 + 3 <= 10 es: {not 10 + 3 != 10}')

"""
Operadores de Pertenencia
Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).
"""

my_list = [3,4,5,"hello",10]

print (2 in my_list)
print(2 not in my_list)
print("hello" in my_list)

"""
Operadores de Identidad
Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.
"""

a = 3
b = 3  
c = 4
print (a is b) 
print (a is not b) 
print (a is not c) 

"""
Operadores Bit a Bit
Un operador bit a bit realiza operaciones en los operandos bit a bit.
"""

a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000


"""
Estructuras de control
"""
#Condicionales

str_test = "Desarrollado"

if str_test == "Desarrollador":
    print(f"{str_test} es Desarrollador")
elif str_test == "Ingeniero":
    print("{str_test} es Ingeniero")
else:
    print("Esta cadena no es ninguna de las anteriores ")    

# Interactivas
    for i in my_list:
        print(i)

contador = 0

while contador <= 10:
    print(contador)
    contador += 1   

#Manejo de Excepciones
a = "1"
b = 2

try:
    print(a + b)
except:
    print("No puedes sumar un str con un int")
finally:
    print("Fin de la exception")

"""
Extra
"""

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
