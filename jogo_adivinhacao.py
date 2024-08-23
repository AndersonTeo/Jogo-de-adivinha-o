import random

def main():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar qual é!")

    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        palpite = input("Digite seu palpite: ")
        
        if not palpite.isdigit():
            print("Por favor, digite um número válido.")
            continue

        palpite = int(palpite)
        tentativas += 1

        if palpite < numero_secreto:
            print("O número é maior.")
        elif palpite > numero_secreto:
            print("O número é menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    main()
