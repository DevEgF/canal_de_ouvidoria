from operacoesbd import criarConexao, listarBancoDados, encerrarConexao, insertNoBancoDados, excluirBancoDados, \
    atualizarBancoDados

conection = criarConexao('localhost', 'root', 'Egito76#', 'ouvidoria')

while True:
    print("-----------------------------")
    print("\nCanal de Ouvidoria\n")
    print("-----------------------------")
    print("1) Listar Manifestações \n2) Adicionar Manifestação \n3) Pesquisar Manifestação \n4) Remover Manifestação \n5) Alterar Manifestação \n6) Quantidade de manifestações \n7) Sair do programa")
    print("-----------------------------")

    entry = input("Digite uma opção: ")

    if entry.isdigit():
        option = int(entry)

        print("Opção selecionada:",option)

        if option == 1:
            selectAllClaimsQuery = "SELECT * FROM claims"
            allClaims = listarBancoDados(conection, selectAllClaimsQuery)

            countClaimsQuery = "select count(*) from claims"
            countResult = listarBancoDados(conection, countClaimsQuery)
            totalClaims = countResult[0][0]

            if totalClaims == 0:
                print("\nNão existem manifestações a serem exibidas\n")
            else:
                print("Lista de manifestações: \n")
                for item in allClaims:
                    print(item[0], "-", item[1])

        elif option == 2:
            newClaim = input("\nDigite sua manifestação: ")
            query = "INSERT INTO claims (claim) VALUES (%s)"
            value = [newClaim]

            insertedClaimInDataBase = insertNoBancoDados(conection, query, value)
            print("\nManifestação cadastrada com sucesso! O código é", insertedClaimInDataBase)

        elif option == 3:
            code = int(input("Digite o código da manifestação a ser pesquisada: "))
            query = "select * from claims where id = %s"

            claimCode = [code]
            researchClaims = listarBancoDados(conection, query, claimCode)
            totalClaims = researchClaims[0][0]

            if code >= 1 and code <= totalClaims:
                for item in researchClaims:
                    print("\nA manifestação registrada é:", item[1])
            else:
                print("O código informado da manifestação não existe!")

        elif option == 4:
            code = int(input("Digite o código da manifestação a ser deletada: "))
            query = "delete from claims where id = %s;"

            claimCode = [code]
            deletedClaim = excluirBancoDados(conection, query, claimCode)

            if deletedClaim > 0:
                print("\nManifestação removida com sucesso!")
            else:
                print("\nO código informado não existe!")

        elif option == 5:
            code = int(input("Digite o código da manifestação a ser substituída: "))
            claimSubstituted = input("Digite a nova manifestação: ")

            query = "UPDATE claims SET claim = %s WHERE id = %s"

            dataToUpdate = (claimSubstituted, code)

            affectedRows = atualizarBancoDados(conection, query, dataToUpdate)

            if affectedRows > 0:
                print("\nManifestação substituída com sucesso!")
            else:
                print("\nO código informado não existe ou a manifestação já era a mesma!")

        elif option == 6:
            countClaimsQuery = "select count(*) from claims"
            countResult = listarBancoDados(conection, countClaimsQuery)

            print("\nAtualmente, temos", countResult[0][0],"manifestações")

        elif option == 7:
            print("\nSaindo do sistema de ouvidoria...Até logo!")
            break

        else:
            print("\nOpção inválida! Por favor, digite um número entre 1 e 6!")
    else:
        print("\nPor favor, digite apenas números.\n")

encerrarConexao(conection)