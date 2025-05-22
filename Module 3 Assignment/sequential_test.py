import timeit
class SequentialStringList:
    def __init__(self):
        self.pylist = []

    #add item to end of internal list
    def add(self, string):
        self.pylist.append(string)

    #find method uses sequential search
    def find(self, str):
        for i in self.pylist:
            if i == str:
                return i
        return None
        
# Test for SequentialStringList
sequential_list = SequentialStringList()
for i in range(20):
    sequential_list.add(f"String{i}")

def test_sequential():
    return sequential_list.find("String17")

def test_sequential_nf():
    return sequential_list.find("notfound")


print("SequentialTest\nTime When Found:", timeit.timeit(test_sequential, number=100000))
print("\nTime When Not Found:", timeit.timeit(test_sequential_nf, number=100000))

