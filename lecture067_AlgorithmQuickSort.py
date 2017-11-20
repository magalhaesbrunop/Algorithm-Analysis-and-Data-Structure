import random
# passa a lista, o início e o fim
def partition(vector, start, end):

    # o pivô é o elemento do início
    pivot = start

    for i in range(start + 1, end + 1):
        if vector[i] <= vector[start]:
            pivot += 1
            vector[i], vector[pivot] = vector[pivot], vector[i]

    vector[pivot], vector[start] = vector[start], vector[pivot]

    return pivot

# passa a lista, o início e o fim
def quickSort(vector, start, end):
    """
    Se o fim for maior que o início,
    então calcula a posição do pivô
    utilizando a função particionada
    """
    if end > start:

        #separa os dados em duas partições
        pivot = partition(vector, start, end)
        """
        Tendo o pivô, chama a função duas 
        vezes para cada partição, a primeira 
        dos elementos que estão antes do pivô 
        e a segunda é a dos elementos que 
        estão depois do pivô
        """
        quickSort(vector, start, pivot - 1)
        quickSort(vector, pivot + 1, end)


vector = random.sample(range(1, 10000), 1000)
print(vector, '\n')
quickSort(vector, 0, len(vector) - 1)
print(vector, '\n')

