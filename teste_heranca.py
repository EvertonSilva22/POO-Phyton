from heranca import Mae, Filha, Neta

print('Criando objeto de Mae...')
mae = Mae(1)

print('\n\n criando objeto de Filha...')
filha = Filha(1, 2)


print('\n\n criando objeto de Neta...')
neta = Neta(1, 2, 3)

print('\n Visualizando os objetos')
print('mae', vars(mae))
print('filha', vars(filha))
print('neta', vars(neta))