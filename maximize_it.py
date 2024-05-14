def main():
    lineas, division = input().split()
    lineas = int(lineas) 
    division = int(division) 
    lista = []
    for x in range(0, lineas):
        numeros = input()
        lista.append([int(num) for num in numeros.split()])
    max_values = [max(sublista) for sublista in lista]
    print(max_values)
    print(division)

if __name__ == "__main__":
    main()