import random
import time
import timeit
##class for regular python lists tests
class List(object):
    def __init__(var, data):
        var.data = data
        var.next = None
    def getdata(var):
        return var.data
    def getnext(var):
        return var.next
    def setdata(var, new_data):
        var.data = new_data
    def setnext(var, new_next):
        var.next = new_next
##class for unordered lists tests
class UnorderedList(object):
    def __init__(var):
        var.N = 0
        var.head = None
    def size(var):
        return var.N
    def isempty(var):
        return var.N == 0
    def add(var, data):
        var.N += 1
        temp = List(data)
        temp.setnext(var.head)
        var.head = temp
    def search(var, data):
        curr = var.head
        found = False
        while curr and not found:
            if curr.getdata() == data:
                found = True
                curr = curr.getnext()
            return found
    def remove(var, item):
        curr = var.head
        prev = None
        while curr.getdata() != item:
            prev = curr
            curr = curr.getnext()
        if not prev:
            var.head = curr.getnext()
        else:
            prev.setnext(curr.getnext())
            var.N -= 1

## code for outputting the program run time
def myProgram():
    y = 3.1415
    for x in range(100):
        y = y ** 0.7
    return y
print('Run Time: ')
print(timeit.timeit(myProgram, number=100000))

## this outputs the python list and linked list run times
for i in range(10, 10001, 1000):
    list1 = list(range(i))
    list2 = UnorderedList()
    for j in range(i):
        list2.add(j)
    j = random.randrange(0, i)
    start_time1 = time.time()
    list1.remove(j)
    end_time1 = time.time()
    start_time2 = time.time()
    list2.remove(j)
    end_time2 = time.time()
    print("List time: {0}. Linked List time: {1}".format(end_time1-start_time1, end_time2-start_time2))
