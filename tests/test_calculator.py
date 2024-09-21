import unittest

from src.calculator import add, subtract, divide 

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertIsNone(add("Arshad", 11))
    
    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertIsNone(subtract("Basha", 22))
    
    def test_divide(self):
        self.assertEqual(divide(3, 3), 1)
        self.assertEqual(divide(0, 1), 0)
        self.assertIsNone(divide(1, 0))
        self.assertEqual(divide(1, 1), 1)
        
if __name__ == '__main__':
    unittest.main()
