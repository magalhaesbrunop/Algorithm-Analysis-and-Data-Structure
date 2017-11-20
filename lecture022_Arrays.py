array = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
]

print(array, '\n')
print(array[0][0], '\n')
print(array[2], '\n')

arrayStudentsAndPoints = [
    ['John ', 8, 7, 6],
    ['Peter ', 4.5, 9, 10],
    ['Mark ', 6, 6, 8]
]

for line in arrayStudentsAndPoints:
    for column in line:
        print(str(column) + '\t', end=' ')
    print(' ')