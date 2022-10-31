"""
This file holds methods to merge sorted Linked Lists
1) merge_sorted_link_lists

"""
from basics import LinkedList, Node


def merge_sorted_link_lists(link_01, link_02):
    """
    Merges two sorted Linked Lists

    :param link_01: instance of the first Linked List
    :param link_02: instance of the second Linked List
    :return: resultant merged Linked List
    """
    # Checks if the first linked list is empty
    if link_01.head is None:
        print("First Linked List is empty")
        return link_02

    # Checks if the second linked list is empty
    if link_02.head is None:
        print("Second Linked List is empty")
        return link_01

    # Checking for the linked list head with the least value to determine the resultant head
    if link_01.head.data <= link_02.head.data:
        node_01, node_02 = link_01.head, link_02.head
        sorted_link_list = link_01
    else:
        node_01, node_02 = link_02.head, link_01.head
        sorted_link_list = link_02

    # Merging the sorted Linked Lists
    print("Merging sorted Linked Lists")
    while node_02 is not None:
        while node_01 is not None and node_01.next is not None:
            if node_01.data <= node_02.data <= node_01.next.data:
                node = Node(node_02.data)
                node.next = node_01.next
                node_01.next = node
                break
            else:
                node_01 = node_01.next

        # Checks for the last node of the resultant Linked List
        if node_01.next is None:
            node_01.next = Node(node_02.data)
        node_02 = node_02.next

    # Traversing the resultant linked list
    sorted_link_list.traverse()
    return sorted_link_list


llink_01 = LinkedList()
node_data_01 = range(2, 22, 2)
for node_value_01 in node_data_01:
    llink_01.append(node_value_01)

llink_02 = LinkedList()
node_data_02 = range(3, 33, 3)
node_data_02 = [3, 3, 3, 4, 4, 5, 5, 7, 7, 77, 78]
for node_value_02 in node_data_02:
    llink_02.append(node_value_02)

merge_sorted_link_lists(llink_01, llink_02)
