## traverse
'''
想好traverse的定义
'''
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return

        def traverse(node1, node2):
            if not node1 or not node2:
                return
            node1.next = node2
            traverse(node1.left, node1.right)
            traverse(node2.left, node2.right)
            traverse(node1.right, node2.left)

        traverse(root.left, root.right)
        return root


## 层序遍历
class Solution(object):
    def connect(self, root):
        if not root:
            return None
        queue = list()
        queue.append(root)
        while queue:
            k = len(queue)
            for i in range(k):
                cur = queue.pop(0)
                if i < k-1:
                    cur.next = queue[0]
                else:
                    cur.next = None
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return root
