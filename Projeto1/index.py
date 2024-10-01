# PRIMEIRO TRABALHO PRÁTICO - ESTRUTURAS DE DADOS
# LANDERSON EVANGELISTA MIRANDA
# versão do python: 3.11.4
class No:
    def __init__(self, x):
        self.chave = x
        self.prox = None
        self.Ordem = None


class Lista:
    def __init__(self):
        self.prim = None

    def Consulta(self, x):
        p = self.prim
        while (p != None) and (p.chave != x):
            p = p.prox
        if p:
            return (True, p)
        return (False, None)

    def Insere(self, x):
        res, p = self.Consulta(x)
        if (res):
            print("palavra ja existente:", x)
            return res
        p = No(x)
        if self.prim == None or p.chave < self.prim.chave:
            p.prox = self.prim
            self.prim = p
            print("palavra inserida:", x)
            return
        curr = self.prim
        while curr.prox != None and curr.prox.chave < p.chave:
            curr = curr.prox
        p.prox = curr.prox
        curr.prox = p
        print("palavra inserida:", x)
        return True

    def Imprimir(self):
        if (self.prim == None):
            print("lista vazia")
        atual = self.prim
        while atual:
            print(atual.chave)
            atual = atual.prox

    def Remove(self, x):
        pant = None
        p = self.prim
        while (p != None) and (p.chave != x):
            pant = p
            p = p.prox
        if (p == None):
            print("palavra inexistente: ", x)
            return False
        if (pant == None):
            self.prim = p.prox
        else:
            pant.prox = p.prox
        print("palavra removida: ", x)
        return True


class OrdemAlfabetica:
    def __init__(self):
        self.prim = None

    def Consulta(self, x):
        p = self.prim
        while (p != None) and (p.chave != x):
            p = p.Ordem
        if p:
            return (True, p)
        return (False, None)

    def Insere(self, x):
        if (len(x) <= 5):
            lista = lista1
        elif (len(x) >= 6 and len(x) <= 10):
            lista = lista2
        elif (len(x) > 10):
            lista = lista3
        res1, p2 = self.Consulta(x)
        if res1:
            return True
        res, p = lista.Consulta(x)
        if self.prim == None or p.chave < self.prim.chave:
            p.Ordem = self.prim
            self.prim = p
            return
        curr = self.prim
        while curr.Ordem != None and curr.Ordem.chave < p.chave:
            curr = curr.Ordem
        p.Ordem = curr.Ordem
        curr.Ordem = p
        return True

    def Imprimir(self):
        atual = self.prim
        while atual:
            print(atual.chave)
            atual = atual.Ordem

    def PalavrasMesmoTamanho(self, x):
        p = self.prim
        contador = 0
        while p:
            palavra = p.chave
            if len(palavra) == x:
                print(palavra)
                contador += 1
            p = p.Ordem
        if (contador == 0):
            print("lista vazia")

    def PalavrasEntreL1eL2(self, l1, l2):
        current = self.prim
        contador = 0
        while current:
            if l1 <= current.chave[0] <= l2:
                print(current.chave)
                contador += 1
            current = current.Ordem
        if contador == 0:
            print("lista vazia")

    def Removel4(self, x):
        pant = None
        p = self.prim
        while (p != None) and (p.chave != x):
            pant = p
            p = p.Ordem
        if (p == None):
            return False
        if (pant == None):
            self.prim = p.Ordem
        else:
            pant.Ordem = p.Ordem
        return True


lista1 = Lista()
lista2 = Lista()
lista3 = Lista()
lista4 = OrdemAlfabetica()
comando = input()
while comando != "e":
    if (comando == "i"):
        palavra = input()
        if (len(palavra) <= 5):
            lista1.Insere(palavra)
        elif (len(palavra) >= 6 and len(palavra) <= 10):
            lista2.Insere(palavra)
        elif (len(palavra) > 10):
            lista3.Insere(palavra)
        lista4.Insere(palavra)
    elif (comando == "l"):
        opcao = int(input())
        if opcao == 1:
            lista1.Imprimir()
        elif opcao == 2:
            lista2.Imprimir()
        elif opcao == 3:
            lista3.Imprimir()
        elif opcao == 4:
            lista4.Imprimir()
    elif (comando == "x"):
        opcao = int(input())
        lista4.PalavrasMesmoTamanho(opcao)
    elif (comando == "o"):
        l1 = input()
        l2 = input()
        lista4.PalavrasEntreL1eL2(l1, l2)
    elif (comando == "r"):
        palavra = input()
        if (len(palavra) <= 5):
            lista1.Remove(palavra)
        elif (len(palavra) >= 6 and len(palavra) <= 10):
            lista2.Remove(palavra)
        elif (len(palavra) > 10):
            lista3.Remove(palavra)
        lista4.Removel4(palavra)
    comando = input()
