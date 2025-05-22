import random
import timeit
class QuickStringList():
    def __init__(self):
        self.pylist = []
    #adds item to internal list
    def add(self, str):
        self.pylist.append(str)
    #quicksorting method
    def quickSort(self, list, low, high):
        if low < high:
            pi = QuickStringList.partition(list,low,high)
            self.quickSort(list, low, pi-1)
            self.quickSort(list, pi+1, high)
    def partition(list,low,high):
        i = ( low-1 )
        pivot = list[high]
        for j in range(low , high):
            if list[j] <= pivot:
                i = i+1
                list[i],list[j] = list[j],list[i]
                list[i+1],list[high] = list[high],list[i+1]
        return ( i+1 )

# Test for MergeSort, adds 20 random numbers between 1 and 100
quick_list = QuickStringList()
for i in range(20):
    quick_list.add(random.randint(0,100))

def test_quickSort():
    n=len(quick_list.pylist)
    quick_list.quickSort(quick_list.pylist, 0, n-1)
  
print("QuickSort Test\nTime:", timeit.timeit(test_quickSort, number=10000))
