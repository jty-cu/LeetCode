# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        def reverse(a, b):
            pre, cur, nxt = None, head, head
            while cur != b:
                nxt = cur.next
                cur.next = pre
                pre, cur = cur, nxt
            return pre

        if not head:
            return None
        a, b = head, head
        for i in range(k):
            if not b:
                return head  ## 剩余长度 < k
            b = b.next
        newHead = reverse(a, b)
        a.next = self.reverseKGroup(b, k)  ## 为什么不是b.next
        return newHead