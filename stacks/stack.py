"""
   Implement stack with Python. Stack can be implemented in several ways.
   The two most common approaches include use of Python list and a linked list.
   The choice depends on the type of application involved.
"""
import sys
sys.path.insert(0, '/home/piklu/study/ds_algo/linkedLists/')
import time

from  singly_linked_list import SinglyLinkedList


class StackList:
    """
        This is a Python list based implementation of a Stack
    """
    # create an empty stack.
    def __init__(self):
        self._theItems = list()
    
    # Returns True if the stack is empty or False otherwise
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self._theItems)
    
    # Returns the top of the item in the stack without removing it
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack."
        return self._theItems[-1]
    
    # Removes and returns the top item of the stack
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._theItems.pop()
    
    # Push an item at the top of the stack
    def push(self, item):
        return self._theItems.append(item)


class StackLinkedList:
    """
        This is a Linked List based implementation of a stack
    """
    # Creates an empty list with Linked List
    def __init__(self):
        self._items = SinglyLinkedList()
    
    # Returns True if stack is Empty otherwise returns False
    def isEmpty(self):
        return self._items.node_counter == 0

    def __len__(self):
        return self._items.node_counter

    # Returns the top item of the stack without removing it
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._items.get_head()

    # Remove and return the last item of the stack
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        last_item = self.peek()
        self._items.delete_start()
        return last_item

    # Push an item at the top of the stack
    def push(self, item):
        self._items.insert_start(item)


if __name__ == "__main__":
    stack_list = StackList()
    stack_llist = StackLinkedList()
    start_time = time.time()
    stack_list.push('Hello')
    stack_list.push('World')
    stack_list.push('Hi')
    stack_list.push('this')
    stack_list.push('is')
    stack_list.push('piklu')
    print("Time to push in list implementation: ", time.time() - start_time)

    print(stack_list.peek())

    nstart = time.time()
    stack_llist.push('Hello')
    stack_llist.push('World')
    stack_llist.push('Hi')
    stack_llist.push('this')
    stack_llist.push('is')
    stack_llist.push('piklu')
    print("Time to push in linked list implementation: ", time.time() - nstart)
    print(stack_llist.peek())
