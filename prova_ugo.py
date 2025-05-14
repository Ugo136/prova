import random

num1 = random.randint(1, 100)
palpite = 0
cont = 0

print("Você tem 10 tentativas para acertar o número inteiro aleatório entre 1 e 100. Boa sorte!")

for i in range(0, 10):
    cont += 1
    palpite = int(input("Digite seu palpite:"))
    
    if palpite > num1:
        print("Seu palpite foi maior que o número escolhido")
        print("Tente novamente")
    elif palpite < num1:
        print("Seu palpite foi menor que o número escolhido")
        print("Tente novamente")
    elif palpite == num1:
        print("Você acertou o número aleatório. Parabéns!")
        break
    if cont == 10:
        print("Número de tentativas excedido. Não seja burro na proxima vez!")
    