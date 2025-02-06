# Sliding Window Maximum

Was able to pinpoint that this will use deque
Implementation of deque was wrong
Got jumbled up in the implementation bit

Intution is to keep only the maximum element in front of queue
Whenever you come to a new element, remove all elements smaller than it, starting from the back of the queue
Whenever we move out of the window, pop the element that is out of the window by removing it from front of the queue
