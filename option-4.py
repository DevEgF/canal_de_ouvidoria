claims = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

code = int(input("Digite o código da manifestação a ser deletada: "))

if code >= 1 and code <= len(claims):
    claims.pop(code-1)
    print("\nManifestação removida com sucesso!")
else:
    print("\nO código informado não existe!")