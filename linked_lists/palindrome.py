"""
This file holds methods to check if a Linked List is a palindrome
1) is_palindrome_using_stack
2) is_palindrome_using_previous_node

"""
from basics import LinkedList


def is_palindrome_using_stack(link_list):
    """
    Checks if a Linked List is a palindrome using stack

    :param link_list: instance of the Linked List
    :return: boolean
    """
    print("Checking if the Linked List is a palindrome")
    node_values = llist.collect_values()
    node = link_list.head
    is_palindrome_state = True
    while node is not None and node_values:
        last_node_data = node_values.pop()
        if node.data != last_node_data:
            is_palindrome_state = False
            break
        node = node.next
    return is_palindrome_state


def is_palindrome_using_previous_node(link_list):
    """
    Checks if a Linked List is a palindrome by accessing the previous node

    :param link_list: instance of the Linked List
    :return: boolean
    """
    print("Checks if a Linked List is a palindrome using previous nodes")
    node = link_list.head
    last = link_list.get_last_node()
    is_palindrome_state = True
    while node is not None:
        if node.data != last.data:
            is_palindrome_state = False
            break
        node = node.next
        last = link_list.get_previous_node(last)
    return is_palindrome_state


# Palindrome using stack
node_data = [1, 2, 3, 4, 3, 2, 1]
llist = LinkedList()
for node_value in node_data:
    llist.append(node_value)
state = is_palindrome_using_stack(llist)
if state:
    print("It is a palindrome")
else:
    print("Not a palindrome")

# Testing getting the previous node of the node specified
llist.get_previous_node(llist.head.next.next.next.next.next)

# Getting the last node of the Linked List
llist.get_last_node()

# Palindrome using last node
state = is_palindrome_using_previous_node(llist)
if state:
    print("It is a palindrome")
else:
    print("Not a palindrome")
