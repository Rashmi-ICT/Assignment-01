import numpy as np

#
class stack:
    def __init__(self, limit=10):
        self.limit = limit
        self.stack = np.array([])

    def push(self, data):
        if len(self.stack) <= self.limit:
            self.stack = np.append(self.stack, data)
            print("PUSH  ELEMENT IS >>", data)


        else:
            print("STACK IS FULL")

    def pop(self):
        if len(self.stack) == 0:
            print("STACK IS EMPTY")

        else:
            find_Pop= (len(self.stack) - 1)
            self.stack = np.delete(self.stack,len(self.stack) - 1)
            print("succusesfully popped element is >> ",find_Pop)
            print("er removing the element of stack",self.stack )




