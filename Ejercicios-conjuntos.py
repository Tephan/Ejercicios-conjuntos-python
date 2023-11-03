conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {3, 4, 5, 6, 7}

#Unión
union_conjuntos = conjunto_a | conjunto_b

#Intersección
interseccion_conjuntos = conjunto_a&conjunto_b

#Diferencia a - b
diferencia_a_b = conjunto_a - conjunto_b

#Diferencia b - a
diferencia_b_a = conjunto_b - conjunto_a

print('Unión de los conjuntos: ',union_conjuntos)
print('Intersección de los conjuntos: ',interseccion_conjuntos)
print('Diferencia de conjunto_a - conjunto_b: ',diferencia_a_b)
print('Diferencia de conjunto_b - conjunto_a: ',diferencia_b_a)

'_______________________________________________________________________________________________________________________'

'''
Ejercicio: Gestión de Compras en una Tienda

Supongamos que tienes una tienda en línea y llevas un registro de los productos que los clientes han 
comprado en forma de conjuntos. Cada conjunto representa los productos comprados por un cliente en una transacción. 
A continuación, se muestran algunos datos de ejemplo:
'''

transaccion_1 = {"producto_a", "producto_b", "producto_c"}
transaccion_2 = {"producto_a", "producto_d", "producto_e"}
transaccion_3 = {"producto_b", "producto_c", "producto_f"}
transaccion_4 = {"producto_g", "producto_h", "producto_i"}


'''
Realiza las siguientes operaciones utilizando conjuntos para analizar los datos de las transacciones:

Encuentra todos los productos únicos que han sido comprados por al menos un cliente y almacénalos en un conjunto llamado productos_totales.
Encuentra los productos que han sido comprados por todos los clientes y almacénalos en un conjunto llamado productos_comprados_por_todos.
Encuentra los productos que han sido comprados por al menos un cliente, pero no por todos los clientes y almacénalos en un conjunto llamado productos_no_comprados_por_todos.
Imprime los resultados de cada operación para verificar que son correctos.
'''

productos_totales=transaccion_1.union(transaccion_2,transaccion_3,transaccion_4)
productos_comprados_por_todos=transaccion_1.intersection(transaccion_2,transaccion_3,transaccion_4)
productos_no_comprados_por_todos=productos_totales - productos_comprados_por_todos

print('Productos totales: ',productos_totales)
print('Productos comprados por todos: ',productos_comprados_por_todos)
print('Productos no comprados por todos: ',productos_no_comprados_por_todos)

'_______________________________________________________________________________________________________________________'

'''
La similitud de Jaccard es una fórmula que te dice qué tan similares son
dos conjuntos. Se define como la cardinalidad de la intersección dividida por
la cardinalidad de la unión. ¿Cuál es la implementación precisa en
Python?
'''

def jaccard(a,b):
    return len(a&b)/len(a|b)

j=jaccard({5,8,2,9},{1,2,3,4,5})
print(j)