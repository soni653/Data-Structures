from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   In array, each element is independent and can be accessed using it's index value. In case of a linked list,
   each node/element points to the next, previous, or maybe both nodes. Array gets memory allocated in the stack 
   section. Whereas, linked list gets memory allocated in Heap section.
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            x = self.storage.tail.get_value()
            self.storage.remove_tail() 
            self.size += -1
            return x
