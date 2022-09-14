class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return '(%s, %s)' % (self.nome, self.idade)


class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.inf = data  # Pointer to data
        self.prox = None  # Initialize next as null

    def __repr__(self):
        return '%s -> %s' % (self.inf, self.prox)


class Fila:

    def __init__(self):
        self.inicio = None
        self.final = None
        self.num_elements = 0

    def enqueue(self, pessoa):
        novoNo = Node(pessoa)
        if self.inicio is None:
            self.inicio = novoNo
            self.final = self.inicio
            self.num_elements += 1
            return print(self.__repr__())

        else:
            if novoNo.inf.idade >= 60:
                node_ini = self.inicio.prox
                ant = None
                while node_ini.prox is not None:
                    print(">>>", node_ini.inf.idade)

                    if node_ini.prox.inf.idade < 60:
                        print("676",self.inicio.prox )
                        self.inicio = ant
                        self.inicio.prox = novoNo
                        self.final = node_ini.prox
                        self.num_elements += 1
                        return print(self.__repr__())
                    ant = node_ini
                    node_ini = node_ini.prox
            else:
                self.final.prox = novoNo  # Adiciona o novonó no último elemento
                self.final = self.final.prox  # Atualiza o fim
                self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.inicio.inf  # Copia o valor que será removio em uma variável local
        self.inicio = self.inicio.prox  # retira o elemento do inicio
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def __repr__(self):
        return "[" + str(self.inicio) + str(self.final) + "]"


f = Fila()
f.enqueue(Pessoa("tr", 10))
f.enqueue(Pessoa("rt", 20))
f.enqueue(Pessoa("uy", 60))
f.enqueue(Pessoa("hg", 40))
f.enqueue(Pessoa("gb", 67))
print(f)
print(f.dequeue())
print(f)
