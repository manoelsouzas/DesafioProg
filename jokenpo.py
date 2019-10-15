from random import randint
lista = ("Pedra", "Papel", "Tesoura")

computador = randint(0,2)

jogador = int(input('''Escolha uma opcao para se jogar: 

[0] Pedra
[1] Papel
[2] Tesoura
 
Digite sua escolha: '''))

print("Jo-Ken-Po!")

print("O computador escolheu: {}".format(lista[computador]))
print("O jogador escolheu: {}".format(lista[jogador]))

if computador == 0:
    if jogador == 0:
        print("Empate!")
    elif jogador == 1:
        print("Jogador perdeu")
    elif jogador == 2:
        print("Computador venceu")
    else:
        print("Operacao invalida")

elif computador == 1:
    if jogador == 0:
        print("Computador perdeu")
    elif jogador == 1:
        print("Empate!")
    elif jogador == 2:
        print("Jogador venceu")
    else:
        print("Operacao invalida")
elif computador == 2:
    if jogador == 0:
        print("Jogador venceu")
    elif jogador == 1:
        print("Computador venceu")
    elif jogador == 2:
        print("Empate!")
    else:
        print("Operacao invalida")
else:
    print("Operacao invalida")