#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author : frontier8186 time: 2019/11/5 16:01

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.


def countingValleys(n, s):
    s_num = []
    for i in range(n):
        if s[i:i + 1] == 'U':
            if i == 0:
                s_num.append(1)
            else:
                s_num.append(s_num[i - 1] + 1)
        else:
            # 'D'
            if i == 0:
                s_num.append(-1)
            else:
                s_num.append(s_num[i - 1] - 1)
    count = 0
    for i in range(len(s_num)):
        if i > 0:
            if s_num[i] == 0 and s_num[i - 1] == -1:
                count = count + 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()