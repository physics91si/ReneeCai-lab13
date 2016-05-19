#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import unittest
import calc

class CalcTest(unittest.TestCase):
    # TODO implement tests here to verify that your functions work!
    def testAddition(self):
        self.assertEqual(calc.calc('1+1'), 2)
    def testNumbers(self):
        self.assertRaises(ValueError, calc.calc, 'three')
    def testSubtraction(self):
        self.assertEqual(calc.calc('3-2'),1)

    def testMultiplication(self):
        self.assertEqual(calc.calc('5*5'),25)
 
    def testDivision(self):
        self.assertEqual(calc.calc('5/5'),1)
        
    def testType(self, a, b):
        typeofnumber = (int, long, float)
 
        if isinstance(a, typeofnumber) and isinstance(b, typeofnumber):
           pass
        else:
            raise ValueError
   

if __name__ == '__main__':
    unittest.main()

