class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # avoid revisiting the same path twice
        path = set()

        # i is the current character that we are looking for
        def dfs(r,c,i):
            if i == len(word):
                return True
            # if go out of bounds
            if (r<0 or c<0 
                or r>= ROWS or c>= COLS 
                or word[i]!=board [r][c]
                or (r,c) in path
                ):
                return False

            path.add((r,c))
            
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            path.remove((r,c))

            return res

        for r in range(COLS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True

        return False