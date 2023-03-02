## 递归
'''
没太理解
递归的两个条件：
1. 终止条件是当前节点或者下一个节点==null (head.next = None)
2. 在函数内部，改变节点的指向，也就是 head 的下一个节点指向 head 递归函数那句 (head.next.next = head)
https://leetcode.cn/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
**递归函数必须有base case, i.e. if not head or not head.next: return head
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)
        head.next.next = head ## head节点和last的尾节点箭头交换
        head.next = None
        return last


## 双指针
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre