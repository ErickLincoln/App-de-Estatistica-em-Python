import math
import os
import random
import re
import sys

#
# Completa a função 'media_ponderada' abaixo.
#
# A função aceita os seguintes parâmetros:
#  1. ARRAY_INTEIRO X
#  2. ARRAY_INTEIRO W
#

def media_ponderada(X, W):
    soma_ponderada = 0
    soma_peso = sum(W)

    for i in range(len(X)):
        soma_ponderada += X[i] * W[i]

    media_ponderada = soma_ponderada / soma_peso

    print("{:.1f}".format(media_ponderada))

if __name__ == '__main__':
    n = int(input().strip())

    valores = list(map(int, input().rstrip().split()))

    pesos = list(map(int, input().rstrip().split()))

    media_ponderada(valores, pesos)
