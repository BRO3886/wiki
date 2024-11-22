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
package main

import "fmt"

func main() {
	var n, w int
	fmt.Scanln(&n, &w)

	weights := make([]int, n)
	profits := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&weights[i], &profits[i])
	}

	fmt.Println(knapsack(weights, profits, 0, w))
}

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
