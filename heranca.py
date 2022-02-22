class Mae:  # Mamifero
    def __init__(self, p1):
        print('executando o init de Mãe')
        self.p1 = p1

class Filha(Mae):  # Felino
     def __init__(self, p1, p2):
        print('executando o init de Filha')
        self.p2 = p2
        Mae.__init__(self, p1)

class Neta(Filha):  # Gato
    def __init__(self, p1, p2, p3):
        print('executando o init de Neta') 
        self.p3 = p3
        Filha.__init__(self, p1, p2)
