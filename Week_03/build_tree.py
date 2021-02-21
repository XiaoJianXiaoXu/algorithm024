from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        rootIndex = inorder.index(root.val)
        # nnn = [1,2,3]
        # rst = nnn[4:]
        # 结果为 []， 当取子数组时， index越界之间返回空数组
        
        left = self.buildTree(preorder[1:1+rootIndex], inorder[0:rootIndex])
        right = self.buildTree(preorder[1+rootIndex:], inorder[rootIndex+1:])
        root.left = left
        root.right = right
        return root

nnn = [1,2,3]
rst = nnn[4:]
print(rst)