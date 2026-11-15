# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        queue = deque([root])
        while queue:
            sub = []
            for i in range(len(queue)):
                c = queue.popleft()
                sub.append(c.val)
                if c.left: queue.append(c.left)
                if c.right: queue.append(c.right)
            if sub: res.append(sub)
        return res