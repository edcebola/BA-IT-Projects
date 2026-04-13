from exercise1 import Stack


class StackBasedQueue():
    def __init__(self):
        # YOUR CODE HERE
        self._size = 0
        self._InboundStack = Stack()
        self._OutboundStack = Stack()

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack]
        values.extend([c for c in self._OutboundStack][::-1])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        # YOUR CODE HERE
        self._InboundStack.push(data)
        self._size += 1

    def dequeue(self):
        # YOUR CODE HERE
        if self._size == 0:
            return None
        if len(self._OutboundStack) == 0:
            while len(self._InboundStack) != 0:
                value = self._InboundStack.pop()
                self._OutboundStack.push(value)
        value = self._OutboundStack.pop()
        self._size -= 1
        return value
