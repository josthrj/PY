#clases en python son como los planos de una casa y los objetos como la casa

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido 
    

    def saludo(self):#no es obligatorio usar self, pero es mejor como buena practica de escritura 
        print("hola soy", self.nombre, self.apellido )

class Admin(Usuario):
    def superSaludo(self):
        print("Hola, me llamo",self.nombre, "y soy un administrador")

#para nombrar una clase la primera letra siempre debe estar en mayuscula\
#  y el resto en minusculas aplica para todos los lenguajes






#usuario = Usuario('felipe','feliz') #asi queda como un objeto
#usuario2 = Usuario('federico','feliz')

#usuario. saludo()
#usuario2. saludo()

#usuario.nombre = "pedro"
#del usuario.nombre #elimina una instancia 

#del usuario

#print(usuario.nombre, usuario.apellido,usuario2.nombre)

#admin = Admin('super','feliz')
#admin.saludo()
#admin.superSaludo()



#ahora la aplicacion de clases y objetos con herencia

class Animal: 
    def __init__(self, nombre, onomatopeya):
        self.nombre=nombre
        self.onomatopeya=onomatopeya
    def saludo(self):
        print('hola soy un', self.tipo,  'y mi sonido es el', self.onomatopeya)




class Gato(Animal):
    tipo = "gato"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre,onomatopeya)
        print('hola,soy un gato extendido')

        
class Perro(Animal):
    tipo="perro"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre,onomatopeya)
        print('intaciando un perro') #super simepre hace referencia a la clase padre
    
class Canario(Animal):
    tipo="Canario"


gato = Gato('Fluffy',"maullido")
gato.saludo()


perro = Perro("federico","ladrido")
perro.saludo()

canario = Canario('piolin','silvido')
canario.saludo()








