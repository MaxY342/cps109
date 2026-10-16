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

# Q2)
def sum_even(n):
    '''
    Assume n is an integer >= 1.
    Return the sum of the integers, between 1-n inclusive, 
    that are even
    '''
    res = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            res += i
    return res

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test_q2_01(self):
        self.assertEqual(sum_even(1), 0)
    def test_q2_02(self):
        self.assertEqual(sum_even(2), 2)
    def test_q2_03(self):
        self.assertEqual(sum_even(3), 2)
    def test_q2_04(self):
        self.assertEqual(sum_even(4), 6)
    def test_q2_05(self):
        self.assertEqual(sum_even(5), 6)
    def test_q2_06(self):
        self.assertEqual(sum_even(6), 12)
    def test_q2_07(self):
        self.assertEqual(sum_even(7), 12)
    def test_q2_08(self):
        self.assertEqual(sum_even(8), 20)
    def test_q2_09(self):
        self.assertEqual(sum_even(9), 20)
    def test_q2_10(self):
        self.assertEqual(sum_even(10), 30)

if __name__ == '__main__':
    unittest.main(exit=True)

