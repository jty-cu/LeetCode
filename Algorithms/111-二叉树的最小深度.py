# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
## dfs
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        res = 10**6
        if root.left:
            res = min(res, self.minDepth(root.left)+1)
        if root.right:
            res = min(res, self.minDepth(root.right)+1)
        return res


## 第一个和第二个：时间换空间
## bfs
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = list()
        depth = 1
        queue.append(root)
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                if not cur.left and not cur.right:
                    return depth
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth += 1
        return depth

## another bfs
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))

        return 0