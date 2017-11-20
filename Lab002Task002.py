"""
опишите алгоритм нахождения
максимального значения в массиве,
используя принцип «разделяй и властвуй»
"""

import random
def partition(vector, start, end):
    pivot = start
    for i in range(start + 1, end + 1):
        if vector[i] <= vector[start]:
            pivot += 1
            vector[i], vector[pivot] = vector[pivot], vector[i]
    vector[pivot], vector[start] = vector[start], vector[pivot]
    return pivot
def divideAndConquer(vector, start, end):
    if end > start:
        pivot = partition(vector, start, end)
        divideAndConquer(vector, start, pivot - 1)
        divideAndConquer(vector, pivot + 1, end)


vector = random.sample(range(1, 10000), 1000)
print(vector, '\n')
divideAndConquer(vector, 0, len(vector) - 1)

print(max(vector ), '\n')