import timeit
class BinaryStringList:
    def __init__(self):
        self.pylist = []

    #add item to end of internal list
    def add(self, string):
        self.pylist.append(string)

    #find method uses binary search
    def find(self, string):
        low = 0
        high = len(self.pylist) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.pylist[mid] < string:
                low = mid + 1
            elif self.pylist[mid] > string:
                high = mid - 1
            else:
                return self.pylist[mid]
        return None
    
# binarystringlist tests arrays of size 200
test_list = BinaryStringList()
for i in range(200):
    test_list.add(f"String{i}")

def test_binary():
    return test_list.find("String17")

def test_binary_nf():
    return test_list.find("nothere")

print("BinaryTest\nTime When Found:\n", timeit.timeit(test_binary, number=100000))
print("\nTime When Not Found:\n", timeit.timeit(test_binary_nf, number=100000))