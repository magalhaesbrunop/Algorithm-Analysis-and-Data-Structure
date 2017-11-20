"""
Напишить реализацию
задачи о рюкзаке
методом «разделяй
и властвуй»
"""
import random


class Backpack:
    def __init__(self, weight, capacity):
        self.weight = weight
        self.capacity = capacity

    def meterObject(self, object):
        self.weight += object.weight


class Object:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.valueoportunity = self.value / self.weight


def selectionsort(list, leng):
    for i in range(0, leng - 1):
        min = i
        for j in range(i + 1, leng):
            if list[min].valorporunidad > list[j].valueoportunity:
                min = j
        aux = list[min]
        list[min] = list[i]
        list[i] = aux


bag = Backpack(0, 100)

objects = []
objects.append(Object(20, 3))
objects.append(Object(50, 5))
objects.append(Object(20, 8))
objects.append(Object(10, 4))
objects.append(Object(50, 1))
objects.append(Object(60, 3))
objects.append(Object(30, 5))
objects.append(Object(70, 8))
objects.append(Object(80, 1))
objects.append(Object(15, 7))

selectionsort(objects, len(objects))

result = []
for i in range(len(objects)):
    result.append(0)

i = len(objetos) - 1  # empezamos desde el final porque están ordenados de menor a mayor
while (mochila.peso < mochila.capacidad):
    objeto = objetos[i]
    if ((mochila.peso + objeto.peso) <= mochila.capacidad):
        resultado[i] = 1
        mochila.meterObjeto(objeto)
    else:
        resultado[i] = (mochila.capacidad - mochila.peso) / objeto.peso
        mochila.peso = mochila.capacidad
    i -= 1

print("Resultado: Fracciones de los objetos en la mochila: ")
for i in range(len(resultado) - 1, -1, -1):
    print("Objeto ", i, ": ", resultado[i])