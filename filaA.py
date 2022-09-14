# Fila com array
class Fila:
    def __init__(self):
        self.storage = []

    def size(self):
        return len(self.storage)

    def enqueue(self, item):
        self.storage.append(item)

    def dequeue(self):
        return self.storage.pop(0)

    def __repr__(self):
        return str(self.storage)


# Setup
f = Fila()
f.enqueue(10)
f.enqueue(20)
f.enqueue(30)
f.enqueue(40)
f.enqueue(50)
print(f)
print(f.dequeue())
print(f.dequeue())
print(f)
