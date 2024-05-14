import re


def capitalizar(s):
    palabras = re.findall('\S+|\s+', s) #encuentra patrones en una cadena de texto y luego los convierte en una lista, la S+ encuentra el conjunto de palabras, el s+ el de espacios en blanco,hace una lista de 5 3 palabras y dos espacios en blanco de x longitud
    resultado = ""
    
    for palabra in palabras:
        if palabra.isspace():
            resultado += palabra
        else:
            resultado += palabra.capitalize()
    
    return resultado

if __name__ == '__main__':
    capitalizar('hello   world  3d');