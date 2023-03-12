'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverse(root, k):
            if not root:
                return
            rank = 0
            res = 0
            traverse(root.left, k)
            rank += 1
            if rank == k:
                res = root.val
                return res
            traverse(root.right, k)
        return traverse(root, k)
错误原因：不能把rank, res的值写在traverse内，否则每次迭代都会重置这个值
比如例子：输入
[3,1,4,null,2]
1
res会永远返回根结点的值
'''

## 中序遍历返回有序数组，递归
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res, rank = 0, 0
        def traverse(root, k):
            nonlocal rank, res
            if not root:
                return
            traverse(root.left, k)
            ## 中序位置
            rank += 1
            if rank == k:
                res = root.val
            traverse(root.right, k)
        traverse(root, k)
        return res

## 搜索树性质 + 迭代
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = list()
        while root or stack:
            while root:
                stack.append(root)
                root = root.left ## 到达最小值
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right