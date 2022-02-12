n = int(input('Digite um número:  '))

if n > 10:
    print('n é maior que 10')
else:
    if n== 10:
        print('n é igual a 10')
    else:
        print('n é menor a 10')

print('fim')

#ou então utilizando elif
n = int(input('Digite um número:  '))

if n > 10:
    print('n é maior que 10')
elif n== 10:
    print('n é igual a 10')
else:
    print('n é menor que 10')

print('fim')