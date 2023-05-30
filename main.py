import random

from CpfTad import CpfTad
from LinkedList import LinkedList
from utils import list2Matrix, main_diagonal, sec_diagonal, count_impares, pares, fibonacci, list_fibonacci

# cpf = CpfTad()
# cpfString = '06988129307'
# cpf.lerCpf(cpfString)
# print(cpf.cpf)
# print("É um CPF válido: ", cpf.isCpfValido())
#
# ll = LinkedList()
# for num in cpfString:
#     ll.add(num)
#
# ll.show_list()
# print(f'size: {ll.size}')
# ll.delete('6')
#
# ll.show_list()
# print(f'size: {ll.size}')
#
# ll.insert(0, '4')
# ll.show_list()
# print(f'size: {ll.size}')
#
# ll.deleteByIndex(10)
# ll.show_list()
# print(f'size: {ll.size}')
# print(f'valor do node 1: {ll.get(1).data}')

# Teste matriz de inteiros
# ll = LinkedList()
# for i in range(10, 0, -1):
#     ll.add(i)
#
# ll.show_list()
# print()
# matrix = list2Matrix(ll, 3)
#
# print(f'Matriz: {matrix}')
# print(main_diagonal(matrix))
# print(sec_diagonal(matrix))
# print(f'Quantidade de ímpares: {count_impares(ll)}')
# print(f'Quantidade de elementos: {ll.count_elements()}')
# print(f'Todos os pares: {pares(ll)}')
# ll.selectSort()
# ll.show_list()
# print()
# print(f'position de 2: {ll.binarySearch(2)}')
list = LinkedList()
# list_fibonacci(list, 6)
for i in range(16):
    list.add(i)

print(list.numeros_feios())
