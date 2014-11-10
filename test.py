import myyacc
import unittest

class TestCalcPolonesa(unittest.TestCase):

    def test_yacc(self):
        result = myyacc.input_expr("3 4 *")
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()
