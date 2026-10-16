import unittest

'''

Fill in the functions below according to their descriptions. 

You don't need to submit on D2L. Just save your code locally. Be
sure to fill in your full name and email below:

FULL NAME: <your name here>
TMU EMAIL: <your email here>

VERY important:

1. Do not modify the filename. Changing the filename will result 
in a score of 0 for this question.

2. Do not modify the function name. Changing the function name 
will result in a score of 0 for this question.

3. Make sure your code compiles before you finish the test, do NOT 
leave syntax errors in your code! 

'''

# Q1) 
def roman_to_arabic(rn):
    '''
    rn is a string representing a roman numeral. Your program should convert
    this number to an arabic base-10 integer, and return it. Your function
    only has to work for first 10 roman numerals. If rn is not one of the first
    10 numerals, return None. The first 10 roman numerals are given below:

    I    = 1
    II   = 2
    III  = 3
    IV   = 4
    V    = 5
    VI   = 6
    VII  = 7
    VIII = 8
    IX   = 9
    X    = 10
    '''
    numeralToNumber = {
        'I': 1,
        'II': 2,
        'III': 3,
        'IV': 4,
        'V': 5,
        'VI': 6,
        'VII': 7,
        'VIII': 8,
        'IX': 9,
        'X': 10
    }
    if rn in numeralToNumber:
        return numeralToNumber[rn]
    return None
    

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test_q1_01(self):
        self.assertEqual(roman_to_arabic('I'), 1)
    def test_q1_02(self):
        self.assertEqual(roman_to_arabic('II'), 2)
    def test_q1_03(self):
        self.assertEqual(roman_to_arabic('III'), 3)
    def test_q1_04(self):
        self.assertEqual(roman_to_arabic('IV'), 4)
    def test_q1_05(self):
        self.assertEqual(roman_to_arabic('V'), 5)
    def test_q1_06(self):
        self.assertEqual(roman_to_arabic('VI'), 6)
    def test_q1_07(self):
        self.assertEqual(roman_to_arabic('VII'), 7)
    def test_q1_08(self):
        self.assertEqual(roman_to_arabic('VIII'), 8)
    def test_q1_09(self):
        self.assertEqual(roman_to_arabic('IX'), 9)
    def test_q1_10(self):
        self.assertEqual(roman_to_arabic('X'), 10)

if __name__ == '__main__':
    unittest.main(exit=True)
