#4)Faça um programa que leia algo pelo teclado e mostre na tela o sseu tipo
#primitivo e todas as informações possiveis sobre ela.
v1 = input('digite algo: ')
print('Tipo da classe', type(v1))
print('É númerico? {}'.format(v1.isnumeric()))
print('É alpha numérico? {}'.format(v1.isalnum()))
print('É alfabético? {}'.format(v1.isalpha()))
print('Todas as letras está em maiúsculas? {}'.format(v1.isupper()))
print('Todas as letras está em minúsculas? {}'.format(v1.islower()))
print('Possui espaço? {}'.format(v1.isspace()))
print('Está capitalizada? {}'.format(v1.istitle()))