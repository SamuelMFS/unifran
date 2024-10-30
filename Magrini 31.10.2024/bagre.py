import random
import time

# Gera uma lista com 20.000 valores aleatórios entre 1 e 10.000
lista_aleatoria = [random.randint(1, 10000) for _ in range(20000)]

# Exibe os primeiros 10 valores como exemplo
print("\n\nlista bagrada" , lista_aleatoria[:20])

lista_teste = [10, 20, 20, 12, 15, 4, 50, 23, 12, 25, 100]
lista_aleatoria_200 = lista_aleatoria[:200]
lista_aleatoria_2000 = lista_aleatoria[:2000]

# ---------------------- #
#       Bubble Sort      #
# ---------------------- #

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        troca_ocorrida = False  # Variável para verificar se houve troca
        # O loop vai até n - i - 1, pois os últimos i elementos já estarão ordenados
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Troca os elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                troca_ocorrida = True  # Marca que houve troca
        # Se nenhuma troca foi feita, interrompe o loop
        if not troca_ocorrida:
            break
    return arr

lista_bubble_sort = lista_aleatoria
inicio = time.time()
bubble_sort_optimized(lista_bubble_sort)
fim = time.time()

print("\n\nlista de buble_sort feito em ", (fim - inicio) , " segundos ", lista_bubble_sort[:20])


# ---------------------- #
#     Selection Sort     #
# ---------------------- #

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume que o menor elemento está na posição i
        min_index = i
        # Encontra o menor elemento na parte desordenada
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Troca o menor elemento encontrado com o primeiro elemento desordenado
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

lista_selection_sort = lista_aleatoria
inicio = time.time()
selection_sort(lista_selection_sort)
fim = time.time()

print("\n\nlista de selection_sort feito em ", (fim - inicio) , " segundos ", lista_selection_sort[:20])

# ---------------------- #
#       Quick Sort       #
# ---------------------- #

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

lista_quick_sort = lista_aleatoria
inicio = time.time()
quick_sort(lista_quick_sort)
fim = time.time()

print("\n\nlista de quick_sort feito em ", (fim - inicio) , " segundos ", lista_quick_sort[:20])

# ---------------------- #
#       Merge Sort       #
# ---------------------- #

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontrar o meio da lista
        left_half = arr[:mid]  # Dividir a lista em duas metades
        right_half = arr[mid:]

        # Chamar merge_sort recursivamente para as duas metades
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Copiar os dados para as metades temporárias
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verificar se ainda há elementos na metade esquerda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verificar se ainda há elementos na metade direita
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


lista_merge_sort = lista_aleatoria
inicio = time.time()
merge_sort(lista_merge_sort)
fim = time.time()

print("\n\nlista de merge_sort feito em ", (fim - inicio) , " segundos ", lista_merge_sort[:20])

# ---------------------- #
#        Tim Sort        #
# ---------------------- #

lista_tim_sort = lista_aleatoria
inicio = time.time()
lista_tim_sort.sort()
fim = time.time()

print("\n\nlista de tim_sort feito em ", (fim - inicio) , " segundos ", lista_tim_sort[:20])