#12)Faça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.
prod = float(input('Informe o preço do produto atual, para receber 5% off: '))
res = prod-(prod * 0.05)
print('O preço com desconto de 5% é: {:.2f}'.format(res))