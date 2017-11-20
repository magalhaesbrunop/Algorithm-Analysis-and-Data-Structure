from collections import deque

deck = deque()
deck.append(1)
deck.appendleft(2)
deck.append(3)
deck.appendleft(4)

for i in deck:
    print(i, end=' ')
print('\n')
deck.remove(2)
print('\n')
deck.pop()
deck.popleft()
for i in deck:
    print(i, end=' ')