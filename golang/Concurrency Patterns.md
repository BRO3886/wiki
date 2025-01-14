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

### Goroutines vs Threads

A goroutine is a lightweight, user-space thread managed by the Go runtime, while an OS thread is a kernel-space thread managed by the operating system. 

The key differences are that goroutines are much smaller (starting at 2KB vs 1-2MB for threads) and are scheduled by Go's runtime scheduler rather than the OS scheduler, making them much cheaper to create and switch between compared to threads. Threads typically share memory and use locks while goroutines can also use channels for communication.

### Goroutine Leaks

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

