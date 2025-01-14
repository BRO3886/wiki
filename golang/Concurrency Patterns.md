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

A thread is managed by the OS (kernel level) while a goroutine is managed by Go runtime (user level). The key differences are that goroutines are much smaller (starting at 2KB vs 1-2MB for threads) and are scheduled by Go's runtime scheduler rather than the OS scheduler, making them much cheaper to create and switch between compared to threads. Threads typically share memory and use locks while goroutines can also use channels for communication.

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

**Generator**

```go
func generator(ctx context.Context) <-chan int {
    ch := make(chan int)
    go func() {
        defer close(ch)
        for i := 0; ; i++ {
            select {
            case <-ctx.Done():
                return
            case ch <- i:
            }
        }
    }()
    return ch
}
```

**Fan out**

```go
func fanOut(ctx context.Context, ch <-chan int, workers int) []<-chan int {
    outputs := make([]<-chan int, workers)
    for i := 0; i < workers; i++ {
        outputs[i] = worker(ctx, ch)
    }
    return outputs
}

func worker(ctx context.Context, ch <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        defer close(out)
        for val := range ch {
            select {
            case <-ctx.Done():
                return
            case out <- process(val):
            }
        }
    }()
    return out
}
```

**Fan in**

```go
func fanIn(ctx context.Context, channels ...<-chan int) <-chan int {
    var wg sync.WaitGroup
    multiplexed := make(chan int)

    wg.Add(len(channels))
    for _, ch := range channels {
        go func(ch <-chan int) {
            defer wg.Done()
            for val := range ch {
                select {
                case <-ctx.Done():
                    return
                case multiplexed <- val:
                }
            }
        }(ch)
    }

    go func() {
        wg.Wait()
        close(multiplexed)
    }()

    return multiplexed
}
```

#### Common patterns

**Worker Pool**

```go
type WorkerPool struct {
    jobs    chan Job
    results chan Result
    workers int
}

func NewWorkerPool(workers int) *WorkerPool {
    return &WorkerPool{
        jobs:    make(chan Job),
        results: make(chan Result),
        workers: workers,
    }
}

func (p *WorkerPool) Start(ctx context.Context) {
    for i := 0; i < p.workers; i++ {
        go func() {
            for job := range p.jobs {
                select {
                case <-ctx.Done():
                    return
                case p.results <- job.Process():
                }
            }
        }()
    }
}
```

**Pipeline** (not very useful imo)

```go
type PipelineStage func(ctx context.Context, in <-chan int) <-chan int

func pipeline(ctx context.Context, source <-chan int, stages ...PipelineStage) <-chan int {
    current := source
    for _, stage := range stages {
        current = stage(ctx, current)
    }
    return current
}
```

### Error handling

Go comes with it's own set of niche issues. It does not have a typical try catch exception handling system because it treats error as a type. Goroutines bring in their own set of issues when used extensively.

**Panic recovery**

```go
func safeGoroutine(f func()) {
    go func() {
        defer func() {
            if r := recover(); r != nil {
                log.Printf("Recovered from panic: %v", r)
            }
        }()
        f()
    }()
}
```

**Using errgroups**

```go
func processRestaurants(ctx context.Context, restaurants []Restaurant) error {
    // Create a new errgroup with context
    g, ctx := errgroup.WithContext(ctx)
    
    // Process each restaurant concurrently
    for _, r := range restaurants {
        r := r // Create new variable for goroutine
        g.Go(func() error {
            // If any error occurs here, other goroutines will be canceled via context
            if err := processRestaurant(ctx, r); err != nil {
                return fmt.Errorf("failed to process restaurant %s: %w", r.Name, err)
            }
            return nil
        })
    }
    
    // Wait for all goroutines to complete and return first error if any
    return g.Wait()
}
```

### Best Practices

#### 1. Always Use Context

- For cancellation
- For timeouts
- For carrying request-scoped values

#### 2. Channel Guidelines

- Close channels from the sender side
- Document channel ownership
- Use directional channel types when possible

#### 3. Error Handling

- Use errgroup for concurrent error handling
- Always handle panic recovery in long-running goroutines
- Propagate errors through channels when needed

#### 4. Resource Management

- Always clean up resources (defer)
- Use WaitGroup for goroutine synchronization
- Set appropriate buffer sizes for channels

#### 5. Testing

- Use race detector (`go test -race`)
- Test concurrent code with different timing scenarios
- Use timeouts in tests

### Others

**Singleflight - For deduplicating concurrent calls**

```go
var g singleflight.Group

func GetData(key string) (interface{}, error) {
    v, err, _ := g.Do(key, func() (interface{}, error) {
        return fetchExpensiveData(key)
    })
    return v, err
}

```

**Context with timeout - to time out operations**

```go
func WithTimeout() {
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()
    
    done := make(chan struct{})
    go func() {
        // do work
        done <- struct{}{}
    }()
    
    select {
    case <-done:
        // work completed
    case <-ctx.Done():
        // timeout
    }
}
```