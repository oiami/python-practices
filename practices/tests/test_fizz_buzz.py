import unittest
from ..fizz_buzz import fizz_buzz

class FizzBuzzTestCase(unittest.TestCase):
    """Test of FizzBuzz"""
    
    def test_fizzbuzz(self):
        self.fizz_buzz = fizz_buzz.fizz_buzz(99)
        self.assertIs(self.fizz_buzz, 'Fizz')

        self.fizz_buzz = fizz_buzz.fizz_buzz(35)
        self.assertIs(self.fizz_buzz, 'Buzz')

        self.fizz_buzz = fizz_buzz.fizz_buzz(90)
        self.assertIs(self.fizz_buzz, 'FizzBuzz')