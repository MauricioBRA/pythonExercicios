#10)Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos Dólares ela pode comprar (cotação do dólar US$1,00 = R$4,86)
money = float(input('Informe quanto voce tem na carteira, para mostrar quantos '
                    'dólares pode comprar:'))
print('Seu valor na carteira é: R${}, pode comprar US${:.2f} dólares.'
      .format(money, money/4.86))
print('OBS: Essa cotação é referente ao dia 12/06/2023')