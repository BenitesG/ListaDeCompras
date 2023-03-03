import os

lista = []

while True:
    opcao = input('Escolha uma opção \n[i]nserir [a]pagar [l]istar: ')

    if opcao.startswith('i'):
        produto = input('Digite o produto: ')
        if produto in lista:
            os.system('cls')
            print('Já existe este produto')
        else:
            lista.append(produto)
            os.system('cls')

    if opcao.startswith('a'):
        indice = input('Escolha o indice para apagar: ')
        os.system('cls')
        if indice.isdigit():
            indice_int = int(indice)

        try:
            lista.pop(indice_int)

        except:
            os.system('cls')
            print('Indice inexistente')

    if opcao.startswith('l'):
        os.system('cls')
        if not lista:
            os.system('cls')
            print('Nada para listar')
        i = 0
        for produto in lista:
            print(i, produto)
            i += 1
