"""
Решите задачу о Ханойской башне
"""
def hanoi(n, A, B, C):
    if n == 1:
            print('Move disc {} from {} to {}.'.format(n, A, B))
            print(A, B, C)
    else:
            hanoi(n-1, A, C, B)
            print('Move disc {} from {} to {}.'.format(n, A, B))
            print(A, B, C)
            hanoi(n-1, C, B, A)

numb = int(input("How many discs: "))
number = numb
a = 'A'
b = 'B'
c = 'C'
print(a, b, c)
hanoi(number, a, b, c)