# solution 1
# 将集合按第一个元素排序
# 比较首尾元素大小

# version 1 (better)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        new0 = sorted(intervals, key = lambda x: x[0])
        result = []
        
        for i in range(n):
            if not result or new0[i][0] > result[-1][1]:
                result.append(new0[i])
            else:
                result[-1][1] = max(result[-1][1], new0[i][1])
        
        return result

# version 2
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        
        if n == 0:
            return [] 
        
        new0 = sorted(intervals, key = lambda x: x[0])
        result = [new0[0]] # 将new0[0]赋给result必须放在check n==0之后
        
        for i in range(n): # or range(1,n)
            if new0[i][0] > result[-1][1]:
                result.append(new0[i])
            else:
                result[-1][1] = max(result[-1][1], new0[i][1])
        
        return result


# solution 2
