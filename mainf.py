class Node:

    # Constructor to create a new node 
    def __init__(self, data):
        self.inf = data # Pointer to data
        self.prox = None # Initialize next as null
    def __repr__(self):
        return '%s -> %s' % (self.inf, self.prox)


class Fila:
    
    def __init__(self):
        self.inicio = None
        self.final = None
        self.num_elements = 0
        
    def enqueue(self, value):
        novoNo = Node(value)
        if self.inicio is None:
            self.inicio = novoNo
            self.final = self.inicio
        else:
            self.final.prox = novoNo # Adiciona o novonó no último elemento 
            self.final = self.final.prox   # Atualiza o fim
        self.num_elements += 1
            
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.inicio.inf  # Copia o valor que será removio em uma variável local
        self.inicio = self.inicio.prox       # retira o elemento do inicio
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0
    def __repr__(self):
        return "[" + str(self.inicio) + "]"

f = Fila()
f.enqueue(10)
f.enqueue(20)
f.enqueue(30)
f.enqueue(40)
f.enqueue(50)
print(f)
print(f.dequeue())
print(f)