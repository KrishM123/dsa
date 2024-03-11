class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def getDiameter(self, node):
            if node:
                height1 = getDiameter(self, node.left)
                height2 = getDiameter(self, node.right)
                self.max_diameter = max(self.max_diameter, height1 + height2)
                return max(height1, height2) + 1
            else:
                return 0
        getDiameter(self, root)
        return self.max_diameter