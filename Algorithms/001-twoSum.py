## 题目类型：数组
'''
Hashtable
一次遍历：time complexity: O(N)
**【字典中存放的是什么，return什么。有两种情况不要搞混了】**
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## 01. 存放 target-num / 余数对应的序号，判断当前数num是否在字典中
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                return [i, d[num]]
            else:
                d[target-num] = i

        ## 02. 存放 num 对应的序号，判断当前余数 target - num 是否在字典中
        d = dict()
        for i, num in enumerate(nums):
            if target - num in d:
                return [i, d[target-num]]
            else:
                d[num] = i
