class NomeDaClasse:
    pass


objeto_1 = NomeDaClasse()
objeto_2 = NomeDaClasse()

objeto_1.atributo_1 = 'Valor do atributo 1'

##########################################
class Livro:
    def __init__(self, nome, autor):
        self.nome= nome
        self.autor= autor
        self.editora= 'Nome da editora'

    def identidade(self):
        return (f'Sou o livro {self.nome}, e estou salvo '
                f'no endereço de memória: {id(self)}')

if __name__== '__main__':
    livro_1 = Livro('O cão dos Baskeville', 'Everton Silva')
    livro_2 = Livro('O Príncipe', 'Nicolau Maquiavel')

    print('livro 1:', vars(livro_1))
    print(livro_1.nome)
    print(livro_1.autor)


#print('livro 2:',vars(livro_2))#