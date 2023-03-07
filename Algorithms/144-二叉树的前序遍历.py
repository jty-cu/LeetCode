# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## solution1: 模版解题：内置dfs
'''
solution1:
是否可以通过遍历一遍二叉树得到答案？如果可以，用一个 traverse / dfs 函数配合**外部变量** 来实现。
nonlocal函数：nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。

solution2:
是否可以定义一个递归函数，通过子问题（子树）的答案推导出原问题的答案？如果可以，写出这个递归函数的定义，并充分利用这个函数的返回值。
'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        def dfs(root):
            nonlocal res
            if not root:
                return res
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
            return res
        a = dfs(root)
        return a

## solution2: 和solution1等价但是无需内置dfs
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # from typing import List
        res = list()
        if not root:
            return res
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res

## solution3: stack
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
            ## 左右子树入栈，注意入栈顺序
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return res