matrizJogo = [
    [11,12,13],
    [21,22,23],
    [31,32,33]
]
while True:
    def jogo():
 
        for i in range(0,9):
            for q in range(0,len(matrizJogo)):
                print(matrizJogo[q])
            if(i%2 == 0):
                print("Vez do jogador 1 [x]")
                escolhaJogadorUm = int(input("Insira a posição de sua escolha: "))
                insereEscolha(escolhaJogadorUm,1)
                if(verificaResultado("x") == 3):
                    for k in range(0,len(matrizJogo)):
                        print(matrizJogo[k])
                    print("o jogador 1 ganhou o jogo!")
                    break
            else:
                print("Vez do jogador 2 [o]")
                escolhaJogadorDois = int(input("Insira o posição de sua escolha: "))
                insereEscolha(escolhaJogadorDois,2)
                if(verificaResultado("o") == 3):
                    for k in range(0,len(matrizJogo)):
                        print(matrizJogo[k])
                    print("O jogador 2 ganhou o jogo!")                    
                    break
            if(i == 8):
                print("Fim de Jogo! \nEmpate!")
    def insereEscolha(caminhoEscolha,jogador):
        if(jogador == 1):
            tratamentoEscolha = str(caminhoEscolha)
            for i in range(0,len(tratamentoEscolha)):
                if(matrizJogo[int(tratamentoEscolha[0])-1][int(tratamentoEscolha[1])-1] != "x" and matrizJogo[int(tratamentoEscolha[0])-1][int(tratamentoEscolha[1])-1] != "o"):
                    matrizJogo[int(tratamentoEscolha[0])-1][int(tratamentoEscolha[1])-1] = "x"
                    break
                else:
                    print("Escolha inválida, jogador 1 perdeu a vez!")
                    break
        if(jogador == 2):
            tratamentoEscolha = str(caminhoEscolha)
            for i in range(0,len(tratamentoEscolha)):
                if(matrizJogo[int(tratamentoEscolha[0])-1][int(tratamentoEscolha[1])-1] != "x" and matrizJogo[int(tratamentoEscolha[0])-1][int(tratamentoEscolha[1])-1] != "o"):
                    matrizJogo[int(tratamentoEscolha[0])-1][int(tratamentoEscolha[1])-1] = "o"
                    break
                else:
                    print("Escolha inválida, jogador 2 perdeu a vez!")
                    break
    def verificaResultado(symbolPlayer):
        pontoDiagonal = 0
        pontoDiagonalSecundaria = 0
        pontoLinhas0 = 0
        pontoLinhas1 = 0
        pontoLinhas2 = 0
        pontosColuna0 = 0
        pontosColuna1 = 0
        pontosColuna2 = 0
        for x in range(0,3):
            for y in range(0,3):
                if(x==y and matrizJogo[x][y] == symbolPlayer):
                    pontoDiagonal += 1
                if((x == 0 and y == 2) or (x == 1 and y == 1) or (x == 2 and y == 0)):
                    if(matrizJogo[x][y] == symbolPlayer):
                        pontoDiagonalSecundaria += 1
                if(x == 0):
                    if(matrizJogo[x][y] == symbolPlayer):
                        pontoLinhas0 += 1
                        if(y == 2 and pontoLinhas0 != 3):
                            pontoLinhas0 = 0
                if(x == 1):
                    if(matrizJogo[x][y] == symbolPlayer):
                        pontoLinhas1 += 1
                        if(y == 2 and pontoLinhas1 != 3):
                            pontoLinhas1 = 0
                if(x == 2):
                    if(matrizJogo[x][y] == symbolPlayer):
                        pontoLinhas2 += 1
                        if(y == 2 and pontoLinhas2 != 3):
                            pontoLinhas2 = 0
                if(y == 0):
                    if(matrizJogo[x][y] == symbolPlayer):
                        pontosColuna0 += 1
                        if(x == 2 and pontosColuna0 != 3):
                            pontosColuna0 = 0
                if(y == 1):
                    if(matrizJogo[x][y] == symbolPlayer):
                        pontosColuna1 += 1
                        if(x == 2 and pontosColuna1 != 3):
                            pontosColuna1 = 0
                if(y == 2):
                    if(matrizJogo[x][y] == symbolPlayer):
                        pontosColuna2 += 1
                        if(x == 2 and pontosColuna2 != 3):
                            pontosColuna2 = 0
                if(pontoDiagonal == 3):
                    return 3
                if(pontoDiagonalSecundaria == 3):
                    return 3
                if(pontoLinhas0 == 3):
                    return 3
                if(pontoLinhas1 == 3):
                    return 3
                if(pontoLinhas2 == 3):
                    return 3
                if(pontosColuna0 == 3):
                    return 3
                if(pontosColuna1 == 3):
                    return 3
                if(pontosColuna2 == 3):
                    return 3
    jogo()
    resposta_final=str(input("Quer encerrar o jogo?[S][N]]"))
    if(resposta_final == "S" or resposta_final == "s"):
        break
    elif(resposta_final != "S" or resposta_final != "s"):
        print("     ")
        matrizJogo = [
        [11,12,13],
        [21,22,23],
        [31,32,33]
        ]       
        