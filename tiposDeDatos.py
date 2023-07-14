#tipos de datos
palabra = 'hola mundo'
#string pueden ser con comillas simples o comillas dobles,no importa

entero = 20 # integer
decimal = 3.14 # float
complejo = 1j 

print   ( palabra, entero, decimal, complejo)

#lista: son un  tipo de variable que permite el almacenamiento de varios,a los que se accede a traves de un indice
#el tamano de una lista es igual al la cantidad de elementos que ella contiene

#creando una lista
mi_list =[1,'dos',True] # con datos
list = [] #vacia

print   (mi_list,list )

#agregando elementos a una lista
mi_list.append (16) #metodo append cambia la lista sin necesidad de crear una nueva lista
 
print(mi_list)

#mi_list.clear()
#borrar todos los elementos de mi list

list2 = mi_list.copy()
##crear copia del contenido de mi_list en un nuevo objeto llamado "list2

mi_list.append  (26) #agrega elementos a la lista, pero noi actualiza los cambios automaticamente en el meetodo copy


print(mi_list,list2)

# contando elementos y calculando el valor de repeticion en lista 

print(list,list2,mi_list.count(16)) #metodo count

#len la funcion len cuenta la cantidad de elementos presente en una cadena de caracteres o lista, es importante recordar que este conteo comienza en el indice 0
#ej 012345678 >>> indice
#ej abcdefghi >>> contenido


#metodo 1
print(len(mi_list), len (list2))



#se puede ejecutar el metodo de las dos maneras sin ningun problema, solo que el metodo 1 es mas limpio
#metodo 2
largoList2 = len(list2)
largoMi_list = len(mi_list)

# print(largoList2, largoMi_list)


#accedidiendo a los elementos de las listas
print(mi_list[0])

mi_list.pop()
print(mi_list)




















