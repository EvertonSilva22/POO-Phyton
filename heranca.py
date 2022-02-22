class Mae:  # Mamifero
    def __init__(self, p1):
        print('executando o init de Mãe')

class Filha(Mae):  # Felino
     def __init__(self, p1, p2):
        print('executando o init de Filha')


class Neta(Filha):  # Gato
    def __init__(self, p1, p2, p3):
        print('executando o init de Neta') 
