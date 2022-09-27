#!/bin/python3

import math
import os
import random
import re
import sys



#if __name__ == '__main__': - нужно снести строку. Вообще не понятно зачем она. и потом вот так.
S = input()
try:
    print(int(S))
except ValueError:
    print("Bad String")
