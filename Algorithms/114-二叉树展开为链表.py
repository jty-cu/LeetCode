## 遍历
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)
        ## 需要遍历完成后进行操作，后序位置
        left = root.left
        right = root.right
        ## 置空左子树
        root.left = None
        ## 把原来的左子树放在右边
        root.right = left
        ## 接上原来的右子树
        p = root
        ## 找到原来左子树的叶子结点
        while p.right:
            p = p.right
        p.right = right