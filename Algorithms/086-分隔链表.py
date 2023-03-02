## 一个链表一分二
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        p1, p2 = ListNode(-1), ListNode(-1)
        prev1, prev2 = p1, p2
        while head:
            if head.val < x:
                prev1.next = head
                prev1 = prev1.next
            else:
                prev2.next = head
                prev2 = prev2.next
            head = head.next
        prev2.next = None
        prev1.next = p2.next
        return p1.next