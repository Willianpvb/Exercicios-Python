class Ouvidoria:
            def __init__(self, n, op):
                    self.n = n
                    self.op = op
                    # eu usaria o switch case
                    if (self.op == 1):
                            #eu criaria uma função para as duas proximas linhas def add_Reclamaçao(self, reclamaçao):
                            listaR = []
                            listaR.append(self.n)
                            print("guardado")
                    elif (self.op == 2):
                            #eu criaria uma função para as duas proximas linhas def add_elogio(self, elogio):
                            listaE = []
                            listaE.append(self.n)
                    elif (self.op == 3):
                            #eu criaria uma função para as duas proximas linhas : def add_Mensagem(self, mensagem):
                            listaM = []
                            listaM.append(self.n)
                    else:
                            print("Saiu")

		
op = int(input("Digite algo: "))
n = input("Digite a ocorrencia: ")

s1 = Ouvidoria(n)
s1.recebeComentario(op)
