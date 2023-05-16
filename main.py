import random

def menu():

    tela = """
    Bem vindo ao jogo de Adivinhação!

    Qual o nível de dificuldade?
    (1) Fácil (2) Médio (3) Difícil
    """
    print(tela)

def jogar():
    
    menu()

    numeroSecreto = round(random.randrange(0, 101))
    totalDeTentativas = 0
    pontos = 1000
    

    nivel = int(input("Escolha o nível de dificuldade: "))

    if nivel == 1:
        totalDeTentativas = 20
    elif nivel == 2:
        totalDeTentativas == 10
    elif nivel == 3:
        totalDeTentativas = 5
    else:
        print("Opção de nível inválida!")
        exit()

    for rodada in range(1, totalDeTentativas + 1):
        chute = int(input("Digite um número: "))

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 a 100!")
            continue

        acertou = chute == numeroSecreto
        chuteMaior = chute > numeroSecreto
        chuteMenor = chute < numeroSecreto

        if acertou:
            print(f"Você acertou! e fez {pontos} pontos!")
            break
        else:
            if chuteMaior:
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif chuteMenor:
                print("Você errou! O seu chute foi menor do que o número secreto.")

            pontosPerdidos = abs(numeroSecreto - chute)
            pontos -= pontosPerdidos

        print(f"tentativa {rodada} de {totalDeTentativas}")
        
    print("Game Over!")

if(__name__ == '__main__'):
    jogar()