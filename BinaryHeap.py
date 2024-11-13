import math

class BinaryHeap:
    def __init__(self, max_size):
        self.__values = [0] * (max_size + 1)  # índice 0 é ignorado para simplificar o cálculo de índices
        self.__max_size = max_size
        self.__size = 0
        
        
    def __str__(self):
        return f"{self.__values[1:]}"
    
    def get_size(self):
        return len(self.__values)
        
    def heapify_up(self, index): 
        parent_index = index // 2
        
        if parent_index >= 1:
            if self.__values[index] > self.__values[parent_index]:
                self.__values[index], self.__values[parent_index] = self.__values[parent_index], self.__values[index]
                index = parent_index
                self.heapify_up(index)
                
    def heapify_down(self, index):
        next_node = 2 * index
        if next_node < self.get_size():
            # Verifica se há um filho direito e encontra o maior dos dois filhos
            if next_node + 1 < self.get_size() and self.__values[next_node + 1] > self.__values[next_node]:
                next_node = next_node + 1
            if self.__values[index] < self.__values[next_node]:
                self.__values[index], self.__values[next_node] = self.__values[next_node], self.__values[index]
                self.heapify_down(next_node)
                
    def insert(self, new_value):
        if self.__size < self.__max_size:
            self.__size += 1
            self.__values[self.__size] = new_value  # Insere o novo valor na última posição
            self.heapify_up(self.__size)  # Reorganiza a heap para manter a propriedade de heap
        else:
            print("Overflow: Heap atingiu a capacidade máxima")
            
    def remove(self):
        if self.__size != 0:
            # Remover o maior elemento (topo da heap)
            max_value = self.__values[1]
            # Substituir o topo pelo último elemento
            self.__values[1] = self.__values[self.__size]
            self.__values = self.__values[:self.__size]
            self.__size -= 1
            self.heapify_down(1)
            return max_value
        else:
            print("Heap vazia")
            return None
        
    def change_priority(self, index, new_priority):
        if index < 1 or index > self.__size:
            print("Índice fora do limite")
            return
        
        old_priority = self.__values[index]
        self.__values[index] = new_priority
        
        if new_priority > old_priority:
            self.heapify_up(index)
        elif new_priority < old_priority:
            self.heapify_down(index)
            
    def get_high_priority(self):
        if self.__size > 0:
            return self.__values[1]
        else:
            print("Heap está vazio")
            return None

    def heap_sort(self):
        original_size = self.__size
        
        for i in range(self.__size, 1, -1):
            # Move a raiz (maior elemento) para o final da lista não ordenada
            self.__values[1], self.__values[i] = self.__values[i], self.__values[1]
            # Diminui o tamanho do heap para excluir o maior elemento da próxima iteração
            self.__size -= 1
            self.heapify_down(1)
        
        self.__size = original_size
        return self.__values[1:]

    def height(self):
        """Calcula a altura do heap."""
        return (self.__size).bit_length() - 1 if self.__size > 0 else 0

    def print_level(self, start_index, end_index, level):
        """Exibe os valores de cada nível com o espaçamento correto."""
        # Define os espaçamentos entre os nós
        spacing = " " * (2 ** (self.height() - level))
        between_spacing = " " * (2 ** max(self.height() - level - 1, 0))
        
        for i in range(start_index, end_index):
            if i <= self.__size:
                print(f"{spacing}{self.__values[i]}", end="")
                if i < end_index - 1:
                    print(f"{between_spacing}", end="")
        print()
        
    def display_heap(self):
        """Exibe a árvore binária de forma hierárquica com indentação."""
        level = 0
        start_index = 1
        while start_index <= self.__size:
            end_index = min(start_index * 2, self.__size + 1)
            self.print_level(start_index, end_index, level)
            level += 1
            start_index = end_index