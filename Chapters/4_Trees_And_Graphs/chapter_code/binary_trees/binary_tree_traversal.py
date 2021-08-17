from typing import Optional

class BinaryTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def inorder_traversal(root: Optional[BinaryTreeNode]):
    if root is not None:
        inorder_traversal(root.left)
        print(root.value)
        inorder_traversal(root.right)

def preorder_traversal(root: Optional[BinaryTreeNode]):
    if root is not None:
        print(root.value)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root: Optional[BinaryTreeNode]):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value)
