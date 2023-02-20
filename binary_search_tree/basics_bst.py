"""
This file holds basic operations using Binary Search Tree such as,,
1) pre_order_recursive_traversal
2) in_order_recursive_traversal
3) post_order_recursive_traversal
4) traversals
5) pre_order_traversal
6) in_order_traversal
7) post_order_traversal
8) insert
9) delete

"""
from stack.basics_st import Stack


class Node:
    """
    Class for defining Node of a Binary Search Tree

    """
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Class for defining a Binary Search Tree

    """
    def __init__(self):
        self.root = None

    def pre_order_recursive_traversal(self, root):
        """
        Pre-order traversal of Binary Search Tree using recursion

        :param root: root node to be considered
        :return: None
        """
        # root -> left -> right
        if root is not None:
            print(root.data, "->", end=" ")
            self.pre_order_recursive_traversal(root.left)
            self.pre_order_recursive_traversal(root.right)

    def in_order_recursive_traversal(self, root):
        """
        In-order traversal of Binary Search Tree using recursion

        :param root: root node to be considered
        :return: None
        """
        # left -> root -> right
        if root is not None:
            self.in_order_recursive_traversal(root.left)
            print(root.data, "->", end=" ")
            self.in_order_recursive_traversal(root.right)

    def post_order_recursive_traversal(self, root):
        """
        Post-order traversal of Binary Search Tree using recursion

        :pram root: root node to be considered
        :return: None
        """
        # left -> right -> root
        if root is not None:
            self.post_order_recursive_traversal(root.left)
            self.post_order_recursive_traversal(root.right)
            print(root.data, "->", end=" ")

    def traversals(self, root):
        """
        Pre-order, In-order and Post-order traversals of Binary Search Tree using a single stack

        :param root: root node to be considered
        :return: pre-order, in-order, post-order traversals as stacks
        """
        pre_t, inn_t, post_t = [], [], []
        s = Stack([[root, 1]])
        while s.stack:
            current = s.peek()

            # Pre-order traversal
            if current[1] == 1:
                pre_t.append(current[0].data)
                current[1] += 1
                if current[0].left is not None:
                    s.append([current[0].left, 1])

            # In-order traversal
            elif current[1] == 2:
                inn_t.append(current[0].data)
                current[1] += 1
                if current[0].right is not None:
                    s.append([current[0].right, 1])

            # Post-order traversal
            else:
                post_t.append(current[0].data)
                s.pop()
        return pre_t, inn_t, post_t

    def pre_order_traversal(self, root):
        """
        Pre-order traversal of Binary Search Tree using Stack

        :param root: root node to be considered
        :return: pre-order traversal
        """
        # root -> left -> right
        pre_t = []
        s = Stack([root])
        while s.stack:
            current = s.pop()
            if current is not None:
                pre_t.append(current.data)
                if current.right is not None:
                    s.append(current.right)
                if current.left is not None:
                    s.append(current.left)
        return pre_t

    def in_order_traversal(self, root):
        """
        In-order traversal of Binary Search Tree using Stack

        :param root: root node to be considered
        :return; in-order traversal
        """
        # left -> root -> right
        inn_t = []
        s = Stack()
        current = root
        while s.stack or current is not None:
            if current is not None:
                s.append(current)
                current = current.left
            else:
                current = s.pop()
                inn_t.append(current.data)
                current = current.right
        return inn_t

    def post_order_traversal(self, root):
        """
        Post-order traversal of Binary Search Tree using Stack

        :param root: root node to be considered
        :return: post-order traversal
        """
        # left -> right -> root
        post_t = []
        s = Stack()
        current = root
        while s.stack or current is not None:
            while current is not None:
                if current.right is not None:
                    s.append(current.right)
                s.append(current)
                current = current.left
            current = s.pop()
            if current.right is not None and current.right == s.peek():
                s.pop()
                s.append(current)
                current = current.right
            else:
                post_t.append(current.data)
                current = None
        return post_t

    def insert(self, root, value):
        """
        Inserts value in a Binary Search  Tree

        :param root: root node to be considered
        :param value: value to be inserted
        :return: root node
        """
        if root is not None:
            # Value lesser than node value
            if root.data > value:
                root.left = self.insert(root.left, value)

            # Value greater than node value
            elif root.data < value:
                root.right = self.insert(root.right, value)

            # Node with the value already exists
            else:
                print(value, " already exists")
                return root

        # Creating a new node for the value
        else:
            print(value, " has been inserted")
            return Node(value)
        return root

    def minimum_node(self, root):
        """
        Finds the node with the minimum value with respect to the root node

        :param root: root node to be considered
        :return: minimum node
        """
        while root.left is not None:
            root = root.left
        return root

    def delete(self, root, value):
        """
        Deletes value from Binary Search Tree

        :param root: root node to be considered
        :param value: value to be inserted
        :return: root node
        """
        if root is not None:
            # Value lesser than the node value
            if root.data > value:
                root.left = self.delete(root.left, value)

            # Value greater than the node value
            elif root.data < value:
                root.right = self.delete(root.right, value)

            # Target node to be deleted has been found
            else:
                # Node with one child -> right child
                if root.left is None:
                    return root.right

                # Node with one child -> left child
                elif root.right is None:
                    return root.left

                # Node with 2 children
                else:
                    min_node = self.minimum_node(root.right)
                    root.data = min_node.data
                    root.right = self.delete(root.right, min_node.data)
                    return root
        return root


bst = BinarySearchTree()
bst.root = Node(100)
bst.root.left = Node(50)
bst.root.right = Node(150)

bst.root.left.left = Node(30)
bst.root.left.right = Node(70)

bst.root.right.left = Node(130)
bst.root.right.right = Node(180)

bst.root.left.left.left = Node(25)
bst.root.left.left.right = Node(40)

bst.root.left.right.left = Node(60)
bst.root.left.right.right = Node(75)

bst.root.right.left.left = Node(120)
bst.root.right.left.right = Node(140)

bst.root.right.right.left = Node(170)
bst.root.right.right.right = Node(200)

print("Pre-order recursive traversal")
bst.pre_order_recursive_traversal(bst.root)
print()

print("In-order recursive traversal")
bst.in_order_recursive_traversal(bst.root)
print()

print("Post-order recursive traversal")
bst.post_order_recursive_traversal(bst.root)
print()

print("Traversals")
pre, inn, post = bst.traversals(bst.root)
print(pre)
print(inn)
print(post)

print("Pre-order traversal using stack")
pre = bst.pre_order_traversal(bst.root)
print(pre)

print("In-order traversal using stack")
inn = bst.in_order_traversal(bst.root)
print(inn)

print("Post-order traversal using stack")
post = bst.post_order_traversal(bst.root)
print(post)

print("Inserting values - 7, 17, 27, 97, 177")
bst.insert(bst.root, 7)
bst.in_order_recursive_traversal(bst.root)
print()

bst.insert(bst.root, 17)
bst.in_order_recursive_traversal(bst.root)
print()

bst.insert(bst.root, 77)
bst.in_order_recursive_traversal(bst.root)
print()

bst.insert(bst.root, 97)
bst.in_order_recursive_traversal(bst.root)
print()

bst.insert(bst.root, 177)
bst.in_order_recursive_traversal(bst.root)
print()

print("Deleting elements - 27, 97")
bst.delete(bst.root, 27)
bst.in_order_recursive_traversal(bst.root)
print()

bst.delete(bst.root, 97)
bst.in_order_recursive_traversal(bst.root)
print()
