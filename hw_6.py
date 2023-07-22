from random import randint


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(element, lst):
    n = len(lst)
    first = 0
    last = n - 1
    resultOK = False
    result = None
    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == element:
            resultOK = True
            result = mid
            break
        elif lst[mid] < element:
            first = mid + 1
        else:
            last = mid - 1
    if resultOK:
        print(f"Элемент найден на позиции {result}.")
    else:
        print("Элемент не найден.")
    print("Конец")