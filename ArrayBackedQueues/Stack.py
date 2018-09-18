# This is an exmaple of an array-backed stack as done in class. 

a = [0]
n = 0

class Stack:
    def __init__(self):
        self.a = [0]
        self.n = 0

    # Here we push the item onto the end of the stack. If there is no space in the list, we append to the end.
    def push(self,x):
        if (self.n + 1 > len(self.a)):
            self.a.append(x)
        else:
            self.a[n] = x
        self.n += 1

    # Here we pop the end item off of the stack. We modify the value of n, and will overwrite this data later.
    def pop(self):
        x = self.a[self.n-1]
        self.n -= 1
        return x
