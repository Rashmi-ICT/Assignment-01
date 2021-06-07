"""
1. Create a class Node with instance variables data and next.
2. Create a class Stack with instance variable head.
3. The variable head points to the first element in the linked list.
4. Define methods push and pop inside the class Stack.
5. The method push adds a node at the front of the linked list.
6. The method pop returns the data of the node at the front of the linked list and removes the node. It returns None if there are no nodes.
7. Create an instance of Stack and present a menu to the user to perform operations on the stack.
"""


# Class to create nodes of linked list
# initialize constructor

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# head is default NULL

class StackLinked:
    def __init__(self):
        self.head = None
