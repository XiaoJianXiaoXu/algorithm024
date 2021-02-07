from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorder(self, node: TreeNode, list: List[int]) -> None:
        if node is None:
            return
        self.inorder(node.left, list)
        list.append(node.val)
        self.inorder(node.right, list)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        list = []
        self.inorder(root, list)
        return list

