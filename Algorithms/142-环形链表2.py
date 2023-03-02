## 链表；快慢指针
'''
如果没有环，return （空）
从相遇到重置的原理
'''

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## has cycle
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if (not fast or not fast.next):
            return

        ## put slow back to head
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow