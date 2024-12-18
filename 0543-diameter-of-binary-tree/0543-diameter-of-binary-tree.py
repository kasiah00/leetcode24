# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDia=0
        def diameter(root):
            if not root:
                return 0
            nonlocal maxDia
            lh=diameter(root.left)
            rh=diameter(root.right)
            maxDia=max(maxDia,lh+rh)
            return 1+max(lh,rh)
        diameter(root)
        return maxDia