"""
This file holds basic operations using Stack such as,
0) __len__
1) append
2) peek
3) pop

"""


class Stack:
    """
    Class for defining a Stack

    """
    def __init__(self, data=None) -> None:
        if data is None:
            data = []
        self.stack = data

    def __len__(self):
        return len(self.stack)

    def append(self, value):
        """
        Appends value to the stack

        :param value: value to be appended to the Stack
        :return: None
        """
        self.stack.append(value)

    def peek(self):
        """
        Peeks the last element of the stack

        :return: last element of the stack
        """
        try:
            return self.stack[-1]
        except IndexError:
            print("IndexError; Found an empty Stack")

    def pop(self, index=-1):
        """
        Pops the element at the index specified

        :param index: index of the element to be popped
        :return: popped element
        """
        try:
            return self.stack.pop(index)
        except IndexError:
            print("IndexError; Invalid index specified")
