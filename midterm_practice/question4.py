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

# Q4)
def pyramid_blocks(n, m):
    '''
    Assume n and m are integers >= 1.
    Consider a solid rectangular pyramid, whose base is n-by-m 
    blocks. The layer above is (n-1)-by-(m-1), and so on. The top 
    layer will be n-by-1, or 1-by-m, depending on which dimension 
    reaches 1 first. Assume n and m are integers. Return the number 
    of blocks in the pyramid.
    '''
    pass # replace 'pass' with a return statement.

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test_q4_01(self):
        self.assertEqual(pyramid_blocks(1, 1), 1)
    def test_q4_02(self):
        self.assertEqual(pyramid_blocks(2, 2), 5)
    def test_q4_03(self):
        self.assertEqual(pyramid_blocks(3, 2), 8)
    def test_q4_04(self):
        self.assertEqual(pyramid_blocks(2, 3), 8)
    def test_q4_05(self):
        self.assertEqual(pyramid_blocks(4, 4), 30)
    def test_q4_06(self):
        self.assertEqual(pyramid_blocks(5, 3), 26)
    def test_q4_07(self):
        self.assertEqual(pyramid_blocks(3, 5), 26)
    def test_q4_08(self):
        self.assertEqual(pyramid_blocks(6, 6), 91)
    def test_q4_09(self):
        self.assertEqual(pyramid_blocks(7, 7), 140)
    def test_q4_10(self):
        self.assertEqual(pyramid_blocks(10, 12), 495)

if __name__ == '__main__':
    unittest.main(exit=True)

