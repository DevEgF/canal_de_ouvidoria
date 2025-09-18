from ouvidoria import *

connection = createConnection('localhost', 'root', 'Egito76#', 'feedback')

if connection:
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
                researchClaimByCod(connection)

            elif option == 4:
                researchClaimByType(connection)

            elif option == 5:
                deleteClaimByCod(connection)

            elif option == 6:
                countResult = countClaimsInDatabase(connection)
                print("\nAtualmente, temos", countResult, "manifestações.")

            elif option == 7:
                print("\nSaindo do sistema de ouvidoria...Até logo!")
                break

            else:
                print("\nOpção inválida! Por favor, digite um número entre 1 e 7!")
        else:
            print("\nPor favor, digite apenas números.\n")

    shutDownConnection(connection)

else:
    print("Connection refused")