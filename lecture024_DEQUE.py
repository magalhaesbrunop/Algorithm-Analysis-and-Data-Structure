class Deque:
    def __init__(self):
        self.deque = []
        self.len = 0

    def empty(self):
        if self.len == 0:
            return True
        return False

    def push_front(self, e):
        self.deque.insert(0, e)
        self.len += 1

    def push_back(self, e):
        self.deque.insert(self.len, e)
        self.len += 1

    def pop_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.len -= 1

    def pop_back(self):
        if not self.empty():
            self.deque.pop(self.len -1)
            self.len -= 1

    def front(self):
        if not self.empty():
            return self.deque[0]

    def back(self):
        if not self.empty():
            return self.deque[-1]

    def show(self):
        for i in self.deque:
            print(i, end= ' ')

deque = Deque()

deque.push_front(10)
deque.push_front(5)
deque.push_back(30)
deque.push_back(20)
deque.push_front(40)
deque.push_back(1)
print(deque.show())
print('front: {}'.format(deque.front()))
print('back:  {}'.format(deque.back()))
deque.pop_back()
deque.pop_front()
deque.pop_back()
deque.pop_back()
print(deque.show())