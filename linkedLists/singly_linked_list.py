"""
    Implement singly linked list in Python
"""


class SinglyLinkedList(object):

    def __init__(self):
        self._head = None
        self._tail = None
        self.node_counter = 0

    class Node(object):

        def __init__(self, data):
            self._data = data
            self._next = None

        def __repr__(self):
            return repr(self._data)

        def set_next(self, node):
            self._next = node

        def get_next(self):
            return self._next

        def get_val(self):
            return self._data

    def create_node(self, data):
        """
        This function creates a new node with the data and returns the node.
        """
        self.node_counter += 1
        return self.Node(data)

    def set_head(self, node):
        self._head = node

    def insert_end(self, data):
        if not self.get_head():
            self.set_head(self.create_node(data))
            self._tail = self.get_head()
        else:
            node = self.create_node(data)
            self._tail.set_next(node)
            self._tail = node

    def insert_start(self, data):
        node = self.create_node(data)
        if not self.get_head():
            self._tail = node
        node.set_next(self.get_head())
        self.set_head(node)

    def insert_between(self, insert_after, new_val):
        curr_node = self.get_head()
        while(curr_node):
            val = curr_node.get_val()
            if (val == insert_after):
                new_node = self.create_node(new_val)
                new_node.set_next(curr_node.get_next())

                # Check if curr node is tail node, then we have to make sure
                # that the new node added after it becomes the tail node
                if self._tail.get_val() == curr_node.get_val():
                    self._tail = new_node

                curr_node.set_next(new_node)
                break
            curr_node = curr_node.get_next()

    def get_head(self):
        return self._head

    def delete_start(self):
        """
            Delete Node at the start of the List
        """
        if not self.get_head():
            return
        new_head = self.get_head().get_next()
        self.set_head(new_head)
        self.node_counter -= 1
    
    def delete_end(self):
        """
            Delete Node at the end of the List
        """
        if not self.get_head():
            return
        # If only one node in the linked List
        if not (self.get_head().get_next()):
            self.set_head(None)
            self._tail = None
            return
        curr = self.get_head()
        while(curr.get_next()):
            next = curr.get_next().get_next()
            if not next:
                break
            curr = curr.get_next()
        curr.set_next(None)
        self._tail = curr
        self.node_counter -= 1
    
    def delete_node(self, val):
        """
            Delete the node with the first occurence with the value
        """
        if not self.get_head():
            return
        
        # if only one node in Linked List:
        if not (self.get_head().get_next()):
            if self.get_head().get_val() == val:
                return self.delete_start()
            else:
                return
        
        # If the value matches the head
        if self.get_head().get_val() == val:
            return self.delete_start()
        
        curr = self.get_head()
        prev = None
        while(curr):
            if curr.get_val() == val:
                prev.set_next(curr.get_next())
                # if curr is last node
                if not curr.get_next():
                    self._tail = prev
                curr.set_next(None)
                self.node_counter -= 1
            prev = curr
            curr = curr.get_next()
        return
    
    def reverse(self, head):
        if not head:
            return
        curr = head
        prev = None
        next_node = curr.get_next()

        while(curr):
            curr.set_next(prev)
            prev = curr
            curr = next_node
            if next_node:
                next_node = next_node.get_next()
        self._tail = head
        self.set_head(prev)

    def __repr__(self):
        nodes = []
        curr = self.get_head()
        while(curr):
            nodes.append(repr(curr))
            curr = curr.get_next()
        return '[' + ', '.join(nodes) + ']'


if __name__ == "__main__":
    my_list = SinglyLinkedList()
    my_list.delete_end()
    print(my_list)
    my_list.insert_start('Scientists')
    print(my_list)
    my_list.insert_end('Newton')
    print(my_list)
    my_list.insert_start('Galileo')
    print(my_list)
    my_list.delete_start()
    print(my_list)
    my_list.insert_start('List of scientists')
    print(my_list)
    my_list.delete_node('Scientists')
    print(my_list)
    my_list.insert_between('List of scientists', 'Gauss')
    print(my_list)
    my_list.delete_end()
    print(my_list)
    my_list.insert_end('Einstein')
    print(my_list)
    my_list.insert_between('Einstein', 'Newton')
    print(my_list)
    my_list.delete_node('Gauss')
    print(my_list)
    my_list.delete_node('Einstein')
    print(my_list)
    my_list.delete_node('Newton')
    my_list.delete_node('List of scientists')
    print(my_list)
    my_list.insert_end('JC Bose')
    print(my_list)
    my_list.insert_end('A P J Kalam')
    print(my_list)
    my_list.insert_start('Indian Scientists')
    print(my_list)
    my_list.insert_between('JC Bose', 'Homie Bhabha')
    print(my_list)
    my_list.insert_between('XYZ', 'Indira')
    print(my_list)
    print("Reversing list: ")
    my_list.reverse(my_list.get_head())
    print(my_list)
    my_list.insert_end("Scientists")
    print(my_list)
    my_list.insert_start("Ramanujam")
    print(my_list)
