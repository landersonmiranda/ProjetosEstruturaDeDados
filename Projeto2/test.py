class No:
    def __init__(self, x):
        self.chave = x
        self.esq = None
        self.dir = None
        self.lista = None


class Lista:
    def __init__(self):
        self.prim = None

    def Consulta(self, x):
        p = self.prim
        while (p != None) and (p.chave != x):
            p = p.lista
        if p:
            return (True, p)
        return (False, None)

    def Insere(self, x):
        if (len(x) <= 5):
            lista = lista1
        elif (len(x) >= 6):
            lista = lista2
        res1, p2 = self.Consulta(x)
        if res1:
            return True
        res, p = arvore1.ArvoreBB_BuscaInterativa(x)
        if self.prim == None or p.chave < self.prim.chave:
            p.lista = self.prim
            self.prim = p
            return
        curr = self.prim
        while curr.lista != None and curr.lista.chave < p.chave:
            curr = curr.lista
        p.lista = curr.lista
        curr.lista = p
        return True

    def Imprimir(self):
        if (self.prim == None):
            print("lista vazia")
        atual = self.prim
        while atual:
            print(atual.chave)
            atual = atual.lista

    def Remove(self, x):
        pant = None
        p = self.prim
        while (p != None) and (p.chave != x):
            pant = p
            p = p.lista
        if (p == None):
            return False
        if (pant == None):
            self.prim = p.lista
        else:
            pant.lista = p.lista
        return True

    def PalavrasMesmoTamanho(self, x):
        p = self.prim
        contador = 0
        while p:
            palavra = p.chave
            if len(palavra) == x:
                print(palavra)
                contador += 1
            p = p.lista
        if (contador == 0):
            print("lista vazia")


class Arvore:
    def __init__(self):
        self.raiz = None

    def ArvoreBB_BuscaInterativa(self, x):
        arv = self.raiz
        while arv != None and arv.chave != x:
            if x < arv.chave:
                arv = arv.esq
            else:
                arv = arv.dir
        if arv:
            return True, arv
        return False, arv

    def ArvoreBB_BuscaComandoC(self, x):
        arv = self.raiz
        while arv != None and arv.chave != x:
            if x < arv.chave:
                arv = arv.esq
            else:
                arv = arv.dir
        if arv:
            print("palavra ja existente:", x)
            return True, arv
        print("palavra inexistente:", x)
        return False, arv

    def ArvoreBB_Inserir(self, x):
        novo_no = No(x)
        # arvore vazia
        if not self.raiz:
            self.raiz = novo_no
            print("palavra inserida:", x)
            return novo_no
        # procurar local pra inserir o nó
        parent = self.raiz
        arv = self.raiz
        while arv != None and arv.chave != x:
            parent = arv
            if x < arv.chave:
                arv = arv.esq
            else:
                arv = arv.dir
        # arvore ja contem chave
        if arv:
            print("palavra ja existente:", x)
            return arv
        # insere novo no
        if parent.chave > x:
            parent.esq = novo_no
        else:
            parent.dir = novo_no
        print("palavra inserida:", x)
        return novo_no

    def achar_pai(self, x):
        no = self.raiz
        parent_node = None
        while no is not None:
            if no.chave == x:
                return parent_node
            parent_node = no
            if no.chave < x:
                no = no.dir
            else:
                no = no.esq
        return parent_node

    def menor_no(self, menor):
        while menor.esq:
            menor = menor.esq
        return menor

    def delete(self, x):
        # busca
        arv = self.raiz
        while arv != None and arv.chave != x:
            if x < arv.chave:
                arv = arv.esq
            else:
                arv = arv.dir
        # nao encontrou
        if not arv:
            print("palavra inexistente:", x)
            return None
        # 2 filhos
        if arv.esq and arv.dir:
            menor = self.menor_no(arv.dir)
            pai_menor = self.achar_pai(menor.chave)
            if menor == arv.dir:
                arv.dir = menor.dir
            else:
                pai_menor.esq = menor.dir
            arv.chave = menor.chave
            print("palavra removida:", x)
            return menor
        pai_arv = self.achar_pai(x)
        # 0 ou 1 filhos
        if arv.esq:
            if not pai_arv:
                self.raiz = arv.esq
            elif arv.chave < pai_arv.chave:
                pai_arv.esq = arv.esq
            else:
                pai_arv.dir = arv.esq
        else:
            if not pai_arv:
                self.raiz = arv.dir
            elif arv.chave < pai_arv.chave:
                pai_arv.esq = arv.dir
            else:
                pai_arv.dir = arv.dir
        print("palavra removida:", x)
        return arv

    def imprimir_intervalo_arvore_recursivo(self, l1, l2, no):
        raiz = self.raiz
        if raiz is None:
            print("lista vazia")
        if no is None:
            return no
        # Verifica se o chave do nó está no intervalo
        if l1 <= no.chave[0] <= l2:
            self.imprimir_intervalo_arvore_recursivo(l1, l2, no.esq)
            print(no.chave)
            self.imprimir_intervalo_arvore_recursivo(l1, l2, no.dir)
        # Se o chave do nó for menor que l1, então vamos para a direita
        elif no.chave < l1:
            self.imprimir_intervalo_arvore_recursivo(l1, l2, no.dir)
        # Se o chave do nó for maior que l2, então vamos para a esquerda
        else:
            self.imprimir_intervalo_arvore_recursivo(l1, l2, no.esq)

    def verificar_palavras_no_intervalo(self, l1, l2):
        return self._verificar_palavras_no_intervalo(self.raiz, l1, l2)

    def _verificar_palavras_no_intervalo(self, no, l1, l2):
        if no is None:
            return False

        if l1 <= no.chave[0] <= l2:
            return True

        if no.chave[0] > l2:
            return self._verificar_palavras_no_intervalo(no.esq, l1, l2)

        if no.chave[0] < l1:
            return self._verificar_palavras_no_intervalo(no.dir, l1, l2)

        return (self._verificar_palavras_no_intervalo(no.esq, l1, l2) or
                self._verificar_palavras_no_intervalo(no.dir, l1, l2))

    def PalavrasEntreL1eL2(self, l1, l2):
        atual = self.raiz
        pai = self.achar_pai(atual)
        while (atual.chave[0] > l1):
            atual = atual.esq
            pai = self.achar_pai(atual)
        while (atual.chave[0] < l2):
            print(atual.chave)
            atual = pai
            pai = self.achar_pai(atual)

    def imprimeEmPreOrdem(self, no):
        raiz = self.raiz
        if raiz is None:
            print("arvore vazia")
            return
        if no is None:
            return no
        else:
            if no:
                print(
                    f"palavra: {no.chave} fesq: {no.esq.chave if no.esq else 'nil'} fdir: {no.dir.chave if no.dir else 'nil'}")
            self.imprimeEmPreOrdem(no.esq)
            self.imprimeEmPreOrdem(no.dir)


arvore1 = Arvore()
lista1 = Lista()
lista2 = Lista()
comando = input()
while comando != "e":
    if (comando == "i"):
        palavra = input()
        arvore1.ArvoreBB_Inserir(palavra)
        if (len(palavra) >= 6):
            lista2.Insere(palavra)
        else:
            lista1.Insere(palavra)
    elif (comando == "c"):
        palavra = input()
        arvore1.ArvoreBB_BuscaComandoC(palavra)
    elif (comando == "l"):
        numero = int(input())
        if (numero == 1):
            lista1.Imprimir()
        elif (numero == 2):
            lista2.Imprimir()
    elif (comando == "x"):
        numero = int(input())
        if (numero <= 5):
            lista1.PalavrasMesmoTamanho(numero)
        else:
            lista2.PalavrasMesmoTamanho(numero)
    elif (comando == "o"):
        l1 = input()
        l2 = input()
        if (arvore1.verificar_palavras_no_intervalo(l1, l2) == True):
            arvore1.imprimir_intervalo_arvore_recursivo(l1, l2, arvore1.raiz)
        else:
            print("lista vazia")
    elif (comando == "r"):
        palavra = input()
        if (len(palavra) <= 5):
            lista1.Remove(palavra)
        else:
            lista2.Remove(palavra)
        arvore1.delete(palavra)
    elif (comando == "p"):
        arvore1.imprimeEmPreOrdem(arvore1.raiz)
    comando = input()
