"""
сравните время вычисления 35-го числа
Фибоначчи при помощи формулы Бине,
метода «разделяй и властвуй»,
методов нисходящего и восходящего
динамического программирования
"""

import timeit, math
n = 35

print('-'*80)
#Fibonacci Dynamic Program
mem = [-1 for i in range(n)]
mem[0] = mem[1] = 1
def fibonacciDynamicProgram(n):

    if mem[n - 1] != -1:
        return mem[n - 1]
    mem[n - 1] = fibonacciDynamicProgram(n - 1) + fibonacciDynamicProgram(n - 2)
    return mem[n - 1]

start = timeit.default_timer()
fibonacciDynamicProgram(n)
end = timeit.default_timer()
print('Фибоначчи динамическое программирование - время выполнения: {:.15f}'.format(end-start))
print('-'*80, '\n')

print('-'*60)
def fibonacciBinet(n):
    sqrt5 = math.sqrt(5)
    phi = (sqrt5 + 1) / 2
    return int(phi ** n / sqrt5 + 0.5)

start = timeit.default_timer()
fibonacciBinet(n)
end = timeit.default_timer()
print('Фибоначчи и Бинет - время выполнения: {:.15f}'.format(end-start))
print('-'*60, '\n')

print('-'*70)
n = 34
fibonacciMemoization = {}
def fibonacciDivideAndConquer(n):
    if n < 2:
        return 1
    try:
        r = fibonacciMemoization[n]
    except:
        r = fibonacciDivideAndConquer(n - 2) + fibonacciDivideAndConquer(n - 1)
        fibonacciMemoization[n] = r
    return r


start = timeit.default_timer()
fibonacciDivideAndConquer(n)
end = timeit.default_timer()

print('Фибоначчи «разделяй и властвуй» - время выполнения: {:.15f}'.format(end-start))
print('-'*70)
