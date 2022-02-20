class Teste:
    def __init__(self):
        self.__nome = 0
        self.cont = 0

    @property
    def nome(self):
        print('executando a propety')
        return self.__nome    

    @nome.setter
    def nome(self, novo_nome):
        self.cont += 1
        print(f'executando o setter... {self.cont}')
        self.__nome = novo_nome    