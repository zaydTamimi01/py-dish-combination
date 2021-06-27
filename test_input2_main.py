import unittest
import json
import sys
from itertools import combinations
from main import Main
inFile = sys.argv[1]
class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Main.add(1,1,2), 3)
    
    # Reading file with exception handling
    def test_openFile(self):
        data = Main.openFile(1,inFile)
        self.assertDictEqual(data, {
	                "Target price": 15,
	                "mixed fruit": 2,
	                "french fries": 13,
	                "side salad": 1,
	                "hot wings": 10,
	                "mozzarella sticks": 5,
	                "sampler plate": 7})
# converting the dict values into list and assigning it to list variable prices 
    def test_dicttoListPrices(self):
        self.assertListEqual(Main.dicttoListPrices(1,{
	                "Target price": 15,
	                "mixed fruit": 2,
	                "french fries": 13,
	                "side salad": 1,
	                "hot wings": 10,
	                "mozzarella sticks": 5,
	                "sampler plate": 7}), [15, 2, 13, 1, 10, 5, 7])

    def test_getTargetPrice(self):
        self.assertEqual(Main.getTargetPrice(1,[15, 2, 13, 1, 10, 5, 7]), 15)

    
    def test_find_combination(self):
        self.assertListEqual(Main.find_combination(1,[2, 13, 1, 10, 5, 7], 15), [(2, 13), (10, 5), (2, 1, 5, 7)])
if __name__ == "__main__":
        unittest.main(argv=['ignore-first-argument'], exit=False)