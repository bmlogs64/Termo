from modulos import listaPalavras

palavra = str(listaPalavras.pop())

respostas = ["#","#","#","#","#"]

tentativa = 6

while True:

    if tentativa < 1:
        break

    if tentativa != 6:
        print(f"Você ainda tem {tentativa} tentativas")

    palavraChutada = input("Qual a palavra?\n")

    if len(palavraChutada) != 5 :
        
        print("Palavra com tamanho errado, tente novamente!")
        continue

    palavraChutadaLista = list(palavraChutada)

    if palavraChutada.upper() == palavra:
        print(f"Você acertou!\nA palavra era {palavra}")
        break

    for i in range(len(palavra)):
        
        if palavraChutadaLista[i].upper() in palavra:

            if palavraChutadaLista[i].upper() == palavra[i]:

                respostas[i] = palavraChutadaLista[i].upper()

            else:

                respostas[i] = palavraChutadaLista[i].lower()

    print(f'{respostas[0]} {respostas[1]} {respostas[2]} {respostas[3]} {respostas[4]}')

    tentativa -= 1
