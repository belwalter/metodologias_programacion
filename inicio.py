
#! TIPOS DE DATOS STR - NUMERICOS (INT , FLOAT, COMPLEX), BOOL, NONE

# numero = "hola"
# print(type(numero))

# numero = 105
# print(type(numero))

# numero = 41.07
# print(type(numero))

# numero = False
# print(type(numero))

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
"""
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
"""

## OPERADORES LOGICOS (AND / OR / NOT)

# print((4>5))
# print((4<8))
# print((4>5) and (4<8))

# persona = "maria"
# edad = 19

# if ((persona=="juan") and (edad==18)):
#     print("juan tiene 18")
# else:
#     print("juan no tiene 18")
    
# if ((persona=="juan") or (edad==18)):
#     print("la persona se llama juan o tiene 18")
# else: 
#     print("la persona no se llama juan ni tiene 18 años")

# print(not True)
# print(not(4>5))

## LISTAS

# lista = [1,2,3,"maria",True]
# print(lista)
# print(lista[3])
# lista[4] = 'juan'
# lista[4] = 5
#print(type(lista[4])) 
# print(len(lista))
# print(len("juan"))

## DICCIONARIOS

domicilio = "9 de julio 200"

dic = {
    'nombre': 'juan',
    'dni': 41112424,
    'domicilio': domicilio,
    'edad': 20,
    'soltero': True
}

# print(dic)
# print(dic['domicilio'])
# print(type(dic['domicilio']))
# dic['edad'] = "veintiuno"
# print(dic['edad'])

## FOR

lista = [1,2,3,"maria",True,'juan',14]

# for i in range(0, len(lista)):
#     # print(i)
#     print(type(lista[i]))

# for key in dic.keys():
#     print(dic[key])

## WHILE

# aux = 0
# while(aux<5):
#     print(aux)
#     aux = aux + 1

lista = [1,2,3,"maria",True,'juan',14]

aux = 0
# while(aux < len(lista)):
#     print(lista[aux])
#     # lista[aux] = aux
#     aux = aux + 1

aux = len(lista)-1
while(aux >= 0):
    print(aux)
    # print(lista[aux])
    # lista[aux] = aux
    aux = aux - 1

aux1 = 0
aux2 = 10

while((aux1<5) and (aux2<12)):
    print("aux1", aux1)
    print("aux2", aux2)
    aux1 = aux1 + 1
    aux2 = aux2 + 1


print(lista)