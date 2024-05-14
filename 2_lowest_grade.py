from operator import itemgetter

def encontrar_2_menor():
    alumnos = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        alumnos.append([name, score])

    min_score = min(alumnos, key=itemgetter(1))
    min_score_filt = [cal for cal in alumnos if cal[1] != min_score[1]]
    seg_min_score = min(min_score_filt, key=itemgetter(1))
    alumnos = [cal for cal in alumnos if cal[1] == seg_min_score[1]]
    alumnos = sorted(alumnos, key=itemgetter(0))
    
    for chango in alumnos:
        print(chango[0])

if __name__ == '__main__':
    encontrar_2_menor()
