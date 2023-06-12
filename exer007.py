#7)Desenvolva um programa que leia as duas notas de um aluno(a), calcule e
# mostre a sua média.
nome = input('Digite o nome do aluno(a):')
nota1 = float(input('Digite a primeria nota:'))
nota2 = float(input('Digite a segunda nota:'))
print('A média do(a) aluno(a) {} é: {}'.format(nome, (nota1+nota2)/2))