def dobrar(x):
    return 2 * x

def triplicar(x):
    triplo = 3 * x
    return triplo

def quatro(x):
    quatro = 4 * x
    return quatro

n1 = float(input('Digite um número: '))  
dobro = dobrar(n1)
print(f'O dobro é: {dobro}')
print(f'O triplo é: {triplicar(n1)}') 
print(f'O Quádruplo é: {quatro(n1)}')     