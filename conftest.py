import pytest
from linked_lists.basics import LinkedList
from data.linked_list import LinkList as ll


@pytest.fixture(scope='module')
def link_list():
    llist = LinkedList()
    for node_value in ll.NODE_DATA:
        llist.append(node_value)
    return llist
