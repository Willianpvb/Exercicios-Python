from time import sleep


class Node:

    # Construtor
    def __init__(self, pessoa):
        self.pessoa = pessoa  # Informação
        self.next = None  # Ponteiro para o próximo elemento

    def __repr__(self):
        return '%s -> %s' % (self.pessoa, self.next)


class LinkedList:

    def __init__(self):
        self.head = None  # guarda o ínicio da lista

    def __repr__(self):
        return str(self.head)

    def vazia(self):
        return self.head is None

    def add_Inicio(self, pessoa):
        if self.verificarPossui(pessoa.getMatricula()) is True:
            return '\n<<<<<<Matricula Já Existente>>>>>\n'
        else:
            new_node = Node(pessoa)  # Cria o novo Nó
            new_node.next = self.head  # adiciona o nó no ínico
            self.head = new_node  # atualiza o ínicio
            return '\nCadastrado com sucesso!\n'

    def add_Fim(self, pessoa):
        if self.verificarPossui(pessoa.getMatricula()) is True:
            return '\n<<<<<<Matricula Já Existente>>>>>\n'
        else:
            # Cria o novo Nó
            new_node = Node(pessoa)

            # verifica se a lista está vazia
            if self.head is None:
                self.head = new_node
                return '\nCadastrado com sucesso!\n'

            # Faz uma cópia do início
            node_aux = self.head

            # percorre até o último elemento.
            # while node_aux.next:
            # ou
            # while node_aux.next!=None:
            while node_aux.next:
                node_aux = node_aux.next

            # Adiciona no fim!
            node_aux.next = new_node
            return '\nCadastrado com sucesso!\n'

    # Inserir em uma determinada posição
    def inserir_Posicao(self, index, pessoa):
        if self.verificarPossui(pessoa.getMatricula()) is True:
            return '\n<<<<<<Matricula Já Existente>>>>>\n'
        else:
            if index == 1:
                # caso seja primeira posição, faz o processo de adicionar no ínicio
                new_node = Node(pessoa)
                new_node.next = self.head
                self.head = new_node
                return '\nCadastrado com sucesso!\n'

            if index > self.tamanho() or index < 0:
                # confere se a posição é válida
                print("ERRO: Posição inválida")
                return
            i = 1
            node_aux = self.head
            # cria um nó auxiliar para percorrer a lista
            while i < index - 1 and node_aux is not None:
                # percorre a lista até uam posição anterior ao index
                node_aux = node_aux.next
                i = i + 1

            new_node = Node(pessoa)  # cria o novo nó
            new_node.next = node_aux.next  # adiciona na posição index
            node_aux.next = new_node
            return '\nCadastrado com sucesso!\n'

    def tamanho(self):
        if self.head is None:
            return 0
        node_aux = self.head
        total = 0  # contador
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
        cont = 0
        node_aux = self.head
        while node_aux is not None:
            if cont == index:
                return node_aux.data
            node_aux = node_aux.next
            cont += 1

    def get_Matri(self, matricula):
        if self.verificarPossui(matricula) is False:
            return "matricula não encontrada!"
        else:
            node_aux = self.head
            ant = None
            # percorre a lista procurando o valor
            while node_aux is not None:
                if node_aux.pessoa.getMatricula() == matricula:
                    return node_aux.pessoa.getNome()
                ant = node_aux
                node_aux = node_aux.next

    # verificar se um elemento possui na lista
    def verificarPossui(self, mat):
        if self.head is None:
            return
        node_aux = self.head
        while node_aux is not None:
            if node_aux.pessoa.getMatricula() == mat:
                return True
            node_aux = node_aux.next
        return False

    def imprimir(self):
        node_aux = self.head
        # Lista vazia?
        if node_aux is None:
            print("lista Vazia!\n")

        while node_aux:
            print(node_aux.pessoa.getMatricula(), '-', node_aux.pessoa.getNome(), end=" -> ")
            node_aux = node_aux.next

    def remover_Inicio(self):
        if self.head is None:
            return "\nLista já vazia!"
        self.head = self.head.next  # atualiza o ínicio e assim remove o primeiro elemento
        return "\nPrimeiro item excluido com sucesso!"

    def remover_Fim(self):
        if self.head is None:
            return "\nLista já vazia!"

        node_aux = self.head  # Nó para percorrer a lista

        if node_aux.next is None:
            self.head = None
            return "\nUltimo item excluido com sucesso!"

        ant = None  # também para percorrer a lista sempre uma posição anterior a variável de cima
        while node_aux.next is not None:
            ant = node_aux
            node_aux = node_aux.next
        ant.next = None  # remove o último elemento
        # opcional
        node_aux = None
        return "\nUltimo item excluido com sucesso!"

    def remover_por_matricula(self, valor):
        ret = ''
        if self.verificarPossui(valor) is False:
            return "matricula não encontrada!"
        else:
            node_aux = self.head
            ant = None
            # verifica se o primeiro nó possui i valor a ser deletado
            if node_aux is not None:
                if node_aux.pessoa.getMatricula() == valor:
                    ret = node_aux.pessoa
                    self.head = node_aux.next
                    node_aux = None
                    return ret.getNome() + "-" + str(ret.getMatricula()) + " excluido com sucesso"
            # percorre a lista procurando o valor
            while node_aux is not None:
                if node_aux.pessoa.getMatricula() == valor:
                    ret = node_aux.pessoa
                    break
                ant = node_aux
                node_aux = node_aux.next

            # Remove o nó do valor
            ant.next = node_aux.next
            node_aux = None
            return ret.getNome()+"-"+str(ret.getMatricula())+" excluido com sucesso"


class Pessoa:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __repr__(self):
        return ""

    def getMatricula(self):
        return self.matricula

    def getNome(self):
        return self.nome


Pessoas = LinkedList()


def m1():

    nome = input("Qual seu nome:")
    matricula = int(input("Qual sua matricula:"))
    p = Pessoa(nome, matricula)
    print(Pessoas.add_Inicio(p))


def m2():

    nome = input("Qual seu nome:").strip()
    matricula = int(input("Qual sua matricula:"))
    p = Pessoa(nome, matricula)
    print(Pessoas.add_Fim(p))


def m3():

    index = int(input("Em qual posição deseja ficar? 1 até {}".format(Pessoas.tamanho())))
    nome = input("Qual seu nome:").strip()
    matricula = int(input("Qual sua matricula:"))
    p = Pessoa(nome, matricula)
    print(Pessoas.inserir_Posicao(index, p))


def m4():
    Pessoas.imprimir()


def m5():

    matricula = int(input("Qual a matricula da Busca?"))
    print("A matricula está ligada ao nome <{}>".format(Pessoas.get_Matri(matricula)))


def m6():
    print("!{} pessoas na lista!".format(Pessoas.tamanho()))


def m7():
    print(Pessoas.remover_Inicio())


def m8():
    print(Pessoas.remover_Fim())


def m9():

    matricula = int(input("Qual matricula deseja remover?"))
    print(Pessoas.remover_por_matricula(matricula))


def menu():
    game = True
    while game:
        print(f"\n____________________________\n"
              f"----------- Menu -----------\n"
              f"1 - Adicionar no INÍCIO\n"
              f"2 - Adicionar no FIM\n"
              f"3 - Adicionar em uma posição\n"
              f"4 - Imprimir Lista\n"
              f"5 - Buscar pela matricula\n"
              f"6 - Tamanho da Lista\n"
              f"7 - Remover no INÍCIO\n"
              f"8 - Remover no Fim\n"
              f"9 - Remover por Matricula\n"
              f"0 - Encerrar Execução\n"
              f"Para cada ação seu respectivo número\n"
              f"Adicione o número da ação escolhida abaixo:"
              )
        action = input("Aqui:")

        # acoes - o que vai acontecer
        if action == '1':
            m1()

        elif action == '2':
            m2()

        elif action == '3':
            m3()

        elif action == '4':
            m4()

        elif action == '5':
            m5()

        elif action == '6':
            m6()

        elif action == '7':
            m7()

        elif action == '8':
            m8()

        elif action == '9':
            m9()

        elif action == '0':
            game = False
        else:
            print("Opção Invalída! Tente NOVAMENTE!!!")
            sleep(2)


menu()
