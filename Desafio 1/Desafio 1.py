import math
import os
import random
import re
import sys


def quartiles(arr):
    # Ordena o array de entrada
    arr = sorted(arr)
    # Obtém o tamanho do array
    n = len(arr)
    
    # Verifica se o tamanho do array é par ou ímpar e divide o array em duas partes
    if n % 2 == 0:
        arr_inferior = arr[:n//2]
        arr_superior = arr[n//2:]
    else:
        arr_inferior = arr[:n//2]
        arr_superior = arr[n//2+1:]
    
    #Calcula as medianas das partes do array
    q1 = mediana(arr_inferior)
    q2 = mediana(arr)
    q3 = mediana(arr_superior)
    
    #Retorna um array com os três quartis
    return [q1, q2, q3]
    
def mediana(arr):
    # Obtém o tamanho do array
    n = len(arr)
    # Verifica se o tamanho do array é par ou ímpar e calcula a mediana
    if n % 2 == 0:
        return (arr[n//2-1] + arr[n//2]) // 2
    else:
        return arr[n//2]

if __name__ == '__main__':
    
    # Abre um arquivo de saída
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Lê o número de elementos do array
    n = int(input().strip())

    # Lê os elementos do array e armazena em uma lista
    data = list(map(int, input().rstrip().split()))

    # Calcula os quartis do array
    res = quartiles(data)

    # Escreve os resultados no arquivo de saída
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    # Fecha o arquivo de saída
    fptr.close()
