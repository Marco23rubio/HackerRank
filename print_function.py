
def run():
    n= int(input("dame n: ")) 
    for x in range(1,n+1):
        if x <n:
            print(x,end="")
        else:
            print(x)


if __name__ == "__main__":
    run()
