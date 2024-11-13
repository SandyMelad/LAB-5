# test_calculator.py

import unittest
from Square import Square  

class TestSquare(unittest.TestCase):

    def setUp(self):
        # This method is run before each test
        self.square = Square()

    def test_area_of_square(self):
        # Test area calculation functionality
        result = self.square.Area_of_square(4, 4)
        self.assertEqual(result, 16)
        
        result = self.square.Area_of_square(5, 5)
        self.assertEqual(result, 25)
        
        result = self.square.Area_of_square(0, 0)
        self.assertEqual(result, 0)
        
        # Test with non-square inputs
        result = self.square.Area_of_square(3, 4)
        self.assertEqual(result, 12)
        
        # Test with negative values (depending on expected behavior)
        result = self.square.Area_of_square(-3, 3)
        self.assertEqual(result, -9)

if __name__ == '__main__':
    unittest.main()