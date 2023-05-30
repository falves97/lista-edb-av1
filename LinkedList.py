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

    def insertSort(self):
        for i in range(1, self.size):
            data_ele = self.get(i).data
            j = i - 1

            while j >= 0 and self.get(j).data > data_ele:
                self.get(j + 1).data = self.get(j).data
                j -= 1

            self.get(j + 1).data = data_ele

    def selectSort(self):
        for i in range(self.size - 1):
            data_ele = self.get(i).data
            menor = self.get(i + 1).data
            pos = i + 1

            for j in range(i + 2, self.size):
                if self.get(j).data < menor:
                    menor = self.get(j).data
                    pos = j

            if menor < data_ele:
                self.get(i).data = self.get(pos).data
                self.get(pos).data = data_ele

    def binarySearch(self, data, init=None, end=None):
        self.insertSort()

        if init is None:
            init = 0
        if end is None:
            end = self.size - 1

        if init > end:
            return None
        else:
            pos = int((end - init) / 2)
            data_resp = self.get(pos).data

            if data_resp == data:
                return pos
            elif data > data_resp:
                return self.binarySearch(data, pos + 1, end)
            else:
                return self.binarySearch(data, init, pos - 1)

    def show_list(self):
        if self._root is not None:

            node = self._root
            while True:
                print(f'{node.data} ', end='')
                if node.next is None:
                    break

                node = node.next

    def count_elements(self):
        node = self._root
        count = 0

        while node is not None:
            count += 1
            node = node.next

        return count

    def to_array(self):
        list = []
        if self._root is not None:

            node = self._root
            while True:
                list.append(node.data)
                if node.next is None:
                    break

                node = node.next
        return list

    def max_divide(self, a, b):
        while a % b == 0 and a != 0:
            a = int(a / b)

        return a

    def is_ugly(self, number):
        number = self.max_divide(number, 2)
        number = self.max_divide(number, 3)
        number = self.max_divide(number, 5)

        return number == 1

    def numeros_feios(self):
        list = []
        if self._root is not None:

            node = self._root
            while True:
                if self.is_ugly(node.data):
                    list.append(node.data)

                if node.next is None:
                    break

                node = node.next
        return list
