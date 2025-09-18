from operacoesbd import *

def showMenu():
    print("\n-----------------------------")
    print("\nCanal de Ouvidoria\n")
    print("-----------------------------")
    print("1) Listar Manifestações \n2) Adicionar Manifestação \n3) Pesquisar Manifestação por código \n4) Pesquisar Manifestação por tipo \n5) Remover Manifestação  \n6) Quantidade de manifestações \n7) Sair do programa")
    print("-----------------------------")

def countClaimsInDatabase(connection) -> int:
    countClaimsQuery = "select count(*) from claims"
    countResult = listDataBase(connection, countClaimsQuery)
    totalClaims = countResult[0][0]
    return totalClaims

def listClaims(connection):
    selectAllClaimsQuery = "SELECT * FROM claims"
    allClaims = listDataBase(connection, selectAllClaimsQuery)

    if countClaimsInDatabase(connection) == 0:
        print("\nNão existem manifestações a serem exibidas")
    else:
        print("\n--- Manifestações encontradas ---\n")
        for item in allClaims:
            print("\n--- Detalhes da Manifestação ---")
            print("Código:",item[0])
            print("Tipo:",item[5])
            print("Título:",item[1])
            print("Descrição:",item[2])
            print("Autor:", item[4])
            print("Respondente:",item[3])
            print("---------------------------------")

def insertNewClaim(connection):
    print("\n--- Adicionar Nova Manifestação ---")

    claimsType = {
        1: "Reclamação",
        2: "Sugestão",
        3: "Elogio"
    }

    while True:
        print("\nPor favor, selecione o tipo da manifestação:")

        for code, type in claimsType.items():
            print(f"{code}) {type}")

        choose_type = input("\nDigite o número do tipo: ")

        if choose_type.isdigit():
            choose_code = int(choose_type)

            if choose_code in claimsType:
                type_selected = claimsType[choose_code]
                break
            else:
                print("\nOpção inválida! Por favor, escolha um dos números listados.")
        else:
            print("\nEntrada inválida. Por favor, digite apenas um número.")

    print(f"\nTipo selecionado: {type_selected}")

    title = input("Digite o Título da manifestação: ")
    description = input("Digite a Descrição detalhada: ")
    author = input("Digite o seu nome (autor): ")
    respondent = input("Digite o seu respondente: ")

    query = "INSERT INTO claims (title, description, author, respondent, type) VALUES (%s, %s, %s, %s, %s)"

    value = [title, description, author, respondent, type_selected]

    insertedClaimInDataBase = insertInDataBase(connection, query, value)
    print(f"\nManifestação cadastrada com sucesso! O código é {insertedClaimInDataBase}")

def researchClaimById(connection):
    code = int(input("Digite o código da manifestação a ser pesquisada: "))
    query = "select * from claims where cod = %s"
    claimCode = [code]

    researchClaims = listDataBase(connection, query, claimCode)

    if researchClaims:
        for item in researchClaims:
            print("\n--- Detalhes da Manifestação ---")
            print("Código:", item[0])
            print("Tipo:", item[5])
            print("Título:", item[1])
            print("Descrição:", item[2])
            print("Autor:", item[3])
            print("Respondente:", item[4])
            print("---------------------------------")
    else:
        print("\nO código informado da manifestação não existe!")

def researchClaimByType(connection):
    print("\n--- Pesquisar Manifestação por Tipo ---")

    claims_type = {
        1: "Reclamação",
        2: "Sugestão",
        3: "Elogio"
    }

    while True:
        print("\nPor favor, selecione o tipo da manifestação a ser pesquisada:")
        for code, type in claims_type.items():
            print(f"{code}) {type}")

        choose_type = input("\nDigite o número do tipo: ")

        if choose_type.isdigit():
            choose_cod = int(choose_type)

            if choose_cod in claims_type:
                type_selected = claims_type[choose_cod]
                break
            else:
                print("\nOpção inválida! Por favor, escolha um dos números listados.")
        else:
            print("\nEntrada inválida. Por favor, digite apenas um número.")

    query = "SELECT * FROM claims WHERE type = %s"

    search_param = [type_selected]

    results = listDataBase(connection, query, search_param)

    if results:
        print(f"\n--- Manifestações encontradas do tipo '{type_selected}' ---\n")
        for item in results:
            print(f"Código: {item[0]}")
            print(f"Título: {item[1]}")
            print(f"Autor: {item[3]}")
            print(f"Descrição: {item[2]}")
            print("-----------------------------")
    else:
        print(f"\nNenhuma manifestação encontrada para o tipo '{type_selected}'.")

def deleteClaimById(connection):
    code = int(input("Digite o código da manifestação a ser deletada: "))
    query = "delete from claims where cod = %s"
    claimCode = [code]

    deletedClaim = deleteOnDataBase(connection, query, claimCode)

    if deletedClaim > 0:
        print("\nManifestação removida com sucesso!")
    else:
        print("\nO código informado não existe!")