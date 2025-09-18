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

def selectedTypeClaim() -> str:
    claimsType = {
        1: "Reclamação",
        2: "Sugestão",
        3: "Elogio"
    }

    while True:
        print("\nPor favor, selecione o tipo da manifestação:")

        for code, type in claimsType.items():
            print(code, type)

        chooseType = input("\nDigite o número do tipo: ")

        if chooseType.isdigit():
            chooseCode = int(chooseType)

            if chooseCode in claimsType:
                typeSelected = claimsType[chooseCode]
                break
            else:
                print("\nOpção inválida! Por favor, escolha um dos números listados.")
        else:
            print("\nEntrada inválida. Por favor, digite apenas um número correspondente ao tipo.")
    return typeSelected

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

    typeSelected = selectedTypeClaim()

    print("Tipo selecionado:", typeSelected)

    title = input("Digite o título da manifestação: ")
    description = input("Digite a descrição detalhada: ")
    author = input("Digite o seu nome (autor): ")
    respondent = input("Digite o seu respondente: ")

    query = "INSERT INTO claims (title, description, author, respondent, type) VALUES (%s, %s, %s, %s, %s)"

    value = [title, description, author, respondent, typeSelected]

    insertedClaimInDataBase = insertInDataBase(connection, query, value)
    print("Manifestação cadastrada com sucesso! O código é", insertedClaimInDataBase)

def researchClaimByCod(connection):
    code = input("Digite o código da manifestação a ser pesquisada: ")

    if code.isdigit():
        cod = int(code)
        query = "select * from claims where cod = %s"
        claimCode = [cod]

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

    else:
        print("\nPor favor, digite apenas números.\n")

def researchClaimByType(connection):
    print("\n--- Pesquisar Manifestação por Tipo ---")

    typeSelected = selectedTypeClaim()
    query = "SELECT * FROM claims WHERE type = %s"
    searchParam = [typeSelected]

    results = listDataBase(connection, query, searchParam)

    if results:
        print("\n--- Manifestações encontradas do tipo",typeSelected,"---\n")
        for item in results:
            print("Código:",item[0])
            print("Título:",item[1])
            print("Autor:",item[3])
            print("Descrição:",item[2])
            print("-----------------------------")
    else:
        print("\nNenhuma manifestação encontrada para o tipo",typeSelected,".")

def deleteClaimByCod(connection):
    code = input("Digite o código da manifestação a ser deletada: ")

    if code.isdigit():
        cod = int(code)

        hasExist = "SELECT cod FROM claims WHERE cod = %s"
        claimCode = [cod]
        existingClaim = listDataBase(connection, hasExist, claimCode)

        if existingClaim:
            queryDelete = "DELETE FROM claims WHERE cod = %s"
            deleteOnDataBase(connection, queryDelete, claimCode)
            print("\nManifestação removida com sucesso!")

        else:
            print("\nO código informado não existe!")

    else:
        print("\nPor favor, digite apenas números.")
