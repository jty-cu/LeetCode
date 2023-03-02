## 链表；双指针
'''
1. 解决这个问题的关键是，通过某些方式，让 p1 和 p2 能够同时到达相交节点 c1。
## 原理是什么：p1-->p2 and p2-->p1, 可以让 p1 和 p2 同时进入公共部分，也就是同时到达相交节点 c1
2. 如果不相交，则同时返回null
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
        return p1