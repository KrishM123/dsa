# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def nodeBalanced(node):
            if node:
                d1 = nodeBalanced(node.left)
                d2 = nodeBalanced(node.right)
                if abs(d1[0] - d2[0]) > 1 or not d1[1] or not d2[1]:
                    return [0, False]
                else:
                    return [max(d1[0], d2[0]) + 1, True]
            else:
                return [0, True]
        
        return nodeBalanced(root)[1]