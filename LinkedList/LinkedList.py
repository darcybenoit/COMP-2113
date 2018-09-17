#Linked List Module
import Node

tail = 0
head = 0
value = 0
num = 0

class LinkedList:
    def __init__(self, value):
        newNode = Node.Node(value)
        self.head = newNode 
        self.tail = newNode
        newNode.next = None
        self.num = 0

    # Traverses (walks) the LinkedList and prints out the values of each node.
    def traverse(self):
        node = self.head
        while node != None:
           print ("Node value = ", node.value)
           node = node.next
        return node

    # Finds a node based on position and returns that node
    def findNodeNum(self, position):
        node = self.head
        for x in range(0, position):
           node = node.next
        return node

    # Adds a node to the end of the LinkedList
    def addNode(self,value):
        newNode = Node.Node(value)
        self.tail.next = newNode
        self.tail = newNode
        newNode.next = None 
        self.num += 1


    # finds the position of a node in the LinkedList (position number) based on the value.
    # Returns a -1 if no node with that value is found. 
    def findNodeValue(self,value):
        i = 0 
        node = self.head
        while True:
           if (node.value == value):
              return i
           elif (node.next == None):
              return -1
           else: 
              node = node.next
              i += 1

    # Deletes a node based on the value of the node. 
    # This will delete the first node it finds with this value.
    def deleteNodeByValue(self,value):
        node = self.head
        if (node.value == value):           # node is the head
            self.head = node.next
        elif (self.tail.value == value):    # node is the tail
            for x in range(0,self.num-1):
                oldNode = node
                node = node.next
            node.next = node.next.next 
            self.tail = node
        else:                               # node is in the middle
            for x in range(0,self.num-1):
                oldNode = node
                node = node.next
                if (node.value == value):
                    oldNode.next = node.next
        self.num -= 1


    # deletes a node based on position in the LinkedList
    def deleteNodeByPosition(self,position):
        node = self.head
        if (position == 0):		# node is the head
           self.head = node.next
        for x in range(0, position-1):	# node is in the middle/end
           node = node.next
        node.next = node.next.next 
        while (node.next != None):	# go to end, fix pointer to tail 
           node = node.next
        self.tail = node
        self.num -= 1
