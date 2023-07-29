# son bloques de codigo que no se van a ejcutar a menos que no sea necesario\
#pueden usarse varias veces si se requiren

def miFuncion():
    print("Hola mundo mi primera funcion")



#miFuncion()


#def imprimeDato(argumentoUno):
    #print('Mi argumento es', argumentoUno) #en este caso las variables que ingresamos las tenemos que llamr argumentos

#imprimeDato('parametro 1') # si llamamos a la funciion y le pasamos informacion dentro de los parentecis le estamos pasando un parametro


#def imprimeDato(nombre, apellido):
    #print('El nombre completo es ', nombre,apellido)


#imprimeDato('federico el', 'perro')# mismo caso con 2 parametro \
#si nuestra funcion se crea con una cantidad x de parametros debemos entregarle todos los parametros\
#si esto no sucede nuestra funcion no se ejecutara correctamente



def imprimeDato(*nombre): # al usar * podreos pasar mas datos a los parametros de la funcion
    print('El nombre completo es ', nombre[0])#al indicar el indice podemos ingresar a los arguemntos segun demanda

#imprimeDato('federico','el','perro','loco')#solo que en este caso aceptara los datos como una tupla


def nombreCompleto(apellido,nombre):
    print(nombre,apellido)




nombreCompleto(nombre='federico', apellido='elperro')


def nombreCompleto2(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])

nombreCompleto2(nombre='federico', apellido='elperro')

def miFuncion2(argumento = 'federico'):
    print(argumento)


#miFuncion2('batan')
#miFuncion2()


def miFuncionLista(lista):
    for el in lista:
        print(el)


#miFuncionLista(['federico','el','perro','loco'])




def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ''
        return i

#nombres = concatenaNombres(['federico','el_perro'])
#print(nombres)



def recursion(i):
    if (i < 1):
        return 
    print(i)
    recursion(i-1)


recursion(6)


#recursividad: Cada llamada genera una nueva llamada a una \
# función con los correspondientes objetos locales.



