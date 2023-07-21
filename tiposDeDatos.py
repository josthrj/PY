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

mi_list.pop()#elimina el ultimo elemento
print(mi_list)


mi_list.remove('dos')#elimina un elemento en especifico
print(mi_list)

#ordenar y modificar la lista 
#mi_list.sort()   #ordena alfabeticamente, pero tienen que ser del mismo tipo de datos 
#mi_list.reverse() #ordena de atras para frente

#tuplas: no pueden modificarse 

tupla = ('hola','mundo','somos','una','tupla')

print(tupla)

#tupla.count >>> igual que en las listas
#tupla.index >>> devuelve la pocision de donde encontro un elemento especificado

#como las tuplas no pueden modificarse para ello deben convertirse en listas

#listaDeTupla = list(tupla)


#listaDeTupla.append('hola')

#print(listaDeTupla)

#range
rangoNumeros = range (6)#genera una secuencia desde cero hasta

print(rangoNumeros)



#diccionarios
diccionario = {
    'nombre': "Angola",    #importante colocar la coma al final
    "capital": "Berlin",
    "edad": 24
    }   #se comienz con corchetes, se debe colocar la exprecion entre comillas
        #se debe colocar coma al final del texto indicado
        #numeros pueden ingresarse sin comillas


print(diccionario)

#del diccionario['edad']     #borra un campo especifica por su nombre
print(diccionario['capital'])


print(diccionario.get('capital'))  #accede al valor que se le especifica

diccionario['nombre'] = 'Alemania' #cambia valor de un dato del diccionario en este caso debe especificar cual va a cambiar

print(len(diccionario))#medir la longitud de un elemento en este caso el diccionario


diccionario['estado'] = 'sajonia'

#for key in diccionario:      #imprimiendo los elementos uno a uno

#print(diccionario)

#diccionario.pop('estado') #elimina un valor de nuestro diccionario
diccionario.popitem()#elimina el ultimo valor que se agrego
#copiaDiccionario = diccionario.copy()   #crea una copia de un diccionario
copiaDiccionario = dict(diccionario)     #crea una copia de un diccionario

#print(diccionario,copiaDiccionario)

#diccionario.clear()
#print(diccionario)


#DICCIONARIOS ANIDADOS

datosDiccionario =  {
    "carros": {
    "topic": "van",
    "marca": "kia"
    },
    "motos":{
        "fazer":"scooter",
        "marca": "honda"
        }

    }




print(datosDiccionario)


#ejecutando de otra forma

carros = {
    "fiat":"punto",
    "motor":"simple"       
    }
motores={
    "ocho":"complejo",
    "cuatro":"simple",
    }

datosDelSegundoDicc = {
    "carros":carros,
    "motores": motores, #como es una variable debe colocarse sin comillas
    }

print(datosDelSegundoDicc)

carrosAntiguos = dict(nombre = "kombi", marca = "volskswagen") #construcctor de dict
print(carrosAntiguos)

#todas las formas anteriores de alteracion de datos son validas la forma de trabajar de la organizacion en la que estemos dira cuales son las que debemos seguir segun los parametros usados


#BOOLEANOS #utiles para trabajar con control de flujo


verdadero = True
falso = False

print(verdadero,falso)
