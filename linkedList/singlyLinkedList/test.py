from singly_linked_list import LinkedList, Node

def test_delete_node():
    llist = LinkedList()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    llist.set_head(first)
    llist.get_head().set_next(second)
    second.set_next(third)
    llist.printList()

    # delete node with key 2
    llist = llist.delete_pos(2)
    print("*" * 20)
    llist.printList()

if __name__ == "__main__":
    test_delete_node()
