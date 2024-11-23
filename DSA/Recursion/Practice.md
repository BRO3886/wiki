## Factorial

```go
func factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorial(n-1)
}
```

## Fibonacci

```go
func fibo(a int) int {
    if a == 0 {
        return 0
    }
    if a == 1 {
        return 1
    }
	return fibo(a-1) + fibo(a-2)
}
```

## Binary representation of a number

```go
package main

import (
	"fmt"
)

func NumToBinary(num int) string {
	if num == 0 {
		return ""
	}
	return NumToBinary(num/2) + fmt.Sprintf("%d", num%2)
}

func main() {
	fmt.Println(NumToBinary(27))
}
```

## 3211. Generate Binary Strings Without Adjacent Zeros - [Link](https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/)

```go
func validStrings(n int) []string {
    l := int(math.Pow(2,float64(n)))
    result := make(chan string, l)
    recurse(n,"", result)
    close(result)
    ans := make([]string, 0, l)
    for item := range result {
        ans = append(ans, item)
    }
    return ans
}

func recurse(n int, rep string, result chan string) {
    if n == 0 {
        result <- rep
        return
    }

    l := len(rep)
    if l > 0 && rep[l-1] == '0' {
        recurse(n-1,rep + "1", result)
    } else {
        recurse(n-1,rep + "0", result)
        recurse(n-1,rep + "1", result)
    }
}
```

## 3n+1 Problem

```go
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	fmt.Println(f(n, 1))
}

func f(a, n int) int {
	if a <= 1 {
		return n
	}

	if a%2 == 0 {
		return f(a/2, n+1)
	} else {
		return f(3*a+1, n+1)
	}
}
```

## 78. Subsets - [Link](https://leetcode.com/problems/subsets/)

```go
func subsets(nums []int) [][]int {
    n := len(nums)
    if n <= 1 {
        return [][]int{{},{nums[0]}}
    }

    last := nums[n-1]
    ans := subsets(nums[:n-1])
    final := [][]int{}
    for _, row := range ans {
        if len(row) == 0 {
            final = append(final, row)
            continue
        }

        temp := make([]int,len(row))
        copy(temp,row)
        final = append(final, row)
        temp = append(temp, last)
        final = append(final, temp)
    }
    final = append(final, []int{last})
    return final
}
```

## 90. Subsets II - [Link](https://leetcode.com/problems/subsets-ii/)

```go
func subsetsWithDup(nums []int) [][]int {
    sort.Ints(nums)
    res := [][]int{}
    sub(nums, 0, []int{}, &res)
    return res
}

func sub(nums []int, s int, curr []int, res *[][]int) {
    newcurr := make([]int, len(curr))
    copy(newcurr, curr)
    *res = append((*res), newcurr)
    if s > len(nums) {
        return
    }
    for i := s; i <len(nums); i++ {
       if i != s && nums[i] == nums[i-1] {
           continue
       }

        sub(nums, i+1, append(curr, nums[i]), res)
    }
}
```

## Sum of a matrix - [Link](https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/N)

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	var r, c int
	fmt.Scanln(&r, &c)

	a := make([][]int, r)
	b := make([][]int, r)

	for i := 0; i < r; i++ {
		a[i] = DefaultSlice(-101, c)
		for j := range a[i] {
			if _, err := fmt.Scan(&a[i][j]); err != nil {
				panic(err)
			}
		}
	}

	for i := 0; i < r; i++ {
		b[i] = DefaultSlice(-101, c)
		for j := range b[i] {
			if _, err := fmt.Scan(&b[i][j]); err != nil {
				panic(err)
			}
		}
	}

	ans := make([][]int, r)
	for i := 0; i < r; i++ {
		ans[i] = DefaultSlice(-101, c)
	}
	doSum(a, b, &ans, 0, 0, r, c)
	sb := strings.Builder{}
	for i := 0; i < r; i++ {
		sb.Reset()
		for j := 0; j < c; j++ {
			sb.WriteString(fmt.Sprintf("%d ", ans[i][j]))
		}
		fmt.Println(strings.TrimSpace(sb.String()))
	}
}

func doSum(a, b [][]int, ans *[][]int, i, j, r, c int) {
	if i >= r || j >= c {
		return
	}

	temp := *ans
	if temp[i][j] != -101 {
		return
	}
	temp[i][j] = a[i][j] + b[i][j]
	doSum(a, b, ans, i+1, j, r, c)
	doSum(a, b, ans, i, j+1, r, c)
}

func DefaultSlice[T any](val T, size int) []T {
	arr := make([]T, size)
	for i := range arr {
		arr[i] = val
	}
	return arr
}
```

## Knapsack - [Link](https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/U)

```go
func knapsack(weights, profits []int, i, w int) int {
	if i >= len(weights) || w <= 0 {
		return 0
	}

	// skip cond
	if weights[i] > w {
		return knapsack(weights, profits, i+1, w)
	}

	return max(knapsack(weights, profits, i+1, w), profits[i]+knapsack(weights, profits, i+1, w-weights[i]))
}
```

## Maximum Path Sum - [Link](https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/X)

```go
func maxPathSum(arr [][]int, i, j, r, c int) int {
	if i == r-1 && j == c-1 {
		return arr[i][j]
	}

	// can only go down
	if j == c-1 {
		return arr[i][j] + maxPathSum(arr, i+1, j, r, c)
	}

	// can only go right
	if i == r-1 {
		return arr[i][j] + maxPathSum(arr, i, j+1, r, c)
	}

	return arr[i][j] + max(maxPathSum(arr, i, j+1, r, c), maxPathSum(arr, i+1, j, r, c))
}
```

## Creating Expression 1 - [Link](https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/V)

```go
func createExpression(arr []int, i, ans, x int) bool {
	if i == len(arr) {
		return ans == x
	}

	return createExpression(arr, i+1, ans+arr[i], x) || createExpression(arr, i+1, ans-arr[i], x)
}
```

## Creating Strings - [Link](https://cses.fi/problemset/task/1622)

```go
func main() {
	var input string
	fmt.Scanln(&input)

	runes := []rune(input)
	sort.SliceStable(runes, func(i, j int) bool {
		return runes[i] < runes[j]
	})

	input = string(runes)

	fm := map[rune]int{}

	n := 0
	for _, char := range input {
		n++
		fm[char]++
	}

	ans := make([]string, 0, n)
	f(0, n, fm, "", &ans)
	fmt.Println(len(ans))
	for _, item := range ans {
		fmt.Println(item)
	}
}

func f(i, n int, fm map[rune]int, curr string, ans *[]string) {
	if i == n {
		*ans = append(*ans, curr)
		return
	}

	for j := 97; j < 124; j++ {
		if fm[rune(j)] > 0 {
			fm[rune(j)]--
			f(i+1, n, fm, curr+string(rune(j)), ans)
			fm[rune(j)]++
		}
	}
}
```

## 131. Palindrome Partitioning - [Link](https://leetcode.com/problems/palindrome-partitioning/description/)

```go
func partition(s string) [][]string {
    ans := make([][]string, 0)
	f(s, 0, []string{}, &ans)
	return ans
}


func f(s string, i int, curr []string, ans *[][]string) {
	fmt.Println(i, curr)
	if i >= len(s) {
		*ans = append(*ans, curr)
		return
	}

	for j := i; j <= len(s)-1; j++ {
		if isPalindrome(s[i : j+1]) {
			temp := append([]string{}, curr...)
			f(s, j+1, append(temp, s[i:j+1]), ans)
		}
	}
}

func isPalindrome(s string) bool {
    left, right := 0, len(s)-1
	for left < right {
		if s[left] != s[right] {
			return false
		}
		left++
		right--
	}
	return true
}
```
