import importlib.util
import sys

# Define the absolute path to the file to import
target_file = "/BA-IT-Projects/Data-Structures-And-Algorithms-Python/Chapter-3/exercise5.py"

spec = importlib.util.spec_from_file_location("exercise5", target_file)
exercise5 = importlib.util.module_from_spec(spec)
sys.modules["exercise5"] = exercise5
spec.loader.exec_module(exercise5)
ListNode = exercise5.ListNode
DoublyLinkedList = exercise5.DoublyLinkedList


class Queue():
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def __repr__(self):
        current_node = self._head
        values = ""
        while current_node:
            values += f", {current_node.data}"
            current_node = current_node.next
        plural = "" if self._size == 1 else "s"
        return f'<Queue ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def enqueue(self, data):
        new_node = ListNode(data)
        if self._head == None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def dequeue(self):
        if not self._size:
            return None

        node_to_remove = self._tail

        if node_to_remove == self._head:
            self._tail = None
            self._head = None
        else:
            previous_node = node_to_remove.prev
            previous_node.next = None
            self._tail = previous_node

        self._size -= 1
        value = node_to_remove.data
        del node_to_remove
        return value
