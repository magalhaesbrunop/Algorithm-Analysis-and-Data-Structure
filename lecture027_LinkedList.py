class Node:

    def __init__(self, label):
        self.label = label
        self.next = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):

        if index >= 0:

            #cria um novo no
            node = Node(label)

            # verifica se a lista esta vazia
            if self.empty():
                self.first = node
                self.last = node
            else:

                if index == 0:
                    # inserção no inicio
                    node.setNext(self.first)
                    self.first = node
                elif index >= self.len_list:
                    # inserção no final
                    self.last.setNext(node)
                    self.last = node
                else:
                    # inserção no meio
                    prev_node = self.first
                    curr_node = self.first.getNext()
                    curr_index = 1

                    while curr_node != None:

                        if curr_index == index:
                            # seta o curr_node como o proximo do no
                            node.setNext(curr_node)
                            # seta o node como o proximo do prev_node
                            prev_node.setNext(node)

                        prev_node = curr_node
                        curr_node = curr_node.getNext()
                        curr_index += 1

            # atualiza o tamanho da lista
            self.len_list += 1

    def pop(self, index):

        if not self.empty() and index >= 0 and index < self.len_list:

            flag_remove = False

            if self.first.getNext() == None:
                # possui apenas 1 elemento
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                # remove do inicio, mas possui mais de 1 elemento
                self.first = self.first.getNext()
                flag_remove = True
            else:
                """
                se chegou aqui é porque a lista possui mais
                de um elemento e a remoção não é no inicio
                """

                prev_node = self.first
                curr_node = self.first.getNext()
                curr_index = 1

                while curr_node != None:

                    if index == curr_index:
                        # o proximo do anterior aponta para o proximo do nó corrente
                        prev_node.setNext(curr_node.getNext())
                        curr_node.setNext(None)
                        flag_remove = True
                        break

                    prev_node = curr_node
                    curr_node = curr_node.getNext()
                    curr_index +=1

            if flag_remove:
                # atualiza o tamanho da lista
                self.len_list -= 1

    def empty(self):
        if self.first == None:
            return True
        return False

    def length(self):
        return self.len_list

    def show(self):

        curr_node = self.first

        while curr_node != None:
            print(curr_node.getLabel(), end=' ')
            curr_node = curr_node.getNext()
        print()

list = LinkedList()

# test inserção
list.push('Marcos', 0)
list.show()
list.push('Maria', 1)
list.show()
list.push('Yankee', 0)
list.show()
list.push('Catarina', 2)
list.show()
list.push('Lilica', 5)
list.show()
list.push('Roberta', 4)
list.show()
print('Tamanho da lista: {}.'.format(list.length()))
list.pop(0)
list.show()
list.pop(2)
list.show()
list.pop(5)
list.show()
print('Tamanho da lista: {}.'.format(list.length()))