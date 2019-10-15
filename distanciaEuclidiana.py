import math

joao = [0, 5, 7, 8, 9, 10, 3]
gabi = [5, 8, 8, 3, 2, 1, 4]
fe = [4, 6, 6, 1, 3, 4, 5]
ramon = [2, 0, 5, 2, 7, 6, 7]
pedrinho = [1, 7, 4, 3, 5, 10, 10]


def dist_euclidiana(v1, v2):
	dim, soma = len(v1), 0
	for i in range(dim):
		soma += math.pow(v1[i] - v2[i], 2)
	return math.sqrt(soma)


vetorResult = []
vetorResult.append(dist_euclidiana(joao, gabi))
vetorResult.append(dist_euclidiana(joao, fe))
vetorResult.append(dist_euclidiana(joao, ramon))
vetorResult.append(dist_euclidiana(joao, pedrinho))

nposicao = vetorResult.index(min(vetorResult))

if nposicao == 1: print("Gabi")
if nposicao == 2: print("Fe")
if nposicao == 3: print("Ramon")
if nposicao == 4: print("Pedrinho")
