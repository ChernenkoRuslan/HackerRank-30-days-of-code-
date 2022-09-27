#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    validNamesList = [] #обязательно создаем, а то не поедет
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        if emailID.find("@gmail.com") != -1: #gmail email found
            validNamesList.append(firstName)
    for i in sorted(validNamesList):
        print(i)