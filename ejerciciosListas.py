#calculod de la media
notas = [6,7,5,5,9]
#lista con las notas obtenidas por el alumno en los exámenes.
suma_de_notas=0 #variable para almacenar sumatoria de 
x = 0
#contador que va a ir incrementando hasta llegar al final del bucle 
while x < 5:
    suma_de_notas += notas[x]
    x += 1
    print("Media: %5.2f" % (suma_de_notas/x))