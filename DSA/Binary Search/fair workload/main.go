package main

import (
	"fmt"
	"strconv"
	"strings"
)

// Problem: https://community.topcoder.com/stat?c=problem_statement&pm=1901&rd=4650

type IFairWorkload interface {
	getMostWork(folders []int, workers int) int
	possible(section, workers int, folders []int) bool
}

type FairWorkload struct {
}

func NewFairWorkload() IFairWorkload {
	return FairWorkload{}
}

// getMostWork implements IFairWorkload.
func (f FairWorkload) getMostWork(folders []int, workers int) int {
	low, high := 0, int(1e9)
	ans := int(1e9)
	for low <= high {
		mid := (low + high) / 2
		fmt.Println(mid, low, high)
		if f.possible(mid, workers, folders) {
			ans = min(ans, mid)
			high = mid - 1
		} else {
			low = mid + 1
		}
	}

	return ans
}

func (f FairWorkload) possible(section, workers int, folders []int) bool {
	usedWorkers := 1
	totalWork := 0
	for _, folder := range folders {
		if totalWork+folder <= section {
			totalWork += folder
		} else {
			if usedWorkers == workers {
				return false
			}
			usedWorkers++
			if folder > section {
				return false
			}
			totalWork = folder
		}
	}
	return true
}

func main() {
	f := NewFairWorkload()

	var arrStr string
	fmt.Scanln(&arrStr)
	folders := arrAtoi(strings.Split(arrStr, ","))

	var workers int
	fmt.Scanln(&workers)

	fmt.Println(f.getMostWork(folders, workers))
}

func arrAtoi(s []string) []int {
	ans := make([]int, 0, len(s))
	for _, i := range s {
		num, _ := strconv.Atoi(i)
		ans = append(ans, num)
	}
	return ans
}
