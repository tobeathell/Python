# -*- coding: UTF-8 -*-

# Filename : 3-sqrt.py
# author by : www.w3cschool.cn

# computing sqrt of int and float
# import cmath modle

import cmath

num = int(raw_input("please input a number: "))
num_sqrt = cmath.sqrt(num)
print('{0} sqrt is {1:03f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
