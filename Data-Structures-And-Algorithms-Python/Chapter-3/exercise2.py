# Implementing pop method for a Singly linked list with tail

# Now the singly linked list has two pointers: a head pointer and a tail pointer.
# Some things are easier and faster this way. In this exercise you will implement again a pop method to the SinglyLinkedList class.

# The pop methods will remove the last element/node from the list and return its value.
# Same as before, if the list is empty, it should return None. The method will update the head and tail properties accordingly.

# To actually remove a variable (like a node), remember you can use the del statement:

# del(variable)


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"<ListNode: {self.data}>"


class SinglyLinkedList:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ""
        while current_node:
            values += f", {current_node.data}"
            current_node = current_node.next
        plural = "" if self._size == 1 else "s"
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        new_node = ListNode(value)

        # If list is empty just point the header to the new node
        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            # if list is not empty, update the last element and point it to the new node
            self._tail.next = new_node
            self._tail = new_node

        # Update list's size
        self._size += 1

    def pop(self):
        current_node = self._head

        if current_node == None:
            return None
        elif self._head.next == None:
            value = self._head.data
            self._head = None
            self._tail = None
            self._size = 0
            return value
        else:
            previous_node = None
            while current_node.next != None:
                previous_node = current_node
                current_node = current_node.next
            value = current_node.data
            previous_node.next = None
            del current_node
            self._tail = previous_node
            self._size -= 1
            return value
