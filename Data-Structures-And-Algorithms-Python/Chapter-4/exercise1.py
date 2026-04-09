class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack

        Parameters:
        - 'data': Data/value being added

        Returns: None
        """

        # YOUR CODE HERE. Remove the next line if necessary
        new_node = Node(data, next = None)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
        

    def pop(self):
        """
        Remove the top node from the stack and return its content

        Parameters: None

        Returns: The content of the node or None if stack is empty
        """

        # YOUR CODE HERE. Remove the next line if necessary
        if not self._size:
          return None
        
        value = self._top.data
        node_to_remove = self._top
        self._top = self._top.next
        del node_to_remove
        self._size -= 1
        return value
        
        

    def __repr__(self):
        # YOUR CODE HERE. Remove the next line if necessary
        current_node = self._top
        values = []
        while current_node:
            values.append(current_node.data)
            current_node = current_node.next
        return f'<Stack ({self._size} {'element' if self._size == 1 else 'elements'}): [{", ".join(values)}]>'