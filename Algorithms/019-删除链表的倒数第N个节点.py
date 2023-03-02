## 链表

## 虚拟头结点的技巧，也是为了防止出现空指针的情况。
## 比如说链表总共有 5 个节点，题目就让你删除倒数第 5 个节点，也就是第一个节点，那按照算法逻辑，应该首先找到倒数第 6 个节点。
## 但第一个节点前面已经没有节点了，这就会出错。
'''
双指针，一次遍历！
1. **return head** is wrong, 看注释
2. dummy节点的使用，p1, p2的起始位置（p2最后应该停留在倒数k-1的位置上，跳过倒数k）
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


'''
栈。倒序-->先进后出
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        while cur:
            stack.append(cur) ## 不能写cur.val，需要把节点放进去
            cur = cur.next
        for i in range(n):
            stack.pop()
        p = stack[-1]
        p.next = p.next.next
        return dummy.next