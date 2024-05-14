def run():
    x = int(input("dame x: "))
    y = int(input("dame y: "))
    z = int(input("dame z: "))
    n = int(input("dame n: "))

    lista = [[i,j,k] for i in range(x+1) for j in range(y+1)for k in range(z+1)if (i+j+k)!=n]


    print(lista)
   
if __name__ == '__main__':
    run()

