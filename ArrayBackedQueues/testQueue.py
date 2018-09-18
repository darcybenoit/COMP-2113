# Here are some calls to test the Queue implementation. We should test all aspects of the Queue - adding to the beginning,
# adding to the middle, adding to the end, and deleting from all three locations.
import Queue

stackA = Queue.Queue()
stackB = Queue.Queue()

stackA.insert(0,25)
stackA.insert(1,442)
stackA.insert(0,20)
stackB.insert(0,100)

print("stackA.pop() ", stackA.remove(1))
print("stackA.pop() ", stackA.remove(0))
print("stackB.pop() ", stackB.remove(0))
print("stackA.pop() ", stackA.remove(0))
