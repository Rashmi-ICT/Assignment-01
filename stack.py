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
# create head
class StackLinked:
    def __init__(self):
        self.head = None


    # print out  all the elements
    def display(self):
        # Node current will point to head
        current = self.head
        while  current is not None:
            print(" PUSH IN  >>>  ",  current.data)

            Node =  current.next

    # function to display total no. of elements
    def size(self):
        current = self.head
        count = 0
        while  current is not None:
            current =  current.next
            count = count + 1

        return count

    # function to push an element in the stack
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def isEmpty(self):
        return self.head is None

    def peek(self):
        if not self.isEmpty():
            return self.head.data
        else:
            print("THE STACK IS EMPTY")
            return -1

    # function to pop an element from the stack
    def pop(self):
        if self.size() == 0:
            print('ALL ELEMENTS ARE POPPED')
        else:

            print('SUCCESSFULLY POPPED >>> ', self.peek())
            self.head = self.head.next
