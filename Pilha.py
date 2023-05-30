from Node import Node


class Fila:
    def __init__(self):
        self._root = None
        self._size = 0

    @property
    def size(self):
        return self._size

    def insert(self, data):
        new_node = Node(data)
        self._size += 1

        if self._root is not None:
            new_node.next = self._root

        self._root = new_node

    def get(self):
        return self._root

    def remove(self):
        if self._root is not None:
            self._root = self._root.next
            self._size -= 1

    def show(self):
        if self._root is not None:

            node = self._root
            while True:
                print(f'{node.data} ', end='')
                if node.next is None:
                    break

                node = node.next
