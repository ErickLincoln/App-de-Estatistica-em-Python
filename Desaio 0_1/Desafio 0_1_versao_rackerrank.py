#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    weighted_sum = 0
    weight_sum = sum(W)

    for i in range(len(X)):
        weighted_sum += X[i] * W[i]

    weighted_mean = weighted_sum / weight_sum

    print("{:.1f}".format(weighted_mean))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
