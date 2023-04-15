#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    arr = sorted(arr)
    n = len(arr)
    
    if n % 2 == 0:
        arr_inferior = arr[:n//2]
        arr_superior = arr[n//2:]
    else:
        arr_inferior = arr[:n//2]
        arr_superior = arr[n//2+1:]
    
    q1 = mediana(arr_inferior)
    q2 = mediana(arr)
    q3 = mediana(arr_superior)
    
    return [q1, q2, q3]
    
def mediana(arr):
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2-1] + arr[n//2]) // 2
    else:
        return arr[n//2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
