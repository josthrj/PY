#loops


#while es una condicion que se repite mientras la condicion sea verdadera

i=0 #variable de control del ciclo while  

#while i < 5:
    #print(i)
    #if i == 3:
       # break   #si el valor de "i" llega a ser igual al numero va a parar la ejecucion
   # i +=1

    
#continue es una palabra reservada que se utiliza dentro de bucles\
#(como for o while) para omitir el resto del bloque de código en la\
#iteración actual y pasar a la siguiente iteración del bucle.


#usuarios = ["federico","pedro","roman","lotter"]

#for usuarios in usuarios:
    #print(usuarios)



#usuario = "federico el perro"

#for c in usuario: #accede a los elemetos de un string en este caso a los caracteres que contiene el string usando la letra "C"
 #   print(c)


#usuarios = ["federico","pedro","roman","lotter"]

#for usuarios in usuarios:
    #if usuarios == "roman":
    #    break
    #print(usuarios)




#c

#for usuarios in usuarios:
    #if usuarios == "roman":
    #    continue
    #print(usuarios)

#for x in range(3, 30, 3):  #en este caso va aumentando las iteraciones del loop de 3 en 3 que es el valor que se ingreso como indicador
#    print(x)
#else:
#    print("hemos terminado")

usuarios = ["federico","pedro","roman","lotter"]

edades = [21, 25, 26, 14]


#iteracion de los elementos que se encuentran anidados \
#en este caso dos for loop


for usuario in usuarios: 
    for edad in edades:
        print(usuario, edad)






