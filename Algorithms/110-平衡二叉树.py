# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def maxDepth(root):
            nonlocal res
            if not root:
                return 0
            left_max = maxDepth(root.left)
            right_max = maxDepth(root.right)
            if abs(left_max - right_max) > 1:
                res = False
            return max(left_max, right_max) + 1

        maxDepth(root)
        return res

