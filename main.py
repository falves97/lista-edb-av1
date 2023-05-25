from CpfTad import CpfTad
from LinkedList import LinkedList
from Node import Node

# cpf = CpfTad()
cpfString = '06988129308'
# cpf.lerCpf(cpfString)
# print(cpf.cpf)
# print("É um CPF válido: ", cpf.isCpfValido())

ll = LinkedList()
for num in cpfString:
    ll.add(num)

ll.show_list()
print(f'size: {ll.size}')
ll.delete('6')

ll.show_list()
print(f'size: {ll.size}')

ll.insert(0, '4')
ll.show_list()
print(f'size: {ll.size}')

ll.deleteByIndex(10)
ll.show_list()
print(f'size: {ll.size}')
print(f'valor do node 1: {ll.get(1).data}')
