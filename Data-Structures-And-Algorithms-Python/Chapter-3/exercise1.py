# Implementing a pop method for a Singly linked list

# Given the base code we have seen until now and that is also provided, implement a pop method

# The pop method will remove the last element from the list and return the data it contains. If the list is empty it should return None

# This is a little bit trickier than the insert, as the method should take into account different cases:
#   List is empty, list has only one node and then the rest of cases.
#   The method should also locate the second to last node, to change its "next" pointer.

# To actually remove a variable (like a node), remember you can use the del statement:
# del variable


class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"<ListNode: {self.data}>"


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def __repr__(self):
        current_node = self._head
        values = ""
        while current_node:
            values += f", {current_node.data}"
            current_node = current_node.next
        return f'<SinglyLinkedList: [{values.lstrip(", ")}]>'

    def append(self, value):
        """
        Append a value to the end of the list

        Parameters:
        - 'value': The data to append

        Returns: None
        """
        # Create the node with the value
        node = ListNode(value)
        # If list is empty just point the header to the new node
        if not self._head:
            self._head = node
        else:
            # if list is not empty, search for the last element and point it to the new node
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node

    def pop(self):
        current_node = self._head

        if current_node == None:
            return None
        elif self._head.next == None:
            value = self._head.data
            self._head = None
            return value
        else:
            previous_node = None
            while current_node.next != None:
                previous_node = current_node
                current_node = current_node.next
            value = current_node.data
            previous_node.next = None
            del current_node
            return value
