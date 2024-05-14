def mutate_string(string, position, character):
    # return string[:position] + character + string[position+1:]
    x = list(string)
    x[position] = character
    string ="".join(x)
    return string

if __name__ == '__main__':
    s = input("dame: ")
    i, c = input("num:").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)