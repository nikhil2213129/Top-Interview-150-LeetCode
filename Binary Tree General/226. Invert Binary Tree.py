# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        return self.mirror(root)
    def mirror(self, root):
        if root is None:
            return
        self.mirror(root.left)
        self.mirror(root.right)
        root.left,root.right=root.right,root.left
        return root

        
