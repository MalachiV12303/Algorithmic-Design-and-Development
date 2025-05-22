import random
import timeit
class BubbleStringList():
    def __init__(self):
        self.pylist = []
    #adds item to internal list
    def add(self, str):
        self.pylist.append(str)
    #bubblesorting method
    def sort(self):
        n = len(self.pylist)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.pylist[j] > self.pylist[j+1] :
                    self.pylist[j], self.pylist[j+1] = self.pylist[j+1], self.pylist[j]

bubble_list = BubbleStringList()
for i in range(20):
    bubble_list.add(random.randint(0,100))

def test_bubbleSort():
    bubble_list.sort()
    
print("BubbleSort Test\nTime:", timeit.timeit(test_bubbleSort, number=10000))