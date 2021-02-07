from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorder(self, node: TreeNode, list: List[int]) -> None:
        if node is None:
            return
        list.append(node.val)
        self.preorder(node.left, list)
        self.preorder(node.right, list)
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        list = []
        self.preorder(root, list)
        return list