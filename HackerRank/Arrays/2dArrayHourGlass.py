


import math
import os
import random
import re
import sys


def whiteMagic(arr, column, row, iterator):
    summation = 0
    for k in range(iterator):
        summation += arr[column][row + k]
    return summation


# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum1 = []
    for column in range(4):
        for row in range(4):
            sum1.append(
                whiteMagic(arr, column, row, 3) + whiteMagic(arr, column + 1, row + 1, 1) + whiteMagic(arr, column + 2,
                                                                                                       row, 3))

    return max(sum1)


if __name__ == '__main__':


    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)
