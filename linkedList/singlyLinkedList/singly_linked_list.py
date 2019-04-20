
class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

    def set_next(self, Node):
        self._next = Node

    def get_next(self):
        return self._next

    def get_data(self):
        return self._data

    def __str__(self):
        return self.get_data()


class LinkedList:
    def __init__(self):
        self._head = None

    def set_head(self, Node):
        self._head = Node

    def get_head(self):
        return self._head

    def printList(self):
        """
        Traversing the linked list
        """
        if not self._head:
            print("Linked List not initialised")
        temp_node = self._head
        while(temp_node):
            print(temp_node.get_data())
            temp_node = temp_node.get_next()

    """
    Here we show the insertion of a Node into a LinkedList
    A node can be inserted at 3 different ways into a list
    a) At the beginning of the List
    b) After a given node
    c) At the end of the LinkedList
    """
    def push(self, new_data):
        """
        Pushes the new_data at the front of the LinkedList as a Node
        """
        if not self._head:
            """ Set the new_data as the head of the LinkedList """
            self.set_head(Node(new_data))
            return
        new_node = Node(new_data)
        new_node.set_next(self.get_head())
        self.set_head(new_node)
        return

    def insert_after(self, prev_node, new_data):
        """
        Inserts the new_node after the prev_node
        """
        if not isinstance(prev_node, Node):
            print("Previous node is not of type Node")
            return
        new_node = Node(new_data)
        new_node.set_next(prev_node.get_next())
        prev_node.set_next(new_node)
        return

    def insert_end(self, new_data):
        """
        Inserts the new_node at the end of LinkedList
        """
        new_node = Node(new_data)
        if not self._head:
            """ Set the new_node as the head of the LinkedList """
            self.set_head(new_node)
            return
        curr_node = self.get_head()
        while(curr_node.get_next()):
            # On exhaustion of this loop curr_node will be last Node
            curr_node = curr_node.get_next()
        curr_node.set_next(new_node)
        return

    def delete_node(self, key):
        """
        Given a key delete the first occurence of the key in the
        LinkedList
        """
        found = False
        prev_node = None
        curr_node = self.get_head()
        if not curr_node:
            print("LinkedList is not initialised")
            return self
        if not curr_node.get_next() and curr_node.get_data() == key:
            print("Single node in the linked list. And the key matches")
            self.set_head(None)
            return self
        while(curr_node):
            if curr_node.get_data() == key:
                """
                If this condition matches, then curr_node is the node
                to be deleted
                """
                found = True
                break
            prev_node = curr_node
            curr_node = curr_node.get_next()
        if found:
            prev_node.set_next(curr_node.get_next())
            curr_node = None
        return self

    def delete_pos(self, pos):
        """
        Delete the node present at the given position
        """
        found = False
        prev_node = None
        curr_node = self.get_head()
        curr_pos = 0 # If we consider pos starts from 0
        if not curr_node:
            print("LinkedList is not initialised")
            return self
        if curr_pos == 0 and curr_node.get_next() is None:
            print("Single node in the linked list. We are deleting the head")
            self.set_head(None)
            return self
        while(curr_node):
            if curr_pos == pos:
                found = True
                break
            curr_pos = curr_pos + 1
            prev_node = curr_node
            curr_node = curr_node.get_next()
        if found:
            prev_node.set_next(curr_node.get_next())
            curr_node = None
        return self

    def search_node(self, key):
        """
        Search the first occurence of the key "key"
        If found return pointer to that Node
        Else None
        """
        curr_node = self.get_head()
        if curr_node is None:
            print("LinkedList is not initialised")
            return None
        while(curr_node):
            if curr_node.get_data() == key:
                return curr_node
            curr_node = curr_node.get_next()
        return None


if __name__ == "__main__":
    llist = LinkedList()
    llist.set_head(Node(1))
    second = Node(2)
    third = Node(3)

    list_head = llist.get_head()
    list_head.set_next(second)
    second.set_next(third)

    llist.printList()
    print("*" * 20)
    print("Adding a new node at the front of the list")
    new_node = "new_data"
    llist.push(new_node)
    llist.printList()
    print("*" * 20)
    print("Insert a new node after second")
    another_new_node = "Something new"
    llist.insert_after(second, another_new_node)
    llist.printList()
    print("*" * 20)
    print("Insert at end")
    last_new_node = "Last"
    llist.insert_end(last_new_node)
    llist.printList()
