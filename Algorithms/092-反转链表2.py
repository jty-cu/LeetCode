# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
reverseN + reverseBetween的节点平移
注意successor的应用
'''
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        successor = None
        def reverseN(head, n):
            global successor ## 这里不能用nonlocal
            if n == 1:
                successor = head.next
                return head
            last = reverseN(head.next, n-1)
            head.next.next = head
            head.next = successor
            return last
        if left == 1:
            return reverseN(head, right)
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head

