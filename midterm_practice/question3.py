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

# Q3)
def integers_exceed(n):
    '''
    How many consecutive integers, starting at 1, must be
    added before the sum exceeds n?
    For example, if n is 11, we must add 1+2+3+4+5 = 15,
    and therefore the answer is 5.
    '''

    pass

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test_q3_01(self):
        self.assertEqual(integers_exceed(0), 1)
    def test_q3_02(self):
        self.assertEqual(integers_exceed(1), 2)
    def test_q3_03(self):
        self.assertEqual(integers_exceed(2), 2)
    def test_q3_04(self):
        self.assertEqual(integers_exceed(3), 3)
    def test_q3_05(self):
        self.assertEqual(integers_exceed(4), 3)
    def test_q3_06(self):
        self.assertEqual(integers_exceed(5), 3)
    def test_q3_07(self):
        self.assertEqual(integers_exceed(6), 4)
    def test_q3_08(self):
        self.assertEqual(integers_exceed(7), 4)
    def test_q3_09(self):
        self.assertEqual(integers_exceed(8), 4)
    def test_q3_10(self):
        self.assertEqual(integers_exceed(11), 5)

if __name__ == '__main__':
    unittest.main(exit=True)

