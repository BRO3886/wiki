
When approaching a system design interview, you’ll typically be asked to design a small part of a larger system—often a single feature or component. 

## Ask Questions!

The key is to start by breaking down the problem statement. Take the time to scope out the problem with the interviewer, clarifying the functionality and discussing the high-level design before diving into details.

## Clarify functional vs non-functional requirements

It’s important to distinguish between **functional** and **non-functional requirements**. For example, a functional requirement might be a rule like _“a user cannot like a tweet more than once.”_ On the other hand, non-functional requirements focus on system qualities, such as _scalability_ (e.g., how the system handles 100 million daily active users), _performance_ (e.g., ensuring low latency for user actions), and _availability_ (e.g., guaranteeing the system is up and running 99.9% of the time).

> A common mistake is jumping straight into the design without fully understanding the problem. Always take a step back, clarify the requirements, and think through the high-level approach before diving into the solution.

## Quick Calculations

When designing a system, estimating data volume is crucial—calculate the size of each data unit, such as an IP address or request count, and multiply it by the expected number of records to determine total storage needs. Projecting storage growth involves factoring in daily data generation and defining retention policies, like deleting data after 30 days, to manage long-term storage requirements. Analyzing read/write patterns helps identify whether the system is write-heavy (e.g., logging requests) or read-heavy (e.g., checking rate limits), which influences database and caching choices

