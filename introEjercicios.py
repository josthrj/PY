print (2+2)
# identacion del curso de python
if 5 > 3: #condicion 1
    print (" 5 es mayor que 3")
    if 3 > 5:    #condicion 2
        print ("esto no se imprime")

#variables 
x = 5
y = "python"

print (x,y)


email =  'josthoonrivas@gmail.com'

print(email)
#importante colocar nombres claros y entendibles a nuesras variables,segub el contexto en que estemos trabajando esto hace referencia a calidad de codigo

# nombres validos y invalidos de variables
# a1 = Si (aunque contenga un numero, el nombre a1 cominenza con una letra)
# valocidad = Si (nombre formado por letras)
# velocidad90 = Si (nombre formado por letras y numeros,pero iniciado por una letra)
# salario_medio = Si (el simbolod de guion bajo(_), esta permitido y facilira la lectura de los nombres grandes)
# salario medio = No (los nombres e las variables no pueden contener espacios en blanco)
# _b = Si (el guion bajo(_),es aceptado en los nombres de variables, aun en el comienzo)
# 1a = No (los nombres de variables no pueden empezar con numeros)
#camelCase = es una convención de nomenclatura en la que cada palabra dentro de una palabra compuesta se escribe con mayúscula, excepto la primera palabra.
#TODO_EN_MAYUSCULAS = se usa para nombrar constantes

#multiples variables 
name, age, city = "Jose",  26,"Boston D.C"

print(name,age,city) #para que pueda imprimor el texto de las variables se hace sin la comillas

a, b, c = 'a1', 'b2','c3'

print(a,b,c)#correcto

a1 = '1'
b2 = '2'
c3 = '3'

print   ('a1', 'b2', 'c3')#incorrecto
print (a1,b2,c3) #correcto
#concatenacion: El proceso es simple e implica vincular dos o más cadenas en secuencia, generalmente usando el operador '+'

inicio = 'hola'
final = 'mundo'

print (inicio + final)



