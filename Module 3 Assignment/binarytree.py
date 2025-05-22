"""Sample Node defined """
import random
import timeit


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def getChildren(self):
        children = []
        if(self.leftChild != None):
            children.append(self.leftChild)
        if(self.rightChild != None):
            children.append(self.rightChild)
        return children
        """ Binary Tree operation performed in this class """

class BinaryTreeStringList:
    def __init__(self):
        self.root = None
    def setRoot(self, val):
        self.root = BinaryTree(val)
    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)
    def insertNode(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            elif val > currentNode.val:
                if(currentNode.rightChild):
                    self.insertNode(currentNode.rightChild, val)
                else:
                    currentNode.rightChild = BinaryTree(val)
            else:
                currentNode.leftChild = BinaryTree(val) 
    def find(self, val):
        return self.findNode(self.root, val)
    
    def findNode(self, currentNode, val):
        if(currentNode is None):
            return False
        elif(val == currentNode.val):
            return True
        elif(val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)
    """ Test the functionality using below driver class"""
bst = BinaryTreeStringList()
root = bst.setRoot(12)


tree_list = BinaryTreeStringList()
for i in range(20):
    tree_list.insert(random.randint(0,100))

def test_binaryTree():
    tree_list.find(25)
    
print("BinaryTree Test\nTime:", timeit.timeit(test_binaryTree, number=10000))