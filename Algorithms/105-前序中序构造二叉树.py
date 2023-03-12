'''
确定头节点后，如何确定递归时，左右子树的前序、中序遍历
return None 的条件
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, inorder, preleft, preright, inleft, inright):
            if preleft > preright:
                return None
            rootval = preorder[preleft]
            index = inorder.index(rootval)
            # index = 0
            # for i in range(inleft, inright+1):
            #     if inorder[i] == rootval:
            #         index = i
            #         break
            ## 创建根节点
            root = TreeNode(rootval)
            ## 计算左子树中的节点数
            left_size = index - inleft
            ## 递归构造左右子树
            root.left = build(preorder, inorder, preleft+1, preleft+left_size, inleft, index-1)
            root.right = build(preorder, inorder, preleft+1+left_size, preright, index+1, inright)
            return root
        return build(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)