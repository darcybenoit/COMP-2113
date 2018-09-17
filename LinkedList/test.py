import Node

head = Node.Node(11)
node2 = Node.Node(12)
node3 = Node.Node(13)
node4 = Node.Node(14)
node5 = Node.Node(15)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head.traverse()
