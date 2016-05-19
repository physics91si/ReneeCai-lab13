#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import sys
import re

def main():
    """Join command-line arguments and pass them to unitcalc(), then print."""
    calculation = ''.join(sys.argv[1:])
    print (calculation)

def calc(s):
    """Parse a string describing an operation on quantities with units."""

    # TODO make this robust for differently formatted inputs
    
    nums = re.sub('\s+', '', s)
    re.split('(-|\+)', nums) #tokenize


 
    if operation=='+':
        return float(num1)+float(num2)
    elif operation=='-':
        return float(num1)-float(num2)
    elif operation=='*':
        return float(num1)*float(num2)
    elif operation=='/':
        return float(num1)//float(num2)


if __name__ == "__main__": main()
