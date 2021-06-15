import numpy as np


# initialize constructor#

class stack:
    def __init__(self, limit=10):
        self.limit = limit
        self.stack = np.array([])



    # add to element in the stack
    def push(self, data):
        if len(self.stack) <= self.limit: # check the stack limit
            self.stack = np.append(self.stack, data) # use append method
            print("PUSH  ELEMENT IS >>", data)


        else:
            print("STACK IS FULL")

    # Remove  the element from the stack
    def pop(self):
        if len(self.stack) == 0:    # check stack length
            print("STACK IS EMPTY")

        else:
            find_Pop=  (self.stack[len(self.stack) - 1])  # find the drop element
            self.stack = np.delete(self.stack,len(self.stack) - 1) # then popped
            print("successfully popped element is >> ",find_Pop)

            print("after removing the element of stack",self.stack ) # after removing the element of stack
            print("\n")

    # the element from the top of the stack
    def top(self):
        if len(self.stack) == 0:
            print("stack is empty")

        else:
            print("top value is ", self.stack[len(self.stack) - 1])

    # if the stack len  is  0 , then the stack is empty, otherwise it is not.
    def isEmpty(self):
        if len(self.stack) == 0:
            print("stack is empty")
        else:
            print("stack not empty")

    # if the stack len  is  equal limit  , then the stack is full, otherwise it is not full.
    def isFull(self):
        if len(self.stack) == self.limit:
            print("stack full")
        else:
            print("stack not full")



    # The function that returns the size of the  list
    def size(self):
        return len(self.stack)


