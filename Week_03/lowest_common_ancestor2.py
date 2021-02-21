class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None

s = Solution()

n5 = TreeNode(5)
n1 = TreeNode(1)
n3 = TreeNode(3)
n3.left = n5
n3.right = n1

result = s.lowestCommonAncestor(n3, n5, n1)
print('111111')
print(result)