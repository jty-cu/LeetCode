# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         a = list(str(x))
#         left, right = 0, len(a)-1
#         while left < right:
#             if a[left] != a[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ## 对 x 进行翻转
        tmp = x
        y = 0
        while tmp > 0:
            t = tmp%10
            tmp = tmp // 10
            y = y*10 + t
        return y == x