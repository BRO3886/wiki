
### Clarifying Functional Requirements

1. **Is this for a backend API?**
    
    - Is the rate limiter intended to protect a backend API, or is it for a different use case? Understanding the context will help define the scope and constraints.
        
2. **Is this for a single microservice or a distributed system?**
    
    - Will the rate limiter be used within a single microservice, or does it need to work across multiple services in a distributed environment? This will impact the design, especially in terms of consistency and scalability.
        
3. **What is the basic working of the rate limiter?**
    
    - Should it limit requests based on user ID, IP address, API keys, or other identifiers? What are the rules for throttling (e.g., X requests per second)?
        
4. **Why does it need to be generic?**
    
    - Should the rate limiter be reusable across different services or use cases? If so, it needs to be flexible enough to accommodate varying rules and configurations without requiring significant changes.
        

### Clarifying Non-Functional Requirements

1. **Why is latency important?**
    
    - The rate limiter should introduce minimal latency to avoid degrading the user experience. For example, if the rate limiter takes too long to process a request, it could slow down the entire system.
        
2. **Why is throughput important?**
    
    - The system must handle a high volume of requests efficiently, especially in scenarios with millions of users or API calls. The rate limiter should not become a bottleneck.
        
3. **What about storage requirements?**
    
    - Storage is needed for rules (e.g., rate limits per user or IP) and potentially for business logic (e.g., storing IP addresses or request counts). However, storage is not the primary focus unless it becomes a scalability concern.
        
4. **Why is availability critical?**
    
    - The rate limiter should be highly available. If it fails, it should fail open (i.e., allow requests to pass through) to ensure users can still access the system as if the rate limiter didn’t exist. This prevents the rate limiter from becoming a single point of failure.

