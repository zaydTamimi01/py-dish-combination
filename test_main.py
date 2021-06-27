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
        self.assertDictEqual(data, {"Target price": 15.05,
	                "mixed fruit": 2.15,
	                "french fries": 2.75,
	                "side salad": 3.35,
	                "hot wings": 3.55,
	                "mozzarella sticks": 4.20,
	                "sampler plate": 5.80})
# converting the dict values into list and assigning it to list variable prices 
    def test_dicttoListPrices(self):
        self.assertListEqual(Main.dicttoListPrices(1,{"Target price": 15.05,
	                "mixed fruit": 2.15,
	                "french fries": 2.75,
	                "side salad": 3.35,
	                "hot wings": 3.55,
	                "mozzarella sticks": 4.20,
	                "sampler plate": 5.80}), [15.05, 2.15, 2.75, 3.35, 3.55, 4.2, 5.8])

    def test_getTargetPrice(self):
        self.assertEqual(Main.getTargetPrice(1,[15.05, 2.15, 2.75, 3.35, 3.55, 4.2, 5.8]), 15.05)

    
    def test_find_combination(self):
        self.assertListEqual(Main.find_combination(1,[2.15, 2.75, 3.35, 3.55, 4.2, 5.8], 15.05), [])
if __name__ == "__main__":
        unittest.main(argv=['ignore-first-argument'], exit=False)