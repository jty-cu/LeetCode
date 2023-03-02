## 链表

'''
双指针，一次遍历！
1. **return head** is wrong, 看注释
2. dummy节点的使用，p1, p2的起始位置
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p1 = head
        p2 = dummy
        for i in range(n):
            p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next ## 不能return head, 对于[1]这样的测试用例会不通过
