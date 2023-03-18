## 有重不可复选全排列

'''
如果把上述剪枝逻辑中的 !used[i - 1] 改成 used[i - 1]，其实也可以通过所有测试用例，但效率会有所下降，这是为什么呢？
之所以这样修改不会产生错误，是因为这种写法相当于维护了 2'' -> 2' -> 2 的相对顺序，最终也可以实现去重的效果。
但为什么这样写效率会下降呢？因为这个写法剪掉的树枝不够多。
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, used):
            nonlocal res
            if len(track) == len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                ## not used[i-1]是在维护2-2‘-2’‘的顺序，如果used[i-1]=False, 说明2还没有使用过就直接到了2‘,直接剪枝
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                track.append(nums[i])
                used[i] = True
                backtrack(nums, used)
                track.pop()
                used[i] = False

        nums.sort()
        res, track = list(), list()
        used = [False for _ in range(len(nums))]
        backtrack(nums, used)
        return res