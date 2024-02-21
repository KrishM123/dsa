class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def findDepth(node, pos):
            if node:
                return max(findDepth(node.left, pos + 1), findDepth(node.right, pos + 1))
            else:
                return pos
        
        return findDepth(root, 0)