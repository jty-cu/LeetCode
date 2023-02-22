## 题目类型：链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ## 双指针
        ## 时间复杂度：O(m+n)，空间复杂度：O(1)
        '''
        prev在这里只是一个移动的指针，prehead才是形成的链表
        双指针有一个结束的操作
        '''
        prehead = ListNode(-1)
        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        if list1:
            prev.next = list1
        if list2:
            prev.next = list2
        return prehead.next


        ## 递归
        ## 时间复杂度：O(m+n)，空间复杂度：O(m+n)
        '''
        终止条件是什么
        如何判断时空复杂度
        '''
        if not list1: return list2
        if not list2: return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
            
## 大佬的代码
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

