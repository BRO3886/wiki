package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"time"
)

type BlockingQueue[T any] interface {
	Enqueue(element T)
	Dequeue() T
	Size() int
}

type blockingQueue[T any] struct {
	capacity int
	queue    chan T
	sizeCtr  int
}

// Dequeue implements BlockingQueue.
func (b *blockingQueue[T]) Dequeue() T {
	ele := <-b.queue
	b.sizeCtr--
	return ele
}

// Enqueue implements BlockingQueue.
func (b *blockingQueue[T]) Enqueue(element T) {
	b.queue <- element
	b.sizeCtr++
}

// Size implements BlockingQueue.
func (b blockingQueue[T]) Size() int {
	return b.sizeCtr
}

func NewBlockingQueue[T any](capacity int) BlockingQueue[T] {
	return &blockingQueue[T]{
		capacity: capacity,
		queue:    make(chan T, capacity),
		sizeCtr:  0,
	}
}

func main() {
	q := NewBlockingQueue[int](10)
	sc := bufio.NewScanner(os.Stdin)
	go func() {
		for sc.Scan() {
			num, err := strconv.Atoi(sc.Text())
			if err != nil {
				continue
			}
			q.Enqueue(num)
			fmt.Println("size=", q.Size())
		}
	}()

	go func() {
		for {
			time.Sleep(2 * time.Second)
			val := q.Dequeue()
			fmt.Println("deque=", val)
			fmt.Println("size=", q.Size())
		}
	}()

	select {}
}
