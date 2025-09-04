claims = []

code = int(input("Digite o código da manifestação a ser substituída: "))

if code >= 1 and code <= len(claims):
    claimSubstitution = input("Digite uma nova manifestação: ")
    claims[code-1] = claimSubstitution
    print("\nManifestação substituída com sucesso!")
else:
    print("\nO código informado não existe!")
