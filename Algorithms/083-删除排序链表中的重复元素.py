## 链表；快慢指针
## 连接到26题
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        fast, slow = head, head
        while fast:
            if (fast.val != slow.val):
                slow.next = fast
                slow = slow.next
            fast = fast.next
        ## 断开slow后面的链接
        slow.next = None
        return head ## 想清楚return啥