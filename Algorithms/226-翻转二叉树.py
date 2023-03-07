## solution1: traverse
'''
写一个 traverse 函数遍历每个节点，让每个节点的左右子节点颠倒过来就行了。
单独抽出一个节点，需要让它做什么？让它把自己的左右子节点交换一下。
需要在什么时候做？好像前中后序位置都可以
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            if not root:
                return
            tmp = root.left
            root.left = root.right
            root.right = tmp
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return root



## solution2: 分解问题 / 递归
'''
对于某一个二叉树节点 x 执行 invertTree(x)，你能利用这个递归函数的定义做点啥？
我可以用 invertTree(x.left) 先把 x 的左子树翻转，再用 invertTree(x.right) 把 x 的右子树翻转，最后把 x 的左右子树交换，
这恰好完成了以 x 为根的整棵二叉树的翻转，即完成了 invertTree(x) 的定义。
**这种「分解问题」的思路，核心在于你要给递归函数一个合适的定义，然后用函数的定义来解释你的代码；如果你的逻辑成功自恰，那么说明你这个算法是正确的。**
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        ## 翻转左右子树
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        ## 重新连接根节点
        root.left = right
        root.right = left
        return root