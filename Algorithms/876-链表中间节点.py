## 链表；快慢指针

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next: ## 注意while条件
            slow = slow.next
            fast = fast.next.next
        return slow