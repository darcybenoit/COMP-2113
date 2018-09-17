import LinkedList

newList = LinkedList.LinkedList(100)
newList.addNode(200)
newList.addNode(300)
newList.addNode(400)
newList.traverse()


newList.deleteNodeByValue(100)
print ("---")
newList.traverse()
newList.addNode(500)

print ("---")
newList.traverse()
print ("---")
head = newList.findNodeNum(0)
head.traverse()
