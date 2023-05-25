from Node import Node


class LinkedList:
    def __init__(self):
        self._root = None
        self._size = 0

    @property
    def size(self):
        return self._size

    def get(self, index):
        if index < 0 or index >= self._size or self._size == 0:
            return

        node = self._root
        for i in range(index):
            node = node.next

        return node

    def add(self, data):
        new_node = Node(data)
        self._size += 1

        if self._root is None:
            self._root = new_node
            return

        node = self._root
        while node.next is not None:
            node = node.next

        node.next = new_node

    def insert(self, index, data):
        if index < 0 or index > self._size:
            return

        previous = None
        node = self._root
        for i in range(index):
            previous = node
            node = node.next

        new_node = Node(data)
        new_node.next = node

        if previous is not None:
            previous.next = new_node
        else:
            self._root = new_node

        self._size += 1

    def deleteByIndex(self, index):
        if index < 0 or index >= self._size or self._size == 0:
            return

        previous = None
        current = None
        next_node = self._root
        for i in range(index + 1):
            previous = current
            current = next_node
            next_node = next_node.next

        if previous is not None:
            previous.next = next_node
        else:
            self._root = next_node

        current.next = None

        self._size -= 1

    def delete(self, data):
        if self._root is None:
            return None

        prevNode = None
        currentNode = self._root

        while True:
            if currentNode is None:
                break

            if currentNode.data == data:
                if currentNode == self._root:
                    self._root = self._root.next
                else:
                    prevNode.next = currentNode.next
                    currentNode.next = None

                self._size -= 1
                break

            prevNode = currentNode
            currentNode = currentNode.next

    def show_list(self):
        if self._root is not None:

            node = self._root
            while True:
                print(f'{node.data} ', end='')
                if node.next is None:
                    break

                node = node.next
