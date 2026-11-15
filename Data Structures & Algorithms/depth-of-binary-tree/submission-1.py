# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, curr, n):
        if not curr: return n
        n += 1
        l = self.dfs(curr.left, n)
        r = self.dfs(curr.right, n)
        
        self.max = max(l,r)
        return self.max
        