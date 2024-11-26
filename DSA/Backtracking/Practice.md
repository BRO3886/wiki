## 37. Sudoku Solver - [Link](https://leetcode.com/problems/sudoku-solver/description/)

```go
func solveSudoku(board [][]byte)  {
    if solve(&board,0,0) {
        return
    }
}

func check(board [][]byte, i, j int, c byte) bool {
    if board[i][j] != byte('.') {
        return false
    }

    for x := 0; x < 9; x++ {
        if board[x][j] == c {
            return false
        }
    }

    for y := 0; y < 9; y++ {
        if board[i][y] == c {
            return false
        }
    }

    startX, startY := (i - i%3), (j - j%3)

    for x := startX; x < startX+3; x++ {
        for y := startY; y < startY+3; y++ {
            if board[x][y] == c {
                return false
            }
        }
    }

    return true
}

func solve(board *[][]byte, i, j int) bool {
    if i == 9 {
        return true
    }

    if j == 9 {
        return solve(board, i+1, 0)
    }

    tmp := *board
    if tmp[i][j] != byte('.') {
        return solve(board, i, j+1)
    }

    for c := '1'; c <= '9'; c++ {
        if !check(*board, i, j, byte(c)) {
            continue
        }

        
        tmp[i][j] = byte(c)
        ans := solve(board, i, j+1)
        if ans {
            return true
        }
        tmp[i][j] = byte('.')
    }

    return false
}
```