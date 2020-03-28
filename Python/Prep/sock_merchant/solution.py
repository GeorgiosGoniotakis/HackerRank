#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    complete_pairs = 0
    colors = dict()

    for sock in ar:
        if str(sock) not in colors:
            colors[str(sock)] = 1
        else:
            complete_pairs += 1
            del colors[str(sock)]
    return complete_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

