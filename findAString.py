import re

def count_substring(string,substring):
    conteo = len(re.findall(f'(?={substring})',string))
    print(conteo)

count_substring('ABCDCDC','CDC')

