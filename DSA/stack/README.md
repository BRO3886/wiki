# Stack

## Basic Stack
Basic implementation in python - push/pop/peek

```python
class Stack:
	def __init__(self):
		self._st = []

	def push(self, item):
		self._st.append(item)

	def pop(self):
		if not self.isempty():
			return self._st.pop()
		raise IndexError("stack is empty")

	def isempty(self):
		return len(self._st) == 0


	def peek(self):
		if not self.isempty():
			return self._st[-1]
		raise IndexError("stack is empty")

	def length(self):
		return len(self._st)
```


## Queue using two stacks
1 queue is for enqueue, other for dequeue

```python
class Queue:
	def __init__(self):
		self.st1 = []
		self.st2 = []

	def enqueue(self, item):
		self.st1.append(item)

	def dequeue(self):
		if not self.st2:
			while self.st1:
				self.st2.append(self.st1.pop())

		if self.st2:
			return self.st2.pop()

		raise IndexError("empty queue")

	def peek(self):
		if not self.st2:
			while self.st1:
				self.st2.append(self.st1.pop())
		if self.st2:
			return self.st2[-1]
		raise IndexError("empty queue")

	def isempty(self):
		return len(self.st1) == 0 and len(self.st2) == 0
```

## Monotonic Stack

keep elements in either increasing or decreasing order

```python
class MonotonicStack:
	def __init__(self):
		self.st = []

	def push(self, item):
		while self.st and self.st[-1] < item:
			self.st.pop()
		self.st.append(item)

	def display(self):
		print(self.st)
```

