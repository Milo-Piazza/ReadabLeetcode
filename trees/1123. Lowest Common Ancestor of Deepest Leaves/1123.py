# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def setDepth(self, root):
        if not root:
            return 0
        leftDepth = self.setDepth(root.left)
        rightDepth = self.setDepth(root.right)
        rootDepth = max(leftDepth, rightDepth) + 1
        root.depth = rootDepth
        return rootDepth

    def getLCA(self, root):
        leftDepth = 0 if not root.left else root.left.depth
        rightDepth = 0 if not root.right else root.right.depth
        if leftDepth == rightDepth:
            return root
        if leftDepth < rightDepth:
            return self.getLCA(root.right)
        if leftDepth > rightDepth:
            return self.getLCA(root.left)        

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.setDepth(root)
        return self.getLCA(root)