class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, label):
        # cria um novo nó
        node = Node(label)

        #verifica se a arvore está vazia
        if self.empty():
            self.root = node
        else:
            # arvore não vazia, insere recursivamente
            dad_node = None
            curr_node = self.root

            while True:

                if curr_node != None:
                    dad_node = curr_node

                    # verifica se vai para esquerda ou direita
                    if node.getLabel() < curr_node.getLabel():
                        # vai para esquerda
                        curr_node = curr_node.getLeft()
                    else:
                        # vai para direita
                        curr_node = curr_node.getRight()
                else:
                    # se curr_node é None, então encontrou onde inserir
                    if node.getLabel() < dad_node.getLabel():
                        dad_node.setLeft(node)
                    else:
                        dad_node.setRight(node)

                    # sai do loop
                    break

    def empty(self):
        if self.root == None:
            return True
        return False

    # mostra em pre-ordem (raiz-esq-dir)
    def show(self, curr_node):
        if curr_node != None:
            print('{}'.format(curr_node.getLabel()), end=' ')
            self.show(curr_node.getLeft())
            self.show(curr_node.getRight())

    def getRoot(self):
        return self.root

    def remove(self):
        dad_node = None # pai
        curr_node = self.root

        while curr_node != None:
            # verifica se encontrou o nó a ser removido
            if label == curr_node.getLabel():

                #caso 1: o nó a ser removido não possui filhos (nó folha)
                if curr_node.getLeft() == None and curr_node.getRight() == None:

                    # verifica se é raiz
                    if dad_node == None:
                        self.root = None
                    else:
                        # verifica se é filho à esquerda ou à direta
                        if dad_node.getLeft() == curr_node:
                            dad_node.setLeft(None)
                        elif dad_node.getRight() == curr_node:
                            dad_node.setRight(None)

                # caso 2: o nó a ser removido possui somente 1 filho
                elif (curr_node.getLeft() == None and curr_node.getRight() != None) or \
                    (curr_node.getLeft() != None and curr_node.getRight() == None):

                    # verifica se o nó a ser removido é a raiz
                    if curr_node == None:
                        # verifica se o filho de curr_node é filho à esquerda
                        if curr_node.getLeft() != None:
                            self.root = curr_node.getLeft()
                        else:
                            self.root = curr_node.getRight()
                    else:
                        # verifica se o filho de curr_node é filho à esquerda
                        if curr_node.getLeft() != None:

                            # verifica se curr_node é filho à esquerda
                            if dad_node.getLeft() and dad_node.getLabel().getLabel() == curr_node.getLabel():
                                dad_node.setLeft(curr_node.getLeft())
                            else: #senão curr_node é filho à direita
                                dad_node.setRight(curr_node.getLeft())
                        else:# senão o filho de curr_node é filho à direta
                            # verifica se curr_node é filho à esquerda
                            if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                                dad_node.setLeft(curr_node.getRight())
                            else:# senão curr_node é filho à direita
                                dad_node.setRight(curr_node.getRight())

                # caso 3: o nó a ser removido possui dois filhos
                # pega o menor elemento da subárvore à direita
                elif curr_node.getLeft() != None and curr_node.getRight() != None:

                    dad_smaller_node = curr_node
                    smaller_node = curr_node.getRight()
                    next_smaller = curr_node.getRight().getLeft()

                    while next_smaller != None:
                        dad_smaller_node = smaller_node
                        smaller_node = next_smaller
                        next_smaller = smaller_node.getLeft()

                    #verifica se o nó a ser removido é a raiz
                    if dad_node == None:

                        #Caso esoecial: o nó que vai ser a nova raiz é filho da raiz
                        if self.root.getLeft().getLabel() == smaller_node.getLabel():
                            smaller_node.setLeft(self.root.getLeft())
                        else:
                            if dad_smaller_node.getLeft() and dad_smaller_node.getLeft.getLabel() == dad_smaller_node.getLeft(None):
                                dad_smaller_node.setLeft(None)
                            else:
                                dad_smaller_node.setRight(None)

                            # seta os filhos à direita e à esquerda de smaller_node
                            smaller_node.setLeft(curr_node.getLeft())
                            smaller_node.setRight(curr_node.getRight())

                            




vertex = BinarySearchTree()
vertex.insert(8)
vertex.insert(3)
vertex.insert(1)
vertex.insert(6)
vertex.insert(4)
vertex.insert(7)
vertex.insert(10)
vertex.insert(14)
vertex.insert(13)

vertex.show(vertex.getRoot())