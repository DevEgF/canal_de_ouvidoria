from operacoesbd import *

def showMenu():
    print("\n-----------------------------")
    print("\nCanal de Ouvidoria\n")
    print("-----------------------------")
    print(
        "1) Listar Manifestações \n2) Adicionar Manifestação \n3) Pesquisar Manifestação \n4) Pesquisar por palavra chave \n5) Remover Manifestação \n6) Alterar Manifestação \n7) Quantidade de manifestações \n8) Sair do programa")
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
        print("\nNão existem manifestações a serem exibidas\n")
    else:
        print("\n--- Manifestações encontradas ---\n")
        for item in allClaims:
            print(item[0], "-", item[1])

def insertNewClaim(connection):
    newClaim = input("\nDigite sua manifestação: ")
    query = "INSERT INTO claims (claim) VALUES (%s)"
    value = [newClaim]

    insertedClaimInDataBase = insertInDataBase(connection, query, value)
    print("\nManifestação cadastrada com sucesso! O código é", insertedClaimInDataBase)

def researchClaimById(connection):
    code = int(input("Digite o código da manifestação a ser pesquisada: "))
    query = "select * from claims where id = %s"
    claimCode = [code]

    researchClaims = listDataBase(connection, query, claimCode)

    if researchClaims:
        for item in researchClaims:
            print("\nA manifestação registrada é:", item[1])
    else:
        print("\nO código informado da manifestação não existe!")

def researchClaimByKeyword(connection):
    keyword = input("Digite a palavra-chave que deseja buscar: ")
    query = "SELECT * FROM claims WHERE claim LIKE %s"
    search_param = [f"%{keyword}%"]

    results = listDataBase(connection, query, search_param)

    if results:
        print(f"\n--- Manifestações encontradas com a palavra-chave '{keyword}' ---\n")
        for item in results:
            print(item[0], "-", item[1])
    else:
        print(f"\nNenhuma manifestação encontrada com a palavra-chave '{keyword}'.")

def updateClaimById(connection):
    code = int(input("Digite o código da manifestação a ser substituída: "))
    claimSubstituted = input("Digite a nova manifestação: ")
    query = "UPDATE claims SET claim = %s WHERE id = %s"

    dataToUpdate = [claimSubstituted, code]

    affectedRows = updateOnDataBase(connection, query, dataToUpdate)

    if affectedRows > 0:
        print("\nManifestação substituída com sucesso!")
    else:
        print("\nO código informado não existe ou a manifestação já era a mesma!")

def deleteClaimById(connection):
    code = int(input("Digite o código da manifestação a ser deletada: "))
    query = "delete from claims where id = %s"
    claimCode = [code]

    deletedClaim = deleteOnDataBase(connection, query, claimCode)

    if deletedClaim > 0:
        print("\nManifestação removida com sucesso!")
    else:
        print("\nO código informado não existe!")