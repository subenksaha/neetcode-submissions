"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        queue = deque([node])
        visited = set()
        root = Node(node.val)
        adj_list = dict({root.val : root})
        while queue:
            curr = queue.popleft()
            if curr.val in visited:
                continue
            visited.add(curr.val)
            clone = adj_list[curr.val]
            clone_neighbors = []
            for neighbor in curr.neighbors:
                clone_neighbor = Node(neighbor.val) if not neighbor.val in adj_list else adj_list[neighbor.val]
                clone_neighbors.append(clone_neighbor)
                adj_list[clone_neighbor.val] = clone_neighbor
                queue.append(neighbor)
            if clone_neighbors:
                clone.neighbors = clone_neighbors
        
        return root
        