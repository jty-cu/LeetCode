'''
including 002, 445
445 = 002 + 206 (翻转链表 + 两数相加)
** function divmod(a, b) = a//b, a%b
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ## 给l1, l2安排指针
        p1, p2 = l1, l2
        ##
        dummy = ListNode(-1)
        ## 移动的指针
        p = dummy
        ## 记录进位
        carry = 0
        while p1 or p2 or carry:
            val = carry
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            ## 更新val and carry
            carry, val = divmod(val, 10)
            p.next = ListNode(val)
            p = p.next
        return dummy.next