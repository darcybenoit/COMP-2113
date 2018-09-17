# Node Module
# Node is used for the LinkedList Module

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    #note: This traverses the LinkedList based on a node
    def traverse(self):
        node = self
        while node != None:
           print (node.value)
           node = node.next
        return node

