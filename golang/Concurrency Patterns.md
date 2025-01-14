## What is concurrency

Concurrency is the ability to handle multiple tasks at the same time by switching between them. Tasks can start, run and complete in overlapping time periods. 

One can think of it as working in the kitchen:
- While waiting for the water to boil, you can chop vegetables
- While the vegetables cook, one can prepare the dough

Here, we switch between the tasks, but only do one at a time.



In golang it is handled through:
- Goroutines (lightweight threads)
- Channels (communication between goroutines)
- Synchronization primitives (mutexes, wait groups)

