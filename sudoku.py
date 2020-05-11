import numpy as np 

grade= [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]


def resolve_quadrado(coluna,linha,solucao):
	global grade
	for i in range(0,9):
		if solucao == grade[coluna][i]:
			return False

	for i in range(0,9):
		if solucao == grade [i][linha]:
			return False

	x=(linha//3)*3
	y=(coluna//3)*3

	for i in range (0,3):
		for j in range (0,3):
			if grade[y+i][x+j] == solucao:
				return False

	return True


def resolve_grade():
	global grade
	for coluna in range(9):
		for linha in range(9):
			if grade[coluna][linha] == 0:
				for solucao in range(1,10):
					if resolve_quadrado(coluna,linha,solucao):
						grade[coluna][linha]=solucao
						resolve_grade()	
						grade[coluna][linha]=0
				return	

	print(np.matrix(grade))

resolve_grade()





