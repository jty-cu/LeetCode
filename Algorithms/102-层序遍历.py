class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = list()
        if not root:
            return res
        queue = [root]
        while queue:
            ## only record this level
            length = len(queue)
            level = list()
            for i in range(length):
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            res.append(level)
        return res
