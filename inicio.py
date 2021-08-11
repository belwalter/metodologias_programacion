
#! TIPOS DE DATOS STR - NUMERICOS (INT , FLOAT, COMPLEX), BOOL, NONE

numero = "hola"
print(type(numero))

numero = 105
print(type(numero))

numero = 41.07
print(type(numero))

numero = False
print(type(numero))

#! FUNCIONES DE CONVERSION INT() STR() FLOAT() BOOL()

# name = input('ingrese su nombre ')
# age = int(input('ingrese su edad '))

# print(type(name), type(age))
# print(name, 2021-age)

#! OPERADORES ARITMETICOS + - * / // % **

# print(2 + 3)
# print(2 - 3)
# print(2 * 3)
# print(2 / 3)
# print(2 // 3)
# print(2 % 3)
# print(2 ** 3)

#! FLUJO DE CONTROL  CONDICIONALES (IF-IF ELSE-ANIDADOS), CICLOS (FOR-WHILE)
#! OPERADORES DE CONTROL > < >= <= == !=

numero = 0
if(numero > 6):    
    print('es mayor')


if(numero % 2 == 0):
    print('el numero es par')
    
else:
    print('el numero es impar')


if(numero > 0):
    print('el numero es positivo')
else:
    if(numero < 0):
        print('el numero es negativo')
    else:
        print('es neutro')


if(numero > 0):
    print('el numero es positivo')
elif(numero < 0):
    print('el numero es negativo')
else:
    print('es neutro')

print('fin')
