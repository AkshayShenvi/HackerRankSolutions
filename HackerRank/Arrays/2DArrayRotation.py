#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    i=0
    temp=0
    while i<d:
        temp= a[0]
        a.pop(0)
        a.append(temp)
        i+=1
    return a

if __name__ == '__main__':




    a=[1,2,3,4,5,6]
    d=2

    result = rotLeft(a, d)

