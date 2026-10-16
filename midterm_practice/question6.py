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

# Q6) 
def deduplicate(s):
    '''
    Assume that s is a string.
    Return a new string that is the same as s, but with consecutive 
    duplicate characters removed. For example, 'feeder' returns 'feder' 
    since it changes the 'ee' to 'e'.
    'boomboomeeraaang' returns 'bombomerang' .
    '''
    res = ''
    prev = ''
    for char in s:
        if char != prev:
            res += char
            prev = char
    return res


# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test_q6_01(self):
        self.assertEqual(deduplicate('abcdef'), 'abcdef')
    def test_q6_02(self):
        self.assertEqual(deduplicate('feeder'), 'feder')
    def test_q6_03(self):
        self.assertEqual(deduplicate('boomboomeeraaang'), 'bombomerang')
    def test_q6_04(self):
        self.assertEqual(deduplicate('aabbccdd'), 'abcd')
    def test_q6_05(self):
        self.assertEqual(deduplicate('aaaaaabbbcccccddeeeeeeeee'), 'abcde')
    def test_q6_06(self):
        self.assertEqual(deduplicate(''), '')
    def test_q6_07(self):
        self.assertEqual(deduplicate('a'), 'a')
    def test_q6_08(self):
        self.assertEqual(deduplicate('#$#@!#$@!'), '#$#@!#$@!')
    def test_q6_09(self):
        self.assertEqual(deduplicate('a  b  c'), 'a b c')
    def test_q6_10(self):
        self.assertEqual(deduplicate('11223344'), '1234')

if __name__ == '__main__':
    unittest.main(exit=True)

