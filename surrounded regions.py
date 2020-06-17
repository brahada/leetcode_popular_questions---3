class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not len(board) or not len(board[0]):
            return
        
        neighs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        visited = set()
        
        def isValid(r, c):
            return r >=0 and r < len(board) and c >= 0 and c < len(board[0])
        
        def dfs(r, c):
            s = []
            s.append((r, c))
            
            while s:
                r, c = s.pop()
                visited.add((r, c))
                board[r][c] = '.'

                for neigh in neighs:
                    new_r = r + neigh[0]
                    new_c = c + neigh[1]
                    
                    if isValid(new_r, new_c) and (new_r, new_c) not in visited and board[new_r][new_c] == 'O':
                        s.append((new_r, new_c))
                        visited.add((new_r, new_c))
            
        for c in range(len(board[0])):
            if board[0][c] == 'O':
                dfs(0, c)
                
            if board[-1][c] == 'O':
                dfs(len(board) - 1, c)
                
        for r in range(len(board)):
            if board[r][0] == 'O':
                dfs(r, 0)
                
            if board[r][-1] == 'O':
                dfs(r, len(board[0]) - 1)
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '.':
                    board[r][c] = 'O'
