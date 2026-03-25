"""
Clases miercoles 25 de marzo de 2026
Hoy veremos:
1. Listas; tuplas y diccionarios
2. Estructuras de control:
-condicionales
-ciclos
-excepciones
3.Ejercicio
"""

#* Listas
# lista1 = [1, 2, 3]
# # print(lista1)

# lista2 = ['a', 'b', 'c']
# # print(lista2)

# a, b, c = 1, 'dos', 3
# lista3 = [a, b, c]
# # print(lista3)
# # print(lista3[1])

# lista3[1] = 2
# #print(lista3)

# lista3.append('cuatro')
# #print(lista3)
# #print(lista3[-2])

# print(lista1, lista2)
# lista1.extend(lista2)
# lista1.insert(2, 'dos')
# print(lista1)

# lista1.remove(lista1[2])
# print(lista1)


#* Diccionarios
# diccionario1 = {'key': 'valor'}
# # print(diccionario1['key'])
# # print(diccionario1.get('key'))

# diccionario2 = {'a' : 1, 'b': 2, 'c' : 3}
# print(diccionario2.keys())
# print(diccionario2.values())
# print(diccionario2.items())

# diccionario2['a'] = 4
# print(diccionario2.items())

# diccionario2.update(diccionario1)
# print(diccionario2.items())

# diccionario2.pop('key')
# print(diccionario2.items())

# #* Tuplas
# tupla1 = (1, 2, 3)
# # print(tupla1)
# # print(tupla1[1])
# # print(tupla1.index(2))
# # print(len(tupla1))

# #* Sets
# set1 = {'a', 'b', 'c', 'c'}
# print(set1)

#* ESTRUCTURAS DE CONTROL
# condicionales
# x, y, z = 2, 2, 3

# if x > y:
#     print('x es mayor que y')
#     print(f'{x} es mayor que {y}')  
# elif y == x:
#     print('y es igual a x')
# elif z > x:
#     print('z es mayor a x')
# else:
#     print('no pasa nada')

#* Ciclos
# for x in range(1, 5+1):
#     print(x)

# for x in range(5, 20 + 1, 5):
#     print(x)

# lista4 = list(range(1,11))
# print(lista4)
# # for i in lista4:
# #     if i == 4:
# #         break
# #     print(i)

# for i in lista4:
#     if i == 4:
#         continue
#     print(i)

#zip en for

# x = 1

# while x < 10:
#     print(x)
#     print('x es menor a 10')
#     x += 1 #x = x + 1

#Excepciones try

#*Operadores
#aritmeticos
"""
+: suma
-: resta
. *: multiplicacion
/: division
· //: division entera
%: modulo
**: potencia
"""
#comparacion
"""
<, >, >=, <=, !=, ==

"""

# if 4 != 5:
#     print('4 es diferente a 5')

# logicos
# and, or, not

#Funciones
# def _suma(a, b=3):
#     return(a + b)

# a = 1
# b = 1

# print(_suma(1,1))

def _filtrar_pares(lista_numeros):
    lista_par = []
    for num in lista_numeros:
        if num % 2 == 0:
            lista_par.append(num)
    return lista_par

lista_prueba = list(range(1,11))
lista_prueba = _filtrar_pares(lista_prueba)
print(lista_prueba)

x, y, z = 2, 2, 3
( x > y) and print ('x es mayor que y')
( x == y) and print ('x es igual que y')
( z > x) and print ('z es mayor que x')

