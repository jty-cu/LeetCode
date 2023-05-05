## 控制结果精度
# def sqrt0(x):
#     left, right = 0, x
#     res = -1
#     while abs(left-right) > 0.1:
#         mid = (right + left) / 2
#         if mid**2 <= x:
#             res = mid
#             left = (mid+left) / 2
#         else:
#             right = (mid+right) / 2
#     return res
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if mid**2 <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res

