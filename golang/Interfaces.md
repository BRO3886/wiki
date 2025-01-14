## What are interfaces?

An interface in Go is a type that defines a set of method signatures but doesn't provide implementations. It specifies behavior by declaring methods that a type must implement. Interfaces provide a way to specify the behavior of an object: if something can do this, then it can be used here.

## Key Characteristics

1. **Implicit Implementation**: In Go, interfaces are implemented implicitly. Types implement interfaces by implementing their methods, without explicitly declaring the implementation.
2. **Type Safety**: Go provides type safety through interfaces while maintaining flexibility. The compiler ensures that types satisfy the interfaces they're used with.
3. **Small Interfaces**: Go encourages small, focused interfaces. The standard library's `io.Reader` and `io.Writer` are prime examples of this philosophy.

Go's interfaces let you use [duck typing](http://en.wikipedia.org/wiki/Duck_typing) like you would in a purely dynamic language like Python but still have the compiler catch obvious mistakes like passing an `int` where an object with a `Read` method was expected, or like calling the `Read` method with the wrong number of arguments. To use interfaces, first define the interface type (say, `ReadCloser`):

```go
type ReadCloser interface {
    Read(b []byte) (n int, err os.Error)
    Close()
}
```

and then define your new function as taking a `ReadCloser`. For example, this function calls `Read` repeatedly to get all the data that was requested and then calls `Close`:

```go
func ReadAndClose(r ReadCloser, buf []byte) (n int, err os.Error) {
    for len(buf) > 0 && err == nil {
        var nr int
        nr, err = r.Read(buf)
        n += nr
        buf = buf[nr:]
    }
    r.Close()
    return
}
```

The code that calls `ReadAndClose` can pass a value of any type as long as it has `Read` and `Close` methods with the right signatures. And, unlike in languages like Python, if you pass a value with the wrong type, you get an error at compile time, not run time.

Source - https://research.swtch.com/interfaces

## Best Practices

### 1. Interface Segregation

Split large interfaces into smaller, more focused ones. This makes them more reusable and easier to implement.

```go
type Reader interface {
    Read(p []byte) (n int, err error)
}

type Writer interface {
    Write(p []byte) (n int, err error)
}

type ReadWriter interface {
    Reader
    Writer
}
```

### 2. Accept Interfaces, Return Structs

This principle provides flexibility to callers while maintaining control over the implementation details:

```go
type RedisCache struct{}

// Extra methods beyond Cache interface
func (r *RedisCache) FlushDB() error { ... }
func (r *RedisCache) Info() (*RedisInfo, error) { ... }
---

redisCache := NewRedisCache()

// Caller can choose to use it as interface if needed
var cache Cache = redisCache

// Or use full concrete type capabilities
redisCache.FlushDB()
```

### 3. Use Embedding for Interface Composition

Compose larger interfaces from smaller ones when needed

```go
type Cache interface {
    Getter
    Setter
    Deleter
}
```

### 4. Document Interface Behavior

Always document the expected behavior of interface methods, including:

- Expected parameter ranges
- Error conditions
- Concurrency guarantees
- State mutations

```go
// RateLimiter limits the rate of operations.
// All methods must be safe for concurrent use.
type RateLimiter interface {
    // Allow returns true if the operation should be allowed.
    // It blocks until the operation is allowed or ctx is cancelled.
    Allow(ctx context.Context) bool
    
    // Reset resets the rate limiter state.
    Reset()
}
```

