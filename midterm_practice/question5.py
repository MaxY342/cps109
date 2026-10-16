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

# Q5)
def first_letter(digits):
    '''
    Assume that digits is a string containing numeric digits.
    Returns a string whose corresponding characters are the first 
    letter of each digit.
    For example: '5113' returns 'foot',  since the first letters 
    of five, one, one, three are f, o, o, t.  
    Similarly, '0123456789613' returns 'zottffssensot'.
    '''

    pass

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test_q5_01(self):
        self.assertEqual(first_letter(''), '')
    def test_q5_02(self):
        self.assertEqual(first_letter('5'), 'f')
    def test_q5_03(self):
        self.assertEqual(first_letter('5113'), 'foot')
    def test_q5_04(self):
        self.assertEqual(first_letter('0123456789613'), 'zottffssensot')
    def test_q5_05(self):
        self.assertEqual(first_letter('123'), 'ott')
    def test_q5_06(self):
        self.assertEqual(first_letter('567'), 'fss')
    def test_q5_07(self):
        self.assertEqual(first_letter('1234567890'), 'ottffssenz')
    def test_q5_08(self):
        self.assertEqual(first_letter('0123456789'), 'zottffssen')
    def test_q5_09(self):
        self.assertEqual(first_letter('11111'), 'ooooo')
    def test_q5_10(self):
        self.assertEqual(first_letter('13579'), 'otfsn')

if __name__ == '__main__':
    unittest.main(exit=True)

