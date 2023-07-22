#dato = input ("ingrese un dato:")

#lista = ['hola','nombre','carro','pista','piloto']
#lista de palabras para buscar el texto ingresado por el usuario

#condiciones para la consulta de datos
#if lista.count(dato) > 0:
#    print('el dato existe:',dato)
#else:
#    print('el dato no exite:',dato )

#calculadora que suma
primero = input('ingrese primer numero')

try:
    primero = int(primero)

except:
    primero = 'hola mundo'  

    if primero== 'hola mundo':
        print("el valor ingresado no es un entero")
        exit()

segundo = input('ingrese segundo numero')

try:
    segundo=int(segundo)
except:
    segundo = 'hola mundo'

if segundo == 'hola mundo':
    print('el valor ingresado no es entero')
    exit()

if primero== 'hola mundo' or segundo== 'hola mundo':
    print('ingreaste mal un dato, prueba de nuevo solo con numeros')

simbolo = input('ingrese operacion')

if simbolo == '+':
    print( 'suma:', primero + segundo)
elif  simbolo=='-':
    print( 'resta:', primero - segundo)
elif  simbolo == '*':
    print( 'multiplicaion:', primero * segundo)
elif simbolo == '/':
    print( 'division:', primero / segundo)
else:
    print ('operador invalido')







#primerNumero = int (primero)
#segundoNumero = int(segundo)
#print(primerNumero + segundoNumero)



