"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def partition(sr, sc, er, ec):
            cr = (sr + er) // 2
            cc = (sc + ec) // 2

            return [
                (sr, sc, cr, cc),  # Top left
                (sr, cc, cr, ec),  # Top right
                (cr, sc, er, cc),  # Bottom left
                (cr, cc, er, ec)   # Bottom right
            ]

        def isSameVal(sr, sc, er, ec):
            val = grid[sr][sc]

            for i in range(sr, er):
                for j in range(sc, ec):
                    if grid[i][j] != val:
                        return False

            return True

        def buildTree(sr, sc, er, ec):

            val = grid[sr][sc]

            # Base case: entire region has the same value
            if isSameVal(sr, sc, er, ec):
                return Node(val == 1, True)

            # Otherwise, divide into four quadrants
            node = Node(val == 1, False)

            tl, tr, bl, br = partition(sr, sc, er, ec)

            node.topLeft = buildTree(*tl)
            node.topRight = buildTree(*tr)
            node.bottomLeft = buildTree(*bl)
            node.bottomRight = buildTree(*br)

            return node

        return buildTree(0, 0, len(grid), len(grid[0]))
