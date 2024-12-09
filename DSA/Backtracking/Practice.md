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

## 39. Combination Sum - [Link](https://leetcode.com/problems/combination-sum/description/)

```go
func combinationSum(candidates []int, target int) [][]int {
    ans := make([][]int, 0)
    backtrack(candidates, target, 0, &ans, []int{})
    return ans   
}

func backtrack(candidates []int, target int, k int, ans *[][]int, curr []int) { 
    if target == 0 {
        *ans = append(*ans, curr)
    }

    if target < 0 {
        return
    }

    for i := k; i < len(candidates); i++ {
        temp := append([]int{}, curr...)
        temp = append(temp, candidates[i])
        backtrack(candidates,target - candidates[i], i, ans, temp)
    }
}
```

## 40. Combination Sum II - [Link](https://leetcode.com/problems/combination-sum-ii/description/)

```go
func combinationSum2(candidates []int, target int) [][]int {
    sort.Ints(candidates)
    ans := make([][]int, 0)
    backtrack(candidates, 0, target, &ans, []int{})
    return ans
}

func backtrack(candidates []int, i int, target int, ans *[][]int, curr []int) {
    if target == 0 {
        *ans = append(*ans, curr)
        return
    }

    if target < 0 {
        return
    }

    for k := i; k < len(candidates); k++ {
        if k != i && candidates[k] == candidates[k-1] {
            continue
        }

        temp := append([]int{}, curr...)
        temp = append(temp, candidates[k])
        backtrack(candidates, k+1, target-candidates[k], ans, temp)
    }
}
```

## Letter Combinations of a Phone Number - [Link](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)

```go
var (
    numLetters = map[rune]string{
        '2':"abc",
        '3':"def",
        '4':"ghi",
        '5':"jkl",
        '6':"mno",
        '7':"pqrs",
        '8':"tuv",
        '9':"wxyz",
    }
)

func letterCombinations(digits string) []string {
    ans := []string{}
    backtrack(digits, 0, len(digits), &ans, "")
    return ans
}

func backtrack(digits string, i, n int, ans *[]string, curr string) {
    if len(digits) == 0 {
        return
    }

    if i >= n {
        *ans = append(*ans, curr)
        return
    }

    if letters, ok := numLetters[rune(digits[i])]; ok {
        for _, l := range letters {
            backtrack(digits, i+1, n, ans, curr + string(l))
        }
    }
}
```

## 51. N-Queens - [Link](https://leetcode.com/problems/n-queens/description/)

```go
func solveNQueens(n int) [][]string {
	ans := make([][]string, 0, n)

	board := make([]string, n)
	for i := 0; i < n; i++ {
		board[i] = ""
		for j := 0; j < n; j++ {
			board[i] += "."
		}
	}

	backtrack(&board, 0, &ans)

	return ans
}

func backtrack(board *[]string, i int, ans *[][]string) {
	n := len(*board)

	if i >= n {
		temp := append([]string{}, *board...)
		*ans = append(*ans, temp)
		return
	}

	for k := 0; k < n; k++ {
		if isValid(*board, i, k) {
			d := *board
			row := d[i]
			temp := []byte(row)
			temp[k] = 'Q'
			d[i] = string(temp)
			board = &d
			backtrack(board, i+1, ans)
			temp[k] = '.'
			d[i] = string(temp)
			board = &d
		}
	}
}

func isValid(board []string, i, j int) bool {
	n := len(board)
	row := []byte(board[i])
	for k := 0; k < n; k++ {
		if row[k] == 'Q' {
			return false
		}
	}

	for k := 0; k < n; k++ {
		r := []byte(board[k])
		if r[j] == 'Q' {
			return false
		}
	}

	return checkDiagonal(board, i, j)
}

func checkDiagonal(board []string, i, j int) bool {
	n := len(board)
	for k, l := i+1, j+1; k < n && l < n; k, l = k+1, l+1 {
		if []byte(board[k])[l] == 'Q' {
			return false
		}
	}

	for k, l := i-1, j-1; k >= 0 && l >= 0; k, l = k-1, l-1 {
		if []byte(board[k])[l] == 'Q' {
			return false
		}
	}

	for k, l := i+1, j-1; k < n && l >= 0; k, l = k+1, l-1 {
		if []byte(board[k])[l] == 'Q' {
			return false
		}
	}

	for k, l := i-1, j+1; k >= 0 && l < n; k, l = k-1, l+1 {
		if []byte(board[k])[l] == 'Q' {
			return false
		}
	}

	return true
}

```