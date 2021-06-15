
# Class to create nodes of linked list
# initialize constructor#

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Represent the head singly  linked list
class StackLinked:
    def __init__(self):
        self.head = None


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
        print(" PUSHED DATA : ", data)




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



    # Remove and return the element from the top of the stack
    # (i.e., LIFO). Raise exception if the stack is empty.
    def pop(self):
        if self.size() == 0:
            print('ALL ELEMENTS ARE POPPED')
        else:

            print(' POPPED  ELEMENT >>> ', self.peek())
            self.head = self.head.next
