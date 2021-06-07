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


# Represent the head singly  linked list
class StackLinked:
    def __init__(self):
        self.head = None



    # print out  all the elements
    def display(self):
        # Node current will point to head
        current = self.head
        while current is not None:
            print(" PUSH IN  >>>  ", current.data)

            current= current.next



    # The function that returns the size of the linked list
    def size(self):
        # Node current will point to head
        current = self.head
        count = 0
        while current is not None:
            current = current.next
            count = count + 1

        return count
    # This function will return the size of the linked list.



    # add to element in the stack
    def push(self, data):
        # allocate node to new element
        newNode = Node(data)
        # make new node as head
        newNode.next = self.head
        self.head = newNode


    # if the head value is null, then the stack is empty, otherwise it is not.
    def isEmpty(self):
        return self.head is None



    # The peek() method will show us the 1st value in our stack
    # the stack. Raise Empty exception if the stack is empty.
    def peek(self):
        if not self.isEmpty():
            return self.head.data
        else:
            print("THE STACK IS EMPTY")
            return -1


    #  Utility function to pop a top element from the stack
    def pop(self):
        if self.size() == 0:
            print('ALL ELEMENTS ARE POPPED')
        else:

            print('SUCCESSFULLY POPPED >>> ', self.peek())
            self.head = self.head.next
