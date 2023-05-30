from LinkedList import LinkedList


def list2Matrix(list, len):
    if not isinstance(list, LinkedList):
        return None

    matrix = []
    for i in range(len):
        matrix.append([])
        for j in range(len):
            pos = i * len + j
            if pos < list.size:
                matrix[i].append(list.get(pos).data)
            else:
                matrix[i].append(0)

    return matrix


def main_diagonal(matrix):
    diagonal = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                diagonal.append(matrix[i][j])
    return diagonal


def sec_diagonal(matrix):
    diagonal = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i + j == len(matrix) - 1:
                diagonal.append(matrix[i][j])
    return diagonal


def count_impares(list):
    count = 0
    for i in range(list.size):
        if list.get(i).data % 2 == 1:
            count += 1

    return count


def pares(list):
    pares = []
    for i in range(list.size):
        if list.get(i).data % 2 == 0:
            pares.append(list.get(i).data)

    return pares


def fibonacci(limit=0):
    if limit <= 1:
        return 1
    else:
        return fibonacci(limit - 1) + fibonacci(limit - 2)


def list_fibonacci(list, limit):
    for i in range(limit):
        list.add(fibonacci(i))
