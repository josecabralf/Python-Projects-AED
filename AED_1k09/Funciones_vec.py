# Algoritmos de Ordenamiento Simples: MENOR A MAYOR

# Ordenar por Seleccion Directa
def selection_sort(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]


# Bubblesort
def bubblesort(v):
    n = len(v)
    for i in range(n-1):
        ordenado = True
        for j in range(n-i-1):
            if v[j] > v[j+1]:
                ordenado = False
                v[j], v[j+1] = v[j+1], v[j]
        if ordenado:
            break


# Inserción Directa
def direct_insertion(v):
    n = len(v)
    for j in range(1, n):
        y = v[j]
        k = j - 1
        while k >= 0 and y < v[k]:
            v[k+1] = v[k]
            k -= 1
        v[k+1] = y


# Algoritos de Ordenamiento Complejos:

# Mergesort
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    # Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


# Merge the sorted halves
def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


# Shellsort
def shellSort(input_list):
    gap = len(input_list) // 2
    while gap > 0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
# Sort the sub list for this gap
    while j >= gap and input_list[j - gap] > temp:
        input_list[j] = input_list[j - gap]
        j = j-gap
        input_list[j] = temp
# Reduce the gap for the next element
    gap = gap//2


# Quicksort
# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot [Conviene usar mediana de 3 entre elemento del medio, high y low]
    pivot = array[high]
    # pointer for greater element
    i = low - 1

    # traverse through all elements, compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found, swap it with the greater element pointed by i
            i = i + 1
            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


def quickSort(array, low, high):
    if low < high:
        # find pivot element such that element smaller than pivot are on the left, & element greater than pivot are on the right
        pi = partition(array, low, high)
        # recursive call on the left of pivot & on the right of pivot
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


# Algoritmos de Búsqueda

# Busca la posición del elemento yendo de a uno.
def linear_search(v, x):
    r = -1
    for i in range(len(v)):
        if x == v[i]:
            r = i

    return r


# Busca la posición del elemento partiendo en 2 el vector de forma sucesiva.
# Busqueda binaria... asume arreglo ordenado...
def binary_search(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1

    return -1
