from collections import deque

class MyQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("cannot dequeue from empty queue") # i am not sure whether i can or cannot raise an indexError
        return self.queue.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("cannot front from empty queue")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0