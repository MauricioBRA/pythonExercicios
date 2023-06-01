#4)Faça um programa que leia algo pelo teclado e mostre na tela o sseu tipo
#primitivo e todas as informações possiveis sobre ela.
v1 = input('digite algo: ')
print('Tipo da classe', type(v1),
      'é númerico? {}'.format(v1.isnumeric()),
      'é alpha numérico? {}'.format(v1.isalnum()),
      'é alfabético? {}'.format(v1.isalpha()),
      'Todas as letras é maiúsculas? {}'.format(v1.isupper()))