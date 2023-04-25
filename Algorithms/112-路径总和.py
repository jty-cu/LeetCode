## DFS
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)

## BFS + stack
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        queue = [(root, root.val)]
        while queue:
            cur, sum0 = queue.pop()
            if not cur.left and not cur.right and sum0 == targetSum:
                return True
            if cur.left: queue.append([cur.left, sum0+cur.left.val])
            if cur.right: queue.append([cur.right, sum0+cur.right.val])
        return False

