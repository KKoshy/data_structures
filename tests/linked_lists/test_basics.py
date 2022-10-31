"""
This file includes unit test cases for basics of the Linked Lists

"""
import logging

from data.linked_list import LinkList as ll
from linked_lists.basics import LinkedList as llist


def test_length(link_list):
    """
    Checks the length of the Linked List

    :param link_list: instance of Linked List
    :return: None
    """
    logging.info("Checking the length of the Linked List")
    length = len(link_list)
    assert length == ll.LENGTH, "Error in finding length of the Linked List"


def test_collect_values(link_list):
    """
    Checks for values in the Linked List

    :param link_list: instance of Linked List
    :return: None
    """
    logging.info("Checking the node values of the Linked List")
    values = link_list.collect_values()
    assert values == ll.NODE_DATA, "Node values missing in Linked List"


def test_push(link_list):
    """
    Checks if push function pushes an element to the head of the Linked List

    :param link_list: instance of Linked List
    :return: None
    """
    logging.info("Checking whether push pushes an element to the head of the Linked List")
    link_list.push(ll.PUSH_VALUE)
    elements = link_list.collect_values()
    assert elements[ll.HEAD] == ll.PUSH_VALUE, \
        "Error in pushing value to the head of the Linked List"


def test_append(link_list):
    """
    Checks if append function appends an element to the tail of the Linked List

    :param link_list: instance of Linked List
    :return: None
    """
    logging.info("Checking whether append appends an element to the tail of the Linked List")
    link_list.append(ll.APPEND_VALUE)
    elements = link_list.collect_values()
    assert elements[ll.TAIL] == ll.APPEND_VALUE, \
        "Error in appending value to the tail of the Linked List"


def test_traverse(link_list):
    """
    Checks for errors while traversing the Linked List

    :param link_list: instance of Linked List
    :return: None
    """
    logging.info("Checking traversal of Linked List")
    try:
        link_list.traverse()
    except:
        logging.error("Error in traversing the Linked List")


def test_traverse_empty_link_list():
    """
    Checks for errors while traversing an empty Linked List

    :return: None
    """
    logging.info("Checking traversal of empty Linked List")
    link_list = llist()
    try:
        link_list.traverse()
    except:
        logging.error("Error in traversing empty Linked List")


def test_insert_at(link_list):
    """
    Checks for inserting value at a specific position in the Linked List

    :param link_list: instance of Linked List
    :return: None
    """
    logging.info("Checking inserting value at a specific position in the Linked List")
    link_list.insert_at(*ll.INSERT_AT)
    values = link_list.collect_values()
    assert values[ll.INSERT_AT[0]] == ll.INSERT_AT[1], \
        "Error in inserting value at the specified position"


def test_insert_after(link_list):
    """
    Checks for inserting values after a specific node in the Linked List

    :param link_list: instance of Linked List
    :return: None
    """
    logging.info("Checking inserting value after a specific node in the Linked List")
    link_list.insert_after(link_list.head.next.next.next, ll.INSERT_AFTER[1])
    values = link_list.collect_values()
    assert values[ll.INSERT_AFTER[0]] == ll.INSERT_AFTER[1], \
        "Error in inserting after the specified node"
