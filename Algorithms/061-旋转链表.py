'''
遍历，确定链表长度，对k进行优化
从旋转点开始，把链表分成两份，拼接
'''
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        ## 遍历，确定链表长度
        l = 0
        dummy = ListNode(-1)
        dummy.next = head
        tail = dummy
        while tail.next:
            tail = tail.next
            l += 1
        ## 更新k
        k = k % l
        if k == 0:
            return head

        ## head --> 从后面转到前面的部分
        ## ans --> 从前面转到后面的部分
        ## 拼接
        i = 0
        ans = ListNode(-1)
        p1 = ans
        while i < l - k:
            p1.next = ListNode(head.val)
            p1 = p1.next
            head = head.next
            i += 1
        p2 = head
        while p2.next:
            p2 = p2.next
        p2.next = ans.next
        return head




