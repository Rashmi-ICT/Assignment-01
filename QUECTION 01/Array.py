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




