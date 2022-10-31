"""
This file holds methods to detect intersection between 2 Linked Lists
1) detect_intersection_using_stack

"""
from basics import LinkedList


def detect_intersection_using_stack(link_01, link_02):
    """
    Detects intersection between two Linked Lists using stack

    :param link_01: instance of the first Linked List
    :param link_02: instance of the second Linked List
    :return: boolean
    """
    # Checks for empty Linked List
    if link_01.head is None or link_02.head is None:
        print("Empty Linked List detected")
        link_01.traverse()
        link_01.traverse()

    # Checks for intersection between two linked lists
    else:
        current_nodes = []
        node_01 = link_01.head
        while node_01 is not None:
            current_nodes.append(node_01)
            node_01 = node_01.next

        node_02 = link_02.head
        while node_02 is not None:
            if node_02 in current_nodes:
                print("Intersection found at node with data ", node_02.data)
                link_01.traverse()
                link_02.traverse()
                return
            node_02 = node_02.next
        print("No intersection found")


llink_01 = LinkedList()
node_values_01 = range(2, 22, 2)
for node_data_01 in node_values_01:
    llink_01.append(node_data_01)

llink_02 = LinkedList()
node_values_02 = range(3, 33, 3)
for node_data_02 in node_values_02:
    llink_02.append(node_data_02)

llink_01.head.next.next.next.next.next = llink_02.head.next.next

detect_intersection_using_stack(llink_01, llink_02)

print(len(llink_01))
