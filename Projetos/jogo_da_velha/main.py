#jogo da velha

tabuleiro = [' ' for _ in range(9)]
# print(tabuleiro)

def exibir_tabuleiro() :
    print()
    for i in range(0, 9, 3):
        # Exibe cada linha do tabuleiro, pegando três elementos por vez
        print(f'{tabuleiro[i]} | {tabuleiro[i+1]} | {tabuleiro[i+2]}')
        if i < 6:
            # Imprime uma linha separadora entre as linhas do tabuleiro
            print('--|---|--')
    print()

def jogada(jogador):
    while True:
        try:
            posicao = int(input(f"Jogador {jogador}, escolha uma posição entre 1 e 9: ")) - 1
            if posicao < 0 or posicao > 8:
                print("Posição inválida! Escolha um número entre 1 e 9")
            elif tabuleiro[posicao] != ' ':
                print("Posição já ocupada! Escolha outra posição.")
            else:
                tabuleiro[posicao] = jogador
                break
        except ValueError:
            print("Entrada inválida! Por favor, Insira um número entre 1 e 9.")

def verificacao_vitoria(jogador):
    combinacoes = [
        [0, 1, 2], 
        [3, 4, 5], 
        [6, 7, 8], 

        [0, 3, 6], 
        [1, 4, 7],
        [2, 5, 8],

        [0, 4, 8],
        [2, 4, 6]
    ]
    for combinacao in combinacoes:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False

def iniciar_jogo():
    jogador_atual = 'X'
    for turno in range(9):
        exibir_tabuleiro()
        jogada(jogador_atual)
        if verificacao_vitoria(jogador_atual):
            exibir_tabuleiro()
            print(f"Jogador {jogador_atual} venceu!")
            return
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
    exibir_tabuleiro()
    print("Empate!")

iniciar_jogo()

