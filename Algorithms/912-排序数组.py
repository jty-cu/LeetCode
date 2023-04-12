'''
merge sort: time complexity: O(NlogN); space complexity: O(logN)
'''

class Solution(object):
    def sortArray(self, nums):
        def merge_sort(nums, low, high):
            if low == high:
                return
            mid = low + (high - low) // 2
            merge_sort(nums, low, mid)
            merge_sort(nums, mid + 1, high)
            ## 在tmp中存入nums
            tmp = list()
            ## 合并两个有序数组
            i, j = low, mid + 1
            while i <= mid or j <= high:
                if i > mid or (j <= high and nums[j] < nums[i]):
                    tmp.append(nums[j])
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            nums[low:high + 1] = tmp

        merge_sort(nums, 0, len(nums) - 1)
        return nums

'''
quick sort: time complexity: O(NlogN)-O(N**2); space complexity: O(logN)-O(N)
'''
class Solution(object):
    def sortArray(self, nums):
        import random
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
            # return

        def shuffle(nums):
            n = len(nums)
            for i in range(n):
                j = i + random.randint(0,n)
                j = j%n
                nums[i], nums[j] = nums[j], nums[i]
                # swap(nums, i, j%n)
            # return

        def partition(nums, low, high):
            pivot = nums[low]
            i, j = low+1, high
            ## aim: nums[low,i)<=pivot, nums(j,high]>pivot
            while i <= j:
                while i < high and nums[i] <= pivot:
                    i += 1
                while j > low and nums[j] > pivot: ## j>low+1可以吗
                    j -= 1
                if i >= j:
                    break
                # swap(nums, i, j)
                nums[i], nums[j] = nums[j], nums[i]
            # swap(nums, low, j) ## 把low放在对的位置上
            nums[low], nums[j] = nums[j], nums[low]
            return j

        def sort(nums, low, high):
            if low >= high:
                return
            p = partition(nums, low, high)
            sort(nums, low, p-1)
            sort(nums, p+1, high)

        shuffle(nums)
        sort(nums, 0, len(nums)-1)
        return nums