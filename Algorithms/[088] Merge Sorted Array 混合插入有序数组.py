# solution 1 直接使用sort

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
        
# solution 2
# 因为两个数组都是sorted, 可以直接比较大小然后插入
# nums1 and nums2 同时开始在nums1中排序

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = m+n-1
        m = m-1
        n = n-1

        while m>=0 and n>=0:
            if nums1[m]>nums2[n]:
                nums1[pos] = nums1[m]
                m -= 1
                pos -= 1
            
            else:
                nums1[pos] = nums2[n]
                n -= 1
                pos -= 1
            
        while n >= 0:
            nums1[pos] = nums2[n]
            n -= 1
            pos -= 1
