class NomeDaClasse:
    pass


objeto_1 = NomeDaClasse()
objeto_2 = NomeDaClasse()

objeto_1.atributo_1 = 'Valor do atributo 1'

##########################################
class Livro:
    def __init__(self):
     self.atributo_1= 'valor1'
     self.atributo_2= 'valor2'

livro_1 = Livro()
livro_2 = Livro()

print('livro 1:', vars(livro_1))
print('livro 2:',vars(livro_2))