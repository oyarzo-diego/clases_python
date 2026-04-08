"""
Encabezado
Esta seccion corresponde al resumen de su codigo
-¿que hace mi algoritmo?
-¿cuales son las principales variables de entrada?
-si el script es una nueva version, ¿que fue lo que se cambio?
-fecha
-autor
"""

# Comentarios con Better Comments
#* titulos o secciones importantes
#! problemas, debugs, warmings
#? preguntas, preposiciones, etc
# TODO: que es lo proximo por hacer

#* SINTAXIS 
#conjunto de reglas del lenguaje de programacion

# Variables
# los nombres de las variables no pueden llevar puntos, ni guiones, ni caracteres especialesy tmapoco empezar por numero

precio_de_cobre = 5.6 #[USD/lb]

p_cu = 5.6 #precio cobre

#tipos de variables

x = 10 #interger
y = 10.0 #float

nombre = 'Juan 211' #str
print(nombre)
print(len(nombre))


x = float(x)
x = int(x)
print(type(x))
print(type(y))

x, y, z = 40, 20, 30

#* Estructuras de control
if x > y:
    print('x es mayor que y')
elif x < y:
    print('x es menor a y')
else:
    print(' x e y son iguales')

