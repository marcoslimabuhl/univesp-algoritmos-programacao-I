# Dada a lista de notas de trabalho de casa dos alunos
# >>> notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
print(notas)
# escreva:

# (a) Uma expressão que avalia para o número de 7 notas.
print(notas.count(7))

# (b) Uma instrução que muda a última nota para 4.
notas[-1] = 4
print(notas)

# (c) Uma expressão que avalia para a nota mais alta.
print(max(notas))

# (d) Uma instrução que classifica as notas da lista.
print(sorted(notas))

# (e) Uma expressão que avalia para a média das notas.
print(sum(notas) / len(notas))