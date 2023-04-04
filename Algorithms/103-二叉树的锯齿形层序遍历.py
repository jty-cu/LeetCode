'''
按照从左向右的顺序记录，但是读取顺序按照sign来判断
没通过，后续看看为啥
'''
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = list()
#         if not root:
#             return res
#         queue = [root]
#         sign = 1
#         while queue:
#             sign *= -1
#             length = len(queue)
#             level = list()
#             for i in range(length):
#                 cur = queue.pop(0)
#                 level.append(cur.val)
#                 if sign == -1:
#                     if cur.right: queue.append(cur.right)
#                     if cur.left: queue.append(cur.left)
#                 else:
#                     if cur.left: queue.append(cur.left)
#                     if cur.right: queue.append(cur.right)
#             res.append(level)
#         return res

'''
正常遍历，隔行取反
'''
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = list()
        if not root:
            return res
        queue = [root]
        sign = True
        while queue:
            sign = not sign
            length = len(queue)
            level = list()
            for i in range(length):
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.right: queue.append(cur.right)
                if cur.left: queue.append(cur.left)
            if sign:
                res.append(level)
            else:
                res.append(level[::-1])
        return res



