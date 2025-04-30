from collections import deque

class Fila:
    def __init__(self):
        self.items = deque() 


    def enfileirar(self, item):
        self.items.append(item) 

    def desenfileirar(self):
        if not self.esta_vazia():
            
            return self.items.popleft()
        raise IndexError("Fila vazia")

    def esta_vazia(self):
        return len(self.items) == 0

    def tamanho(self):
        return len(self.items)

    def frente(self):
        if not self.esta_vazia():
            return self.items[0]
        return None
