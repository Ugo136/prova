import random

dificuldade = input("Escolha a dificuldade digitando 'normal', 'dificil' ou 'impossivel'")

if dificuldade == "normal":
    num1 = random.randint(1, 100)
    palpite = 0
    cont = 0
    jogo = True
    escolha = 0
    pontuacao = 0
    
    print("Neste jogo tem sistema de pontuação. Caso você acerte em 1 tentativa você gahará 10 pontos, entre 15 e 19 apenas 3, entre 8 e 14 apenas 5 , entre 2 e 7 apenas 7. Caso não acerte obviamente ganhará 0.")
    print("Você tem 20 tentativas para acertar o número inteiro aleatório entre 1 e 100. Boa sorte!")
    
    while jogo:
        cont += 1
        if cont == 1:
            pontuacao = 10
        if 2 <= cont <= 7:
            pontuacao = 7
        if 8 <= cont <= 14:
            pontuacao = 5
        if 15 <= cont <= 19:
            pontuacao = 3
        if cont == 20:
            pontuacao = 0
        
        palpite = int(input("Digite seu palpite:"))
    
        if palpite > num1:
            print("Seu palpite foi maior que o número escolhido")
            print("Tente novamente")
    
        elif palpite < num1:
            print("Seu palpite foi menor que o número escolhido")
            print("Tente novamente")
    
        elif palpite == num1:
            print("Você acertou o número aleatório. Parabéns!")
            print("Sua pontuação foi", pontuacao)
            print("O número de tentativas usadas foi", cont)
        
            escolha = input("Quer jogar novamente? digite 'sim' ou 'não' para decidir:")
            
            if escolha == "sim":
                cont = 0
                num1 = random.randint(1, 100)
            
                print("Você tem 20 tentativas para acertar o número inteiro aleatório entre 1 e 100. Boa sorte!")
            
            elif escolha == "não":
                jogo = False
        
        if cont == 21:
            print("Número de tentativas excedido.")
            escolha = input("Quer jogar novamente? digite 'sim' ou 'não' para decidir:")
            
            if escolha == "sim":
                cont = 0
                num1 = random.randint(1, 100)
                
                print("Você tem 20 tentativas para acertar o número inteiro aleatório entre 1 e 100. Boa sorte!")
                
            elif escolha == "não":
                print("Sua pontuação foi", pontuacao)
                print("O número de tentativas foi excedido")
                jogo = False

if dificuldade == "dificil":
    num1 = random.randint(1, 100)
    palpite = 0
    cont = 0
    jogo = True
    escolha = 0
    pontuacao = 0
    
    print("Neste jogo tem sistema de pontuação. Caso você acerte em 1 tentativa você gahará 10 pontos, entre 9 e 7 apenas 3, entre 4 e 6 apenas 5 , entre 2 e 3 apenas 7, se for em 1 tentativa pontuação máxima 10. Caso não acerte obviamente 0.")
    print("Você tem 10 tentativas para acertar o número inteiro aleatório entre 1 e 100. Boa sorte!")
    
    while jogo:
        cont += 1
        if cont == 1:
            pontuacao = 10
        if 2 <= cont <= 3:
            pontuacao = 7
        if 4 <= cont <= 6:
            pontuacao = 5
        if 7 <= cont <= 9:
            pontuacao = 3
        if cont == 10:
            pontuacao = 0
        
        palpite = int(input("Digite seu palpite:"))
    
        if palpite > num1:
            print("Seu palpite foi maior que o número escolhido")
            print("Tente novamente")
    
        elif palpite < num1:
            print("Seu palpite foi menor que o número escolhido")
            print("Tente novamente")
    
        elif palpite == num1:
            print("Você acertou o número aleatório. Parabéns!")
            print("Sua pontuação foi", pontuacao)
            print("O número de tentativas usadas foi", cont)
        
            escolha = input("Quer jogar novamente? digite 'sim' ou 'não' para decidir:")
            
            if escolha == "sim":
                cont = 0
                num1 = random.randint(1, 100)
            
                print("Você tem 10 tentativas para acertar o número inteiro aleatório entre 1 e 100. Boa sorte!")
            
            elif escolha == "não":
                jogo = False
        
        if cont == 10:
            print("Número de tentativas excedido.")
            escolha = input("Quer jogar novamente? digite 'sim' ou 'não' para decidir:")
            
            if escolha == "sim":
                cont = 0
                num1 = random.randint(1, 100)
                
                print("Você tem 10 tentativas para acertar o número inteiro aleatório entre 1 e 100. Boa sorte!")
                
            elif escolha == "não":
                print("Sua pontuação foi", pontuacao)
                print("O número de tentativas foi excedido")
                jogo = False

if dificuldade == "impossivel":
    num1 = round(random.uniform(1, 50), 2)
    
    palpite = 0
    cont = 0
    jogo = True
    escolha = 0
    pontuacao = 0
    
    print("Neste jogo tem sistema de pontuação. Caso você acerte em 1 tentativa você gahará 10 pontos, entre 9 e 7 apenas 3, entre 4 e 6 apenas 5 , entre 2 e 3 apenas 7, se for em 1 tentativa pontuação máxima 10. Caso não acerte obviamente 0.")
    print("Você tem 10 tentativas para acertar o número real com 2 casas decimais aleatório entre 1 e 50. Boa sorte!")
    
    while jogo:
        cont += 1
        if cont == 1:
            pontuacao = 10
        if 2 <= cont <= 3:
            pontuacao = 7
        if 4 <= cont <= 6:
            pontuacao = 5
        if 7 <= cont <= 9:
            pontuacao = 3
        if cont == 10:
            pontuacao = 0
        
        palpite = float(input("Digite seu palpite:"))
    
        if palpite > num1:
            print("Seu palpite foi maior que o número escolhido")
            print("Tente novamente")
    
        elif palpite < num1:
            print("Seu palpite foi menor que o número escolhido")
            print("Tente novamente")
    
        elif palpite == num1:
            print("Você acertou o número aleatório. Parabéns!")
            print("Sua pontuação foi", pontuacao)
            print("O número de tentativas usadas foi", cont)
        
            escolha = input("Quer jogar novamente? digite 'sim' ou 'não' para decidir:")
            
            if escolha == "sim":
                cont = 0
                num1 = round(random.uniform(1, 50), 2)
            
                print("Você tem 10 tentativas para acertar o número real com 2 casas decimais aleatório entre 1 e 50. Boa sorte!")
            
            elif escolha == "não":
                jogo = False
        
        if cont == 10:
            print("Número de tentativas excedido.")
            escolha = input("Quer jogar novamente? digite 'sim' ou 'não' para decidir:")
            
            if escolha == "sim":
                cont = 0
                num1 = round(random.uniform(1, 50), 2)
                
                print("Você tem 10 tentativas para acertar o número real com 2 casas decimais aleatório entre 1 e 50. Boa sorte!")
                
            elif escolha == "não":
                print("Sua pontuação foi", pontuacao)
                print("O número de tentativas foi excedido")
                jogo = False
