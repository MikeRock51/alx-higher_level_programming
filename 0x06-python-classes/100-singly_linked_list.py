#!/usr/bin/python3


class Node():
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes a node and it's next field"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data"""
        return (self.__data)

    @property
    def next_node(self):
        """Retrieves the next node"""
        return (self.__next_node)

    @data.setter
    def data(self, value):
        """Sets the value of data"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node"""
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """Initializes an empty list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node to the list in a sorted position
        Args:
            value: The value to be added to the list
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            new_node.next_node = None
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Makes the list printable."""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
