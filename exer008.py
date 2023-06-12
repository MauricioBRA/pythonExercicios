#8)Escreva um programa que leia um valor em metros e o exiba convertido em
# centimetros e milímetros.
me = float(input('Digite um valor de metros para ser convertido em '
                 'centimetros e milímetros:'))
print('O valor em metros {}, convertido para centimetros é: {}\n'
      'O valor em metros {}, convertido para milímetros é: {}'
      .format(me, me*100, me, me*1000))