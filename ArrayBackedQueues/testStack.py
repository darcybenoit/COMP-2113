# This is an example of being able to use multiple stacks in the same program.
# We test the push/pop for each Stack, making sure to interleave them so that we can see that they are independent.
import Stack

stackA = Stack.Stack()
stackB = Stack.Stack()

print("StackA.push()")
stackA.push(25)
print("StackA.push()")
stackA.push(442)
print("StackA.push()")
stackA.push(20)
print("StackB.push()")
stackB.push(100)

print("stackA.pop() ", stackA.pop())
print("stackA.pop() ", stackA.pop())
print("stackB.pop() ", stackB.pop())
print("stackA.pop() ", stackA.pop())
