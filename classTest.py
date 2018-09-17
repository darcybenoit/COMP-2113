import Node

head = Node.Node(11)
n2 = Node.Node(12)
n3 = Node.Node(13)
head.next = n2
n2.next = n3

head.traverse()
