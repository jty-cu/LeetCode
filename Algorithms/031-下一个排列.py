class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return nums

        ## 从后向前寻找 nums[i] < nums[j]
        ## 如果 i == -1, 那就是最后一个排列
        i, j = n - 2, n - 1
        k = n - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        ## 如果不是最后一个排列, 寻找[j, end]中第一个比nums[i]大的数字，因为[j,end]都是降序，所以倒着找第一个比k大的数，一定是最接近k的
        if i >= 0:
            while nums[k] <= nums[i]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]
        ## 交换后[j, end]还是降序
        ## 把[j, end]从降序变成升序
        left, right = j, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums



