class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)


class Gato(Animal):
    tipo = "gato"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)  # Llamada al constructor de la clase padre
        print('Hola, soy un gato extendido')

class Perro(Animal):
    tipo = "perro"
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print('Iniciando un perro')  # super siempre hace referencia a la clase padre

class Canario(Animal):
    tipo = "Canario"


gato = Gato('Fluffy', "maullido")
gato.saludo()

perro = Perro("Federico", "ladrido")
perro.saludo()

canario = Canario('Piolin', 'silbido')
canario.saludo()
