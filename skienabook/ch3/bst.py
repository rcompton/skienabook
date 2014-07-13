import logging

__author__ = 'ryan'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BstNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, new_node):
        if self.value < new_node.value:
            if self.right is not None:
                self.right.insert(new_node)
            else:
                self.right = new_node
        elif self.value > new_node.value:
            if self.left is not None:
                self.left.insert(new_node)
            else:
                self.left = new_node
        elif self.value == new_node.value:
            return

    def max_first_traverse_helper(self, l):
        if self.right is not None:
            self.right.max_first_traverse_helper(l)
        l.append(self.value)
        if self.left is not None:
            self.left.max_first_traverse_helper(l)
        return


class BSTree:
    def __init__(self, root):
        self.root = root

    def insert(self, new_node):
        self.root.insert(new_node)

    def max_first_traverse(self):
        l = []
        self.root.max_first_traverse_helper(l)
        return l