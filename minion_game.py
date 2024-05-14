def minion_game(string):
    
    vocales = ['a', 'e', 'i', 'o', 'u']
    kevin = 0

    for i in range(len(string)):
        if string[i].lower() in vocales:
            kevin += len(string) - i

    stuart = 0

    for i in range(len(string)):
        if string[i].lower() not in vocales:
            stuart += len(string) - i
    
    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == "__main__":
    s = input()
    minion_game(s)