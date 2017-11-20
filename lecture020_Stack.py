class Stack:

    def __init__(self): # Função onde eu inicio a pilha
        self.stack = []

    def push(self, e): # Função onde eu coloco os elementos
        self.stack.append(e)

    def pop(self): # Função onde eu retiro os elementos
        if not self.empty():
            self.stack.pop(len(self.stack)-1)

    def top(self): # Função que retorna o último elemento da pilha
        if not self.empty():
            return self.stack[-1]
        print('Stack empty')

    def empty(self):
        if(len(self.stack)==0):
            return True
        return False

    def show(self):
        if not self.empty():
            return self.stack

    def length(self): # Função que mostra o tamanho da pilha
            return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)

print('\nThe first element in the stack is: {}.'.format(stack.top()),'\n')
stack.pop()
print('After "pop" element.')
print('The first element in the stack is: {}.'.format(stack.top()),'\n')
print('Number of elements in the stack is: {}.'.format(stack.length()),'\n')
print('Elements in the stack is: {}.'.format(stack.show()),'\n')
