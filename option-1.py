claims = []

if len(claims) == 0:
    print("\nNão existem manifestações a serem exibidas\n")
else:
    print("Lista de manifestações: ")
    for item in claims:
        print("-", item)
