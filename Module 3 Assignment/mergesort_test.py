import random
import timeit
class MergeStringList():
    def __init__(self):
        self.pylist = []
    #adds item to internal list
    def add(self, str):
        self.pylist.append(str)

    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
    # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)
    # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
        # Merge the temp arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    # l is for left index and r is right index of the
    # sub-array of arr to be sorted

    def mergeSort(self, arr):
        if len(arr) > 1:
            #creates second 
            mid = len(arr)//2
            sub_array1 = arr[:mid]
            sub_array2 = arr[mid:]

            #sort both halves
            self.mergeSort(sub_array1)
            self.mergeSort(sub_array2)

            i=j=k=0

            #sorts arrays
            while i < len(sub_array1) and j < len(sub_array2):
                if sub_array1[i] < sub_array2[j]:
                    self.pylist[k] = sub_array1[i]
                    i += 1
                else:
                    self.pylist[k] = sub_array2[j]
                    j += 1
                k += 1

            #places remaining elements back in
            while i < len(sub_array1):
                self.pylist[k] = sub_array1[i]
                i += 1
                k += 1

            while j < len(sub_array2):
                self.pylist[k] = sub_array2[j]
                j += 1
                k += 1


# Test for MergeSort, adds 20 random numbers between 1 and 100
merge_list = MergeStringList()
for i in range(20):
    merge_list.add(random.randint(0,100))

def test_mergeSort():
    merge_list.mergeSort(merge_list.pylist)
    
print("MergeSort Test\nTime:", timeit.timeit(test_mergeSort, number=10000))