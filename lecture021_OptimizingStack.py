class Stack:

    def __init__(self): # Função onde eu inicio a pilha
        self.stack = []
        self.len_stack = 0 # Mostra quantos elementos tem na pilha

    def push(self, e): # Função onde eu coloco os elementos
        self.stack.append(e)
        self.len_stack += 1

    def pop(self): # Função onde eu retiro os elementos
        if not self.empty():
            self.stack.pop(self.len_stack - 1) # O elemento começa na posição 0, então precisa subtrair o ultimo elemento
            self.len_stack -= 1 # Decremento da pilha

    def top(self): # Função que retorna o último elemento da pilha
        if not self.empty():
            return self.stack[-1]
        print('Stack empty')

    def empty(self): # Função quer diz se a pilha está vazia ou não
        if self.len_stack == 0:
            return True
        return False

    def lenght(self): # Função que mostra o tamanho da pilha
            return self.len_stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print('The first element in the stack is {}.'.format(stack.top()),'\n')
stack.pop()
print('After "pop" element.')
print('The first element in the stack is {}.'.format(stack.top()),'\n')
print('Quantity of elements in the stack is {}.'.format(stack.lenght()),'\n')