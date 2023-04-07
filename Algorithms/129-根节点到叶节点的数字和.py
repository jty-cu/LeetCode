# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        cur = 0
        def traverse(root):
            nonlocal res, cur
            if not root:
                return
            cur = cur*10+root.val
            if not root.left and not root.right:
                res += cur
            traverse(root.left)
            traverse(root.right)
            cur = (cur-root.val) // 10
        traverse(root)
        return res
