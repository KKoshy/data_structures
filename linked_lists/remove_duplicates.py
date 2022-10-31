"""
This file holds methods to remove duplicates from Linked Lists
1) remove_duplicates_using_stack
2) remove_duplicates_from_sorted_link_list

"""
from basics import LinkedList


def remove_duplicates_using_stack(link_list):
    """
    Removes duplicates from unsorted Linked List using stack

    :param link_list: Instance of the Linked List
    :return: resultant Linked List without duplicates
    """
    # Checks for empty Linked List
    if link_list.head is None:
        print("No duplicates: Empty Linked List passed")

    # Removes duplicates from non-empty Linked List
    else:
        current_data = []
        prev = link_list.head
        current = link_list.head
        print("Removing duplicates from Linked List")
        while current is not None:
            if current.data in current_data:
                prev.next = current.next
                current = current.next
            else:
                current_data.append(current.data)
                prev = current
                current = current.next

    link_list.traverse()
    return link_list


def remove_duplicates_from_sorted_link_list(link_list):
    """
    Removes duplicates from a sorted Linked List

    :param link_list: Instance of the Linked List
    :return: resultant Linked List without duplicates
    """
    # Checks for empty Linked List
    if link_list.head is None:
        print("No duplicates: Empty Linked List passed")

    # Removes duplicates from non-empty Linked List
    else:
        node = link_list.head
        while node is not None and node.next is not None:
            if node.data == node.next.data:
                node.next = node.next.next
                node = link_list.head
            else:
                node = node.next

    link_list.traverse()
    return link_list


link_01 = LinkedList()
node_data = [2, 3, 4, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9,
             9, 9, 9, 4, 4, 4, 9, 9, 9, 2, 2, 2, 2, 1, 1, 10]
for node_value in node_data:
    link_01.append(node_value)
remove_duplicates_using_stack(link_01)

link_01 = LinkedList()
node_data = [2, 3, 4, 4, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9, 10]
for node_value in node_data:
    link_01.append(node_value)
remove_duplicates_from_sorted_link_list(link_01)
