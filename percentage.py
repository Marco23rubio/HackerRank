
def run():
    dictionario = {}
    cantidad = int(input("Cuantos alumnos ingresará? "))
    promedios = 3
    lista = []

    while cantidad > 0:
        lista.clear()
        promedios = 3
        nombre = input("Dame el nombre: ")
        cantidad -= 1
        while promedios > 0:
            califa = int(input("Dame la calificación: "))
            lista.append(califa)
            promedios -= 1
        dictionario[nombre] = lista
    
    estudiante = input("Que estudiante quieres?")
    suma_total = sum(dictionario[estudiante])
    n= len(dictionario[estudiante])
    print(round(suma_total/n,2))

if __name__ == '__main__':
    run()

