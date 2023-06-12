#11)Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
print('Aqui voce irá ter o resultado da tita necessária para pintar uma parede em m²!')
lar = float(input('Digite a largura da parede em metros:'))
alt = float(input('Digite a altura da parede em metros:'))
res = lar * alt
print('A área para ser pintada em m² é: {}, e a quantidade de tinta que será gasta é: '
      '{} litros\n OBS: 1 litro de tinta pinta 2m²'.format(res, res/2))