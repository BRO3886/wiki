https://leetcode.com/problems/surrounded-regions/description/
### Intuition

The '#' symbol serves as a clever way to mark 'O' cells that cannot be captured because they're connected to the border. Without this temporary marking, we'd lose track of which 'O's we've already visited during our BFS. After the BFS completes, we know that any remaining 'O's (not marked as '#') must be completely surrounded and can be flipped to 'X's, while our temporary '#' markers can be restored back to 'O's.

### Code

```python
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        dxs = [
            (1,0),(-1,0),(0,1),(0,-1)
        ]

        if m == 1 and n == 1:
            return

        q = deque()
        for i in range(0,m):
            if board[i][0] == 'O':
                q.append((i,0))
            if board[i][n-1] == 'O':
                q.append((i,n-1))
        
        for j in range(0,n):
            if board[0][j] == 'O':
                q.append((0,j))
            if board[m-1][j] == 'O':
                q.append((m-1,j))

        while q:
            ci,cj = q.popleft()
            board[ci][cj] = '#'
            for d in dxs:
                dx,dy = ci+d[0],cj+d[1]
                if 0 <= dx <= m-1 and 0 <= dy <= n-1 and board[dx][dy] == 'O':
                    q.append((dx,dy))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'

        return
```