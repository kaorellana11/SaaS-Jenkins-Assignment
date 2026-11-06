#cmd to run this: python -m unittest discover -s C:\coding-stuff\SaaS\jenkins
#test
import unittest
import simple

class testOddOrEven(unittest.TestCase):
    def test_odd_or_even(self):
        self.assertEqual(simple.odd_or_even(6), "even")

if __name__ == "__main__":
    unittest.main()
