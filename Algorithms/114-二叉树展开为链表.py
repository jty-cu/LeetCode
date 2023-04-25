## 遍历
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
            ## 后序位置，先将左右子树拉平
        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right
        ## 把左子树放在右子树的位置上
        root.left = None
        root.right = left
        ## 把原来的右子树接到现在的右子树后面
        p = root
        while p.right:
            p = p.right  ## 定位到现在右子树的末端节点
        p.right = right  ## 连接

        return root

