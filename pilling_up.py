

def armando_cubos():
    numero_cubos = int(input())
    for cubo in range(numero_cubos):
        tamano_array=int(input())
        entrada=input()
        numeros = entrada.split()
        array_input=[int(x) for x in numeros]
        array_apilar=[]
        texto="Yes"

        while array_input !=[]:
            primer_valor_input = array_input[0]
            ultimo_valor_input = array_input[-1]
            valor_mayor=max(primer_valor_input,ultimo_valor_input)
            if(array_apilar==[]):
                array_apilar.append(valor_mayor)
                if(primer_valor_input>ultimo_valor_input):
                    array_input.pop(0)
                else:
                    array_input.pop(-1)
            else:
                ultimo_valor_apilar = array_apilar[-1]
                if(valor_mayor<=ultimo_valor_apilar):
                    array_apilar.append(valor_mayor)
                    if(primer_valor_input>=ultimo_valor_input):
                        array_input.pop(0)
                    else:
                        array_input.pop(-1)
                else:
                    texto="No"
                    break
        print(texto)

            
armando_cubos()
    