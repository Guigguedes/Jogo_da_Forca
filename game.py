import os
import sys
from functions import limpaTela, menuEscolhas, jogar, escolhaPalavra, jogo, indicaPalavra, erros, derrota, vitoria, historico, restart

iniciar = 1

while iniciar == 1:
    desafiante = input('Insira o nome do Desafiante: ')
    competidor = input('Insira o nome do Competidor: ')

    competidorVencedor = 0
    desafianteVencedor = 0

    limpaTela()

    descoberto = []

    palavra = escolhaPalavra()

    dica1 = input('Dica 1: ')
    dica2 = input('Dica 2: ')
    dica3 = input('Dica 3: ')
    contadorDica = 0 
    erro = 0
    contador = 0
    limite = False
    limpaTela()

    acerto = False
    e = False

    for z in range(0, len(palavra)):
        descoberto.append('_')
    while acerto == False:
        print('Erros: ',contador)
        print('A palavra é: ')
        print(descoberto)
        print('Ela possui',len(palavra), 'letras.')
        print('')
        escolha = menuEscolhas()
        if escolha == '2':
            contadorDica = contadorDica + 1
            if contadorDica == 1:
                limpaTela()
                print('Dica 1: ', dica1)
                print("")
                indicaPalavra(descoberto,palavra,contador)
                print('')
                tentativa = jogar()
                contador = contador + jogo(tentativa,palavra,descoberto)
                limpaTela()
                if contador == 5:
                    limite = 1
                    break
                if descoberto == palavra:
                    acerto = True
                    break
            elif contadorDica == 2:
                limpaTela()
                print('Dica 2: ', dica2)
                print('')
                indicaPalavra(descoberto,palavra,contador)
                print('')
                tentativa = jogar()
                contador = contador + jogo(tentativa,palavra,descoberto)
                limpaTela()
                if contador == 5:
                    limite = 1
                    break
                if descoberto == palavra:
                    acerto = True
                    break
            elif contadorDica == 3:
                limpaTela()
                print('Dica 3: ', dica3)
                print("")
                indicaPalavra(descoberto,palavra,contador)
                print('')
                tentativa = jogar()
                contador = contador + jogo(tentativa,palavra,descoberto)
                limpaTela()
                if contador == 5:
                    limite = 1
                    break
                if descoberto == palavra:
                    acerto = True
                    break
            else:
                limpaTela()
                print('Você não possui mais dicas!')
                print('')
                indicaPalavra(descoberto,palavra,contador)
                print('')
                tentativa = jogar()
                contador = contador + jogo(tentativa,palavra,descoberto)
                limpaTela()
                if contador == 5:
                    limite = 1
                    break
                if descoberto == palavra:
                    acerto = True
                    break
        elif escolha == "1":
            limpaTela()
            indicaPalavra(descoberto,palavra,contador)
            print('')
            tentativa = jogar()
            contador = contador + jogo(tentativa,palavra,descoberto)
            limpaTela()
            if contador == 5:
                limite = 1
                break
            if competidor == palavra:
                acerto = True
                break
            if descoberto == palavra:
                acerto = True
                break
    if acerto == True:
        limpaTela()
        print(competidor,', você venceu!')
        print('')
        competidorVencedor = 1
        palavra = str(palavra)
        print('Histórico de partidas:')
        historico(competidorVencedor,palavra,competidor,desafiante)
        fim = restart()
        if fim == 1:
            limpaTela()
            pass
        else:
            iniciar = 0
            limpaTela()
    if limite == 1:
        limpaTela()
        print(desafiante,', você venceu!')
        print('')
        desafianteVencedor = 1
        palavra = str(palavra)
        print('Histórico de partidas:')
        historico(desafianteVencedor,palavra,desafiante,competidor)
        fim = restart()
        if fim == 1:
            limpaTela()
            pass
        else:
            iniciar = 0
            limpaTela()


