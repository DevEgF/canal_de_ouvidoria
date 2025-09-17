from ouvidoria import *

connection = createConnection('localhost', 'root', 'Egito76#', 'ouvidoria')

while True:
    showMenu()

    entry = input("Digite uma opção: ")

    if entry.isdigit():
        option = int(entry)
        print("Opção selecionada:", option)

        if option == 1:
            listClaims(connection)

        elif option == 2:
            insertNewClaim(connection)

        elif option == 3:
            researchClaimById(connection)

        elif option == 4:
            researchClaimByKeyword(connection)

        elif option == 5:
            deleteClaimById(connection)

        elif option == 6:
            updateClaimById(connection)

        elif option == 7:
            countResult = countClaimsInDatabase(connection)
            print("\nAtualmente, temos", countResult, "manifestações.")

        elif option == 8:
            print("\nSaindo do sistema de ouvidoria...Até logo!")
            break

        else:
            print("\nOpção inválida! Por favor, digite um número entre 1 e 8!")
    else:
        print("\nPor favor, digite apenas números.\n")

shutDownConnection(connection)