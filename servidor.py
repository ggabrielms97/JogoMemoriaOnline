# coding=utf-8
import time
import socket
import sys
from JogoDaMemoria import EstadoJogo

# Cria o socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind no endereco e porta
server_address = ('localhost', 5000)
sock.bind(server_address)

# Fica ouvindo por 2 conexoes
sock.listen(2)


while True:

    print('Aguardando a conexao do jogador')
    connection, client_address = sock.accept()

    try:
        print('Jogador chegou! :)')
        estado = EstadoJogo()  ##
        # Parametros da partida
        ##

        # Tamanho (da lateral) do tabuleiro. NECESSARIAMENTE PAR E MENOR QUE 10!
        dim = 4

        # Numero de jogadores
        nJogadores = 2

        # Numero total de pares de pecas
        totalDePares = dim ** 2 / 2  # dim x 2 x 2 / 2
        ##
        # Programa principal
        ##

        # Cria um novo tabuleiro para a partida
        tabuleiro = estado.novoTabuleiro(dim)

        # Cria um novo placar zerado
        placar = estado.novoPlacar(nJogadores)

        # Partida continua enquanto ainda ha pares de pecas a
        # casar.
        paresEncontrados = 0
        vez = 0
        while paresEncontrados < totalDePares:

            # Requisita primeira peca do proximo jogador
            while True:

                # Imprime status do jogo
                estado.imprimeStatus(tabuleiro, placar, vez)

                # Solicita coordenadas da primeira peca.
                coordenadas = estado.leCoordenada(dim)
                if coordenadas == False:
                    continue

                i1, j1 = coordenadas

                # Testa se peca ja esta aberta (ou removida)
                if estado.abrePeca(tabuleiro, i1, j1) == False:
                    print "Escolha uma peca ainda fechada!"
                    raw_input("Pressione <enter> para continuar...")
                    continue

                break

                # Requisita segunda peca do proximo jogador
            while True:

                # Imprime status do jogo
                estado.imprimeStatus(tabuleiro, placar, vez)

                # Solicita coordenadas da segunda peca.
                coordenadas = estado.leCoordenada(dim)
                if coordenadas == False:
                    continue

                i2, j2 = coordenadas

                # Testa se peca ja esta aberta (ou removida)
                if estado.abrePeca(tabuleiro, i2, j2) == False:
                    print "Escolha uma peca ainda fechada!"
                    raw_input("Pressione <enter> para continuar...")
                    continue

                break

                # Imprime status do jogo
            estado.imprimeStatus(tabuleiro, placar, vez)

            print "Pecas escolhidas --> ({0}, {1}) e ({2}, {3})\n".format(i1, j1, i2, j2)

            # Pecas escolhidas sao iguais?
            if tabuleiro[i1][j1] == tabuleiro[i2][j2]:

                print "Pecas casam! Ponto para o jogador {0}.".format(vez + 1)

                estado.incrementaPlacar(placar, vez)
                paresEncontrados = paresEncontrados + 1
                estado.removePeca(tabuleiro, i1, j1)
                estado.removePeca(tabuleiro, i2, j2)

                time.sleep(5)
            else:

                print "Pecas nao casam!"

                time.sleep(3)

                estado.fechaPeca(tabuleiro, i1, j1)
                estado.fechaPeca(tabuleiro, i2, j2)
                vez = (vez + 1) % nJogadores

        # Verificar o vencedor e imprimir
        pontuacaoMaxima = max(placar)
        vencedores = []
        for i in range(0, nJogadores):

            if placar[i] == pontuacaoMaxima:
                vencedores.append(i)

        if len(vencedores) > 1:

            sys.stdout.write("Houve empate entre os jogadores ")
            for i in vencedores:
                sys.stdout.write(str(i + 1) + ' ')

            sys.stdout.write("\n")

        else:

            print "Jogador {0} foi o vencedor!".format(vencedores[0] + 1)




    finally:
        # Clean up the connection
        connection.close()
