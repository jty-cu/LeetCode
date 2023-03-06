## 数组；技巧型变换
'''
有时候咱们拍脑袋的常规思维，在计算机看来可能并不是最优雅的；但是计算机觉得最优雅的思维，对咱们来说却不那么直观。也许这就是算法的魅力所在吧。
回到之前说的顺时针旋转二维矩阵的问题，常规的思路就是去寻找原始坐标和旋转后坐标的映射规律，但我们是否可以让思维跳跃跳跃，尝试把矩阵进行反转、镜像对称等操作，可能会出现新的突破口。
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ## 沿对角线镜像翻转矩阵
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        ## 对每一行数组做翻转
        # 先定义函数
        def myreverse(x):
            left, right = 0, len(x)-1
            while left < right:
                x[left], x[right] = x[right], x[left]
                left += 1
                right -= 1
            return x
        # 开始翻转
        for i in range(n):
            matrix[i] = myreverse(matrix[i])