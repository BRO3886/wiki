package main

import "fmt"

func possible(val, divisons int, arr []int) bool {
	usedDivisions := 1
	currTotal := 0
	for _, a := range arr {
		if currTotal+a <= val {
			currTotal += a
		} else {
			if usedDivisions == divisons {
				return false
			}
			if a > val {
				return false
			}
			usedDivisions++
			currTotal = a
		}
	}
	return true
}

func main() {
	var size, divisions int
	fmt.Scanln(&size, &divisions)
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		fmt.Scan(&arr[i])
	}

	low, high := 0, int(1e9)
	ans := int(1e9)
	for low <= high {
		mid := (low + high) / 2
		if possible(mid, divisions, arr) {
			ans = min(ans, mid)
			high = mid - 1
		} else {
			low = mid + 1
		}
	}

	fmt.Println(ans)
}
