import os
import sys
import time
import random


class EstadoJogo:
	##
	# Funcoes uteis
	##

	# Limpa a tela.
	def limpaTela(self):
		
		os.system('cls' if os.name == 'nt' else 'clear')

	##
	# Funcoes de manipulacao do tabuleiro
	##

	# Imprime estado atual do tabuleiro
	def imprimeTabuleiro(self, tabuleiro):

		# Limpa a tela
		self.limpaTela()

		# Imprime coordenadas horizontais
		dim = len(tabuleiro)
		sys.stdout.write("     ")
		for i in range(0, dim):
			sys.stdout.write("{0:2d} ".format(i))

		sys.stdout.write("\n")

		# Imprime separador horizontal
		sys.stdout.write("-----")
		for i in range(0, dim):
			sys.stdout.write("---")

		sys.stdout.write("\n")

		for i in range(0, dim):

			# Imprime coordenadas verticais
			sys.stdout.write("{0:2d} | ".format(i))

			# Imprime conteudo da linha 'i'
			for j in range(0, dim):

				# Peca ja foi removida?
				if tabuleiro[i][j] == '-':

					# Sim.
					sys.stdout.write(" - ")

				# Peca esta levantada?
				elif tabuleiro[i][j] >= 0:

					# Sim, imprime valor.
					sys.stdout.write("{0:2d} ".format(tabuleiro[i][j]))
				else:

					# Nao, imprime '?'
					sys.stdout.write(" ? ")

			sys.stdout.write("\n")

	# Cria um novo tabuleiro com pecas aleatorias. 
	# 'dim' eh a dimensao do tabuleiro, necessariamente
	# par.
	def novoTabuleiro(self, dim):

		# Cria um tabuleiro vazio.
		tabuleiro = []
		for i in range(0, dim):

			linha = []
			for j in range(0, dim):

				linha.append(0)

			tabuleiro.append(linha)

		# Cria uma lista de todas as posicoes do tabuleiro. Util para
		# sortearmos posicoes aleatoriamente para as pecas.
		posicoesDisponiveis = []
		for i in range(0, dim):

			for j in range(0, dim):

				posicoesDisponiveis.append((i, j))

		# Varre todas as pecas que serao colocadas no 
		# tabuleiro e posiciona cada par de pecas iguais
		# em posicoes aleatorias.
		for j in range(0, dim / 2):
			for i in range(1, dim + 1):

				# Sorteio da posicao da segunda peca com valor 'i'
				maximo = len(posicoesDisponiveis)
				indiceAleatorio = random.randint(0, maximo - 1)
				rI, rJ = posicoesDisponiveis.pop(indiceAleatorio)

				tabuleiro[rI][rJ] = -i

				# Sorteio da posicao da segunda peca com valor 'i'
				maximo = len(posicoesDisponiveis)
				indiceAleatorio = random.randint(0, maximo - 1)
				rI, rJ = posicoesDisponiveis.pop(indiceAleatorio)

				tabuleiro[rI][rJ] = -i

		return tabuleiro

	# Abre (revela) peca na posicao (i, j). Se posicao ja esta
	# aberta ou se ja foi removida, retorna False. Retorna True
	# caso contrario.
	def abrePeca(self, tabuleiro, i, j):

		if tabuleiro[i][j] == '-':
			return False
		elif tabuleiro[i][j] < 0:
			tabuleiro[i][j] = -tabuleiro[i][j]
			return True

		return False

	# Fecha peca na posicao (i, j). Se posicao ja esta
	# fechada ou se ja foi removida, retorna False. Retorna True
	# caso contrario.
	def fechaPeca(self, tabuleiro, i, j):

		if tabuleiro[i][j] == '-':
			return False
		elif tabuleiro[i][j] > 0:
			tabuleiro[i][j] = -tabuleiro[i][j]
			return True

		return False

	# Remove peca na posicao (i, j). Se posicao ja esta
	# removida, retorna False. Retorna True
	# caso contrario.
	def removePeca(self, tabuleiro, i, j):

		if tabuleiro[i][j] == '-':
			return False
		else:
			tabuleiro[i][j] = "-"
			return True

	## 
	# Funcoes de manipulacao do placar
	##

	# Cria um novo placar zerado.
	def novoPlacar(self, nJogadores):

		return [0] * nJogadores

	# Adiciona um ponto no placar para o jogador especificado.
	def incrementaPlacar(self, placar, jogador):

		placar[jogador] = placar[jogador] + 1

	# Imprime o placar atual.
	def imprimePlacar(self, placar):

		nJogadores = len(placar)

		print "Placar:"
		print "---------------------"
		for i in range(0, nJogadores):
			print "Jogador {0}: {1:2d}".format(i + 1, placar[i])

	##
	# Funcoes de interacao com o usuario
	#

	# Imprime informacoes basicas sobre o estado atual da partida.
	def imprimeStatus(self, tabuleiro, placar, vez):

			self.imprimeTabuleiro(tabuleiro)
			sys.stdout.write('\n')

			self.imprimePlacar(placar)
			sys.stdout.write('\n')
			sys.stdout.write('\n')

			print "Vez do Jogador {0}.\n".format(vez + 1)

	# Le um coordenadas de uma peca. Retorna uma tupla do tipo (i, j)
	# em caso de sucesso, ou False em caso de erro.
	def leCoordenada(self, dim):

		input = raw_input("Especifique uma peca: ")

		try:
			i = int(input.split(' ')[0])
			j = int(input.split(' ')[1])
		except ValueError:
			print "Coordenadas invalidas! Use o formato \"i j\" (sem aspas),"
			print "onde i e j sao inteiros maiores ou iguais a 0 e menores que {0}".format(dim)
			raw_input("Pressione <enter> para continuar...")
			return False

		if i < 0 or i >= dim:

			print "Coordenada i deve ser maior ou igual a zero e menor que {0}".format(dim)
			raw_input("Pressione <enter> para continuar...")
			return False

		if j < 0 or j >= dim:

			print "Coordenada j deve ser maior ou igual a zero e menor que {0}".format(dim)
			raw_input("Pressione <enter> para continuar...")
			return False

		return (i, j)

