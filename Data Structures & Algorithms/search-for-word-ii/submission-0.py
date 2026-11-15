from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores a complete word ending here


class Solution:
    def findWords(
        self,
        board: List[List[str]],
        words: List[str]
    ) -> List[str]:

        root = TrieNode()

        # Build the Trie
        for word in words:
            curr = root

            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char]

            curr.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(row: int, col: int, node: TrieNode) -> None:
            char = board[row][col]

            # This cell's character must continue a Trie path
            if char not in node.children:
                return

            next_node = node.children[char]

            # A complete word was found
            if next_node.word is not None:
                result.append(next_node.word)

                # Prevent finding the same word again
                next_node.word = None

            # Mark this cell as visited
            board[row][col] = "#"

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and board[new_row][new_col] != "#"
                ):
                    dfs(new_row, new_col, next_node)

            # Backtrack: restore the cell
            board[row][col] = char

        # Start a DFS from every cell
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return result