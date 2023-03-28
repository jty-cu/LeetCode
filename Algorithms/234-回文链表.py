# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## s1: 用后续遍历实现倒序读链表
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # global left
        left = head

        def traverse(right):
            nonlocal left
            if not right:
                return True
            res = traverse(right.next)
            res = res and right.val == left.val
            left = left.next
            return res

        return traverse(head)


## s2: 数学方法
def isPalindrome(self, head):
    s1 = 0
    s2 = 0
    t = 1

    while head != None:
        s1 = s1 * 10 + head.val
        s2 = s2 + t * head.val
        t = t * 10
        head = head.next

    return s1 == s2



