claims = []

code = int(input("Digite o código da manifestação a ser pesquisada: "))

if code >= 1 and code <= len(claims):
    claimResearched = claims[code - 1]
    print("\nA manifestação registrada é:", claimResearched)
else:
    print("O código informado da manifestação não existe!")