#13)Faça um algoritmo que leia o slário de um funcionário e mostre
# seu novo salário, com 15% de aumento.
salario = float(input('Informe o seu salário atual, para sofrer um '
                      'aumento de 15%: R$'))
res = salario+(salario*0.15)
print('O seu salário de R${}, sofreum um aumento de 15%. '
      'Valor Atualizado é: {:.2f}'.format(salario, res))