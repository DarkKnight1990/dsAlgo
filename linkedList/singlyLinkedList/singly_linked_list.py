
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
    def push(self, new_node):
        """
        Pushes the new_node at the front of the LinkedList
        """
        if not isinstance(new_node, Node):
            print("New node to be added should be of type: Node,\
            so not pushing the node")
            return
        if not self._head:
            """ Set the new_node as the head of the LinkedList """
            self.set_head(new_node)
            return
        new_node.set_next(self.get_head())
        self.set_head(new_node)
        return

    def insert_after(self, prev_node, new_node):
        """
        Inserts the new_node after the prev_node
        """
        if not isinstance(new_node, Node):
            print("New node is not of type Node")
            return
        new_node.set_next(prev_node.get_next())
        prev_node.set_next(new_node)
        return

    def insert_end(self, new_node):
        """
        Inserts the new_node at the end of LinkedList
        """
        if not isinstance(new_node, Node):
            print("New node is not of type Node")
            return
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
    new_node = Node("new_data")
    llist.push(new_node)
    llist.printList()
    print("*" * 20)
    print("Insert a new node after second")
    another_new_node = Node("Something new")
    llist.insert_after(second, another_new_node)
    llist.printList()
    print("*" * 20)
    print("Insert at end")
    last_new_node = Node("Last")
    llist.insert_end(last_new_node)
    llist.printList()
