## What is concurrency

Concurrency is the ability to handle multiple tasks at the same time by switching between them. Tasks can start, run and complete in overlapping time periods. 

One can think of it as working in the kitchen:
- While waiting for the water to boil, you can chop vegetables
- While the vegetables cook, one can prepare the dough

Here, we switch between the tasks, but only do one at a time.

### Difference between concurrency and parallelism

With parallelism, one is actually performing multiple tasks simultaneously. Building on the kitchen example, you could think of parallelism to be a restaurant kitchen with multiple chefs. One chef is chopping vegetables, one is cooking, one is finishing the dish - all of them working simultaneously.

## Concurrency in golang

Concurrency in golang is handled through:
- Goroutines (lightweight threads)
- Channels (communication between goroutines)
- Synchronization primitives (mutexes, wait groups)

> Rob Pike famously said:
> "Concurrency is about dealing with lots of things at once. Parallelism is about doing lots of things at once."

### Goroutines

A goroutine is a lightweight, user-space thread managed by the Go runtime.

```go
func main() {
    // Start a goroutine
    go func() {
        fmt.Println("Running in background")
    }()
    
    // Main continues executing
    fmt.Println("Main function")
}
```

#### Goroutines vs Threads

A thread is managed by the OS (kernel level) while a goro The key differences are that goroutines are much smaller (starting at 2KB vs 1-2MB for threads) and are scheduled by Go's runtime scheduler rather than the OS scheduler, making them much cheaper to create and switch between compared to threads. Threads typically share memory and use locks while goroutines can also use channels for communication.

#### Goroutine Leaks

A goroutine leak occurs when you create a goroutine that cannot exit and continues to consume resources indefinitely. This is similar to a memory leak, but instead of memory, you're leaking goroutines.

```go
// Bad - Leaky goroutine
func leak() {
    ch := make(chan int)
    go func() {
        for {
            ch <- 42  // Will block forever
        }
    }()
}

// Good - With cancellation
func noLeak(ctx context.Context) {
    ch := make(chan int)
    go func() {
        for {
            select {
            case <-ctx.Done():
                return
            case ch <- 42:
            }
        }
    }()
}
```

#### Race Conditions

A race condition occurs when multiple goroutines are writing to the same resource - similar to what happens with multiple threads. To prevent race conditions, locks, or mutex locks are used in golang.

```go
// Bad - Race condition
var counter int
go func() { counter++ }()
go func() { counter++ }()

// Good - Using mutex
var counter int
var mu sync.Mutex
go func() {
    mu.Lock()
    counter++
    mu.Unlock()
}()
```

### Channels

A channel is a communication mechanism that allows goroutines to share data with each other "safely". One can think of it as a pipe through which we send and receive data between goroutines.

```go
// Create a channel
ch := make(chan int)

// Send data through channel
go func() {
    ch <- 42  // Send value to channel
}()

// Receive data from channel
value := <-ch  // Receive value from channel
```

#### Types of channels

```go
// Unbuffered channel
ch1 := make(chan int)

// Buffered channel
ch2 := make(chan int, 5)

// Receive-only channel
ch3 := make(<-chan int)

// Send-only channel
ch4 := make(chan<- int)
```

#### Channel Patterns


