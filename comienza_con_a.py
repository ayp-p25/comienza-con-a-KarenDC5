"""
Determinar si una palabra comienza con la letra "a"
Karen Durán
757136
Ingeniería CiviL
Algoritmos y Programación 
ESI232B2
14/02/25
15 minutos 
"""

# Entradas
palabra = input("Escribe una palabra: ")

# Proceso
if palabra [0] in ['a', 'á', 'A', 'Á']:
    comienza = True 
else: 
    comienza = False  

# Salidas
if comienza: 
    print(palabra, "comienza con 'A'") 
else: 
    print(palabra, "no comienza con 'A'")
