'''
后序遍历左右子树下标
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(postorder, inorder, pleft, pright, inleft, inright):
            if inleft > inright:
                return None
            rootval = postorder[pright]
            index = inorder.index(rootval)
            left_size = index - inleft
            root = TreeNode(rootval)

            root.left = build(postorder, inorder, pleft, pleft+left_size-1, inleft, index-1)
            root.right = build(postorder, inorder, pleft+left_size, pright-1, index+1, inright)
            return root