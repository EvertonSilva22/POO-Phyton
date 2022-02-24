#sobrecarga 

def sobrecarga(nome, numero=None):
    print(nome)
    if numero:
        print(numero)


print('Primeira função')
sobrecarga('Everton')     

print('\nsegunda execução')
sobrecarga('Everton', 10)