#6)Crie um algoritmo que leia um número e mostre o seu dobro,
# triplo e a raiz quadrada.
v = float(input('Digite um valor para mostrar o seu dobro, triplo e a raiz quadrada:'))
print('O dobro de {} é: {}\n O triplo de {} é: {}\n A raiz quadrada de {} é: {:.3f}'
      .format(v, v*2, v, v*3, v, v**(1/2)))