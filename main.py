# importing the required libraries
import json
import sys
from itertools import combinations

inFile = sys.argv[1]
class Main():
    
    prices = []
    def add(self,x,y):
        return x + y

    # Reading file with exception handling
    def openFile(self, fileName):
        try:
            with open(fileName,'r') as i:
                data = json.load(i)

            return data
        except IOError as e:
           print("I/O error({0}): {1}").format(e.errno, e.strerror)
        except: #handle other exceptions such as attribute errors
           print("Unexpected error:", sys.exc_info()[0])

    # converting the dict values into list and assigning it to list variable prices 
    def dicttoListPrices(self, dictPrices):
        prices = list(dictPrices.values())
        return prices

    def getTargetPrice(self, priceList):
        return priceList[0]


    # Remove the target price from list to make it a list of prices of dishes
    def popTargetPrice(self, priceListt):
        priceListt.pop(0)

    # function to find the combination of the dishes
    def find_combination(self, thelist, target):
        arr = []
        p = []    
        if len(thelist) > 0:
            for r in range(0,len(thelist)+1):        
                arr += list(combinations(thelist, r))

            for item in arr:        
                if sum(item) == target:
                    p.append(item)
        else:
            print("There are no dishes")
        return p

    if __name__ == "__main__":
        pass
        
obj = Main()
dataFromFile = obj.openFile(inFile)
prices = obj.dicttoListPrices(dataFromFile)
target_price = obj.getTargetPrice(prices)
obj.popTargetPrice(prices)
result = obj.find_combination(prices, target_price)
if not result:
    print("No combination of the dishes that is equal to the target price.")
else:
    print(result)
