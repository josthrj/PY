#control de flujo
#if 2 < 5 : #siempre colocar ':' al final de la condicion
#   print("2 es menor que 5")


# verificaion de variables EJ

#a = 25
#b = 26



#if  a == b:
#    print(f"{a} y {b} son iguales.")
    
#if  a < b:
#    print(f"El numero mayor es el {b}")

#if  a > b:
#    print(f"El numero mas pequeño es el {a}. ")

#if  a!= b:
#    print("a es diferente de b")

#if  a <= b:
#    print("{a} no puede ser igual o mayor que {b}")

#if a >=b:
#    print ("{a} debe ser mayor o igual que {b}")



if  2 > 3 :
    print('2 es menor que 3')
elif 2 > 3:
    print('2 es mayor que 5')   
else:
    print ('No se cumple ninguna condición.')#solo si las condiciones anteriores no se cumplem


#si la condicion en if es verdadera la condicion en elif no sera tomada en cuenta

#if de una sola linea 
if 2 < 5: print('if en una linea')


#operador ternario es cuando tenemos un if de una sola linea que es cuando evalua en true y evalua en false
print('cuando devuelve true') if 5 > 2 else print('caundo devuelve false')




# AND Y OR 
# and: resulta verdadero(true) solo si los dos operadores son verdadero
# or: resulta falso solo si sus dos operadores resultan falso, si uno de los operadores da verdadero o si los dos lo hacen el resultado es verdadero


if 2 < 5 and 3 > 2:   # en este caso las dos condiciones deben devolver true o no seran ejecutadas
    print('ambas devuelven true')

if 1 < 0 or 1 > 0: #en este caso solo uno de los valores tiene que ser true para poder pasar al siguiente
    print('una sola de las condicioes da true')

if 1 < 0 or 1 < 0: # en este caso las dos condiciones son false y no se duvuelve nada
    print('ambas condiciones son false no devuelve nada')


