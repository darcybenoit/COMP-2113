import LinkedList

newList = LinkedList.LinkedList(100)
newList.addNode(200)
newList.addNode(300)
newList.addNode(400)
newList.traverse()


newList.addNodeByPosition(4, 9999)

#n = newList.findNodeByValue(500)
#if (n):
   #print ("found node value = ", n.value)
#else:
   #print ("Nothing found")
#newList.deleteNodeByPosition(3)
print ("---")
newList.traverse()
newList.addNode(500)

print ("---")
newList.traverse()
print ("---")
head = newList.findNodeNum(0)
head.traverse()
