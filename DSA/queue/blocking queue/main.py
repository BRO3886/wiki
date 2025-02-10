import random
from threading import Condition, Thread
from collections import deque
import time


class BoundedBlockingQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = deque(maxlen=self.capacity)
        self.cond = Condition()

        self.isFull = False

    def enqueue(self, element):
        with self.cond:
            while self.isFull:
                self.cond.wait()

            self.queue.append(element)
            if len(self.queue) >= self.capacity:
                self.isFull = True
            else:
                self.isFull = False

            self.cond.notify()

    def dequeue(self):
        with self.cond:
            while not self.queue:
                self.cond.wait()

            element = self.queue.popleft()
            if len(self.queue) < self.capacity:
                self.isFull = False
            else:
                self.isFull = True

            self.cond.notify()
            return element

    def size(self):
        with self.cond:
            return len(self.queue)


bq = BoundedBlockingQueue(10)
done = False

print("press enter to quit")


def rm():
    while not done:
        item = bq.dequeue()
        print(f"Consumed: {item}, Queue size: {bq.size()}")
        time.sleep(2)


def incr():
    while not done:
        item = random.randint(0, 100)
        bq.enqueue(item)
        print(f"Produced: {item}, Queue size: {bq.size()}")
        time.sleep(1)


producer = Thread(target=incr, args={}, daemon=True)
consumer = Thread(target=rm, args={}, daemon=True)
producer.start()
consumer.start()

input()
done = True
