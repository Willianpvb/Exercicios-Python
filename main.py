''' 
         head(cabeça)    Segundo            Terceiro 
         |                |                  | 
         |                |                  | 
    +----+------+     +----+------+     +----+------+ 
    | 1  |  o-------->| 2  |  o-------->|  3 | None | 
    +----+------+     +----+------+     +----+------+  
'''
class Node:

    # Construtor 
    def __init__(self, inf):
        self.inf = inf # Informação
        self.next = None # Ponteiro para o próximo elemento
    
    def __repr__(self):
        return '%s -> %s' % (self.inf, self.next)

class LinkedList:

    def __init__(self):
        self.head = None #guarda o ínicio da lista

    def __repr__(self):
        return str(self.head)

    def vazia(self):
      return self.head==None
      
    def add_Inicio(self, data):
        new_node = Node(data)# Cria o novo Nó
        new_node.next = self.head# adiciona o nó no ínico
        self.head = new_node# atualiza o ínicio


    def add_Fim(self, data):
        #Cria o novo Nó
        new_node = Node(data)

        # verifica se a lista está vazia
        if self.head == None:
            self.head = new_node
            return
        
        #Faz uma cópia do início
        node_aux = self.head

        # percorre até o último elemento.
        #while node_aux.next:
        #ou
        #while node_aux.next!=None:
        while node_aux.next:
            node_aux = node_aux.next

        # Adiciona no fim!    
        node_aux.next = new_node

    # Inserir em uma determinada posição 
    def inserir_Posicao (self, index, data):
        if index == 1:#caso seja primeira posição, faz o processo de adicionar no ínicio
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        i = 1
        if index > self.tamanho() or index < 0:#confere se a posição é válida
            print("ERRO: Posição inválida")
            return
        node_aux = self.head#cria um nó auxiliar para percorrer a lista
        while i < index-1 and node_aux != None:#percorre a lista até uam posição anterior ao index
            node_aux = node_aux.next
            i = i + 1
        
       
        new_node = Node(data)#cria o novo nó
        new_node.next = node_aux.next #adiciona na posição index
        node_aux.next  = new_node 
    
    def tamanho(self):
        
        if self.head == None:
            return 0
        node_aux = self.head
        total = 0 #  contador
        # Loop para percorre a lista completa 
        while node_aux:
            total += 1
            node_aux = node_aux.next
        return total

    
    # buscar elemento de uma posição
    def get(self, index):
        if index >= self.length() or index < 0:
            print("ERRO: Posição inválida")
            return None
        cont  = 0
        node_aux = self.head
        while node_aux != None:
            if cont == index: 
                return node_aux.data
            node_aux  = node_aux.next
            cont += 1
    
    
    
    # verificar se um elemento possui na lista
    def verificarPossui(self, value):
        if self.head == None:
            print("Lista vazia")
            return
        node_aux = self.head
        while node_aux != None:
            if node_aux.inf == value:
                return True
            node_aux = node_aux.next
        return False


  
    def imprimir(self): 
        node_aux = self.head 
        # Lista vazia?
        if node_aux is None:
            print("lista Vazia!\n----------")
            return
        while node_aux: 
            print(node_aux.inf, end=" - > ")
            node_aux = node_aux.next
        print("\n----------") 

    
    def remover_Inicio(self):
        if self.head == None:
            print("Lista já vazia")
            return 
        self.head = self.head.next#atualiza o ínicio e assim remove o primeiro elemento
    
    
    def remover_Fim(self):
        if self.head is None:
            print("Lista Vazia")
            return
        node_aux = self.head #Nó para percorrer a lista
        ant=None #também para percorrer a lista sempre uma posição anterior a variável de cima
        while node_aux.next != None:
            ant=node_aux
            node_aux = node_aux.next
        ant.next=None#remove o último elemento
        #opcional
        node_aux=None

    
    def remover_por_valor(self, valor):
        node_aux = self.head  
        ant=None
        # verifica se o primeiro nó possui i valor a ser deletado
        if node_aux != None:  
            if node_aux.inf == valor:  
                self.head = node_aux.next
                node_aux = None
                return
        #percorre a lista procurando o valor
        while node_aux != None:  
            if node_aux.inf == valor:  
                break
            ant = node_aux  
            node_aux = node_aux.next
  
        # percorreu a lista toda e não achou o valor 
        if node_aux == None:  
            return
  
        # Remove o nó do valor
        ant.next = node_aux.next
        node_aux = None

	
# Test
my_list = LinkedList()
my_list.imprimir()
# Add the elements
my_list.add_Fim(3)
my_list.add_Fim(2)
my_list.add_Fim(7)
my_list.add_Fim(1)

my_list.imprimir()
print("Total de elementos: ", my_list.tamanho())
aux=7
if (my_list.verificarPossui(aux)):
  print("Valor 7 presente na lista!")
else:
  print("A lista não possui esse valor")
aux=77
if (my_list.verificarPossui(aux)):
  print("Valor ", aux," presente na lista!")
else:
  print("A lista não possui o valor ", aux)


my_list.remover_Inicio()
my_list.imprimir()

my_list.remover_Fim()
my_list.imprimir()

my_list.add_Inicio(1)
my_list.imprimir()

my_list.add_Fim(3)
my_list.imprimir()

my_list.inserir_Posicao(2, 88)
my_list.imprimir()

my_list.remover_por_valor(7)
my_list.imprimir()

