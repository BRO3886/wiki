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