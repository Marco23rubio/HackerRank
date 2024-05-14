def segundo_menor(numeros):
    
    if len(numeros) < 2:
        return None

    if len(numeros) == 2 and numeros[0] == numeros[1]:
        return None

    duplicados = set()
    unicos = []

    for n in numeros:
        if n not in duplicados:
            duplicados.add(n)
            unicos.append(n)
        
    unicos.sort()
        
    return unicos[-2]

    

a = input("Dame: ")
numeros = list(map(int,a.split()))

print(segundo_menor(numeros))

