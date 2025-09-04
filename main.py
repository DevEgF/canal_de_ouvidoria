claims = []

while True:
    print("-----------------------------")
    print("\nCanal de Ouvidoria\n")
    print("-----------------------------")
    print("1) Listar Manifestações \n2) Adicionar Manifestação \n3) Pesquisar Manifestação \n4) Remover Manifestação \n5) Alterar Manifestação \n6) Sair")
    print("-----------------------------")

    option = int(input("Digite uma opção: "))

    if option == 1:
        if len(claims) == 0:
            print("\nNão existem manifestações a serem exibidas\n")
        else:
            print("Lista de manifestações: ")
            claimsIds = range(len(claims))
            for id in claimsIds:
                print(id + 1, "-", claims[id])

    elif option == 2:
        newClaim = input("\nDigite sua manifestação: ")
        claims.append(newClaim)
        print("\nManifestação cadastrada com sucesso!")

    elif option == 3:
        code = int(input("Digite o código da manifestação a ser pesquisada: "))

        if code >= 1 and code <= len(claims):
            claimResearched = claims[code - 1]
            print("\nA manifestação registrada é:", claimResearched)
        else:
            print("O código informado da manifestação não existe!")

    elif option == 4:
        code = int(input("Digite o código da manifestação a ser deletada: "))

        if code >= 1 and code <= len(claims):
            claims.pop(code - 1)
            print("\nManifestação removida com sucesso!")
        else:
            print("\nO código informado não existe!")

    elif option == 5:
        code = int(input("Digite o código da manifestação a ser substituída: "))

        if code >= 1 and code <= len(claims):
            claimSubstitution = input("Digite uma nova manifestação: ")
            claims[code - 1] = claimSubstitution
            print("\nManifestação substituída com sucesso!")
        else:
            print("\nO código informado não existe!")

    elif option == 6:
        print("\nSaindo do sistema de ouvidoria...Até logo!")
        break

    else:
        print("\nOpção inválida! Por favor, digite um número entre 1 e 6!")