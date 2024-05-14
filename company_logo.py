from operator import itemgetter

def main():
    palabra = input()
    palabra = palabra.lower()
    letras = list(set(palabra))

    conteos = [(letra, palabra.count(letra)) for letra in letras]
    conteos.sort(key=itemgetter(0))  
    conteos.sort(key=itemgetter(1), reverse=True) 

    for letra, conteo in conteos[:3]:
        print(letra, conteo)

if __name__ == "__main__":
    main()
