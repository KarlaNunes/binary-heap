from BinaryHeap import BinaryHeap

"""
Conjunto 1: Dados Aleatórios Pequenos
Dados de Construção: [10, 5, 20, 1, 15, 30, 25]
"""
# print("=== Construção do Heap ===")
# initial_values = [10, 5, 20, 1, 15, 30, 25]
# max_size = 10
# heap = BinaryHeap(max_size)

# for value in initial_values:
#     heap.insert(value)
#     print(f"Inserido {value}")

# heap.display_heap()

# # # 2. Alteração de Prioridade
# print("\n=== Alteração de Prioridade ===")
# print("Alterando prioridade do índice 3 para 50")
# heap.change_priority(3, 50)
# heap.display_heap()

# print("Alterando prioridade do índice 1 para 8")
# heap.change_priority(1, 8)
# heap.display_heap()

# # # 3. Remoções
# print("\n=== Remoções Consecutivas ===")
# for _ in range(3):
#     removed = heap.remove()
#     print(f"Removido {removed}: \n")
#     heap.display_heap()

# # # 4. Heapsort
# print("\n=== Heapsort ===")
# sorted_elements = heap.heap_sort()
# print(f"Elementos ordenados: {sorted_elements}")

# # # 5. Seleção da Alta Prioridade
# print("\n=== Alta Prioridade ===")
# if sorted_elements:
#     print(f"Elemento de alta prioridade: {sorted_elements[0]}")
# else:
#     print("Heap está vazio!")
    
"""
Conjunto 2: Sequência Crescente
Dados de Construção: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
# print("=== Construção do Heap ===")
# ascending_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# max_size = 10
# heap = BinaryHeap(max_size)

# for value in ascending_values:
#     heap.insert(value)
#     print(f"Inserido {value}")
#     heap.display_heap()

# # # 2. Alteração de Prioridade
# print("\n=== Alteração de Prioridade ===")
# print("Alterando prioridade do índice 4 para 15")
# heap.change_priority(4, 15)
# heap.display_heap()

# print("Alterando prioridade do índice 8 para 3")
# heap.change_priority(8, 3)
# heap.display_heap()

# # # 3. Remoções Consecutivas
# print("\n=== Remoções Consecutivas ===")
# for _ in range(5):
#     removed = heap.remove()
#     print(f"Removido {removed}:")
#     heap.display_heap()

# # # 4. Heapsort
# print("\n=== Heapsort ===")
# sorted_elements = heap.heap_sort()
# print(f"Elementos ordenados: {sorted_elements}")

# # # 5. Seleção da Alta Prioridade
# print("\n=== Alta Prioridade ===")
# high_priority = heap.get_high_priority()
# if high_priority is not None:
#     print(f"Elemento de alta prioridade: {high_priority}")
# else:
#     print("Heap está vazio!")

"""
Conjunto 3: Sequência Decrescente
Dados de Construção: [50, 40, 30, 20, 10, 5, 3]
"""

# print("=== Construção do Heap ===")
# descending_values = [50, 40, 30, 20, 10, 5, 3]
# max_size = 10
# heap = BinaryHeap(max_size)

# # 1. Construção do Heap
# for value in descending_values:
#     heap.insert(value)
#     print(f"Inserido {value}")
#     heap.display_heap()

# # 2. Alteração de Prioridade
# print("\n=== Alteração de Prioridade ===")
# print("Alterando prioridade do índice 2 para 60")
# heap.change_priority(2, 60)
# heap.display_heap()

# print("Alterando prioridade do índice 5 para 1")
# heap.change_priority(5, 1)
# heap.display_heap()

# # # 3. Remoções Consecutivas
# print("\n=== Remoções Consecutivas ===")
# for _ in range(3):
#     removed = heap.remove()
#     print(f"Removido {removed}:")
#     heap.display_heap()

# # # 4. Heapsort
# print("\n=== Heapsort ===")
# sorted_elements = heap.heap_sort()
# print(f"Elementos ordenados: {sorted_elements}")

# # # 5. Seleção da Alta Prioridade
# print("\n=== Alta Prioridade ===")
# high_priority = heap.get_high_priority()
# if high_priority is not None:
#     print(f"Elemento de alta prioridade: {high_priority}")
# else:
#     print("Heap está vazio!")
"""
Conjunto 4: Dados Aleatórios Maiores
Dados de Construção: [13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18]
"""

print("=== Construção do Heap ===")
random_large_values = [13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18]
max_size = 15
heap = BinaryHeap(max_size)

# 1. Construção do Heap
for value in random_large_values:
    heap.insert(value)
    print(f"Inserido {value}")
    heap.display_heap()

# 2. Alteração de Prioridade
print("\n=== Alteração de Prioridade ===")
print("Alterando prioridade do índice 7 para 35")
heap.change_priority(7, 35)
heap.display_heap()

print("Alterando prioridade do índice 10 para 12")
heap.change_priority(10, 12)
heap.display_heap()

# # 3. Remoções Consecutivas
print("\n=== Remoções Consecutivas ===")
for _ in range(4):
    removed = heap.remove()
    print(f"Removido {removed}:")
    heap.display_heap()

# # 4. Heapsort
print("\n=== Heapsort ===")
sorted_elements = heap.heap_sort()
print(f"Elementos ordenados: {sorted_elements}")

# # 5. Seleção da Alta Prioridade
print("\n=== Alta Prioridade ===")
high_priority = heap.get_high_priority()
if high_priority is not None:
    print(f"Elemento de alta prioridade: {high_priority}")
else:
    print("Heap está vazio!")


